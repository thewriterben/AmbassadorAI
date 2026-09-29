// Builds the design resource package for Med (DGD design lead).
// Copies every visual and audio asset of the app shell, the in-app arcade and
// the web arcade, with screens, tokens, a manifest and a guide. No code, no
// keys, no quiz content.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';

const DATE = '2026-09-29';
const OUT = `F:/Documents/dgdappsource/design-package/DGD-Design-Resources-${DATE}`;
const V1 = 'C:/src/puzzle-app';
const V2 = 'C:/src/puzzle-app-v2';
const WEB = 'C:/src/dgd-web-arcade/client';
const NAT = 'C:/src/dgd-native';
const AMB = 'F:/Documents/GitHub/AmbassadorAI/arcade';
const SHOTS = 'C:/Users/Benji/AppData/Local/Temp/claude/design-shots';
const E2E = 'C:/src/dgd-web-arcade/tools/e2e/out';

fs.rmSync(OUT, { recursive: true, force: true });
const rows = []; // manifest
const sha = (f) => crypto.createHash('sha1').update(fs.readFileSync(f)).digest('hex');

function pngInfo(f) {
  const b = fs.readFileSync(f);
  if (b.readUInt32BE(0) !== 0x89504e47) return {};
  const w = b.readUInt32BE(16), h = b.readUInt32BE(20), ct = b[25];
  const alpha = ct === 4 || ct === 6 || b.indexOf('tRNS') > 0;
  return { w, h, alpha };
}
function audioInfo(f) {
  const r = spawnSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration:stream=sample_rate,channels', '-of', 'json', f], { encoding: 'utf8' });
  try {
    const j = JSON.parse(r.stdout);
    return { dur: Number(j.format.duration), rate: Number(j.streams[0].sample_rate), ch: j.streams[0].channels };
  } catch { return {}; }
}

/** Copy one file into the package and record it. */
function add(src, dest, meta) {
  const to = path.join(OUT, dest);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.copyFileSync(src, to);
  const ext = path.extname(src).toLowerCase();
  const info = ext === '.png' ? pngInfo(src) : ['.wav', '.mp3'].includes(ext) ? audioInfo(src) : {};
  rows.push({ pkg: dest.replaceAll('\\', '/'), source: meta.source, surface: meta.surface, kind: meta.kind, use: meta.use ?? '', note: meta.note ?? '', bytes: fs.statSync(src).size, sha: sha(src), ...info });
}

// ------------------------------------------------------------ descriptions
const IMG = {
  bg_dark: 'Full-screen dark background behind the arcade screens',
  board_cell: 'One cell of the Coin Quest board grid',
  logo_orange: 'DGD "G" mark, orange (headers, level screen)',
  logo_white: 'DGD "G" mark, white (drawn on the board)',
  node_current: 'Level map: the level you are on',
  node_done: 'Level map: a cleared level',
  node_locked: 'Level map: a locked level',
  piece_gold: 'Coin Quest piece: gold coin', piece_silver: 'Coin Quest piece: silver coin', piece_copper: 'Coin Quest piece: copper coin',
  piece_red: 'Coin Quest piece: rose/red coin', piece_blue: 'Coin Quest piece: sapphire/blue coin', piece_green: 'Coin Quest piece: emerald/green coin',
  piece_ingot: 'Coin Quest special: gold ingot (drop it to the bottom)', piece_vault: 'Coin Quest obstacle: vault', piece_vault_armored: 'Coin Quest obstacle: armoured vault (two hits)',
  seal_1: 'Coin Quest obstacle: wax seal, first layer', seal_2: 'Coin Quest obstacle: wax seal, second layer',
  coin_gold: 'Hero coin on the arcade home; 1st-place medal', coin_silver: '2nd-place medal; When Pigs Fly silver pickup', coin_rose: '3rd-place medal; web home decoration',
  coin_copper: 'When Pigs Fly copper pickup', coin_gold_shiny: 'When Pigs Fly gold pickup', coin_emerald: 'Web home: Coin Quest card coin', coin_sapphire: 'Web home: Coin Quest card coin',
  card_pigs: 'Web home: When Pigs Fly game card',
  boar_piglet: 'When Pigs Fly boar, stage 1 (piglet): 8-frame sprite sheet', boar_juvenile: 'When Pigs Fly boar, stage 2 (juvenile): 8-frame sprite sheet', boar_razorback: 'When Pigs Fly boar, stage 3 (razorback): 8-frame sprite sheet',
};
const V1_USED = ['bg_dark', 'board_cell', 'coin_gold', 'coin_rose', 'coin_silver', 'logo_orange', 'logo_white', 'node_current', 'node_done', 'node_locked',
  'piece_blue', 'piece_copper', 'piece_gold', 'piece_green', 'piece_ingot', 'piece_red', 'piece_silver', 'piece_vault', 'piece_vault_armored', 'seal_1', 'seal_2'];
