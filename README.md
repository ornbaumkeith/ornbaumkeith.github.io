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
- Home-page illustrations are explicitly labeled product concepts. The ClearWorth page uses original app screenshots supplied by the owner and original logo artwork from the Phase 27.3 release package.

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
