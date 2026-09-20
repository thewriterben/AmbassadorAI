"""Coin Quest sound set — metal, coins, vault. Same filenames as before.

Timbre notes:
  coin clink  = inharmonic metal partials (ratios ~1, 2.76, 5.4, 8.9) with a
                very fast attack, short ring, tiny noise transient.
  cha-ching   = register bell (bright harmonic) + drawer slide (filtered noise)
  vault thunk = sub thud + metallic ring + latch click
  dial click  = short filtered click with faint ring
Key: A major pentatonic so clinks in a cascade remain consonant.
"""
import os, wave
import numpy as np

OUT = "/sessions/compassionate-sleepy-mccarthy/mnt/outputs/cq_sfx"
os.makedirs(OUT, exist_ok=True)
SR = 22050
rng = np.random.default_rng(21)

def t(dur): return np.arange(int(SR * dur)) / SR

def env(n, a=0.002, curve=8.0, r=0.03):
    out = np.exp(-curve * np.linspace(0, 1, n))
    ai = int(a * SR); ri = int(r * SR)
    if ai > 0: out[:ai] *= np.linspace(0, 1, ai)
    if 0 < ri < n: out[-ri:] *= np.linspace(1, 0, ri)
    return out

def add(*parts):
    n = max(len(p) for p in parts); out = np.zeros(n)
    for p in parts: out[: len(p)] += p
    return out

def seq(events):
    n = max(int(s * SR) + len(sig) for s, sig in events); out = np.zeros(n)
    for s, sig in events:
        i = int(s * SR); out[i : i + len(sig)] += sig
    return out

def lowpass(sig, lp=0.25):
    y = np.zeros_like(sig); acc = 0.0
    for i in range(len(sig)):
        acc += lp * (sig[i] - acc); y[i] = acc
    return y

def highpass(sig, lp=0.1):
    return sig - lowpass(sig, lp)

def reverb(sig, mix=0.18, taps=((0.023, 0.5), (0.041, 0.35), (0.067, 0.25), (0.097, 0.15))):
    out = np.copy(sig)
    for delay, g in taps:
        d = int(delay * SR); out[d:] += mix * g * sig[:-d]
    return out

def noise(dur, a=0.001, curve=10.0, lp=0.5):
    n = int(SR * dur); return lowpass(rng.standard_normal(n), lp) * env(n, a=a, curve=curve)

# ---- metal ----
METAL = ((1.0, 1.0), (2.76, 0.55), (5.40, 0.30), (8.93, 0.14), (13.3, 0.06))   # bell/bar inharmonic set
COIN  = ((1.0, 1.0), (1.51, 0.4), (2.76, 0.6), (4.2, 0.25), (5.4, 0.35), (7.1, 0.1))  # thinner disc

def metal(freq, dur, partials=METAL, curve=7.0, a=0.001, wobble=0.0):
    tt = t(dur); n = len(tt); sig = np.zeros(n)
    for i, (ratio, amp) in enumerate(partials):
        f = freq * ratio * (1 + wobble * np.sin(2 * np.pi * (6 + i) * tt))
        # higher partials die faster
        e = np.exp(-curve * (1 + i * 0.6) * np.linspace(0, 1, n))
        sig += amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * e
    ai = int(a * SR)
    if ai > 0: sig[:ai] *= np.linspace(0, 1, ai)
    return sig

def clink(freq, dur=0.22, vol=1.0, bright=1.0):
    body = metal(freq, dur, COIN, curve=9)
    tick = highpass(noise(0.012, curve=14, lp=0.9), 0.3) * 0.7 * bright
    return add(body, tick) * vol

def tone(freq, dur, partials=((1, 1.0), (2, 0.4), (3, 0.15)), curve=6.0, a=0.003, detune=0.0):
    tt = t(dur); n = len(tt); sig = np.zeros(n)
    for m, amp in partials:
        sig += amp * np.sin(2 * np.pi * freq * m * tt)
        if detune: sig += amp * 0.5 * np.sin(2 * np.pi * freq * m * (1 + detune) * tt)
    return sig * env(n, a=a, curve=curve)

def norm(sig, peak): m = np.max(np.abs(sig)) or 1.0; return sig / m * peak

