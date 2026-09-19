"""Procedural sound set for Puzzle Pack — warm, glassy, "gold" palette.

Design: sine/triangle partials with soft attack, short exponential decay,
gentle low-pass, light reverb tail. Pitches sit in a pentatonic (A major)
so cascades and jingles always sound consonant. Output 22.05 kHz mono WAV.
"""
import math, os, wave, struct
import numpy as np

OUT = "/sessions/compassionate-sleepy-mccarthy/mnt/outputs/sfx"
os.makedirs(OUT, exist_ok=True)
SR = 22050
rng = np.random.default_rng(7)

def t(dur): return np.arange(int(SR * dur)) / SR

def env(n, a=0.004, d=0.25, sustain=0.0, r=0.05, curve=6.0):
    """Attack / exponential decay / release envelope."""
    x = np.linspace(0, 1, n)
    out = np.ones(n)
    ai = int(a * SR); di = int(d * SR); ri = int(r * SR)
    if ai > 0: out[:ai] = np.linspace(0, 1, ai)
    dec = np.exp(-curve * np.linspace(0, 1, max(1, n - ai)))
    out[ai:] = sustain + (1 - sustain) * dec[: n - ai]
    if ri > 0 and ri < n: out[-ri:] *= np.linspace(1, 0, ri)
    return out

def tone(freq, dur, partials=((1, 1.0), (2, 0.35), (3, 0.12), (4.01, 0.05)), a=0.004, d=0.25, curve=6.0,
         detune=0.0, bend=0.0):
    tt = t(dur); n = len(tt)
    f = freq * (1 + bend * (1 - np.exp(-tt * 30)))  # quick pitch settle
    sig = np.zeros(n)
    for mult, amp in partials:
        ph = 2 * np.pi * np.cumsum(f * mult) / SR
        sig += amp * np.sin(ph)
        if detune:
            ph2 = 2 * np.pi * np.cumsum(f * mult * (1 + detune)) / SR
            sig += amp * 0.6 * np.sin(ph2)
    return sig * env(n, a=a, d=d, curve=curve)

def noise(dur, a=0.002, d=0.08, curve=8.0, lp=0.3):
    n = int(SR * dur)
    x = rng.standard_normal(n)
    # one-pole low-pass
    y = np.zeros(n); acc = 0.0
    for i in range(n):
        acc += lp * (x[i] - acc); y[i] = acc
    return y * env(n, a=a, d=d, curve=curve)

def lowpass(sig, lp=0.25):
    y = np.zeros_like(sig); acc = 0.0
    for i in range(len(sig)):
        acc += lp * (sig[i] - acc); y[i] = acc
    return y

def reverb(sig, mix=0.18, taps=((0.031, 0.5), (0.053, 0.35), (0.079, 0.25), (0.113, 0.15))):
    out = np.copy(sig)
    for delay, g in taps:
        d = int(delay * SR)
        out[d:] += mix * g * sig[:-d]
    return out

class S(np.ndarray):
    pass

def _pad(a, b):
    n = max(len(a), len(b)); return np.pad(a, (0, n - len(a))), np.pad(b, (0, n - len(b)))

def add(*parts):
    n = max(len(p) for p in parts); out = np.zeros(n)
    for p in parts: out[: len(p)] += p
    return out

def mix(*parts):
    n = max(len(p) for p in parts)
    out = np.zeros(n)
    for p in parts: out[: len(p)] += p
    return out

def seq(events):
    """events: list of (start_sec, signal)."""
    n = max(int(s * SR) + len(sig) for s, sig in events)
    out = np.zeros(n)
    for s, sig in events:
        i = int(s * SR); out[i : i + len(sig)] += sig
    return out

def norm(sig, peak=0.85):
    m = np.max(np.abs(sig)) or 1.0
    return sig / m * peak

def save(name, sig, peak=0.85):
    sig = norm(sig, peak)
    data = (np.clip(sig, -1, 1) * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name), "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(data.tobytes())
    print(name, f"{len(sig)/SR:.2f}s")

# Pentatonic A major: A C# E F# A ...
A4 = 440.0
def n(semi, octave=0): return A4 * 2 ** ((semi + 12 * octave) / 12)
PENT = [0, 4, 7, 9, 12, 16, 19, 21, 24]

# --- UI ---
save("tap.wav", reverb(add(tone(n(12), 0.09, d=0.06, curve=9), 0.3 * noise(0.03, d=0.02)), mix=0.08), 0.6)
save("swap.wav", reverb(add(tone(n(7), 0.12, d=0.08, curve=8, bend=0.08) * 0.8, 0.25 * noise(0.05, d=0.03, lp=0.5)), mix=0.1), 0.6)
save("invalid.wav", lowpass(add(tone(n(-14), 0.22, partials=((1, 1), (1.5, 0.5), (2.7, 0.2)), d=0.15, curve=7),
                            tone(n(-13.6), 0.22, d=0.15, curve=7) * 0.5), 0.2), 0.7)

# --- Pops: three pitches for cascade depth ---
for i, semi in enumerate([12, 16, 19]):
    pop = tone(n(semi), 0.16, partials=((1, 1), (2, 0.4), (3, 0.15)), d=0.1, curve=9, bend=-0.06)
    click = noise(0.02, d=0.012, lp=0.6) * 0.5
    save(f"pop{i+1}.wav", reverb(add(pop, click), mix=0.12), 0.75)

