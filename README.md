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

## ClearWorth 1.2.0 website release

The primary download points to the public 1.2.0 testing pre-release and its SHA-256 checksum. The installer is unsigned and full source validation remains blocked by dependency audit findings. Do not describe this candidate as production-ready or as a completed security remediation.

Update `content/clearworth.html`, `content/home.html`, and `projects.json`, then run `python scripts/build.py`. The generated ClearWorth page, homepage, and project directory must remain consistent. Earlier supplied screenshots and silent videos remain development examples, not proof of 1.2.0 acceptance. Historical 1.0.0 documents under `docs/` describe that earlier release only.

The home-card ClearWorth and Tandem actions share one purple primary button and green underlined supporting links, with wrapping between whole actions, and the gallery now includes first-time Administrator setup alongside returning-user sign-in. The newer review manifest confirms 1.0.0; website security wording preserves the unresolved audit and release-validation limits.

## Website accessibility

The [October 22, 2026 accessibility report](docs/Website-Accessibility-Audit-2026-10-22.md) records WCAG 2.2 AA review scope, changes, automated results, score methodology, contrast measurements, and remaining human/assistive-technology checks. The automated score is not a conformance certificate.

After regeneration, run `python scripts/check_accessibility.py` for dependency-free structural and internal-link checks. Recheck keyboard navigation, responsive layouts, text spacing, and media alternatives after changes to shared styles or content.