TRIM_DB = -2.0  # master trim applied to every file
def save(name, sig, peak=0.85):
    peak = peak * 10 ** (TRIM_DB / 20)
    data = (np.clip(norm(sig, peak), -1, 1) * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name), "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(data.tobytes())
    print(name, f"{len(sig)/SR:.2f}s")

A4 = 440.0
SFX_PITCH_SEMI = -2.0  # global pitch shift for effects (not the music)
PITCH = 2 ** (SFX_PITCH_SEMI / 12)
def n(semi, octv=0): return A4 * PITCH * 2 ** ((semi + 12 * octv) / 12)
PENT = [0, 4, 7, 9, 12, 16, 19, 21, 24]

# ---- UI: vault dial click / coin tap ----
save("tap.wav", reverb(add(highpass(noise(0.03, curve=16, lp=0.7), 0.2), metal(n(24), 0.08, curve=14) * 0.4), mix=0.06), 0.55)

# swap: coin slide + light clink
slide = lowpass(noise(0.10, a=0.01, curve=6, lp=0.35), 0.4)
save("swap.wav", reverb(add(slide * 0.6, clink(n(19), 0.14, 0.7, bright=0.6)), mix=0.08), 0.6)

# invalid: dull coin on felt (dead thud, no ring)
thud = lowpass(add(tone(n(-16), 0.16, partials=((1, 1), (1.6, 0.3)), curve=12), noise(0.05, curve=12, lp=0.2)), 0.2)
save("invalid.wav", add(thud, thud * 0.5 * np.concatenate([np.zeros(int(0.07 * SR)), np.ones(len(thud) - int(0.07 * SR))])), 0.7)

# pops: coin clinks, rising with cascade depth; each a tiny 2-coin double hit
for i, semi in enumerate([12, 16, 19]):
    c1 = clink(n(semi), 0.24, 1.0)
    c2 = clink(n(semi + 7), 0.18, 0.55)
    save(f"pop{i+1}.wav", reverb(seq([(0.0, c1), (0.028, c2)]), mix=0.12), 0.8)

# land: coins settling on the tray (soft metal patter)
land = seq([(k * 0.018, clink(n(PENT[rng.integers(3, 7)], -1), 0.10, 0.35, bright=0.4)) for k in range(4)])
save("land.wav", lowpass(land, 0.6), 0.45)

# special create: coin spin-down (rising pitch flutter, accelerating)
tt = t(0.6); rate = 8 + 40 * (tt / 0.6) ** 2
spin = np.zeros(len(tt))
for k in range(1, 22):
    # each "flip" emits a soft clink; spacing shrinks
    tk = 0.6 * (1 - (1 - k / 22) ** 0.5)
    i = int(tk * SR)
    c = clink(n(16 + (k % 3) * 2), 0.09, 0.5 * (1 - k / 30), bright=0.5)
    spin[i : i + len(c)] += c[: len(spin) - i]
save("special_create.wav", reverb(spin, mix=0.2), 0.7)

# special fire: vault bolt slide + metallic sweep + thunk
bolt = lowpass(noise(0.32, a=0.03, curve=4, lp=0.12), 0.3)
sw_t = t(0.32); sweep = np.sin(2 * np.pi * np.cumsum((180 + 1100 * (sw_t / 0.32) ** 2) * PITCH) / SR) * env(len(sw_t), a=0.01, curve=3)
thunk = lowpass(add(tone(n(-24), 0.5, partials=((1, 1), (2, 0.3)), curve=6), metal(n(-5), 0.5, curve=5) * 0.5), 0.2)
save("special_fire.wav", reverb(seq([(0.0, bolt * 0.9), (0.0, sweep * 0.35), (0.22, thunk)]), mix=0.25), 0.85)

# bomb: mint press — big metallic slam + shimmer of many coins
slam = lowpass(add(tone(n(-26), 0.7, partials=((1, 1), (2, 0.4), (3, 0.15)), curve=5), noise(0.12, curve=8, lp=0.15) * 1.2), 0.25)
shimmer = seq([(0.05 + rng.uniform(0, 0.45), clink(n(PENT[rng.integers(4, 9)], 1), 0.25, rng.uniform(0.2, 0.5), 0.6)) for _ in range(18)])
save("bomb.wav", reverb(add(slam * 1.3, metal(n(-3), 0.9, curve=4) * 0.6, shimmer), mix=0.3), 0.9)

