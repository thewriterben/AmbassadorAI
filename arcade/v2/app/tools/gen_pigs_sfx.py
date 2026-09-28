"""When Pigs Fly sound effects: the boar's own voice and wings.

Until these the boar borrowed Coin Quest's sounds: a UI tap for every flap,
a vault clang for every strike. This writes, into assets/audio/:

  flap_<stage>_1..3    a wingbeat per stage: the piglet's light, feathery
                       flutter, the juvenile's feathered whoosh, the
                       razorback's heavy leathery beat with a low thump
  grunt_<stage>_1..3   the boar's cry when it strikes a gate: a piglet's
                       squeal, a juvenile's grunt, a razorback's deep
                       snorting growl (layered over the game's impact)
  snort_<stage>        a contented snort on touchdown
  stage_up             the fanfare when the boar grows into its next stage
  ab_dash              dash: a sharp rushing whoosh with a rising drive tone
  ab_grapple           grapple: a whip crack and a chain rattling out
  ab_blink             blink: a teleport zap, a fast sweep and a sparkle pop
  ab_freeze_fire       freeze shot leaving the snout: an icy "pew"
  ab_freeze_hit        the shot freezing its coin: a crystalline crackle
  ab_tractor           tractor beam: a warbling hum that swells up

Everything is synthesised, like the rest of the app's effects (see
gen_cq_audio2.py): 22,050 Hz mono 16-bit, three round-robin takes of
anything that repeats, a tone below concert pitch.

  - Wings are noise through a band that sweeps down over the stroke, with a
    feather flutter (amplitude ripple) for the feathered wings and a low
    sine thump for the dragon's.
  - Voices are a glottal pulse train (a jittered, band-limited sawtooth)
    with a pitch contour, shaped by nasal formants in the frequency domain,
    plus breath noise. Pigs are nasal: a strong formant near 1 kHz and a
    dip near 2 kHz.

    python tools/gen_pigs_sfx.py
"""
import math
import os
import wave

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "assets", "audio"))
SR = 22050
PITCH = 2 ** (-2 / 12)  # a tone below concert pitch, as the other effects
rng = np.random.default_rng(11)


