# Store listing — draft copy and declarations

Everything the publishing team needs to paste into Play Console and App Store
Connect. Character limits are noted and every field here is inside them.

**Two warnings.** The descriptions avoid "earn", "reward", "cash", "value" and
anything implying a return, because DGD is a gold-backed asset and store
reviewers read game copy for exactly that. Please do not soften that in editing.
And the declarations in sections 3 and 4 are statements DGD makes on the record
— I wrote them from the database schema and the client, but compliance should
read them before submission.

---

## 1. Google Play

**App name** (30 max) — 14 used

    DGD Arcade

**Short description** (80 max) — 76 used

    Match the coins through the story of Digital Gold. Sixty levels, no ads.

**Full description** (4000 max) — ~1100 used

    DGD Arcade is the game side of the Digital Gold ambassador programme.

    COIN QUEST: DIGITAL GOLD
    Sixty hand-built levels across six worlds, following how Digital Gold is
    made and kept. Match three or more coins to clear them. Line up four or
    five to create pieces that clear whole rows, columns or neighbourhoods.

    Each world introduces something new:
    • The Mint — where coins are struck. Learn the swap.
    • The Ledger — seals to strip, one layer at a time.
    • The Vaults — sealed vaults crack open beside a match.
    • The Chain — move bullion down the line.
    • The Exchange — everything at once, with fewer moves.
    • The Network — the long haul.

    Every level has been played thousands of times by a simulation to tune its
    difficulty, so the curve is deliberate rather than accidental.

    EXPERIENCE POINTS AND BADGES
    Play earns experience points and badges, and a weekly leaderboard shows how
    you compare. Leaderboard names are assigned by us from a word list — you
    cannot type one — so the board never carries anyone's real name.

    Experience points and badges are part of the game. They have no monetary
    value, cannot be exchanged for anything, and are not connected to any
    wallet, exchange or financial product.

    NO ACCOUNTS, NO ADVERTS, NO PURCHASES
    There is no sign-up and no login. We never ask for your name, email address
    or phone number. There is no advertising anywhere in the app and nothing to
    buy. You can delete your play record from inside the app at any time.

    MORE GAMES COMING
    Ten more are in development.

**Category:** Games → Puzzle
**Tags:** match 3, puzzle, casual, educational
**Contact email:** *[needs the monitored inbox — see MEETING-BRIEF 1.2]*
**Website:** https://digitalgold.co
**Privacy policy:** *[needs the hosted URL]*

### Graphics

| Asset | Requirement | Status |
|---|---|---|
| App icon | 512×512 PNG, 32-bit, no transparency | `arcade/store/play-icon-512.png` |
| Feature graphic | 1024×500 PNG or JPG, no transparency | `arcade/store/feature-graphic-1024x500.png` |
| Phone screenshots | 2–8, min 320px, max 3840px, 16:9 or 9:16 | **Pending — phone was unplugged.** Plug the Pixel in and say so; five minutes |
| Tablet screenshots | Optional | Not supplied — phone-only layout |

**Shot list**, in the order they should appear on the listing. The first two
carry the whole pitch, because most people never scroll past them.

1. **Home** — coin, PROOF OF PLAY, the Coin Quest card, the no-monetary-value
   footer. Establishes what the app is and that it is clean.
2. **A board mid-cascade** — level 20-something, several coins clearing, a
   score popup visible. This is the one that sells a match-3.
3. **The level map** — six worlds, stars, obvious progression.
4. **A vault or ingot level** — level 28 or 31, showing the mechanics that are
   not just "match three".
5. **Win celebration** — fireworks and the star rating.
6. **Settings** — the deletion controls. Unusual on a listing, but it visibly
   backs the data-safety answers, which is worth a slot in an app attached to
   a financial brand.

---

## 2. Apple App Store

**App name** (30 max) — 14 used

    DGD Arcade

**Subtitle** (30 max) — 29 used

    Match-3 through Digital Gold

**Promotional text** (170 max, editable without review) — 138 used

    Sixty levels across six worlds, following how Digital Gold is made and
    kept. No adverts, no purchases, no account. Ten more games coming.

**Keywords** (100 max, comma-separated, no spaces after commas) — 94 used

    match3,puzzle,coins,gold,vault,casual,brain,tiles,swap,levels,offline,noads,education,arcade