# combos: quick coin runs up the pentatonic (2..5 notes)
for i in range(2, 6):
    notes = PENT[i : i + 3]
    run = seq([(k * 0.055, clink(n(s, 1), 0.3, 0.9 - k * 0.15)) for k, s in enumerate(notes)])
    save(f"combo{i}.wav", reverb(run, mix=0.22), 0.72)

# win: cha-ching — register bell + drawer + coin shower (a few clinks, not "rain")
bell = tone(n(12), 1.1, partials=((1, 1), (2, 0.5), (3, 0.3), (4.2, 0.15), (5.9, 0.08)), curve=4, detune=0.003)
drawer = lowpass(noise(0.28, a=0.02, curve=5, lp=0.25), 0.5)
latch = highpass(noise(0.02, curve=16, lp=0.8), 0.3)
coins = seq([(0.35 + k * 0.045, clink(n(PENT[(k * 2) % 9], 1), 0.3, 0.8 - k * 0.08)) for k in range(7)])
save("win.wav", reverb(seq([(0.0, bell), (0.0, latch * 0.8), (0.06, drawer * 0.8), (0.0, coins)]), mix=0.3), 0.85)

# lose: vault door closing — heavy swing + sub thud + ring decay
swing = lowpass(noise(0.5, a=0.15, curve=3, lp=0.1), 0.25)
door = lowpass(add(tone(n(-28), 0.9, partials=((1, 1), (2, 0.35)), curve=5), metal(n(-8), 1.0, curve=3) * 0.5), 0.25)
save("lose.wav", reverb(seq([(0.0, swing * 0.8), (0.42, door), (0.42, highpass(noise(0.02, curve=16, lp=0.8), 0.3) * 0.6)]), mix=0.3), 0.8)

# stars: coin drop into a dish — clink + short bounce
for i in range(3):
    base = n(12 + [0, 4, 7][i], 1)
    s = seq([(0.0, clink(base, 0.35, 1.0)), (0.11, clink(base, 0.22, 0.45)), (0.18, clink(base, 0.14, 0.2))])
    save(f"star{i+1}.wav", reverb(s, mix=0.28), 0.75)

# payout: long coin cascade into a metal tray + bell swell (the "flashy" win)
cascade = seq([(0.02 * k + rng.uniform(0, 0.015), clink(n(PENT[rng.integers(2, 9)], rng.integers(0, 2)), 0.28, rng.uniform(0.35, 0.9), 0.9)) for k in range(70)])
swell = tone(n(12), 2.0, partials=((1, 1), (2, 0.5), (3, 0.3), (4.2, 0.2), (5.9, 0.1)), curve=2.5, a=0.3, detune=0.004)
swell2 = tone(n(16), 2.0, partials=((1, 1), (2, 0.4), (3, 0.2)), curve=2.5, a=0.5, detune=0.004) * 0.7
tray = lowpass(noise(1.6, a=0.05, curve=3, lp=0.2), 0.3) * 0.5
save("payout.wav", reverb(add(cascade, swell * 0.5, swell2 * 0.4, tray), mix=0.3), 0.9)

# ---- extra coin foley ----
# coin flip: fingernail flick + short accelerating flutter (select a piece)
flick = highpass(noise(0.02, curve=14, lp=0.85), 0.25)
flut = seq([(0.03 + k * (0.035 - k * 0.0018), clink(n(19 + (k % 2) * 3), 0.07, 0.35 - k * 0.03, 0.5)) for k in range(8)])
save("coin_flip.wav", reverb(add(flick * 0.9, flut), mix=0.1), 0.6)

# coin roll: edge rolling on a wooden tray, slowing into a wobble-settle (swap)
rt = t(0.55)
roll_n = lowpass(rng.standard_normal(len(rt)), 0.25) * (0.35 + 0.65 * np.sin(2 * np.pi * np.cumsum(28 - 20 * rt / 0.55) / SR) ** 2)
roll_n *= np.exp(-2.5 * rt / 0.55)
wobble = seq([(0.30 + 0.06 * k + 0.004 * k * k, clink(n(14), 0.05, 0.25 * (1 - k / 7), 0.3)) for k in range(6)])
save("coin_roll.wav", reverb(add(roll_n * 0.5, wobble), mix=0.1), 0.5)