def write(name, x, peak_db=-3.0):
    x = np.asarray(x, dtype=float)
    m = np.max(np.abs(x)) or 1.0
    x = x / m * (10 ** (peak_db / 20))
    # 3 ms fades so no take starts or ends on a click.
    f = int(0.003 * SR)
    x[:f] *= np.linspace(0, 1, f)
    x[-f:] *= np.linspace(1, 0, f)
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(os.path.join(OUT, name + ".wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def env(n, attack, decay_curve):
    """Linear attack over `attack` seconds, then exponential decay."""
    e = np.exp(-decay_curve * np.linspace(0, 1, n))
    a = max(1, int(attack * SR))
    e[:a] *= np.linspace(0, 1, a)
    return e


def sweep_filter(x, centre, width):
    """Noise through a band whose centre (Hz) follows `centre`, an array per
    sample: short overlapping frames, each weighted in the frequency domain
    by a gaussian band, overlap-added."""
    n = 512
    hop = n // 4
    win = np.hanning(n)
    out = np.zeros(len(x) + n)
    freqs = np.fft.rfftfreq(n, 1 / SR)
    pad = np.concatenate([x, np.zeros(n)])
    for i in range(0, len(x), hop):
        fr = pad[i:i + n] * win
        c = centre[min(i + n // 2, len(centre) - 1)]
        w = width[min(i + n // 2, len(width) - 1)] if hasattr(width, "__len__") else width
        g = np.exp(-0.5 * ((freqs - c) / w) ** 2)
        out[i:i + n] += np.fft.irfft(np.fft.rfft(fr) * g, n) * win
    return out[:len(x)] / 1.5


def formants(x, peaks, dips=(), floor=0.08, lowpass=None):
    """Shapes a signal with gaussian formant peaks and dips: (Hz, width, gain),
    over a flat floor, optionally rolled off above `lowpass` Hz."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.full_like(f, floor)
    for c, w, a in peaks:
        g += a * np.exp(-0.5 * ((f - c) / w) ** 2)
    for c, w, a in dips:
        g *= 1 - a * np.exp(-0.5 * ((f - c) / w) ** 2)
    if lowpass:
        g /= 1 + (f / lowpass) ** 4
    return np.fft.irfft(X * g, len(x))


def glottal(f0, jitter=0.006):
    """A band-limited sawtooth-like pulse train following the pitch contour
    f0 (Hz per sample), with a little jitter so it sounds alive."""
    f = f0 * (1 + jitter * rng.standard_normal(len(f0)).cumsum() / np.sqrt(len(f0)) * 8)
    ph = np.cumsum(f / SR)
    out = np.zeros(len(f0))
    for k in range(1, 30):
        mask = (k * f) < SR * 0.45
        out += mask * np.sin(2 * np.pi * k * ph) / k
    return out


# ----------------------------------------------------------------- wings

def flap(stage, take):
    j = 1 + 0.06 * (take - 2)  # each take a touch different
    if stage == "piglet":
        dur, lo, hi, flutter, thump = 0.16, 1400, 3800, 42.0, 0.0
    elif stage == "juvenile":
        dur, lo, hi, flutter, thump = 0.26, 700, 2400, 28.0, 0.0
    else:
        dur, lo, hi, flutter, thump = 0.36, 260, 1100, 0.0, 1.0
    n = int(dur * j * SR)
    tt = np.arange(n) / SR
    noise = rng.standard_normal(n)
    # The band sweeps down through the stroke.
    centre = (hi * j + (lo - hi * j) * (tt / tt[-1]) ** 0.7) * PITCH
    x = sweep_filter(noise, centre, (hi - lo) * 0.35)
    e = env(n, 0.035 if stage != "razorback" else 0.05, 5.0)
    if flutter:
        # Feathers: a quick ripple as the vanes pass through the air.
        e *= 0.72 + 0.28 * np.sin(2 * np.pi * flutter * j * tt) ** 2
    x *= e
    if thump:
        # The dragon's membrane: a low body thump and a leathery snap.
        th = np.sin(2 * np.pi * 58 * PITCH * tt * (1 - 0.3 * tt / tt[-1])) * env(n, 0.012, 9.0)
        snap = sweep_filter(rng.standard_normal(n), np.full(n, 1800.0), 500) * env(n, 0.002, 40.0)
        x = x + 0.9 * th / (np.max(np.abs(th)) or 1) * np.max(np.abs(x)) + 0.35 * snap
    return x


# ----------------------------------------------------------------- voices

def voice(f0, dur, peaks, dips, breath, attack, decay, rough=0.0, lowpass=None, floor=0.08):
    n = len(f0)
    g = glottal(f0)
    if rough:
        # Growl: a slow, irregular amplitude flutter from the throat.
        tt = np.arange(n) / SR
        g *= 1 - rough * (0.5 + 0.5 * np.sin(2 * np.pi * 31 * tt + 3 * np.sin(2 * np.pi * 7 * tt)))
    v = formants(g, peaks, dips, floor=floor, lowpass=lowpass)
    b = formants(rng.standard_normal(n), [(p[0], p[1] * 2.5, p[2]) for p in peaks], floor=floor * 0.25, lowpass=lowpass)
    x = (v / (np.max(np.abs(v)) or 1) + b / (np.max(np.abs(b)) or 1) * breath) * env(n, attack, decay)
    return x


def contour(dur, start, peak, end, peak_at=0.3):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    up = start + (peak - start) * np.clip(t / peak_at, 0, 1) ** 0.6
    down = peak + (end - peak) * np.clip((t - peak_at) / (1 - peak_at), 0, 1) ** 1.4
    return np.where(t < peak_at, up, down) * PITCH


NASAL_DIP = [(2100, 260, 0.7)]


def grunt(stage, take):
    j = 1 + 0.05 * (take - 2)
    if stage == "piglet":
        # A squeal: high, rising then falling, bright.
        dur = 0.34 * j
        f0 = contour(dur, 760 * j, 1050 * j, 620 * j, 0.35)
        return voice(f0, dur, [(1300, 260, 1.0), (2900, 400, 0.6), (4300, 600, 0.3)], [(2100, 200, 0.5)],
                     breath=0.25, attack=0.02, decay=3.0)
    if stage == "juvenile":
        # A grunt: low, short, falling, nasal.
        dur = 0.26 * j
        f0 = contour(dur, 150 * j, 170 * j, 110 * j, 0.2)
        # Kept below ~2.5 kHz, where a grunt lives; the breath is a whisper
        # under the voice, not a hiss over it.
        return voice(f0, dur, [(520, 120, 1.0), (1050, 180, 0.8), (2600, 300, 0.2)], NASAL_DIP,
                     breath=0.22, attack=0.012, decay=4.0, rough=0.3, lowpass=2600, floor=0.02)
    # The razorback: a deep snorting growl, longer, rough.
    dur = 0.46 * j
    f0 = contour(dur, 86 * j, 98 * j, 62 * j, 0.25)
    growl = voice(f0, dur, [(380, 100, 1.0), (880, 160, 0.9), (2400, 300, 0.15)], NASAL_DIP,
                  breath=0.3, attack=0.02, decay=3.2, rough=0.55, lowpass=1900, floor=0.02)
    n = len(growl)
    snort = sweep_filter(rng.standard_normal(n), np.full(n, 900.0 * PITCH), 350) * env(n, 0.004, 22.0)
    return growl / (np.max(np.abs(growl)) or 1) + 0.45 * snort / (np.max(np.abs(snort)) or 1)


def snort(stage):
    base = {"piglet": 420.0, "juvenile": 160.0, "razorback": 95.0}[stage]
    dur = {"piglet": 0.2, "juvenile": 0.24, "razorback": 0.3}[stage]
    f0 = contour(dur, base, base * 1.08, base * 0.85, 0.3)
    v = voice(f0, dur, [(base * 4, base, 1.0), (1000, 200, 0.7)], NASAL_DIP, breath=0.5, attack=0.01, decay=5.0,
              lowpass=3500, floor=0.03)
    n = len(v)
    # Two quick nasal puffs: the snort.
    puff = sweep_filter(rng.standard_normal(n), np.full(n, 1100.0), 450)
    tt = np.arange(n) / SR
    puffs = np.exp(-((tt - 0.02) / 0.012) ** 2) + 0.8 * np.exp(-((tt - 0.09) / 0.014) ** 2)
    return 0.55 * v + puff * puffs / (np.max(np.abs(puff)) or 1)


# ----------------------------------------------------------------- stage up

def stage_up():
    dur = 1.6
    n = int(dur * SR)
    tt = np.arange(n) / SR
    out = np.zeros(n)
    # A rising arpeggio of bells, root-third-fifth-octave, in D (a tone below
    # C, with the other effects), each with slightly inharmonic partials.
    notes = [587.33, 739.99, 880.0, 1174.66]
    for i, f in enumerate(notes):
        start = int(i * 0.11 * SR)
        m = n - start
        u = np.arange(m) / SR
        tone = np.zeros(m)
        for k, (ratio, amp, d) in enumerate([(1, 1.0, 2.2), (2.01, 0.45, 3.2), (3.02, 0.22, 4.5), (4.17, 0.12, 6.0)]):
            tone += amp * np.sin(2 * np.pi * f * ratio * u) * np.exp(-d * u)
        att = np.minimum(1, u / 0.004)
        out[start:] += tone * att * (0.8 + 0.2 * i / 3)
    # A shimmer rising under it.
    shimmer = sweep_filter(rng.standard_normal(n), 2000 + 5000 * (tt / dur), 900)
    shimmer *= np.sin(np.pi * np.clip(tt / 1.1, 0, 1)) ** 2
    out += 0.35 * shimmer / (np.max(np.abs(shimmer)) or 1) * np.max(np.abs(out))
    return out


# ----------------------------------------------------------------- abilities
# They fire rarely (every one is on a cooldown or a charge count), so one
# take each. None is pig-like: these are the powers the shop sells, and they
# should sound like gear, not like the boar.

def _t(dur):
    return np.arange(int(dur * SR)) / SR


def bell(freqs, dur, decay=6.0):
    """Short metal: slightly inharmonic partials, each ringing down."""
    tt = _t(dur)
    out = np.zeros(len(tt))
    for k, (ratio, amp) in enumerate([(1, 1.0), (2.76, 0.5), (5.4, 0.25), (8.93, 0.12)]):
        for f in freqs:
            hz = f * ratio * PITCH
            if hz > SR * 0.45:
                continue  # above Nyquist it would fold back as a stray tone
            out += amp * np.sin(2 * np.pi * hz * tt) * np.exp(-(decay + 3 * k) * tt)
    return out


def ab_dash():
    dur = 0.42
    n = int(dur * SR)
    tt = _t(dur)
    # Air rushing past: a band sweeping up, then falling away.
    centre = 700 + 3800 * np.sin(np.pi * np.clip(tt / 0.32, 0, 1)) ** 0.8
    rush = sweep_filter(rng.standard_normal(n), centre, 900) * env(n, 0.03, 5.0)
    # The drive: a buzzy tone sliding up an octave.
    f = (140 + 140 * np.clip(tt / 0.25, 0, 1) ** 0.7) * PITCH
    drive = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * 0.5 + np.sin(2 * np.pi * np.cumsum(f) / SR)
    drive = formants(drive, [(900, 400, 1.0), (2200, 600, 0.4)], lowpass=3000) * env(n, 0.01, 6.0)
    return rush / np.max(np.abs(rush)) + 0.5 * drive / np.max(np.abs(drive))


def ab_grapple():
    dur = 0.6
    n = int(dur * SR)
    out = np.zeros(n)
    # The whip: a very short, bright crack.
    crack = sweep_filter(rng.standard_normal(n), np.full(n, 3200.0), 1400) * env(n, 0.001, 70.0)
    out += 1.2 * crack / np.max(np.abs(crack))
    # The chain paying out: clinks, quick at first and slowing, each a small
    # bell a little different in pitch.
    t0 = 0.03
    gap = 0.028
    i = 0
    while t0 < dur - 0.08:
        start = int(t0 * SR)
        clink = bell([1900 + 260 * ((i * 7) % 5)], 0.08, decay=38.0)
        m = min(len(clink), n - start)
        out[start:start + m] += 0.55 * (0.85 ** (i * 0.5)) * clink[:m]
        t0 += gap
        gap *= 1.12
        i += 1
    return out


def ab_blink():
    dur = 0.36
    n = int(dur * SR)
    tt = _t(dur)
    # Out of here: a sine swept down fast, ring-modulated, then back in:
    # a quick sweep up ending in a pop.
    f = np.where(tt < 0.14, 1600 - 1300 * (tt / 0.14), 300 + 2600 * np.clip((tt - 0.14) / 0.12, 0, 1) ** 1.5) * PITCH
    zap = np.sin(2 * np.pi * np.cumsum(f) / SR) * (0.6 + 0.4 * np.sin(2 * np.pi * 55 * tt))
    zap *= np.where(tt < 0.14, 1 - 0.4 * tt / 0.14, 0.6 + 0.4 * np.clip((tt - 0.14) / 0.12, 0, 1)) * env(n, 0.004, 1.5)
    pop_at = int(0.26 * SR)
    sparkle = bell([2637], dur - 0.26, decay=18.0)
    out = zap / np.max(np.abs(zap))
    out[pop_at:pop_at + len(sparkle)] += 0.8 * sparkle / np.max(np.abs(sparkle))
    return out


def ab_freeze_fire():
    dur = 0.3
    n = int(dur * SR)
    tt = _t(dur)
    # A "pew": a clear tone dropping fast, with a glassy overtone and a puff.
    f = (2400 * np.exp(-9 * tt) + 700) * PITCH
    ph = np.cumsum(f) / SR
    tone = np.sin(2 * np.pi * ph) + 0.35 * np.sin(2 * np.pi * 2.7 * ph)
    puff = sweep_filter(rng.standard_normal(n), np.full(n, 5000.0), 1500) * env(n, 0.002, 30.0)
    return tone * env(n, 0.003, 6.0) + 0.25 * puff / np.max(np.abs(puff))


def ab_freeze_hit():
    dur = 0.7
    n = int(dur * SR)
    out = np.zeros(n)
    # Ice forming: a cluster of high glassy chimes landing close together,
    # over a thin crackle.
    for i, (f, at) in enumerate([(2960, 0.0), (3520, 0.025), (4190, 0.05), (3136, 0.09), (4700, 0.13)]):
        c = bell([f], dur - at, decay=9.0 + 2 * i)
        start = int(at * SR)
        out[start:start + len(c)] += (0.9 - 0.12 * i) * c[:n - start]
    crackle = rng.standard_normal(n) * (rng.random(n) < 0.04)
    crackle = sweep_filter(crackle, np.full(n, 6000.0), 2000) * env(n, 0.002, 7.0)
    return out / np.max(np.abs(out)) + 0.5 * crackle / (np.max(np.abs(crackle)) or 1)


def ab_tractor():
    dur = 1.0
    n = int(dur * SR)
    tt = _t(dur)
    # A hum that swells in and warbles: two detuned tones with a slow
    # vibrato and their harmonics, the pitch rising a little as it locks.
    # Pitched where a phone speaker can play it: the first version sat at
    # 180-240 Hz, which phones barely reproduce, and would have been all
    # but silent.
    base = (340 + 110 * np.clip(tt / 0.6, 0, 1)) * PITCH
    vib = 1 + 0.035 * np.sin(2 * np.pi * 7.5 * tt)
    ph1 = np.cumsum(base * vib) / SR
    ph2 = np.cumsum(base * 1.012 * vib) / SR
    hum = (np.sin(2 * np.pi * ph1) + np.sin(2 * np.pi * ph2) + 0.55 * np.sin(2 * np.pi * 2 * ph1)
           + 0.35 * np.sin(2 * np.pi * 3 * ph2) + 0.2 * np.sin(2 * np.pi * 4 * ph1))
    shape = np.sin(np.pi * np.clip(tt / dur, 0, 1)) ** 0.6
    return formants(hum, [(700, 300, 1.0), (1600, 500, 0.5)], lowpass=3500) * shape


def main():
    os.makedirs(OUT, exist_ok=True)
    written = []
    for stage in ("piglet", "juvenile", "razorback"):
        for take in (1, 2, 3):
            write(f"flap_{stage}_{take}", flap(stage, take), peak_db=-4.0)
            write(f"grunt_{stage}_{take}", grunt(stage, take), peak_db=-2.5)
            written += [f"flap_{stage}_{take}", f"grunt_{stage}_{take}"]
        write(f"snort_{stage}", snort(stage), peak_db=-4.0)
        written.append(f"snort_{stage}")
    write("stage_up", stage_up(), peak_db=-2.0)
    written.append("stage_up")
    for name, fn, peak in [
        ("ab_dash", ab_dash, -3.0),
        ("ab_grapple", ab_grapple, -3.0),
        ("ab_blink", ab_blink, -3.0),
        ("ab_freeze_fire", ab_freeze_fire, -4.0),
        ("ab_freeze_hit", ab_freeze_hit, -3.5),
        ("ab_tractor", ab_tractor, -3.0),
    ]:
        write(name, fn(), peak_db=peak)
        written.append(name)
    print(f"wrote {len(written)} effects to {OUT}")


if __name__ == "__main__":
    main()
