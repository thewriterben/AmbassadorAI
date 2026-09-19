"""Coin Quest audio, second pass.

Three things the first pass got wrong:
  1. one sound per event, so a long cascade fired the identical sample 12 times
     and turned to mush -> every repeatable effect now has 3 round-robin takes;
  2. thin metal with a short decay -> richer inharmonic partial sets and longer
     tails, with a real body resonance under the strike;
  3. a single 23 s ambient bed behind every screen -> four beds that share a key
     so the app can crossfade between them.

Writes WAVs for effects and MP3s for music (via ffmpeg) straight into
assets/audio/.
"""
import math
import os
import shutil
import subprocess
import wave

import numpy as np

OUT = r"C:\src\puzzle-app\assets\audio"
SR = 22050
TRIM_DB = -2.0          # master trim, unchanged from the first pass
SFX_PITCH_SEMI = -2.0   # effects sit a tone below concert pitch
A4 = 440.0
PITCH = 2 ** (SFX_PITCH_SEMI / 12)

rng = np.random.default_rng(7)


def t(dur):
    return np.arange(int(SR * dur)) / SR


def env(n, a=0.002, curve=8.0):
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


def reverb(sig, mix=0.18, taps=((0.023, 0.5), (0.041, 0.35), (0.067, 0.25), (0.097, 0.15))):
    out = sig.copy()
    for delay, gain in taps:
        d = int(delay * SR)
        if d < len(sig):
            out[d:] += sig[:-d] * gain * mix
    return out


def noise(dur, a=0.001, curve=10.0, lp=0.5):
    n = int(SR * dur)
    return lowpass(rng.uniform(-1, 1, n), lp) * env(n, a=a, curve=curve)


# Inharmonic partial sets. More partials + slower high-end rolloff than v1.
BELL = ((1.0, 1.0), (2.76, 0.60), (5.40, 0.36), (8.93, 0.20), (13.3, 0.11), (18.6, 0.05))
DISC = ((1.0, 1.0), (1.51, 0.45), (2.76, 0.62), (4.20, 0.30), (5.40, 0.38), (7.10, 0.16), (9.8, 0.07))
SLAB = ((1.0, 1.0), (1.72, 0.50), (2.30, 0.35), (3.41, 0.22), (4.90, 0.12))


def metal(freq, dur, partials=BELL, curve=6.0, a=0.001, wobble=0.0, spread=0.0):
    tt = t(dur)
    n = len(tt)
    sig = np.zeros(n)
    for i, (ratio, amp) in enumerate(partials):
        r = ratio * (1 + spread * (rng.random() - 0.5) * 0.02)
        f = freq * r * (1 + wobble * np.sin(2 * np.pi * (6 + i) * tt))
        # Highs die faster, but not as fast as the first pass: this is the tail.
        e = np.exp(-curve * (1 + i * 0.42) * np.linspace(0, 1, n))
        sig += amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * e
    ai = max(1, int(a * SR))
    sig[:ai] *= np.linspace(0, 1, ai)
    return sig


def body(freq, dur, amount=0.35):
    """A low resonance under the strike, so coins read as objects not pings."""
    n = int(SR * dur)
    return amount * np.sin(2 * np.pi * freq * 0.5 * t(dur)) * env(n, a=0.004, curve=11.0)


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
    print(f"  {name:28} {len(sig)/SR:5.2f}s")


def note(semi, octv=0):
    return A4 * PITCH * 2 ** ((semi + 12 * octv) / 12)


# --------------------------------------------------------------- effects

def coin_strike(freq, dur=0.30, bright=1.0, seed_shift=0.0):
    b = metal(freq * (1 + seed_shift), dur, DISC, curve=7.0, spread=1.0)
    tick = highpass(noise(0.014, curve=13, lp=0.9), 0.3) * 0.65 * bright
    return add(b, tick, body(freq, dur * 0.6))


def variants(name, make, count=3):
    """Round-robin takes. Same sound, small deliberate differences."""
    for i in range(count):
        save(f"{name}{i + 1}.wav", make(i))