const WEB_USED = ['bg_dark', 'board_cell', 'boar_juvenile', 'boar_piglet', 'boar_razorback', 'card_pigs', 'coin_copper', 'coin_emerald', 'coin_gold', 'coin_gold_shiny',
  'coin_rose', 'coin_sapphire', 'coin_silver', 'logo_orange', 'logo_white', 'piece_blue', 'piece_copper', 'piece_gold', 'piece_green', 'piece_ingot', 'piece_red',
  'piece_silver', 'piece_vault', 'piece_vault_armored', 'seal_1', 'seal_2'];

function audioUse(n) {
  const s = n.replace(/\.(wav|mp3)$/, '');
  const table = [
    [/^music_quest/, 'Music: Coin Quest (Quest Tune), level map and levels'], [/^music_pigs/, 'Music: When Pigs Fly'],
    [/^vo_/, 'Voice line after a level or a big combo'], [/^fw_/, 'Fireworks on a win (web only; muted in the phone app)'],
    [/^tap/, 'UI tap'], [/^swap/, 'Coin swap'], [/^invalid/, 'Swap that does not match'], [/^land/, 'Coins landing after a fall'],
    [/^pop/, 'Coins clearing (pitch rises with the cascade)'], [/^combo/, 'Cascade combo'], [/^star/, 'Star earned on the result screen'],
    [/^special_create/, 'Special coin made (four or five in a row)'], [/^special_fire/, 'Special coin fired'], [/^bomb/, 'Bomb coin'],
    [/^vault_hit/, 'Vault hit'], [/^vault_break/, 'Vault broken'], [/^seal/, 'Seal cracked'], [/^ingot_land/, 'Ingot reaching the bottom'],
    [/^coin_(flip|spin|roll|drop)/, 'Coin movement'], [/^coins_pour/, 'Coins pouring (result screen)'], [/^win_fill/, 'Result screen score fill'],
    [/^win/, 'Level won'], [/^lose/, 'Level lost'], [/^ting/, 'Small positive cue'],
    [/^flap_/, 'When Pigs Fly: wing flap, per boar stage'], [/^grunt_/, 'When Pigs Fly: hit / hurt grunt, per stage'], [/^snort_/, 'When Pigs Fly: snort, per stage'],
    [/^ab_/, 'When Pigs Fly: ability sound (dash, grapple, blink, freeze, tractor)'], [/^stage_up/, 'When Pigs Fly: boar grows into the next stage'],
  ];
  for (const [re, t] of table) if (re.test(s)) return t;
  return 'Sound effect';
}
const namedIn = (file) => new Set([...fs.readFileSync(file, 'utf8').matchAll(/['"]([A-Za-z0-9_]+\.(?:wav|mp3))['"]/g)].map((m) => m[1]));
/** Names built in code from a prefix and a counter, e.g. `_rr('pop1_', 3)`. */
function audioUsed(audioDart, dir) {
  const src = fs.readFileSync(audioDart, 'utf8');
  const names = namedIn(audioDart);
  for (const m of src.matchAll(/_rr\('([a-z0-9_]+)',\s*(\d+)/g)) for (let i = 1; i <= Number(m[2]); i++) names.add(`${m[1]}${i}.wav`);
  for (const m of src.matchAll(/'([a-z0-9_]+)_\$\{?[a-z.]+\}?\.wav'/g)) for (const f of fs.readdirSync(dir)) if (f.startsWith(m[1] + '_')) names.add(f);
  return [...names].filter((n) => fs.existsSync(path.join(dir, n))).sort();
}

// ======================================================= 1. app shell
const S1 = '1-app-shell';
for (const d of ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']) {
  for (const f of fs.readdirSync(`${NAT}/android/app/src/main/res/mipmap-${d}`)) {
    add(`${NAT}/android/app/src/main/res/mipmap-${d}/${f}`, `${S1}/android/launcher-icon/mipmap-${d}/${f}`, {
      source: `dgd-native:android/app/src/main/res/mipmap-${d}/${f}`, surface: 'app shell', kind: 'launcher icon',
      use: { 'ic_launcher.png': 'Legacy square icon', 'ic_launcher_round.png': 'Legacy round icon', 'ic_launcher_foreground.png': 'Adaptive icon foreground layer', 'ic_launcher_monochrome.png': 'Themed (monochrome) icon, Android 13+' }[f],
    });
  }
}
for (const f of ['ic_launcher.xml', 'ic_launcher_round.xml']) add(`${NAT}/android/app/src/main/res/mipmap-anydpi-v26/${f}`, `${S1}/android/launcher-icon/mipmap-anydpi-v26/${f}`, { source: `dgd-native:android/app/src/main/res/mipmap-anydpi-v26/${f}`, surface: 'app shell', kind: 'launcher icon definition', use: 'How Android layers the adaptive icon (background colour + foreground + monochrome)' });
add(`${NAT}/android/app/src/main/res/values/ic_launcher_background.xml`, `${S1}/android/launcher-icon/ic_launcher_background.xml`, { source: 'dgd-native:android/app/src/main/res/values/ic_launcher_background.xml', surface: 'app shell', kind: 'launcher icon background colour' });
add(`${NAT}/android/app/src/main/res/drawable/dgd_coin.png`, `${S1}/android/images/dgd_coin.png`, { source: 'dgd-native:android/app/src/main/res/drawable/dgd_coin.png', surface: 'app shell', kind: 'image', use: 'DGD coin (full)' });
add(`${NAT}/android/app/src/main/res/drawable/dgd_coin_face.png`, `${S1}/android/images/dgd_coin_face.png`, { source: 'dgd-native:android/app/src/main/res/drawable/dgd_coin_face.png', surface: 'app shell', kind: 'image', use: 'Spinning coin at the top of the ticker screen' });
add(`${NAT}/android/app/src/main/res/raw/open_coin.wav`, `${S1}/android/audio/open_coin.wav`, { source: 'dgd-native:android/app/src/main/res/raw/open_coin.wav', surface: 'app shell', kind: 'audio', use: 'Ticker: coin spins in on open' });
add(`${NAT}/android/app/src/main/res/raw/burst_firework.wav`, `${S1}/android/audio/burst_firework.wav`, { source: 'dgd-native:android/app/src/main/res/raw/burst_firework.wav', surface: 'app shell', kind: 'audio', use: 'Ticker: particle burst on the coin' });
for (const f of ['colors.xml', 'themes.xml']) add(`${NAT}/android/app/src/main/res/values/${f}`, `${S1}/android/values/${f}`, { source: `dgd-native:android/app/src/main/res/values/${f}`, surface: 'app shell', kind: 'theme values' });
const XC = `${NAT}/apple/DigitalGoldTicker/Assets.xcassets`;
for (const [src, dest, use] of [
  ['AppIcon.appiconset/AppIcon.png', 'AppIcon.png', 'iOS app icon (1024, one size)'],
  ['DGDCoin.imageset/DGDCoin.png', 'DGDCoin.png', 'DGD coin (full)'], ['DGDCoinFace.imageset/DGDCoinFace.png', 'DGDCoinFace.png', 'Spinning coin, ticker screen'],
  ['InviteAppIcon.imageset/AppIcon.png', 'InviteAppIcon.png', 'App icon shown on the Invite Friends screen'],
  ['AccentColor.colorset/Contents.json', 'AccentColor.json', 'iOS accent colour'],
]) add(`${XC}/${src}`, `${S1}/ios/${dest}`, { source: `dgd-native:apple/DigitalGoldTicker/Assets.xcassets/${src}`, surface: 'app shell (iOS)', kind: dest.endsWith('json') ? 'colour' : 'image', use, note: 'iOS is built on the Mac; returned art is passed on there' });
add(`${AMB}/integration/ic_launcher-playstore.png`, `${S1}/store/play-store-icon-512.png`, { source: 'AmbassadorAI:arcade/integration/ic_launcher-playstore.png', surface: 'app shell', kind: 'store graphic', use: 'Google Play listing icon for the DGD app (512x512, no transparency)' });

// ================================================= 2. in-app arcade (v1)
const S2 = '2-in-app-arcade';
for (const n of V1_USED) {
  const f = `${V1}/assets/images/${n}.png`;
  const webTwin = WEB_USED.includes(n) && sha(f) === sha(`${WEB}/assets/images/${n}.png`);
  add(f, `${S2}/images/${n}.png`, { source: `puzzle-app:assets/images/${n}.png`, surface: 'in-app arcade', kind: 'image', use: IMG[n], note: webTwin ? 'Identical file in the web arcade: one new design replaces both' : '' });
  const hi = `${V1}/assets/_images_full/${n}.png`;
  if (fs.existsSync(hi)) add(hi, `${S2}/images-hires-originals/${n}.png`, { source: `puzzle-app:assets/_images_full/${n}.png`, surface: 'in-app arcade', kind: 'hi-res original', use: `Original master of ${n}.png (reference, not shipped)` });
}
for (const n of ['coinquest_sheet.png', 'contact_sheet.png']) add(`${V1}/assets/${n}`, `${S2}/reference/${n}`, { source: `puzzle-app:assets/${n}`, surface: 'in-app arcade', kind: 'reference sheet', use: 'Earlier art board (reference only)' });
for (const n of audioUsed(`${V1}/lib/audio.dart`, `${V1}/assets/audio`)) {
  const kind = n.startsWith('music_') ? 'music' : n.startsWith('vo_') ? 'voice' : 'sfx';
  add(`${V1}/assets/audio/${n}`, `${S2}/audio/${kind}/${n}`, { source: `puzzle-app:assets/audio/${n}`, surface: 'in-app arcade', kind: `audio (${kind})`, use: audioUse(n),
    note: n.startsWith('fw_') || n === 'vo_you_win.wav' ? 'Not played inside the DGD app (no prize-style celebration there)' : '' });
}

// ===================================================== 3. web arcade
const S3 = '3-web-arcade';
for (const n of WEB_USED) {
  const f = `${WEB}/assets/images/${n}.png`;
  const appTwin = V1_USED.includes(n) && sha(f) === sha(`${V1}/assets/images/${n}.png`);
  add(f, `${S3}/images/${n}.png`, { source: `puzzle-app-v2:assets/images/${n}.png (copied into dgd-web-arcade/client)`, surface: 'web arcade', kind: n.startsWith('boar_') ? 'sprite sheet' : 'image', use: IMG[n],
    note: [appTwin ? 'Identical file in the in-app arcade: one new design replaces both' : '', n.startsWith('boar_') ? 'Sheet contract: see the guide. New drawn poses are in progress separately; coordinate before redrawing' : ''].filter(Boolean).join('. ') });
}
for (const f of ['favicon.png', 'icons/Icon-192.png', 'icons/Icon-512.png', 'icons/Icon-maskable-192.png', 'icons/Icon-maskable-512.png', 'manifest.json']) {
  add(`${WEB}/web/${f}`, `${S3}/browser/${f}`, { source: `dgd-web-arcade:client/web/${f}`, surface: 'web arcade', kind: f.endsWith('json') ? 'web app manifest' : 'browser icon',
    use: { 'favicon.png': 'Browser tab icon', 'manifest.json': 'Name and colours when saved to a home screen' }[f] ?? 'Home-screen icon when the site is saved as an app', note: 'STILL THE FLUTTER DEFAULT: needs a DGD design' });
}
add(`${WEB}/web/rules.html`, `${S3}/pages/rules.html`, { source: 'dgd-web-arcade:client/web/rules.html', surface: 'web arcade', kind: 'page (HTML/CSS)', use: 'Rewards & official rules page; its own CSS palette', note: 'Restyle freely; the wording is counsel\'s and COUNSEL boxes are placeholders' });
for (const n of [...new Set([...audioUsed(`${V2}/lib/audio.dart`, `${WEB}/assets/audio`), 'music_quest.mp3', 'music_pigs.mp3'])].filter((n) => n !== 'music_level.mp3').sort()) {
  const kind = n.startsWith('music_') ? 'music' : n.startsWith('vo_') ? 'voice' : 'sfx';
  add(`${WEB}/assets/audio/${n}`, `${S3}/audio/${kind}/${n}`, { source: `puzzle-app-v2:assets/audio/${n}`, surface: 'web arcade', kind: `audio (${kind})`, use: audioUse(n) });
}

// ============================================================ fonts
for (const f of fs.readdirSync(`${V1}/assets/fonts`)) add(`${V1}/assets/fonts/${f}`, `fonts/${f}`, { source: `puzzle-app:assets/fonts/${f}`, surface: 'both arcades', kind: 'font',
  use: { 'InstrumentSans.ttf': 'Arcade UI text', 'GeistMono-Bold.ttf': 'Labels, counters, kickers (bold)', 'GeistMono-Medium.ttf': 'Labels, counters (medium)', 'PTSerif-BoldItalic.ttf': 'The italic "Arcade" in the DGD Arcade wordmark' }[f],
  note: 'SIL Open Font License; the app shell uses the phone\'s own fonts (Roboto and the system serif)' });

// ========================================================== screens
const shot = (src, dest, surface, use) => { if (fs.existsSync(src)) add(src, dest, { source: 'screenshot', surface, kind: 'screen', use }); else console.warn('missing', src); };
shot('F:/Documents/dgdappsource/web-arcade/screenshots-v2/android-107-home.png', `${S1}/screens/01-ticker-live.png`, 'app shell', 'Ticker with live figures (Pixel 9a)');
shot(`${SHOTS}/app-01-home-offline.png`, `${S1}/screens/02-ticker-offline.png`, 'app shell', 'Ticker when figures cannot load');
shot(`${SHOTS}/app-04-arcade-menu.png`, `${S1}/screens/03-arcade-menu.png`, 'app shell', 'Arcade menu: in-app arcade or the web arcade');
shot(`${SHOTS}/app-02-login.png`, `${S1}/screens/04-log-in.png`, 'app shell', 'Log in sheet (preview)');
shot(`${SHOTS}/app-03-join.png`, `${S1}/screens/05-join.png`, 'app shell', 'Join the Network sheet, step 1 (preview)');
shot(`${AMB}/rc-1.0.6-shots/02-membership.png`, `${S1}/screens/06-membership.png`, 'app shell', 'My Membership: credentials step (test account)');
shot(`${AMB}/rc-1.0.6-shots/03-invite-open.png`, `${S1}/screens/07-invite.png`, 'app shell', 'Invite Friends');
shot(`${AMB}/rc-1.0.6-shots/04-qr.png`, `${S1}/screens/08-invite-qr.png`, 'app shell', 'Invite: QR for the app');
shot(`${AMB}/rc-1.0.6-shots/05-qr-scrolled.png`, `${S1}/screens/09-invite-qr-scrolled.png`, 'app shell', 'Invite: QR, scrolled');
shot(`${SHOTS}/arcade-01-home.png`, `${S2}/screens/01-arcade-home.png`, 'in-app arcade', 'Arcade home (silent)');
shot(`${SHOTS}/arcade-02-settings.png`, `${S2}/screens/02-settings.png`, 'in-app arcade', 'Settings and your data');
shot(`${SHOTS}/arcade-03-level-map.png`, `${S2}/screens/03-level-map.png`, 'in-app arcade', 'Coin Quest level map');
shot(`${SHOTS}/arcade-04-level-goal.png`, `${S2}/screens/04-level-goal.png`, 'in-app arcade', 'Level goal sheet');
shot(`${SHOTS}/arcade-05-coach.png`, `${S2}/screens/05-coach.png`, 'in-app arcade', 'First-level coaching overlay');
shot(`${SHOTS}/arcade-06-level.png`, `${S2}/screens/06-level.png`, 'in-app arcade', 'A level being played');
shot(`${E2E}/level1-result.png`, `${S2}/screens/07-level-result-web-equivalent.png`, 'in-app arcade', 'Level result (captured on the web; the app shows the same sheet without fireworks)');
for (const [f, d, u] of [
  ['deploy-landing.png', '01-landing-guest.png', 'Landing, as a guest'], ['tour-home.png', '02-landing-signed-in.png', 'Landing, signed in'],
  ['tour-coinquest.png', '03-coin-quest-levels.png', 'Coin Quest level list'], ['level1-playing.png', '04-coin-quest-level.png', 'Coin Quest level'],
  ['level1-result.png', '05-coin-quest-result.png', 'Coin Quest result'], ['tour-pigs.png', '06-pigs-home.png', 'When Pigs Fly home (boar, abilities)'],
  ['pigs-ready.png', '07-pigs-ready.png', 'When Pigs Fly: ready to fly'], ['pigs-flying.png', '08-pigs-flying.png', 'When Pigs Fly: in flight'],
  ['pigs-result-1.png', '09-pigs-result.png', 'When Pigs Fly: result'], ['tour-quiz.png', '10-knowledge-check.png', 'Knowledge check'],
  ['tour-board.png', '11-top-100.png', 'Top 100 boards'], ['tour-record.png', '12-my-record.png', 'My record'], ['deploy-rules.png', '13-rules-page.png', 'Rewards & official rules page'],
]) shot(`${E2E}/${f}`, `${S3}/screens/${d}`, 'web arcade', u);

// ========================================================== tokens
const dartColors = (file) => Object.fromEntries([...fs.readFileSync(file, 'utf8').matchAll(/static const (\w+) = Color\(0x([0-9A-Fa-f]{8})\)/g)].map((m) => [m[1], '#' + m[2].slice(2) + (m[2].slice(0, 2).toUpperCase() === 'FF' ? '' : ` @${Math.round(parseInt(m[2].slice(0, 2), 16) / 2.55)}%`)]));
const ktColors = Object.fromEntries([...fs.readFileSync(`${NAT}/android/app/src/main/java/com/digitalgold/ticker/ui/GoldTheme.kt`, 'utf8').matchAll(/val (\w+) = Color\(0xFF([0-9A-Fa-f]{6})\)/g)].map((m) => [m[1], '#' + m[2]]));
const rulesCss = Object.fromEntries([...fs.readFileSync(`${WEB}/web/rules.html`, 'utf8').matchAll(/--([a-z]+):(#[0-9a-fA-F]{3,6})/g)].map((m) => [m[1], m[2]]));
const tokens = {
  note: 'Colours as they are in the code today. Brand orange and highlight come from digitalgold.co CSS.',
  'app-shell (GoldTheme.kt)': ktColors,
  'arcades (AppTheme in theme.dart; same in app and web)': dartColors(`${V1}/lib/theme.dart`),
  'rules page (rules.html CSS)': rulesCss,
  fonts: { arcadeUi: 'Instrument Sans', arcadeLabels: 'Geist Mono (Medium, Bold)', arcadeWordmark: 'PT Serif Bold Italic', appShell: 'Roboto (system) and the system serif for figures' },
};
fs.mkdirSync(`${OUT}/tokens`, { recursive: true });
fs.writeFileSync(`${OUT}/tokens/design-tokens.json`, JSON.stringify(tokens, null, 2));
fs.writeFileSync(`${OUT}/tokens/tokens.js`, 'window.TOKENS = ' + JSON.stringify(tokens) + ';');

// ========================================================== manifest
const cols = ['pkg', 'surface', 'kind', 'use', 'w', 'h', 'alpha', 'dur', 'rate', 'ch', 'bytes', 'note', 'source', 'sha'];
const esc = (v) => (v === undefined || v === null ? '' : /[",\n]/.test(String(v)) ? `"${String(v).replaceAll('"', '""')}"` : String(v));
fs.writeFileSync(`${OUT}/manifest.csv`, [cols.join(','), ...rows.map((r) => cols.map((c) => esc(c === 'dur' && r.dur ? r.dur.toFixed(2) : r[c])).join(','))].join('\r\n'));
fs.writeFileSync(`${OUT}/manifest.js`, 'window.MANIFEST = ' + JSON.stringify(rows.map(({ sha, ...r }) => r)) + ';');
for (const f of ['START-HERE.html', 'RETURN-SPEC.md', 'CHANGES-TEMPLATE.txt']) fs.copyFileSync(`C:/Users/Benji/AppData/Local/Temp/claude/design-tpl/${f}`, `${OUT}/${f}`);
console.log(JSON.stringify({ files: rows.length, bytes: rows.reduce((a, r) => a + r.bytes, 0), bySurface: rows.reduce((a, r) => ((a[r.surface] = (a[r.surface] ?? 0) + 1), a), {}) }));