# gem land (soft thud)
save("land.wav", lowpass(add(tone(n(-10), 0.08, partials=((1, 1), (2, 0.2)), d=0.05, curve=10), 0.3 * noise(0.03, d=0.02, lp=0.15)), 0.3), 0.45)

# --- Specials ---
sparkle = seq([(k * 0.035, tone(n(PENT[(k + 3) % len(PENT)], 1), 0.25, d=0.18, curve=7) * (0.9 - k * 0.1)) for k in range(6)])
save("special_create.wav", reverb(sparkle, mix=0.25), 0.7)

whoosh = noise(0.35, a=0.02, d=0.28, curve=4, lp=0.12)
sweep_t = t(0.35); sweep = np.sin(2 * np.pi * np.cumsum(220 + 900 * (sweep_t / 0.35) ** 2) / SR) * env(len(sweep_t), a=0.01, d=0.3, curve=3)
boom = lowpass(tone(n(-24), 0.5, partials=((1, 1), (2, 0.3)), d=0.4, curve=5), 0.15)
save("special_fire.wav", reverb(add(whoosh * 0.9, sweep * 0.5, boom * 0.8), mix=0.25), 0.85)

# bomb (bigger)
rumble = lowpass(noise(0.8, a=0.005, d=0.6, curve=4, lp=0.08), 0.1)
save("bomb.wav", reverb(add(boom * 1.2, rumble, seq([(0.0, tone(n(0, 1), 0.4, d=0.3)), (0.08, tone(n(4, 1), 0.4, d=0.3)), (0.16, tone(n(7, 1), 0.5, d=0.4))]) * 0.6), mix=0.3), 0.9)

# --- Combo chimes: rising with depth ---
for i in range(2, 6):
    notes = PENT[i : i + 3]
    ch = seq([(k * 0.06, tone(n(s, 1), 0.3, d=0.22, curve=6)) for k, s in enumerate(notes)])
    save(f"combo{i}.wav", reverb(ch, mix=0.25), 0.7)

# --- Level end ---
win = seq([
    (0.00, tone(n(0), 0.5, d=0.4)), (0.12, tone(n(4), 0.5, d=0.4)), (0.24, tone(n(7), 0.5, d=0.4)),
    (0.36, tone(n(12), 0.9, d=0.7, detune=0.004)), (0.36, tone(n(4, 1), 0.9, d=0.7) * 0.6),
    (0.60, tone(n(16), 1.0, d=0.8, detune=0.004) * 0.8),
])
save("win.wav", reverb(win, mix=0.3), 0.85)

lose = seq([(0.0, tone(n(7), 0.5, d=0.4)), (0.22, tone(n(3), 0.5, d=0.4)), (0.44, tone(n(-2), 1.0, d=0.8))])
save("lose.wav", reverb(lowpass(lose, 0.35), mix=0.3), 0.75)

for i in range(3):
    save(f"star{i+1}.wav", reverb(tone(n(12 + [0, 4, 7][i], 1), 0.45, d=0.35, detune=0.003), mix=0.3), 0.7)

# --- Ambient loop (24 s) ---
DUR = 24.0
tt = t(DUR); N = len(tt)
chords = [[0, 4, 7, 11], [-3, 0, 4, 7], [-5, 0, 4, 9], [-7, -3, 0, 4]]  # Amaj7 F#m7 Dmaj9-ish E-ish
amb = np.zeros(N)
seg = N // len(chords)
for ci, ch in enumerate(chords):
    for semi in ch:
        for octv, amp in ((-1, 0.5), (0, 0.35), (1, 0.12)):
            f = n(semi, octv)
            # slow LFO detuned pair for shimmer
            lfo = 1 + 0.0015 * np.sin(2 * np.pi * 0.07 * tt + semi)
            partial = np.sin(2 * np.pi * np.cumsum(f * lfo) / SR) + 0.5 * np.sin(2 * np.pi * np.cumsum(f * 1.003) / SR)
            g = np.zeros(N)
            s, e = ci * seg, min(N, (ci + 1) * seg)
            fade = int(1.5 * SR)
            g[s:e] = 1
            g[s : s + fade] = np.linspace(0, 1, fade); g[e - fade : e] = np.linspace(1, 0, fade)
            amb += amp * partial * g
# breathing filter + very quiet sparkle
amb = lowpass(amb, 0.05)
amb *= 0.6 + 0.4 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.05 * tt))
spark = np.zeros(N)
for k in range(40):
    st = rng.uniform(0, DUR - 1); semi = PENT[rng.integers(len(PENT))]
    s = tone(n(semi, 1), 0.8, d=0.7, curve=5) * rng.uniform(0.03, 0.08)
    i = int(st * SR); spark[i : i + len(s)] += s[: N - i]
amb = add(amb, spark)
# seamless-ish loop: crossfade tail into head
xf = int(1.0 * SR)
amb[:xf] = amb[:xf] * np.linspace(0, 1, xf) + amb[-xf:] * np.linspace(1, 0, xf)
amb = amb[:-xf]
save("ambient.wav", reverb(amb, mix=0.2), 0.5)

print("done", len(os.listdir(OUT)))
