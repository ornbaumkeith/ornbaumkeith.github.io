# Keith Ornbaum — Projects

A responsive portfolio for personal software, GIS, and automation projects.

Website: https://ornbaumkeith.github.io/

## Structure

- `index.html` — home and featured projects
- `projects/index.html` — searchable project directory
- `projects/clearworth/index.html` — ClearWorth overview and availability
- `about/index.html` — professional background
- `projects.json` — project catalog and optional demo, download, and source links
- `assets/` — shared stylesheet, search behavior, favicon, and original ClearWorth screenshots/logo
- `content/clearworth.html` — editable ClearWorth page content preserved during regeneration
- `scripts/build.py` — generates static pages from the catalog

## Run locally (PowerShell)

From the repository folder, with Python 3 installed:

```powershell
py -3 .\scripts\build.py
py -3 -m http.server 8000
```

Open http://localhost:8000/ in your browser. Stop the server with Ctrl+C.

No npm install or build dependencies are required. The site uses optional Google Fonts with local system font fallbacks.

## Add a project

1. Add an object to `projects.json`. Use a unique lowercase, hyphenated `id` for its folder name.
2. Provide `name`, `category`, `status`, `summary`, `tags`, and `stack`. Set optional resource URLs to `null` until published.
3. Run `py -3 .\scripts\build.py`. The project directory, home cards, category options, and a basic project page are generated automatically.
4. Commit the catalog and generated HTML. Customize the generator for richer project-specific pages so regeneration preserves your changes.

Example object (template only; not a published project):

```json
{
  "id": "your-project",
  "name": "Your Project",
  "category": "GIS tool",
  "status": "In development",
  "summary": "Describe the real problem the project solves.",
  "tags": ["GIS", "Automation"],
  "stack": ["Python"],
  "featured": false,
  "download_url": null,
  "demo_url": null,
  "source_url": null
}
```

The home currently presents the full published catalog. The `featured` field is available for future selection rules.

## Downloads, demos, and documentation

- Publish Windows installers and ZIPs as GitHub Release assets in a project repository, then add their real URLs to `download_url`.
- For ClearWorth, update the dedicated availability section in `content/clearworth.html` when a public release is ready, including actual version and installation instructions.
- Static web demos can live under a project folder. Link them using `demo_url`.
- Add public guides under a project folder and link them from its page.
- Application source remains separate unless a `source_url` is intentionally provided. This portfolio does not contain ClearWorth source code or financial data.
- The home page uses supplied ClearWorth and Tandem previews. ClearWorth's current images are labeled as October 3, 2026 development captures; replace them with reviewed release media when supplied.

## GitHub Pages

This is a plain HTML/CSS/JavaScript site. The `.nojekyll` file bypasses Jekyll processing.
In repository Settings → Pages, use **Deploy from a branch**, branch **master**, folder **/(root)**.
Changes to that branch are published by GitHub Pages when that configuration is enabled.

The existing repository history retains the original starter site for rollback.

## Blog

`blog/index.html` is the blog landing page, linked from the navigation across the site. It starts with an honest empty state; no posts are published until content is provided.

To publish a post:

1. Write the article body as HTML in `content/blog/<id>.html`, using headings, paragraphs, lists, and local images as needed.
2. Add an entry to `posts.json` with `id` (lowercase letters, numbers, hyphens), `title`, `date` (YYYY-MM-DD), `category`, and `summary`.
3. Run `py -3 .\scripts\build.py` and review the generated blog index and article page.
4. Commit the post content, catalog, and generated pages to publish.

Posts are ordered newest first. Use only information you intend to publish publicly. The blog is a static publishing workflow managed through the repository.

## ClearWorth 1.0.0 release preparation

See [the publishing guide](docs/ClearWorth-1.0.0-Publishing.md) for source findings, Windows validation, release assets, GitHub publication and media sharing. The website references ClearWorth Version 1.0.0 throughout. Application binaries and final validation are handled in the application release workflow. No download URL is set before a verified public release exists.

`content/home.html` preserves the detailed ClearWorth and Tandem home showcases during regeneration. Update it with the home page when editing featured copy. `content/clearworth.html` remains authoritative for the dedicated ClearWorth page. The ClearWorth page includes fourteen silent MP4 walkthroughs, ten current screenshots and generated poster frames under `assets/clearworth/latest/`. Earlier October 3 captures remain in an expandable archive. Current supplied media documents development behavior; the 1.0.0 installer remains planned. Videos use native controls, full-screen support and `preload="none"`.

## Additional ClearWorth media

The current page contains fourteen controlled, silent MP4 walkthroughs, including Dashboard creation, dashboard analytics, widget customization (converted from the supplied animated GIF), Planning Studio, and Help. The supplied login GIF is a single-frame image and is presented as a PNG. Current screenshots include Planning, income schedules, login, Calendar, and Budget. The Help clip retains an earlier transaction location; its caption points readers to Import in the latest reviewed source. Development captures do not establish final 1.0.0 validation.

The final media batch adds Reports, Global Search, Security controls, Settings/themes and Import/Sync clips, plus Reports, Security Audit and Backup/Restore screenshots. Public excerpts omit profile contacts, populated user lists and Windows save dialogs. The misleadingly named backup recording is labeled Import/Sync based on its content. Website text and publishing guidance use Version 1.0.0 with no development-stage labels. The application source archive has not been relabeled or rebuilt by website edits.

The home-card ClearWorth and Tandem actions share one purple primary button and green underlined supporting links, with wrapping between whole actions, and the gallery now includes first-time Administrator setup alongside returning-user sign-in. The newer review manifest confirms 1.0.0; website security wording preserves the unresolved audit and release-validation limits.

## Website accessibility

The [October 22, 2026 accessibility report](docs/Website-Accessibility-Audit-2026-10-22.md) records WCAG 2.2 AA review scope, changes, automated results, score methodology, contrast measurements, and remaining human/assistive-technology checks. The automated score is not a conformance certificate.

After regeneration, run `python scripts/check_accessibility.py` for dependency-free structural and internal-link checks. Recheck keyboard navigation, responsive layouts, text spacing, and media alternatives after changes to shared styles or content.

