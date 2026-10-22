# Website accessibility audit — October 22, 2026

## Outcome and score

ClearWorth now follows the Tandem home-card pattern: one purple Explore button, followed by green supporting links. Watch demos, Technology, and Security are green links. Both cards use the same styling, spacing, underlines, hover states, and keyboard focus treatment.

**Automated accessibility score: 100/100.** This is the axe-core rule pass rate, calculated as `100 × passed rule evaluations / (passed + failed rule evaluations)`. The final run produced **873 passed rule evaluations and zero failed rule evaluations across 24 page/layout scans**. Repeated evaluations at different layouts are counted separately. Not-applicable rules and checks needing human review are excluded from this score. This is **not a Lighthouse score, a percentage of WCAG criteria satisfied, a desktop-app score, or a certification**.

The initial eight-page, two-layout scan had 554 passed and 16 failed rule evaluations, giving **97.2/100** under the same formula. There were eight failing rule/page combinations per layout: seven visible-label/accessibility-name mismatches and one heading-order issue. The later text-spacing configuration was added after remediation, so the final scan has eight additional configurations.

**Target: WCAG 2.2 Level AA.** All detected automated violations were fixed. The review also addressed keyboard usability, media alternatives, contrast, responsive layouts, and structural quality. A complete conformance claim remains pending the assistive-technology and human evaluation described below. WCAG AAA criteria, jurisdiction-specific legal certification, external sites, and the installed ClearWorth/Tandem applications are outside this website audit.

## Scope and methods

All eight published HTML pages were reviewed: Home, Projects, ClearWorth, Tandem, About, Blog, The journey to ClearWorth, and the 404 page. The website has no sign-in, checkout, or data-submission workflow; application login screenshots are informational images.

- axe-core **4.14.0**, using WCAG 2 A/AA, WCAG 2.1 A/AA, WCAG 2.2 AA, and best-practice rule tags.
- Chromium browser scans at 1280 CSS pixels and 320 CSS pixels, plus 320 pixels with text-spacing overrides. Each iframe had a 960-pixel height. Expanded disclosures were included in scans.
- Text-spacing overrides: line height 1.5, paragraph spacing 2em, letter spacing 0.12em, and word spacing 0.16em. All 24 configurations had no horizontal document overflow. This is reflow testing, not a claim that native 200%/400% browser zoom was tested on every browser.
- Keyboard checks for skip navigation, visible focus, search/filter/reset, video playback, text walkthrough disclosure, and the screenshot archive.
- Source checks for language, titles, headings, landmarks, labels, alternative text, duplicate IDs, positive tabindex, local links, fragments, and ARIA references.
- Contrast calculations for shared colors and gradient endpoints, alongside automated contrast checks. No text/gradient endpoint pair reviewed fell below the relevant AA threshold.
- Audio-stream inspection of all fourteen MP4 files, confirming no audio streams. Sampled visual frames from the beginning, middle, and later portion of each clip informed text walkthroughs.

## Changes published

| Area | Before | Update |
| --- | --- | --- |
| ClearWorth actions | Four purple actions | Purple Explore button; green Watch demos, Technology, and Security links, matching Tandem |
| Link visibility | Supporting links largely identified by color | Persistent underlines, thicker hover underlines, and identical styles across both projects |
| Accessible home link | Its ARIA name omitted part of the visible brand text | Removed the redundant label; the visible name supplies the accessible name |
| Directory headings | Project titles jumped from h1 to h3 | Project titles and the collection heading use h2 with the existing visual sizes |
| ARIA grouping | An unnamed-role div carried an unsupported label | Areas of interest now has a valid group role |
| Skip navigation | Destination was not explicitly focusable | Main landmark has tabindex -1; skip activation moves keyboard focus to main |
| Keyboard focus | Some native controls/disclosures lacked consistent treatment | Visible two-color focus treatment covers links, buttons, fields, summaries, and video; linked screenshots receive an inset two-color indicator |
| Input boundaries | Very light borders | Darker search/select borders, clearer placeholder text, and 48-pixel field height |
| Touch targets | Several navigation/supporting links had small heights | 44-pixel navigation, footer, section, card-link, and disclosure targets |
| Reflow | Potentially rigid controls and sticky mobile header | Wrapping navigation/actions, resilient grid children and table text, and a non-sticky header on narrow layouts |
| Motion/contrast preferences | Basic smooth-scroll opt-out | Reduced-motion rules and forced-colors-compatible control/focus borders |
| Walkthrough access | Short captions and silent video only | Fourteen expandable text walkthroughs linked to their players using aria-details; existing labels, captions, native controls, and MP4 links retained |
| Search semantics | Labels and status existed | Added aria-controls relationships; verified result announcements, no-results state, keyboard reset, and focus return |
| Regeneration | Changes could diverge between pages and source | Updated templates, editable content, generated pages, shared assets, and versioned stylesheet/script URLs |
| Regression checks | No dedicated structural check | Added scripts/check_accessibility.py; 215 local references passed validation |

