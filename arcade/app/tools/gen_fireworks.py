"""Firework audio for the Coin Quest win screen.

A firework is three sounds, not one, and using a single "boom" is what makes
game fireworks sound like a door slamming:

  * the lift — a hissing whistle that climbs while the shell rises;
  * the break — a hard transient, a low body that carries the distance, and a
    short tail of debris;
  * the crackle — several dozen tiny ticks scattered over a second as the
    stars burn out.

Three takes of each, so a seven-shell show never fires the same sample twice
in a row, plus one finale that breaks three times in 200 ms.

Everything is synthesised; no samples. 44.1 kHz mono 16-bit to match the rest
of the effects bed, levelled to leave headroom under the voice lines.
"""
import os
import wave

import numpy as np

OUT = r"C:\src\puzzle-app\assets\audio"
SR = 44100
RNG = np.random.default_rng(20260915)


def write(name, x, peak=0.72):
    """Normalise, soft-clip and write. Peak sits under the voice lines."""
    x = np.nan_to_num(x)
    m = np.max(np.abs(x))
    if m > 0:
        x = x / m * peak
    # Gentle saturation rather than a hard ceiling — a clipped transient reads
    # as a click on a phone speaker.
    x = np.tanh(x * 1.25) / np.tanh(1.25) * peak
    # 3 ms fades so nothing starts or ends on a step.
    n = int(SR * 0.003)
    if len(x) > 2 * n:
        x[:n] *= np.linspace(0, 1, n)
        x[-n:] *= np.linspace(1, 0, n)
    with wave.open(os.path.join(OUT, name), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())
    print(f"  {name:20} {os.path.getsize(os.path.join(OUT, name)) // 1024:3} KB"
          f"  {len(x) / SR:.2f}s")


def noise(dur):
    return RNG.normal(0, 1, int(SR * dur))


def onepole_lp(x, cutoff):
    """Cheap one-pole low-pass. Cutoff may be an array for a sweep."""
    a = np.exp(-2 * np.pi * np.asarray(cutoff, dtype=float) / SR)
    a = np.broadcast_to(a, x.shape).copy()
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a[i]) * x[i] + a[i] * acc
        y[i] = acc
    return y


def onepole_hp(x, cutoff):
    return x - onepole_lp(x, cutoff)


def bandpass(x, lo, hi):
    return onepole_hp(onepole_lp(x, hi), lo)


def env(dur, attack, decay, curve=3.0):
    """Percussive envelope: near-instant rise, exponential fall."""
    n = int(SR * dur)
    t = np.arange(n) / SR
    a = np.clip(t / max(attack, 1e-5), 0, 1)
    d = np.exp(-curve * np.clip((t - attack) / max(decay, 1e-5), 0, None))
    return a * d


# ----------------------------------------------------------------- the lift

def lift(dur=0.72, f0=780, f1=2300):
    """Rising hiss plus a thin whistle gliding up with it."""
    n = int(SR * dur)
    t = np.arange(n) / SR
    # Ease the climb: a shell decelerates as it rises.
    k = 1 - (1 - t / dur) ** 2
    centre = f0 + (f1 - f0) * k

    hiss = bandpass(noise(dur), centre * 0.55, centre * 1.7)
    # Swell in, then duck away as it reaches the top of the arc.
    shape = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.7
    hiss *= shape

    phase = 2 * np.pi * np.cumsum(centre * 1.35) / SR
    whistle = np.sin(phase) * shape * 0.30
    # A little vibrato keeps the tone from sounding like a test oscillator.
    whistle *= 1 + 0.08 * np.sin(2 * np.pi * 11 * t)

    return hiss * 0.55 + whistle


# ---------------------------------------------------------------- the break

def break_(dur=1.25, size=1.0, distance=0.35):
    """Transient + low body + debris tail.

    `size` scales the body's pitch down and its length up. `distance` rolls
    off the highs and delays the body, which is most of what makes one shell
    read as further away than another.
    """
    n = int(SR * dur)
    out = np.zeros(n)

    # Crack: a few milliseconds of bright noise. This is the part the ear
    # locates; without it the boom has no position.
    crack = noise(dur) * env(dur, 0.0004, 0.055, curve=6)
    crack = onepole_hp(crack, 900) * (1.0 - 0.55 * distance)
    out += crack * 0.9

    # Body: the low thump, pitch falling as it decays.
    t = np.arange(n) / SR
    f = (95 / size) * np.exp(-2.6 * t) + 32
    body = np.sin(2 * np.pi * np.cumsum(f) / SR)
    body *= env(dur, 0.004, 0.26 * size, curve=3.2)
    # Distance delays the body behind the crack — sound takes its time.
    shift = int(SR * 0.012 * distance)
    out[shift:] += (body * 0.85)[: n - shift]

    # Tail: burning debris, darkening as it goes.
    tail = noise(dur) * env(dur, 0.01, 0.42 * size, curve=2.4)
    tail = onepole_lp(tail, np.linspace(4200, 600, n)) * (1.0 - 0.4 * distance)
    out += tail * 0.5

    return out


# -------------------------------------------------------------- the crackle

def crackle(dur=1.35, ticks=70):
    """Dozens of tiny ticks thinning out over the second after the break."""
    n = int(SR * dur)
    out = np.zeros(n)
    # Weight the times early: crackle is densest right after the break.
    times = np.sort(RNG.random(ticks) ** 1.7) * dur * 0.92
    for tm in times:
        i = int(tm * SR)
        ln = int(SR * RNG.uniform(0.004, 0.011))
        if i + ln >= n:
            continue
        tick = RNG.normal(0, 1, ln) * np.exp(-np.linspace(0, 7, ln))
        tick = onepole_hp(tick, RNG.uniform(1800, 4200))
        # Quieter as the shell burns out.
        out[i:i + ln] += tick * (1 - tm / dur) ** 1.4 * RNG.uniform(0.5, 1.0)
    return out


def finale(dur=2.1):
    """Three breaks inside 200 ms, the way a show ends."""
    n = int(SR * dur)
    out = np.zeros(n)
    for off, sz, dist in ((0.0, 1.25, 0.15), (0.09, 0.9, 0.45), (0.2, 1.1, 0.3)):
        b = break_(dur - off, size=sz, distance=dist)
        i = int(off * SR)
        out[i:i + len(b)] += b * (0.9 if off else 1.0)
    c = crackle(dur * 0.8, ticks=110)
    out[int(SR * 0.18):int(SR * 0.18) + len(c)] += c * 0.55
    return out


if __name__ == "__main__":
    print("fireworks")
    for i, (f0, f1, d) in enumerate(
        ((760, 2200, 0.68), (840, 2500, 0.78), (700, 2050, 0.62)), start=1
    ):
        write(f"fw_lift_{i}.wav", lift(d, f0, f1), peak=0.42)

    for i, (sz, dist) in enumerate(((1.0, 0.25), (0.82, 0.55), (1.18, 0.12)), start=1):
        write(f"fw_burst_{i}.wav", break_(size=sz, distance=dist), peak=0.78)

    for i, ticks in enumerate((70, 55, 88), start=1):
        write(f"fw_crackle_{i}.wav", crackle(ticks=ticks), peak=0.40)

    write("fw_finale.wav", finale(), peak=0.82)