# coin drop: single coin onto a tray, two bounces (piece settling)
drop = seq([(0.0, clink(n(9), 0.22, 1.0)), (0.09, clink(n(9), 0.14, 0.45)), (0.15, clink(n(9), 0.09, 0.2)), (0.19, lowpass(noise(0.05, curve=10, lp=0.3), 0.3) * 0.4)])
save("coin_drop.wav", reverb(drop, mix=0.12), 0.55)

# coin spin: long wobbling spin-down on a hard surface (hint appears)
spin_t = t(1.1); spin_sig = np.zeros(len(spin_t))
for k in range(1, 34):
    tk = 1.1 * (1 - (1 - k / 34) ** 0.55)
    i = int(tk * SR); c = clink(n(16), 0.06, 0.28 * (0.4 + 0.6 * k / 34), 0.4)
    spin_sig[i:i+len(c)] += c[:len(spin_sig) - i]
save("coin_spin.wav", reverb(add(spin_sig, lowpass(noise(1.0, a=0.2, curve=2, lp=0.2), 0.3) * 0.15), mix=0.15), 0.5)

# ting: a single tiny bright ring (sparkle / sheen)
save("ting.wav", reverb(metal(n(24, 1), 0.5, partials=((1, 1), (2.76, 0.3), (5.4, 0.08)), curve=5), mix=0.3), 0.35)

# coins pour: a small handful poured into a dish (map / menu)
pour = seq([(rng.uniform(0, 0.45), clink(n(PENT[rng.integers(2, 8)], rng.integers(0, 2)), 0.2, rng.uniform(0.25, 0.7), 0.7)) for _ in range(16)])
save("coins_pour.wav", reverb(add(pour, lowpass(noise(0.5, a=0.02, curve=4, lp=0.25), 0.4) * 0.3), mix=0.2), 0.6)

# music keeps concert pitch
PITCH = 1.0

# ---- ambient: "counting house" — music-box plucks over a warm pad, 24 s ----
DUR = 24.0; tt = t(DUR); N = len(tt)
pad = np.zeros(N)
chords = [[0, 4, 7, 11], [-3, 0, 4, 7], [-5, 0, 4, 9], [-7, -3, 0, 4]]
seg = N // 4
for ci, ch in enumerate(chords):
    g = np.zeros(N); s, e = ci * seg, min(N, (ci + 1) * seg); f = int(1.2 * SR)
    g[s:e] = 1; g[s:s+f] = np.linspace(0, 1, f); g[e-f:e] = np.linspace(1, 0, f)
    for semi in ch:
        for octv, amp in ((-1, 0.45), (0, 0.3)):
            fr = n(semi, octv)
            pad += amp * (np.sin(2 * np.pi * fr * tt) + 0.5 * np.sin(2 * np.pi * fr * 1.004 * tt)) * g
pad = lowpass(pad, 0.04) * (0.7 + 0.3 * np.sin(2 * np.pi * 0.04 * tt))
# music-box melody: sparse pentatonic plucks on an 8th-note grid at 84 bpm
beat = 60 / 84 / 2
plucks = np.zeros(N)
melody = [0, 4, 7, 12, 9, 7, 4, 0, 16, 12, 9, 7, 4, 7, 12, 19]
for k in range(int(DUR / beat)):
    if rng.random() < 0.55:
        semi = melody[k % len(melody)] + (12 if rng.random() < 0.2 else 0)
        p = metal(n(semi, 1), 0.9, partials=((1, 1), (2.76, 0.25), (5.4, 0.08)), curve=6) * rng.uniform(0.08, 0.16)
        i = int(k * beat * SR); plucks[i:i+len(p)] += p[:N-i]
amb = add(pad, plucks)
xf = int(1.0 * SR)
amb[:xf] = amb[:xf] * np.linspace(0, 1, xf) + amb[-xf:] * np.linspace(1, 0, xf)
amb = amb[:-xf]
save("ambient.wav", reverb(amb, mix=0.22), 0.5)
print("done")