ClearWorth Version 1.0.0 information, first-time Administrator setup image, returning-user sign-in image, and pending public-installer status remain in place. No phase labels were introduced.

## Per-page automated results

Each row represents three configurations: desktop, narrow, and narrow with increased text spacing. Counts are per configuration; the same counts occurred in all three configurations.

| Page | Passed rules | Failed rules | Page overflow |
| --- | ---: | ---: | --- |
| Home | 41 | 0 | None |
| Projects | 42 | 0 | None |
| ClearWorth | 46 | 0 | None |
| Tandem | 42 | 0 | None |
| About | 35 | 0 | None |
| Blog | 32 | 0 | None |
| The journey to ClearWorth | 34 | 0 | None |
| 404 | 19 | 0 | None |
| Total per configuration | 291 | 0 | None |

The automated engine continued to request human review for contrast over gradients (20 nodes on Home, six on ClearWorth, nine on About per configuration) and for the fourteen silent video players. These are **incomplete checks**, not automatic passes or confirmed failures. They were not suppressed. Color-pair calculations and audio inspection addressed part of that review; comprehensive media-equivalence review remains open.

## Contrast and interaction evidence

| Shared color pairing | Measured ratio | Relevant threshold |
| --- | ---: | ---: |
| White text / purple primary button | 5.48:1 | 4.5:1 normal text |
| Green supporting link / white | 5.85:1 | 4.5:1 normal text |
| Green supporting link / page background | 5.58:1 | 4.5:1 normal text |
| Muted text / page background | 6.28:1 | 4.5:1 normal text |
| Input border / white | 4.73:1 | 3:1 UI boundary |
| Light body text / lighter dark-gradient endpoint | 10.67:1 | 4.5:1 normal text |
| Lavender / lighter dark-gradient endpoint | 6.12:1 | 4.5:1 normal text |
| Muted caption / lavender-gradient endpoint | 5.50:1 | 4.5:1 normal text |

Keyboard checks confirmed that Skip to content focuses main, the next Tab reaches the first main-content action, search produces one matching project, an incompatible category produces zero results, and Enter on Reset search restores both cards and focuses the search field. Enter toggles the video text disclosure and archive. Space started and paused the first video with native controls; playback reached readyState 4. All fourteen players have accessible names and description references. Native media controls remain browser-dependent.

## WCAG 2.2 A/AA coverage and limitations

“Reviewed” below means source, automated checks, or the described browser interaction was evaluated. It does not substitute for a complete assistive-technology test. “Not applicable” is based on the current site, not future interactive additions.

