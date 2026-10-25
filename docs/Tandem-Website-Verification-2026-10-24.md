# Tandem website update — October 24, 2026

## Scope

Updated the existing Tandem project page, its homepage showcase, and the project directory/catalog. Other current projects, spreadsheet resources, and study-companion pages are preserved. The source ZIP is reviewed locally; application source, credentials, and binaries are not published as part of this website update.

## Evidence and product claims

The supplied `Tandem_MVP_0.5.0_Redesign_Source.zip` identifies version 0.5.0 in package.json and app.json. Reviewed README, architecture, security and 0.5.0 testing notes, shared/domain.ts, native/browser storage, source screens, and API implementation.

- Confirmed React Native/Expo, React/TypeScript, React Native Web, Node/Express, SQLite, native SecureStore, Expo calendar/notifications, Zod, Helmet, rate limiting and Nodemailer roles.
- Confirmed Apple/Android target platforms, iPad support configuration, responsive phone/wider navigation, personal/shared goals, daily/weekly actions, calendar, reflections, connected circles, copying and encouragement.
- Confirmed scoring: 2 XP/action, 10 XP/step, 50 XP/goal, 25 XP shared-goal team bonus, 200 XP/level. These development rules may change.
- Friendly competition is described through progress, XP, accountability, and self-agreed challenges with partners/other couples. No ranked cross-couple leaderboard, formal tournament, or prize system is claimed.
- Source default steps are Prep & Plan, Schedule & System, Track & Adjust, and Finish & Review.
- Coming soon is the public availability message. No release date, store approval, or download URL is invented. The ZIP is source/testing material, not a signed APK/AAB/IPA.
- Separate sharing toggles in the design image are explicitly distinguished from current goal-level server visibility. Native release validation and dependency remediation remain outstanding; no security or platform certification is claimed.

## Supplied images

Nineteen original PNG files copied byte-for-byte to assets/tandem/latest. No generated, retouched, or substitute images used. All receive visible captions, descriptive alternative text, dimensions, lazy loading (except the hero), and full-size image links.

Groups: Home (3), Goals/Journey (5), Calendar/Activity (5), Circles/Profile (3), Create Goal (3). The hero repeats one original Home image. Mobile_Goals_Dark.png is correctly captioned Journey; Mobile_Journey_White.png is correctly captioned Activity; msedge_JiXb3a5MKl.png is captioned Circles. Supplied example workspace values and names are not presented as verified user statistics.

## Accessibility verification

axe-core 4.14.0 checked the homepage, Tandem page, and directory at 1280, 768, 390 and 320 CSS pixels (12 scans), using WCAG 2 A/AA, 2.1 A/AA, 2.2 AA and best-practice tags. Results: zero detected violations, zero duplicate IDs and no horizontal document overflow. Each Tandem scan passed 42 applicable rules, with no incomplete rules. The homepage retains 22 gradient-contrast review nodes; these are engine limitations, not automatic passes. Existing shared color choices remain unchanged.

Keyboard checks verified the visible skip link, focus transfer to main, and Enter activation of a linked original screenshot. Native links, focus indicators, logical headings, navigation landmarks, table captions/scoped headers and visible image descriptions are retained. This website review does not certify the app or full WCAG conformance; NVDA/VoiceOver, native OS modes, and device-level app accessibility still require human testing.
