# DGD Arcade — privacy policy and Play data safety

**DRAFT. Not reviewed by a lawyer, and I am not one.** Play requires a hosted
privacy policy URL and a data safety declaration before a track goes live, and
both are statements DGD makes on the record. Everything below is written from
what the code actually does — I read the database schema and the client rather
than adapting a template — but it needs review by whoever owns compliance at DGD
before it is published or submitted.

Where the app's behaviour changes, this has to change with it. The declaration
being accurate is the part Play enforces.

---

## What the app actually does with data

Established by reading `arcade/server/src/db.ts` (the schema), `auth.ts`
(account creation) and `arcade/app/lib/arcade/api.dart` (what the client sends).

**There are no user accounts.** On first launch the app asks the server for an
anonymous player record and gets back an opaque id and a bearer token, which it
stores on the device. No email address, phone number, username, password or
social login is involved at any point. Nothing asks the player who they are.

**The display name is assigned, never typed.** Leaderboard handles come from a
fixed word list on the server ("Burnished Cipher 416"). A player can re-roll
theirs up to three times a day. Because they cannot enter free text, the
leaderboard cannot carry a real name, a handle a player uses elsewhere, or
anything else that identifies them.

**What is stored on DGD's server**, per anonymous player:

| | |
|---|---|
| Identifier | random opaque id; a SHA-256 hash of the bearer token, not the token |
| Platform | the string `android`, `ios` or `web` — not a device id, model or fingerprint |
| Progress | XP, badges, streak, expeditions started and completed, tablets answered correctly, ledgers solved |
| Learning state | which questions have been seen, when each is next due, right/wrong counts |
| Play records | per-expedition and per-round timings and answers, used for the plausibility checks that stop XP farming |
| Moderation | a status flag: normal, XP-only, or blocked |

**What is stored only on the device**, in shared preferences: Coin Quest level
clears, stars and best scores; the sound and music toggles; whether the first-run
coaching cards have been shown; the bearer token and player id. Uninstalling the
app removes all of it.

**What is not collected at all:** no name, email, phone, address or date of
birth. No contacts, photos, files, microphone, camera or location. No advertising
identifier. No analytics or crash-reporting SDK. No third-party tracker of any
kind — the app's only dependencies are shared_preferences, flame, flame_audio,
url_launcher and http, none of which phone home.

**No purchases, no ads, no wallet.** There is no in-app purchase, no
advertising, and no connection to any wallet, exchange or trading function. XP
and badges have no monetary value and cannot be exchanged for anything — the
in-app footer says so on every home screen.

**Transmission and retention.** The app talks to DGD's server over HTTPS. Like
any web server it sees request IP addresses transiently; these are not stored in
the database. Player records persist until deleted.

**Deletion.** Built 2026-09-17. Settings → **Delete my play record** calls
`DELETE /v1/me`, which erases the player row and every row keyed to it — badges,
learning state, expeditions and the tablets issued within them, ledger plays,
mini rounds and the XP ledger — in a single transaction. The bearer token is
only ever resolved by hashing it against the deleted row, so it stops working
the moment the row is gone, and the app forgets it locally. A second, separate
control clears Coin Quest progress held on the device.

---

## Draft policy text

> ### Privacy Policy — DGD Arcade
>
> *Last updated: [DATE]*
>
> DGD Arcade is an educational game published by [LEGAL ENTITY NAME]. This
> policy explains what the app collects and why.
>
> **We do not ask who you are.** DGD Arcade has no sign-up, no login and no user
> accounts. We never ask for your name, email address, phone number or any other
> contact detail, and we have no way to contact you.
>
> **An anonymous play record.** So that your progress survives across sessions
> and so the leaderboard works, the app creates an anonymous record on our
> server when you first open it. That record holds a random identifier, which
> platform you are playing on (Android, iOS or web), and your progress in the
> games: experience points, badges, streaks, which quiz questions you have
> answered and when each is next due, and the timing of your plays. Nothing in
> it identifies you.
>
> **Your leaderboard name is assigned by us.** You cannot type one. We generate
> it from a fixed word list, and you may re-roll it. This is deliberate: it means
> the leaderboard cannot carry your real name.
>
> **Stored on your device.** Your Coin Quest progress, your sound settings and
> your anonymous access token are stored on your device and are removed when you
> uninstall the app.
>
> **What we do not collect.** We do not collect your location, contacts, photos,
> files, microphone or camera. We do not use an advertising identifier. We do not
> use analytics or crash-reporting services. There are no third-party trackers in
> this app, and we do not sell or share your data with anyone.
>
> **No purchases or advertising.** DGD Arcade contains no advertising and no
> in-app purchases. Experience points and badges have no monetary value, cannot
> be exchanged for anything, and are not connected to any wallet, exchange or
> financial product.
>
> **Children.** DGD Arcade is not directed at children under [AGE]. We do not
> knowingly collect information from them, and because we collect no contact
> details we have no way to identify a user's age.
>
> **Security.** Traffic between the app and our server is encrypted in transit.
> Access tokens are stored on our server only as a cryptographic hash.
>
> **Deleting your data.** Open **Settings** in the app and choose **Delete my
> play record**. This permanently erases the anonymous record we hold for you —
> your experience points, badges, streak and play history — and cannot be
> undone. A separate control clears your game progress from your device. If you
> would rather ask us to do it, write to [EMAIL ADDRESS].
>
> **Changes.** We will post any change to this policy at this address and update
> the date above.
>
> **Contact.** [EMAIL ADDRESS]

---

## Play data safety — draft answers

| Question | Draft answer | Why |
|---|---|---|
| Does your app collect or share user data? | Yes | The anonymous play record leaves the device |
| Is data encrypted in transit? | Yes | HTTPS |
| Can users request data deletion? | **Yes** | Settings → Delete my play record |
| Personal info (name, email, address, phone, race, political, sexual orientation, etc.) | None | Never asked for |
| Financial info | None | No purchases, no wallet |
| Location | None | |
| Contacts, photos, files, calendar, messages | None | No permission requested |
| App activity — in-app actions | Collected, not shared | XP, answers, play timings |
| App activity — other user-generated content | None | Handles are assigned, not typed |
| App info and performance — crash logs, diagnostics | None | No crash SDK |
| Device or other IDs | **None** | `deviceHint` is the platform string only |
| Purpose | App functionality; fraud prevention and compliance | Progress, and the anti-farming checks |
| Data shared with third parties | None | |

The only Android permission in the manifest is `INTERNET`.

---

## Open items before this can be published

1. ~~**Deletion mechanism.**~~ **Done, 2026-09-17.** `DELETE /v1/me` plus the
   Settings controls described above, covered by server and widget tests. Still
   needs the contact address in item 2 to complete the policy wording.
2. **Legal entity name and contact address.** I do not know which entity
   publishes this or what address should receive privacy requests.
3. **Minimum age**, which drives the target-audience questionnaire and whether
   Families policy applies.
4. **Hosting for the policy** — it needs a stable public URL, ideally on
   digitalgold.co, before Play will accept it.
5. **The financial-products question.** DGD is a gold-backed digital asset, and
   Play treats finance and crypto as their own policy area. This app has no
   trading, wallet or purchase in it, which should keep it clear — but I have
   not verified that against current Play policy, and the questionnaire wording
   decides it. This needs a human who owns compliance, not a guess from me.
6. **Retention period.** The policy says records persist until deleted. If DGD
   wants a defined retention window, that is a policy decision and then a cron
   job.