def build_effects():
    print("effects")
    # Match pops: one per cascade depth (1-5), three takes each. Pitch climbs
    # with depth; the tail lengthens so deep cascades feel bigger, not louder.
    for depth in range(1, 6):
        base = note([0, 4, 7, 11, 14][depth - 1], 1)
        dur = 0.26 + depth * 0.03

        def make(i, base=base, dur=dur):
            shift = (i - 1) * 0.006
            s = coin_strike(base, dur, bright=1.0 + i * 0.12, seed_shift=shift)
            return reverb(s, mix=0.10 + depth * 0.02)

        variants(f"pop{depth}_", make)

    # Tap / select: short, dry, three takes.
    variants("tap_", lambda i: coin_strike(note(7, 1), 0.13, bright=0.8, seed_shift=(i - 1) * 0.01))
    # Swap: two coins sliding past each other.
    variants("swap_", lambda i: add(
        coin_strike(note(2, 1), 0.16, seed_shift=(i - 1) * 0.008),
        np.concatenate([np.zeros(int(0.05 * SR)), coin_strike(note(5, 1), 0.16) * 0.7]),
    ))
    # Invalid: a dull, damped knock. No pitch, no sparkle.
    variants("invalid_", lambda i: lowpass(
        add(metal(note(-5, 0), 0.16, SLAB, curve=16.0), noise(0.05, curve=18, lp=0.25) * 0.5), 0.18))
    # Land: a coin settling.
    variants("land_", lambda i: add(
        coin_strike(note(-3, 1), 0.18, bright=0.6, seed_shift=(i - 1) * 0.012),
        body(note(-3, 0), 0.22, 0.5)))

    # Seal stripped: paper/wax tearing, not metal.
    variants("seal_", lambda i: highpass(
        noise(0.20, a=0.004, curve=7.0, lp=0.65) * (0.8 + i * 0.1), 0.22))

    # Vault: armour hit (held) vs break (gave way).
    save("vault_hit.wav", add(
        metal(note(-7, 0), 0.34, SLAB, curve=9.0),
        noise(0.06, curve=12, lp=0.3) * 0.6,
        body(note(-7, -1), 0.30, 0.7)))
    save("vault_break.wav", reverb(add(
        metal(note(-9, 0), 0.75, SLAB, curve=4.2),
        metal(note(-2, 0), 0.55, BELL, curve=5.0) * 0.5,
        noise(0.22, curve=6, lp=0.35) * 0.8,
        body(note(-9, -1), 0.70, 0.9)), mix=0.3))

    # Ingot delivered: a heavy bar landing, then a bright confirm.
    save("ingot_land.wav", reverb(add(
        metal(note(-12, 0), 0.55, SLAB, curve=6.5),
        body(note(-12, -1), 0.50, 1.0),
        noise(0.09, curve=9, lp=0.22) * 0.5,
        np.concatenate([np.zeros(int(0.16 * SR)),
                        metal(note(7, 1), 0.45, BELL, curve=5.0) * 0.45]),
    ), mix=0.26))

    # Specials.
    save("special_create.wav", reverb(add(
        metal(note(0, 1), 0.5, BELL, curve=5.0),
        np.concatenate([np.zeros(int(0.07 * SR)), metal(note(7, 1), 0.45, BELL, curve=5.2) * 0.6]),
        np.concatenate([np.zeros(int(0.14 * SR)), metal(note(12, 1), 0.4, BELL, curve=5.4) * 0.4]),
    ), mix=0.28))
    save("special_fire.wav", add(
        highpass(noise(0.30, a=0.002, curve=5.0, lp=0.8), 0.25) * 0.9,
        metal(note(12, 1), 0.28, DISC, curve=8.0) * 0.5))
    save("bomb.wav", reverb(add(
        noise(0.45, a=0.001, curve=4.0, lp=0.18) * 1.0,
        metal(note(-12, 0), 0.6, SLAB, curve=5.0) * 0.8,
        body(note(-12, -1), 0.55, 1.0)), mix=0.34))

    # Combo chimes: a rising pentatonic, one per depth.
    for i, semi in enumerate([7, 11, 14, 19]):
        save(f"combo{i + 2}.wav", reverb(
            metal(note(semi, 1), 0.5 + i * 0.05, BELL, curve=5.0), mix=0.3))

    # Outcomes.
    save("win.wav", reverb(add(*[
        np.concatenate([np.zeros(int(0.11 * i * SR)),
                        metal(note(s, 1), 0.9 - i * 0.05, BELL, curve=3.6) * (1.0 - i * 0.12)])
        for i, s in enumerate([0, 4, 7, 12])]), mix=0.36))
    save("lose.wav", reverb(add(*[
        np.concatenate([np.zeros(int(0.14 * i * SR)),
                        metal(note(s, 0), 0.8, SLAB, curve=5.0) * (0.9 - i * 0.2)])
        for i, s in enumerate([0, -3, -7])]), mix=0.3))
    for i in range(3):
        save(f"star{i + 1}.wav", reverb(metal(note([7, 12, 16][i], 1), 0.55, BELL, curve=4.6), mix=0.32))
    save("payout.wav", reverb(add(*[
        np.concatenate([np.zeros(int(0.045 * i * SR)), coin_strike(note(s, 1), 0.4) * 0.75])
        for i, s in enumerate([0, 4, 7, 12, 16])]), mix=0.32))

    # Coin foley.
    variants("coin_flip_", lambda i: coin_strike(note(9, 1), 0.2, bright=1.1, seed_shift=(i - 1) * 0.01))
    save("coin_roll.wav", add(*[
        np.concatenate([np.zeros(int(0.03 * i * SR)), coin_strike(note(4 + i, 1), 0.14) * 0.5])
        for i in range(5)]))
    save("coin_drop.wav", add(coin_strike(note(-5, 1), 0.26, bright=0.7), body(note(-5, 0), 0.3, 0.6)))
    save("coin_spin.wav", add(*[
        np.concatenate([np.zeros(int(0.055 * i * SR)), coin_strike(note(7, 1), 0.12) * (0.62 ** i)])
        for i in range(7)]))
    save("ting.wav", reverb(metal(note(16, 1), 0.5, BELL, curve=4.4), mix=0.3))
    save("coins_pour.wav", reverb(add(*[
        np.concatenate([np.zeros(int(rng.uniform(0, 0.5) * SR)),
                        coin_strike(note(int(rng.choice([0, 4, 7, 9, 12])), 1), 0.22) * 0.4])
        for _ in range(22)]), mix=0.26))


