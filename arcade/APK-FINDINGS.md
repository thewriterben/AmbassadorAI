# What is actually in the other DGD app

Read from `DigitalGold-Android-2-92fd68c-debug.apk`, 2026-09-18. 18.8 MB, debug
build, git commit `92fd68c`.

This changes the merge question materially, so read the first two findings
before planning anything around it.

---

## 1. It is not a Flutter app

There is no `assets/flutter_assets/`, no `libflutter.so`, no Dart runtime. What
is in there instead:

- `kotlin/` — Kotlin standard library
- `okhttp3/` — the standard Android HTTP client
- `libandroidx.graphics.path.so` — a **Jetpack Compose** dependency
- `DebugProbesKt.bin` — Kotlin coroutines debugging
- nine `classes*.dex` files, the largest 44 MB

**It is a native Android app written in Kotlin with Jetpack Compose.** Our
arcade is Flutter. These are two different technology stacks that do not merge
by combining source trees — there is no shared language, no shared UI framework
and no shared build system.

That does not make combining them impossible. It makes it a different job than
the one we were scoping.

## 2. It is a live price ticker for DGD

Package: **`com.digitalgold.ticker`**. Version 1.0.0. The bundled
`assets/stats-source.json` is a detailed specification of exactly what it does:

- fetches the live account count from `https://digitalgold.co/api/forms/stats`
- computes a **5-decimal USD price** and a **market cap** from that count using
  the continuous model lifted from the website's own JavaScript
- at the time the file was written: **3,683 accounts, $11.16031, $82,947,331**
- polls every 45 seconds, matching the site

It also registers deep links for `digitalgold.co` and `www.digitalgold.co`, and
links out to `https://digitalgold.co/signup` and `https://digitalgold.co/app`.

Permissions are modest: `INTERNET`, `VIBRATE`, and `DUMP`.

---

## 3. The part that matters most: this collides with our compliance position

Everything written for the arcade so far states, in the app and on the record:

> XP and badges have no monetary value, cannot be exchanged for anything, and
> are not connected to any wallet, exchange or financial product.

And the draft store declarations say **Financial info: None**.

**A merged app would display a live USD price and market cap for a gold-backed
digital asset, while awarding points for playing games.** That is a materially
different product from either half, and it makes several things I have already
drafted untrue:

| Document | What breaks |
|---|---|
| `STORE-LISTING.md` §3 data safety | "Financial info — None" becomes wrong |
| `STORE-LISTING.md` §4 Apple labels | "Financial Info — Not collected" becomes wrong |
| `PRIVACY-DRAFT.md` | "no connection to any wallet, exchange or trading function" becomes wrong |
| `MEETING-BRIEF.md` §2.1 | The financial-products question moves from *probably clear* to *definitely in scope* |
| In-app footer | Still true of XP, but sits in an app now quoting a live price |

This is not a reason not to merge. It is a reason the **compliance sign-off has
to happen before the merge, not after** — because the answers change, and a
wrong answer on a financial-products questionnaire is a pulled listing rather
than a rejected build.

**Raise this in the meeting.** It is the single most consequential thing in this
file.

## 4. A fragility worth flagging to them regardless

The ticker does not read the price from an API. It **computes** it on the device
from constants extracted from the website's JavaScript bundle —
`V0 = 3.4015831925355799`, growth factors, and derived exponents `k`, `m`, `c`.

Their own `stats-source.json` lists the consequence as a known failure mode:

> **model_constants_change** — Site updates V0/k/m/c → client-computed
> 5-decimal price/mcap drift from digitalgold.co cards.

So if DGD ever changes the pricing model, this app silently displays **a wrong
price for a financial asset**, with no way to know. That is worse than showing
nothing. Worth raising with whoever owns the app, independently of any merge —
the robust fix is for the site to publish the 5-decimal figure in the API.

## 5. Why it might not run — candidates, not conclusions

I cannot diagnose this from a binary without the source or a crash log. Three
things in the file are worth checking first:

1. **The Origin-header trap.** Their own doc says a foreign `Origin` header makes
   the API return HTTP 500, and that only `https://digitalgold.co` is accepted.
   The guidance in the file is written for **iOS URLSession** — but this is an
   Android app using **OkHttp**, which behaves differently. If OkHttp is sending
   an Origin, every fetch fails and the ticker has no data. This is my first
   suspect.
2. **A placeholder App Store link** — `https://apps.apple.com/app/id0000000000`
   is in the code. Unfinished, and it would 404 if tapped.
3. **It is a debug build**, so it may simply never have been built for release.

**No API keys, tokens or passwords** were found by pattern search. Nothing here
needs rotating on the evidence available.

## 6. The iOS oddity

`stats-source.json` repeatedly gives **iOS** guidance — "iOS URLSession should
omit Origin", "CORS does not apply natively in iOS URLSession" — inside an
**Android** APK. The research was written for an iOS app and shipped unchanged
into the Android build. That suggests either an iOS version exists, or one AI
research document is being reused across both platforms without being adapted.

Worth asking, because it changes what "merge" has to cover.

---

## What this means for combining them

Given two different stacks, there are three honest options.

**A. Flutter add-to-app.** Flutter supports embedding a Flutter module inside an
existing native Android app. Their Kotlin app stays the shell; the arcade
becomes a screen inside it. This is a real, supported path — but it is
integration work on both sides, needs their build configured for it, and their
app is Android-only today, so iOS would need the same again.

**B. Rebuild one side.** Either the ticker is rewritten in Flutter (it is a
small surface: one API call, a computed model, a few screens) or the arcade is
rewritten in Kotlin (60 levels, a game engine, months). If a merge is truly
wanted, **rebuilding the ticker in Flutter is by far the cheaper direction** —
and the `stats-source.json` in this APK is a complete, unusually good
specification for doing exactly that.

**C. Ship two apps.** The arcade is finished and has its listing copy written.
The ticker ships separately when it works. Slower to a single product, fastest
to something in a store.

**On Monday:** option A is not a weekend's work across two codebases and two
platforms, and option B is a rebuild. Neither lands by Monday with the
compliance questions still open.