| Criteria | Review outcome |
| --- | --- |
| 1.1.1 Non-text content | Image alternatives, linked-image names, captions, and concept-illustration labels reviewed; expert judgment of every image's equivalent meaning remains advisable |
| 1.2.1 Audio-only/video-only | All clips confirmed silent; text alternatives added; full visual-information equivalence needs a dedicated end-to-end media review |
| 1.2.2 Captions; 1.2.3 Audio description/media alternative; 1.2.5 Audio description | No synchronized audio content on this site; reassess if narration/audio is added |
| 1.3.1 Info/relationships; 1.3.2 Meaningful sequence | Headings, landmarks, lists, captions, table headers and form relationships reviewed; native screen-reader reading order still needs testing |
| 1.3.3 Sensory characteristics | Website navigation and instructions use names and text, not color/position alone |
| 1.3.4 Orientation | Responsive layouts have no orientation lock; physical-device portrait/landscape testing pending |
| 1.3.5 Identify input purpose | Website has search/filter controls, no personal-data entry fields requiring autocomplete purposes |
| 1.4.1 Use of color | Supporting links now underlined; site statuses use text; application screenshots are not interactive website controls |
| 1.4.2 Audio control | Not applicable: no audio streams/autoplay audio |
| 1.4.3 Contrast minimum | Automated checks plus shared-color/gradient calculations passed reviewed pairs; unresolved engine items are documented above |
| 1.4.4 Resize text | Narrow layout reviewed; native text-only zoom and 200% zoom across browsers pending |
| 1.4.5 Images of text | Product logo and explanatory application screenshots retained; substantive website copy remains HTML |
| 1.4.10 Reflow | All pages passed 320 CSS-pixel width without horizontal page overflow; native 400% zoom cross-browser verification pending |
| 1.4.11 Non-text contrast | Input borders and focus indicators improved; native high-contrast/media-control testing pending |
| 1.4.12 Text spacing | All eight pages passed the stated overrides at 320 pixels; no detected page overflow |
| 1.4.13 Content on hover/focus | No custom hover-only tooltips, menus, or popovers in current site |
| 2.1.1 Keyboard; 2.1.2 No keyboard trap | Key website interactions tested using keyboard; no custom traps or dialogs found; broader AT/browser matrix pending |
| 2.1.4 Character key shortcuts | No single-character website shortcuts |
| 2.2.1 Timing adjustable; 2.2.2 Pause/stop/hide | No website time limits or autoplay; video is user-controlled with native pause |
| 2.3.1 Three flashes | No flashing website effects; sampled videos show ordinary interface changes, not a formal photosensitivity analysis |
| 2.4.1 Bypass blocks | Skip link focuses the main landmark on navigation-bearing pages; standalone 404 has no repeated navigation |
| 2.4.2 Page titled | Descriptive titles on all eight pages |
| 2.4.3 Focus order | DOM order and sampled keyboard flow reviewed; no positive tabindex |
| 2.4.4 Link purpose | Contextual project names, descriptive image/MP4 links, and supporting link text reviewed |
| 2.4.5 Multiple ways | Shared navigation, project directory/search and contextual links provide routes through the site |
| 2.4.6 Headings/labels | Heading-order issue fixed; controls have visible labels; disclosures have readable summaries |
| 2.4.7 Focus visible; 2.4.11 Focus not obscured | Focus styles improved and sampled; narrow header no longer sticky; full AT/zoom matrix pending |
| 2.5.1 Pointer gestures; 2.5.7 Dragging movements | Website has no custom multipoint/path/drag gestures; app actions shown in video are outside scope |
| 2.5.2 Pointer cancellation | Native links, buttons, fields and disclosures used; no custom pointerdown activation |
| 2.5.3 Label in name | Visible-label/accessibility-name mismatch fixed; scans pass |
| 2.5.4 Motion actuation | No device-motion interactions |
| 2.5.8 Target size minimum | Automated target checks pass; major navigation/action targets enlarged to 44 pixels; inline text links/native controls use applicable exceptions |
| 3.1.1 Language of page; 3.1.2 Language of parts | English language declared; no substantive passages in another language identified |
| 3.2.1 On focus; 3.2.2 On input | Focus does not navigate automatically; search/category changes update results in place with a status message |
| 3.2.3 Consistent navigation; 3.2.4 Consistent identification | Shared templates and identical project action styles applied across pages |
| 3.2.6 Consistent help | No dedicated recurring help mechanism; professional contact links remain contextual |
| 3.3.1 Error identification; 3.3.2 Labels/instructions; 3.3.3 Error suggestion | Search/filter labels and no-results guidance reviewed; no transactional form-validation workflow |
| 3.3.4 Error prevention; 3.3.7 Redundant entry; 3.3.8 Accessible authentication | No website financial/legal submission, multi-step data-entry, or authentication workflow |
| 4.1.2 Name/role/value | Automated checks pass; native controls and valid ARIA relationships used |
| 4.1.3 Status messages | Search count uses role=status; updates and reset verified in DOM; spoken announcement verification pending |

## Remaining validation before a conformance claim

1. Test NVDA with Windows Chrome/Firefox and VoiceOver with Safari, including spoken search updates, table reading, skip navigation, image links, disclosure states, and native video controls.
2. Test actual 200% text enlargement, 400% browser zoom, physical mobile portrait/landscape, Windows High Contrast, and the OS reduced-motion preference. CSS support and narrow-layout tests are implemented, but those environment tests were not completed here.
3. Have a human reviewer assess the full fourteen videos against their text alternatives, and every explanatory image against its alt/caption. The current walkthrough text describes the main actions and results; sampled-frame review is not a comprehensive transcript-equivalence certification.
4. Include people with disabilities in usability testing and record the browser/assistive-technology versions and findings.

No known automated violations remain. The uncompleted manual evaluations above prevent an unqualified claim that the website meets every WCAG AA requirement or every accessibility recommendation.

## Maintenance

After content changes, run `python scripts/build.py` followed by `python scripts/check_accessibility.py`. Repeat axe scans and manual keyboard/reflow review after shared-template or CSS changes. Recheck media alternatives whenever screenshots or recordings are replaced. Keep meaningful information in HTML rather than only in screenshots. Preserve native controls, visible focus, descriptive links, and accessible status messages.

## Standards references

- [WCAG 2 overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Understanding conformance](https://www.w3.org/WAI/WCAG22/Understanding/conformance)
- [axe-core](https://github.com/dequelabs/axe-core)

W3C describes conformance testing as a combination of automated testing and human evaluation. The score in this report intentionally does not treat automation as proof of full conformance.