# ----------------------------------------------------------------- music

def pad(freq, dur, amp=1.0, detune=0.004):
    tt = t(dur)
    n = len(tt)
    sig = np.zeros(n)
    for m, a in ((1, 1.0), (2, 0.28), (3, 0.12), (4, 0.06)):
        sig += a * np.sin(2 * np.pi * freq * m * tt)
        sig += a * 0.6 * np.sin(2 * np.pi * freq * m * (1 + detune) * tt)
    # Slow swell in and out so loops seam cleanly.
    e = np.minimum(np.linspace(0, 1, n) * 6, 1) * np.minimum(np.linspace(1, 0, n) * 6, 1)
    return sig * e * amp


def pluck(freq, dur, amp=1.0):
    n = int(SR * dur)
    return metal(freq, dur, ((1, 1.0), (2, 0.3), (3.01, 0.12)), curve=6.5) * amp


def bed(name, seconds, chords, motif, bpm, motif_amp=0.5, dark=False, pulse=None):
    """Builds one music bed: a chord pad, a sparse motif, optional pulse."""
    n = int(SR * seconds)
    out = np.zeros(n)
    beat = 60.0 / bpm
    bar = beat * 4
    # Pads
    for i, chord in enumerate(chords):
        start = int(i * bar * SR)
        seg = np.zeros(int(bar * SR))
        for semi in chord:
            seg += pad(note(semi, -1 if dark else 0), bar, amp=0.5 / len(chord))
        end = min(n, start + len(seg))
        out[start:end] += seg[: end - start]
    # Motif
    for beat_index, semi in motif:
        start = int(beat_index * beat * SR)
        s = pluck(note(semi, 1), 0.9, amp=motif_amp)
        end = min(n, start + len(s))
        if start < n:
            out[start:end] += s[: end - start]
    # Optional pulse for the tension bed.
    if pulse:
        for i in range(int(seconds / (beat / pulse))):
            start = int(i * (beat / pulse) * SR)
            s = lowpass(noise(0.10, curve=14, lp=0.2), 0.12) * 0.30
            end = min(n, start + len(s))
            if start < n:
                out[start:end] += s[: end - start]
    out = reverb(out, mix=0.30)
    # Seam: crossfade the last second into the first so the loop is invisible.
    x = int(1.0 * SR)
    fade = np.linspace(0, 1, x)
    out[:x] = out[:x] * fade + out[-x:] * (1 - fade)
    out = out[:-x]
    return out


def build_music():
    print("music")
    # All four share A minor / C major so crossfades between screens agree.
    Am = [0, 3, 7]
    F = [-4, 0, 5]
    C = [-9, -5, 0]
    G = [-2, 2, 7]

    beds = {
        # Menu: slow, wide, almost still.
        "music_menu": bed("menu", 26, [Am, F, C, G], [(0, 0), (6, 7), (11, 3), (14, 0)], bpm=62, motif_amp=0.45),
        # Level map: same harmony, a little more movement.
        "music_map": bed("map", 26, [Am, C, F, G], [(0, 7), (2, 12), (5, 3), (8, 7), (12, 0), (14, 12)],
                         bpm=72, motif_amp=0.5),
        # In level: steadier, brighter motif.
        "music_level": bed("level", 24, [Am, F, C, G],
                           [(0, 0), (1.5, 4), (3, 7), (5, 12), (7, 7), (9, 4), (11, 0), (13, 7)],
                           bpm=84, motif_amp=0.42),
        # Low on moves: darker register, a soft pulse underneath.
        "music_tension": bed("tension", 20, [Am, Am, F, G], [(0, 0), (4, -1), (8, 0), (12, 3)],
                             bpm=96, motif_amp=0.36, dark=True, pulse=1),
    }
    ff = shutil.which("ffmpeg")
    for name, sig in beds.items():
        wav = os.path.join(OUT, f"{name}.wav")
        data = (np.clip(norm(sig, 0.62 * 10 ** (TRIM_DB / 20)), -1, 1) * 32767).astype(np.int16)
        with wave.open(wav, "w") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes(data.tobytes())
        if ff:
            mp3 = os.path.join(OUT, f"{name}.mp3")
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", wav, "-b:a", "96k", mp3], check=True)
            os.remove(wav)
            print(f"  {name}.mp3  {len(sig)/SR:5.1f}s  {os.path.getsize(mp3)//1024} KB")
        else:
            print(f"  {name}.wav (ffmpeg missing, left as wav)")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_effects()
    build_music()
    print("done")
