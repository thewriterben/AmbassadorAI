"""Finish the spoken lines for Coin Quest: Digital Gold.

Sources are ElevenLabs takes (voice "Hannah") in `C:\\src\\vo\\el`, 44.1 kHz
mono. These are performed recordings, not synthesis artefacts, so the job here
is only to make them sit in the game mix — deliberately much lighter than the
chain the earlier TTS takes needed. No added room: these already have one, and
layering a fake reflection on top is what makes a good take sound cheap.

What is applied:
  * trim the dead air at both ends, so the line lands on the beat that
    triggered it rather than a beat later;
  * a gentle high shelf, because any bright vocal fights the snare and the
    coin pops for the same 7-9 kHz;
  * a high-pass below the phone speaker's useful range;
  * loudness matched to the effects bed at -17 LUFS, -3 dBFS true peak.
"""
import os
import subprocess
import sys

FFMPEG = r"C:\Users\Benji\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"
SRC = r"C:\src\vo\el2"
OUT = r"C:\src\puzzle-app\assets\audio"

# source stem -> shipped asset.
#
# Two of the uploads did not say what their filenames claimed — "nice 3" is
# "You win!" and "You're on fire!" is just "Fire!" — so the stems here are the
# transcribed line, not the original filename. Worth re-checking by ear if this
# set is ever replaced.
LINES = {
    # Standard praise, cascade of 4-5.
    "you_rock": "vo_you_rock.wav",
    "wow": "vo_wow.wav",
    "great_work": "vo_great_work.wav",
    "way_to_go": "vo_way_to_go.wav",
    "keep_going": "vo_keep_going.wav",
    # Big praise, cascade of 6+.
    "so_big": "vo_so_big.wav",
    "fire": "vo_fire.wav",
    "unstoppable": "vo_unstoppable.wav",
    "incredible": "vo_incredible.wav",
    # Level complete.
    "level_complete": "vo_level_complete.wav",
    "you_win": "vo_you_win.wav",
    # Out of moves.
    "almost": "vo_almost.wav",
    "one_more": "vo_one_more.wav",
    "got_this": "vo_got_this.wav",
    "dont_give_up": "vo_dont_give_up.wav",
    "believe": "vo_believe.wav",
}

RETIRED = ["vo_youre_a_winner.wav"]

FILTER = (
    "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0:"
    "detection=peak,"
    "areverse,"
    "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0:"
    "detection=peak,"
    "areverse,"
    "highshelf=f=7500:g=-2.5,"
    "highpass=f=85,"
    "loudnorm=I=-17:TP=-3.0:LRA=7,"
    "aformat=sample_fmts=s16:sample_rates=44100:channel_layouts=mono"
)


def main():
    if not os.path.exists(FFMPEG):
        sys.exit(f"ffmpeg not found at {FFMPEG}")

    missing = [s for s in LINES if not os.path.exists(os.path.join(SRC, f"{s}.mp3"))]
    if missing:
        sys.exit(f"missing sources in {SRC}: {', '.join(missing)}")

    print("voice")
    for stem, dst_name in LINES.items():
        dst = os.path.join(OUT, dst_name)
        subprocess.run(
            [FFMPEG, "-y", "-loglevel", "error",
             "-i", os.path.join(SRC, f"{stem}.mp3"), "-af", FILTER, dst],
            check=True,
        )
        print(f"  {dst_name:22} {os.path.getsize(dst) // 1024} KB")

    for name in RETIRED:
        p = os.path.join(OUT, name)
        if os.path.exists(p):
            os.remove(p)
            print(f"  removed {name}")


if __name__ == "__main__":
    main()
