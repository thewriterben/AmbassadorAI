"""Coin Quest audio, third pass: percussion.

Drums, thumps and pops replace the metal palette. Every sound is built from
three primitives rather than sampled:

  kick  - a pitch-swept sine with a click transient
  tom   - a shorter sweep, tuned, with a touch of body
  snare - noise through a bandpass plus two tuned partials
  pop   - a very short pitched blip with a sharp attack

Cascade depth walks up a tom tuning, so a long chain plays as a fill rather
than the same hit twelve times. Three round-robin takes of everything that
repeats; the limiter in audio.dart handles the rest.
"""
import os
import shutil
import subprocess
import wave

import numpy as np

OUT = r"C:\src\puzzle-app\assets\audio"
SR = 22050
TRIM_DB = -2.0
rng = np.random.default_rng(11)


def t(dur):
    return np.arange(int(SR * dur)) / SR


def env(n, a=0.001, curve=9.0):
    e = np.exp(-curve * np.linspace(0, 1, n))
    ai = max(1, int(a * SR))
    e[:ai] *= np.linspace(0, 1, ai)
    return e


def add(*parts):
    n = max(len(p) for p in parts)
    out = np.zeros(n)
    for p in parts:
        out[: len(p)] += p
    return out


def lowpass(sig, k=0.25):
    out = np.zeros_like(sig)
    acc = 0.0
    for i, s in enumerate(sig):
        acc += k * (s - acc)
        out[i] = acc
    return out


def highpass(sig, k=0.1):
    return sig - lowpass(sig, k)


def bandpass(sig, lo=0.05, hi=0.45):
    return lowpass(sig, hi) - lowpass(sig, lo)


def reverb(sig, mix=0.12, taps=((0.017, 0.5), (0.031, 0.32), (0.053, 0.2))):
    out = sig.copy()
    for delay, gain in taps:
        d = int(delay * SR)
        if d < len(sig):
            out[d:] += sig[:-d] * gain * mix
    return out


def noise(dur, a=0.0005, curve=12.0):
    n = int(SR * dur)
    return rng.uniform(-1, 1, n) * env(n, a=a, curve=curve)


# ------------------------------------------------------------- primitives

def kick(f0=110, f1=42, dur=0.34, curve=7.0, click=0.5):
    """Pitch-swept sine: the thump."""
    tt = t(dur)
    n = len(tt)
    sweep = f1 + (f0 - f1) * np.exp(-9 * tt)
    body = np.sin(2 * np.pi * np.cumsum(sweep) / SR) * env(n, a=0.0008, curve=curve)
    tick = highpass(noise(0.006, curve=30), 0.45) * click
    return add(body, tick)


def tom(freq=180, dur=0.26, curve=9.0, bend=0.55):
    """Tuned drum: shorter sweep, a little skin noise."""
    tt = t(dur)
    n = len(tt)
    sweep = freq * (1 + bend * np.exp(-16 * tt))
    body = np.sin(2 * np.pi * np.cumsum(sweep) / SR) * env(n, a=0.0006, curve=curve)
    skin = bandpass(noise(dur * 0.3, curve=20), 0.10, 0.55) * 0.28
    return add(body, skin)


def snare(dur=0.24, tune=190, bright=1.0):
    n = int(SR * dur)
    rattle = bandpass(noise(dur, curve=11), 0.06, 0.60) * 1.0 * bright
    shell = (np.sin(2 * np.pi * tune * t(dur)) + 0.7 * np.sin(2 * np.pi * tune * 1.48 * t(dur)))
    return add(rattle, shell * env(n, a=0.0006, curve=14) * 0.55)


def pop(freq=520, dur=0.075, curve=26.0):
    """Short pitched blip: the match sound."""
    n = int(SR * dur)
    tt = t(dur)
    sweep = freq * (1 + 0.9 * np.exp(-40 * tt))
    body = np.sin(2 * np.pi * np.cumsum(sweep) / SR) * env(n, a=0.0004, curve=curve)
    tick = highpass(noise(0.004, curve=40), 0.5) * 0.45
    return add(body, tick)


