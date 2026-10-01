// Smoke test for a deployed DGD Arcade server. Node 18+ (uses global fetch).
//
//   node smoke.mjs https://arcade.example.org
//
// It registers one throwaway player, walks the calls DGD App 2.0 makes, checks
// that the server refuses what it should refuse, and then deletes the player
// with DELETE /v1/me. It leaves nothing behind except one entry in the
// per-address signup bucket (10 an hour by default).
//
// It does not wait out a round's minimum duration, so it never earns XP and
// never appears on the weekly standings.

const base = (process.argv[2] ?? '').replace(/\/+$/, '');
if (!/^https?:\/\//.test(base)) {
  console.error('usage: node smoke.mjs https://<arcade host>');
  process.exit(2);
}

let failed = 0;
const check = (ok, what, detail = '') => {
  console.log(`${ok ? 'ok  ' : 'FAIL'}  ${what}${detail ? `  (${detail})` : ''}`);
  if (!ok) failed++;
};

async function call(method, path, { token, body } = {}) {
  const res = await fetch(base + path, {
    method,
    headers: {
      ...(body ? { 'content-type': 'application/json' } : {}),
      ...(token ? { authorization: `Bearer ${token}` } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  let json = null;
  try {
    json = await res.json();
  } catch {
    // Non-JSON body; the status is what gets checked.
  }
  return { status: res.status, json };
}

const health = await call('GET', '/healthz');
check(health.status === 200 && health.json?.ok === true, 'GET /healthz', `bank ${health.json?.bank}, day ${health.json?.day}`);

check((await call('GET', '/v1/me')).status === 401, 'GET /v1/me without a token is refused');

const reg = await call('POST', '/v1/players', { body: { deviceHint: 'smoke-test' } });
check(reg.status === 201 && typeof reg.json?.token === 'string', 'POST /v1/players', `status ${reg.status}`);
if (reg.status !== 201) {
  console.error('cannot continue without a player');
  process.exit(1);
}
const token = reg.json.token;

try {
  const me = await call('GET', '/v1/me', { token });
  check(me.status === 200 && typeof me.json?.handle === 'string', 'GET /v1/me', `handle ${me.json?.handle}`);
  check(me.json?.passage && typeof me.json.passage === 'object', 'snapshot carries the When Pigs Fly profile');

  const board = await call('GET', '/v1/leaderboard?limit=abc', { token });
  check(board.status === 200, 'GET /v1/leaderboard with a junk limit answers 200');

  for (const game of ['coin_quest', 'passage']) {
    const start = await call('POST', `/v1/mini/${game}/start`, { token });
    check(start.status === 201 && typeof start.json?.token === 'string', `POST /v1/mini/${game}/start`);
    // Claimed at once, so it is under the game's minimum duration.
    const claim = await call('POST', `/v1/mini/${game}`, { token, body: { token: start.json?.token, right: 3, total: 3 } });
    check(claim.status === 409 && claim.json?.error === 'too_fast', `an instant ${game} claim is refused`, claim.json?.error);
  }

  const unknown = await call('POST', '/v1/mini/not_a_game/start', { token });
  check(unknown.status === 404, 'an unknown game is refused');

  const upgrade = await call('POST', '/v1/passage/abilities/dash/upgrade', { token });
  check(upgrade.status === 409, 'an ability a new player cannot afford is refused', upgrade.json?.error);

  const loadout = await call('POST', '/v1/passage/loadout', { token, body: { abilities: ['dash'] } });
  check(loadout.status === 400, 'a loadout of abilities the player does not own is refused', loadout.json?.error);

  const reroll = await call('POST', '/v1/me/handle/reroll', { token });
  check(reroll.status === 200 && typeof reroll.json?.handle === 'string', 'POST /v1/me/handle/reroll', `${reroll.json?.rerollsLeft} left today`);
} finally {
  const del = await call('DELETE', '/v1/me', { token });
  check(del.status === 200 && del.json?.deleted === true, 'DELETE /v1/me');
  check((await call('GET', '/v1/me', { token })).status === 401, 'the deleted player token no longer works');
}

console.log(failed ? `\n${failed} check(s) failed` : '\nall checks passed');
process.exit(failed ? 1 : 0);