**Description:** as the Play full description above. Apple does not allow
bullet characters to render as a list, so the "•" lines read as plain lines,
which is fine.

**Support URL:** *[needs a real page — a contact form or a support inbox]*
**Marketing URL:** https://digitalgold.co
**Category:** Games → Puzzle. Secondary: Games → Casual
**Copyright:** *[needs the legal entity name, e.g. "2026 <entity>"]*

### Screenshots
Apple requires at least one set. Supplying the 6.9" set covers the current
iPhone range; older sizes are generated from it by Apple where allowed.

**Not yet captured** — needs an iOS build on the Mac first. The Android
screenshots are the same screens at the same sizes, so the shot list carries
over exactly.

---

## 3. Play data safety — draft answers

Established by reading `arcade/server/src/db.ts`, `auth.ts` and
`arcade/app/lib/arcade/api.dart`.

| Question | Answer | Why |
|---|---|---|
| Does the app collect or share user data? | **Yes** | The anonymous play record leaves the device |
| Is data encrypted in transit? | **Yes** | HTTPS |
| Can users request data deletion? | **Yes** | Settings → Delete my play record, built 2026-09-17 |
| Personal info (name, email, address, phone, race, political views, sexual orientation…) | **None** | Never asked for |
| Financial info | **None** | No purchases, no wallet |
| Location | **None** | No permission requested |
| Contacts, photos, files, calendar, messages | **None** | No permission requested |
| App activity — in-app actions | **Collected, not shared** | XP, answers, play timings |
| App activity — user-generated content | **None** | Handles are assigned, never typed |
| App info and performance — crash logs, diagnostics | **None** | No crash SDK |
| Device or other IDs | **None** | `deviceHint` is the platform string only — "android", "ios" or "web" |
| Purpose | App functionality; fraud prevention | Progress, and the anti-farming checks |
| Data shared with third parties | **None** | |
| Data processed ephemerally | IP address | Seen transiently by the web server, not stored |

The only Android permission in the manifest is `INTERNET`.

---

## 4. Apple privacy labels — draft answers

Apple's categories differ from Google's, so this is not a copy of section 3.

| Apple category | Answer |
|---|---|
| Contact Info | Not collected |
| Health & Fitness | Not collected |
| Financial Info | Not collected |
| Location | Not collected |
| Sensitive Info | Not collected |
| Contacts | Not collected |
| User Content | Not collected |
| Browsing History | Not collected |
| Search History | Not collected |
| Identifiers | Not collected — no IDFA, no device ID; the player id is generated by us and not linked to any identity |
| Purchases | Not collected |
| Usage Data → Product Interaction | **Collected. Not linked to identity. Not used for tracking.** App functionality |
| Diagnostics | Not collected |

**Tracking:** No. The app does not track across apps or websites, does not use
an advertising identifier, and contains no third-party SDKs.

---

## 5. Content rating — draft answers

Needs sign-off (`MEETING-BRIEF.md` 2.3).

| Question | Draft answer |
|---|---|
| Violence | None |
| Sexuality, nudity | None |
| Profanity, crude humour | None |
| Controlled substances | None |
| **Simulated gambling** | **None** — match-3 with no wagering, no chance-based prizes, no loot boxes, no purchase of any kind |
| User interaction | None — no chat, no user-generated content, no sharing of personal info |
| Shares location | No |
| Digital purchases | No |
| Expected rating | Everyone / 4+ |

Worth stating plainly on the forms: the app awards points that cannot be bought,
sold, exchanged or withdrawn, and there is no mechanism of chance that pays out
anything. That is the distinction between this and simulated gambling.

---

## 6. Blanks that must be filled before submission

Repeated here so nothing is missed. All five come from `MEETING-BRIEF.md` 1.2,
plus two store-specific ones.

1. Legal entity name — policy, copyright line, both listings
2. Contact email — Play requires a monitored address on the listing
3. Privacy policy URL — both stores, hosted and live
4. Minimum age — drives the target-audience questionnaire on both
5. Retention period — or "until deleted"
6. Apple support URL — a real page, not the marketing site
7. Copyright year and holder — Apple only