def norm(sig, peak):
    m = np.max(np.abs(sig)) or 1.0
    return sig / m * peak


def save(name, sig, peak=0.85):
    peak = peak * 10 ** (TRIM_DB / 20)
    data = (np.clip(norm(sig, peak), -1, 1) * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    print(f"  {name:24} {len(sig)/SR:5.2f}s")


def variants(name, make, count=3):
    for i in range(count):
        save(f"{name}{i + 1}.wav", make(i))


def build():
    print("percussion")
    # Match pops: a tom tuning that climbs with cascade depth, so a long chain
    # plays as a drum fill instead of one sound repeated.
    tunings = [150, 178, 205, 244, 290]
    for depth, freq in enumerate(tunings, start=1):
        def make(i, freq=freq, depth=depth):
            detune = 1 + (i - 1) * 0.02
            return add(
                tom(freq * detune, 0.20 + depth * 0.012, curve=11.0),
                pop(freq * 2.6 * detune, 0.06) * 0.55,
            )
        variants(f"pop{depth}_", make)

    variants("tap_", lambda i: pop(430 * (1 + (i - 1) * 0.03), 0.055, curve=32) * 0.9)
    variants("swap_", lambda i: add(tom(210 * (1 + (i - 1) * 0.02), 0.13, curve=16), pop(600, 0.04) * 0.35))
    # Invalid: a dead, damped thud. No pitch to speak of.
    variants("invalid_", lambda i: lowpass(add(kick(92, 56, 0.16, curve=18, click=0.15),
                                               noise(0.05, curve=24) * 0.35), 0.12))
    variants("land_", lambda i: kick(120 * (1 + (i - 1) * 0.02), 48, 0.20, curve=13, click=0.25))
    # Seal stripped: a rim/paper tick.
    variants("seal_", lambda i: add(highpass(noise(0.07, curve=22), 0.32) * 0.8,
                                    pop(760 + i * 40, 0.035) * 0.4))

    # Vault: a rack tom that holds, then a floor-tom break.
    save("vault_hit.wav", add(tom(130, 0.30, curve=9), noise(0.05, curve=18) * 0.35))
    save("vault_break.wav", reverb(add(
        kick(150, 40, 0.55, curve=5.0, click=0.7),
        tom(96, 0.45, curve=6.5) * 0.8,
        snare(0.30, 150, bright=0.9) * 0.6), mix=0.2))

    # Ingot delivered: the biggest thump in the game, plus a kit accent.
    save("ingot_land.wav", reverb(add(
        kick(170, 34, 0.70, curve=3.8, click=0.8),
        tom(78, 0.55, curve=5.0) * 0.7,
        np.concatenate([np.zeros(int(0.12 * SR)), snare(0.26, 200) * 0.45])), mix=0.22))

    save("special_create.wav", add(*[
        np.concatenate([np.zeros(int(0.045 * i * SR)), tom(160 * (1.18 ** i), 0.16, curve=13) * (0.9 - i * 0.12)])
        for i in range(4)]))
    save("special_fire.wav", add(snare(0.26, 210, bright=1.2), kick(130, 50, 0.22, curve=12) * 0.6))
    save("bomb.wav", reverb(add(
        kick(190, 30, 0.80, curve=3.2, click=0.9),
        noise(0.30, curve=7) * 0.55,
        tom(70, 0.55, curve=5.0) * 0.6), mix=0.26))

    # Combo fills: a short run up the toms, longer as the chain deepens.
    for n_hits, name in ((3, "combo2"), (4, "combo3"), (5, "combo4"), (6, "combo5")):
        save(f"{name}.wav", add(*[
            np.concatenate([np.zeros(int(0.055 * i * SR)), tom(150 * (1.16 ** i), 0.18, curve=12) * (1 - i * 0.08)])
            for i in range(n_hits)]))

    # Outcomes.
    save("win.wav", reverb(add(
        *[np.concatenate([np.zeros(int(0.075 * i * SR)), tom(150 * (1.18 ** i), 0.22, curve=9) * (1 - i * 0.07)])
          for i in range(6)],
        np.concatenate([np.zeros(int(0.45 * SR)), add(kick(180, 40, 0.6, curve=4), snare(0.5, 200) * 0.7)]),
    ), mix=0.24))
    save("lose.wav", add(*[
        np.concatenate([np.zeros(int(0.16 * i * SR)), tom(150 * (0.74 ** i), 0.32, curve=8) * (0.95 - i * 0.2)])
        for i in range(3)]))
    for i in range(3):
        save(f"star{i + 1}.wav", add(tom(220 * (1.22 ** i), 0.20, curve=11), pop(700 * (1.2 ** i), 0.05) * 0.4))
    save("payout.wav", add(*[
        np.concatenate([np.zeros(int(0.05 * i * SR)), tom(160 * (1.14 ** i), 0.20, curve=11) * 0.8])
        for i in range(5)]))

    # Foley, now percussive.
    variants("coin_flip_", lambda i: pop(560 + i * 30, 0.05, curve=30) * 0.8)
    save("coin_roll.wav", add(*[
        np.concatenate([np.zeros(int(0.026 * i * SR)), pop(480 + i * 45, 0.04) * 0.5]) for i in range(6)]))
    save("coin_drop.wav", kick(115, 45, 0.22, curve=13))
    save("coin_spin.wav", add(*[
        np.concatenate([np.zeros(int(0.05 * i * SR)), pop(600, 0.035) * (0.66 ** i)]) for i in range(7)]))
    save("ting.wav", add(pop(880, 0.06, curve=22) * 0.7, tom(300, 0.10, curve=18) * 0.3))
    save("coins_pour.wav", add(*[
        np.concatenate([np.zeros(int(rng.uniform(0, 0.55) * SR)), pop(rng.uniform(380, 820), 0.045) * 0.35])
        for _ in range(26)]))

    # A four-bar drum loop for the win screen fireworks.
    bpm, beat = 104, 60.0 / 104
    total = int(SR * beat * 8)
    loop = np.zeros(total)
    for i in range(8):
        s = int(i * beat * SR)
        hit = kick(170, 40, 0.34) if i % 2 == 0 else snare(0.22, 200) * 0.8
        loop[s:s + len(hit)] += hit[: total - s]
        h = int((i + 0.5) * beat * SR)
        tick = highpass(noise(0.03, curve=26), 0.4) * 0.22
        loop[h:h + len(tick)] += tick[: total - h]
    save("win_fill.wav", reverb(loop, mix=0.18))


def build_music_drums():
    """Adds a kick/snare layer to the level and tension beds."""
    ff = shutil.which("ffmpeg")
    if not ff:
        print("  ffmpeg missing; music layer skipped")
        return
    for name, bpm, gain in (("music_level", 84, 0.5), ("music_tension", 96, 0.62)):
        src = os.path.join(OUT, f"{name}.mp3")
        if not os.path.exists(src):
            continue
        wav = os.path.join(OUT, "_tmp.wav")
        subprocess.run([ff, "-y", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", str(SR), wav], check=True)
        with wave.open(wav) as w:
            bed = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32767
        beat = 60.0 / bpm
        drums = np.zeros(len(bed))
        i = 0
        while i * beat * SR < len(bed):
            s = int(i * beat * SR)
            hit = kick(160, 42, 0.30) if i % 4 in (0, 2) else (snare(0.20, 200) * 0.55 if i % 4 == 1 else None)
            if hit is not None:
                e = min(len(bed), s + len(hit))
                drums[s:e] += hit[: e - s]
            i += 1
        mixed = np.clip(bed + drums * gain * 0.5, -1, 1)
        data = (norm(mixed, 0.62 * 10 ** (TRIM_DB / 20)) * 32767).astype(np.int16)
        with wave.open(wav, "w") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes(data.tobytes())
        subprocess.run([ff, "-y", "-loglevel", "error", "-i", wav, "-b:a", "96k", src], check=True)
        os.remove(wav)
        print(f"  {name}.mp3 + drums")


if __name__ == "__main__":
    build()
    print("music")
    build_music_drums()
    print("done")
