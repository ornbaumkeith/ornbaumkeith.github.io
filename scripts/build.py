from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parents[1]
projects = json.loads((ROOT / 'projects.json').read_text())

def esc(s): return escape(str(s), quote=True)
def page(title, description, content, active='home', depth=0):
    prefix = '../' * depth
    def link(path): return prefix + path
    nav = ''.join(f'<a href="{link(path)}"'+(' aria-current="page"' if key == active else '')+f'>{label}</a>' for key,path,label in [('home','index.html','Home'),('projects','projects/index.html','Projects'),('blog','blog/index.html','Blog'),('about','about/index.html','About')])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | Keith Ornbaum</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#111114"><link rel="icon" href="{link('assets/favicon.svg')}" type="image/svg+xml"><link rel="stylesheet" href="{link('assets/style.css')}"><script src="{link('assets/app.js')}" defer></script></head><body>
<a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap nav"><a class="brand" href="{link('index.html')}" aria-label="Keith Ornbaum home"><span class="monogram" aria-hidden="true">KO</span>Keith Ornbaum<span style="font-weight:400;color:var(--muted)"> / Projects</span></a><nav class="nav-links" aria-label="Main navigation">{nav}<a class="external" href="https://github.com/ornbaumkeith">GitHub <span aria-hidden="true">↗</span></a></nav></div></header>
<main id="main" class="wrap">{content}</main><footer class="footer"><div class="wrap footer-inner"><span>© 2026 Keith Ornbaum. Built with purpose.</span><div class="footer-links"><a href="{link('projects/index.html')}">Explore projects</a><a href="https://github.com/ornbaumkeith">GitHub ↗</a></div></div></footer></body></html>'''

def cards(prefix=''):
    out=[]
    for p in projects:
        path=f"{prefix}projects/{p['id']}/index.html"
        chips=''.join(f'<span class="pill">{esc(t)}</span>' for t in p['tags'])
        # Editorial product illustration, never represented as an application screenshot.
        art = '<div class="abstract" role="img" aria-label="ClearWorth concept illustration: income, expenses, and goals"><div class="mark">ClearWorth<span style="color:#81ba93">.</span></div><div class="row"><span>Income</span><b>Plan ahead</b></div><div class="row"><span>Expenses</span><b>Stay organized</b></div><div class="row"><span>Goals</span><b>Track progress</b></div><p class="visual-label">Product concept · not an app screenshot</p></div>' if p['id']=='clearworth' else f'<div class="abstract"><div class="mark">{esc(p["name"])}</div><p>{esc(p["category"])}</p></div>'
        search=esc(' '.join([p['name'],p['summary'],p['category'],*p['tags'],*p['stack']]).lower())
        links=f'<a class="button" href="{path}">Explore project <span aria-hidden="true">↗</span></a>'
        for field,label in [('demo_url','Live demo'),('download_url','Download'),('source_url','Source')]:
            if p.get(field): links+=f'<a class="text-link" href="{esc(p[field])}">{label} ↗</a>'
        out.append(f'<article class="project-card" data-project data-category="{esc(p["category"])}" data-search="{search}"><div class="project-art">{art}</div><div class="project-copy"><div class="chips"><span class="pill">{esc(p["category"])}</span><span class="pill">{esc(p["status"])}</span></div><h3><a href="{path}">{esc(p["name"])}</a></h3><p>{esc(p["summary"])}</p><div class="chips">{chips}</div><div class="card-links">{links}</div></div></article>')
    return '<div style="display:grid;gap:24px">'+''.join(out)+'</div>'

quiet='<aside class="quiet-panel"><div><h3>A growing collection.</h3><p>This portfolio will expand as more projects are ready to share.</p></div><span class="small-tag">Software · GIS · Automation</span></aside>'
home='''<section class="hero"><div class="hero-grid"><div><div class="eyebrow">Software, GIS & automation</div><h1>Ideas into tools.<br><span class="accent">Tools into impact.</span></h1><p class="intro">I'm Keith Ornbaum. This is a home for the projects I build, the problems they solve, and the work behind them.</p><div class="actions"><a class="button" href="projects/index.html">Explore projects <span aria-hidden="true">↗</span></a><a class="button secondary" href="about/index.html">Meet the builder</a></div><p class="hero-note">Practical projects. Thoughtful design. Room to grow.</p></div><div class="showcase"><div class="showcase-top"><span>In the spotlight</span><span>Desktop application</span></div><div class="cw-symbol" aria-hidden="true">↗</div><h2>ClearWorth</h2><p>A clearer view of your finances, built around a local-first Windows experience.</p><div class="chips"><span class="pill">Windows</span><span class="pill">Personal finance</span><span class="pill">In development</span></div><div class="diagram" role="img" aria-label="ClearWorth brings planning, tracking, and financial review together"><div><span aria-hidden="true">◷</span>Plan</div><div><span aria-hidden="true">▤</span>Track</div><div><span aria-hidden="true">↗</span>Review</div></div><p class="visual-label">An overview of the project, not an app screenshot.</p></div></div></section><div class="strip" aria-label="Areas of interest"><span>Desktop software</span><span>Location intelligence</span><span>Workflow automation</span><span>Data & databases</span></div><section class="section" aria-labelledby="featured-heading"><div class="section-head"><div><div class="eyebrow">Selected work</div><h2 id="featured-heading">Projects with a purpose.</h2></div><a class="text-link" href="projects/index.html">View project directory ↗</a></div>'''+cards()+quiet+'''</section><section class="about-band" aria-labelledby="about-heading"><div><div class="eyebrow">Behind the projects</div><h2 id="about-heading">A builder's mindset.<br>A practical approach.</h2><p>My background spans enterprise GIS, location intelligence, databases, and automation. I bring that same focus on useful solutions to my personal projects.</p><a class="text-link" href="about/index.html">More about me ↗</a></div><div class="focus-list"><div class="focus-item">Make complex work easier <span aria-hidden="true">01</span></div><div class="focus-item">Connect data and decisions <span aria-hidden="true">02</span></div><div class="focus-item">Build, learn, and improve <span aria-hidden="true">03</span></div></div></section>'''
(ROOT/'index.html').write_text(page('Projects & practical tools','Explore software, GIS, and automation projects by Keith Ornbaum, including ClearWorth.',home))
options=''.join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in sorted({p['category'] for p in projects}))
directory='''<section class="page-hero"><div class="eyebrow">Project directory</div><h1>Explore the work.</h1><p>Applications, tools, and ideas built to solve practical problems. Each project has its own space for the details, resources, and next steps.</p></section><section aria-label="Project collection"><div class="toolbar"><div class="search"><label for="project-search">Find a project</label><input id="project-search" type="search" placeholder="Search by name, topic, or technology…"></div><div class="filter"><label for="project-category">Project type</label><select id="project-category"><option value="all">All projects</option>'''+options+'''</select></div></div><p id="result-count" class="result-count" role="status">'''+str(len(projects))+''' project shown</p>'''+cards('../')+'''<div id="empty-results" class="empty" hidden><h3>No projects found.</h3><p>Try another search or browse the full collection.</p><button id="reset-search" class="button" type="button">Reset search</button></div>'''+quiet+'''</section>'''
(ROOT/'projects/index.html').write_text(page('Project directory','Browse projects by Keith Ornbaum. Search software, GIS, and automation work.',directory,'projects',1))
features=[('Income & expenses','Organize income sources, recurring expenses, due dates, and payment status.'),('Financial planning','Review weekly, monthly, and annual finances, including projected activity.'),('Savings & debt','Keep savings goals and debt planning alongside everyday finances.'),('Financial calendar','Bring financial dates and personal events into a single calendar.'),('Metrics & charts','Review financial activity through dashboards, metrics, and charts.'),('Local-first workflow','Work with local data, file imports, and backup and restore tools.')]
feature_html=''.join(f'<article class="feature"><h3>{h}</h3><p>{p}</p></article>' for h,p in features)
cw = (ROOT / 'content/clearworth.html').read_text()
(ROOT/'projects/clearworth/index.html').write_text(page('ClearWorth','Discover ClearWorth, a local-first Windows personal finance application by Keith Ornbaum.',cw,'projects',2))
about='''<section class="page-hero"><div class="eyebrow">About the builder</div><h1>Hi, I'm Keith.</h1><p>I work at the intersection of enterprise GIS, data, automation, and practical problem solving.</p></section><section class="section" style="padding-top:20px"><p class="bio">This portfolio is a place to share my personal projects, explain the ideas behind them, and make useful tools easier to discover.</p><div class="bio-grid" style="margin-top:45px"><div><h2 style="font-size:30px">Experience that connects.</h2><p>My professional background includes enterprise GIS and location intelligence, with work across ArcGIS Enterprise, SQL Server, data workflows, and automation.</p><p>That experience shapes how I approach personal projects: understand the problem, make the workflow clear, and improve through testing and feedback.</p></div><div><h2 style="font-size:30px">A portfolio that grows.</h2><p>ClearWorth is the first featured project here. The site is designed to grow into a collection of applications, GIS tools, automation projects, and supporting resources.</p><p>Each project can have its own overview, technical details, documentation, demos, and downloads when those resources are available.</p><a class="text-link" href="../projects/index.html">Explore the project collection ↗</a></div></div><div class="actions"><a class="button" href="https://github.com/ornbaumkeith">Find me on GitHub ↗</a></div></section>'''
(ROOT/'about/index.html').write_text(page('About','About Keith Ornbaum: enterprise GIS, data, automation, and personal software projects.',about,'about',1))
# New entries receive a project page automatically. ClearWorth has the richer custom page above.
for p in projects:
    if p['id']=='clearworth': continue
    folder=ROOT/'projects'/p['id']; folder.mkdir(parents=True,exist_ok=True)
    body=f'<div class="crumb"><a href="../index.html">Projects</a> / {esc(p["name"])}</div><section class="page-hero"><div class="eyebrow">{esc(p["category"])} · {esc(p["status"])}</div><h1>{esc(p["name"])}</h1><p>{esc(p["summary"])}</p><div class="chips">'+''.join(f'<span class="pill">{esc(t)}</span>' for t in p['tags'])+'</div></section><section class="section"><h2>Project resources</h2><div class="actions">'
    for field,label in [('demo_url','Open live demo'),('download_url','Download project'),('source_url','View source')]:
        if p.get(field): body+=f'<a class="button" href="{esc(p[field])}">{label} ↗</a>'
    if not any(p.get(f) for f in ['demo_url','download_url','source_url']): body+='<p>Public resources have not been published yet.</p>'
    body+='</div><p class="back"><a class="text-link" href="../index.html">← All projects</a></p></section>'
    (folder/'index.html').write_text(page(p['name'],p['summary'],body,'projects',2))
print(f'Built portfolio with {len(projects)} project(s).')

# Blog entries are published only when the owner supplies finished post content.
posts = json.loads((ROOT / 'posts.json').read_text())
post_cards = []
for post in sorted(posts, key=lambda p: p['date'], reverse=True):
    slug = post['id']
    if not slug or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in slug):
        raise ValueError('Post IDs must use lowercase letters, numbers, and hyphens.')
    body = (ROOT / 'content/blog' / (slug + '.html')).read_text()
    folder = ROOT / 'blog' / slug
    folder.mkdir(parents=True, exist_ok=True)
    article = f'<div class="crumb"><a href="../index.html">Blog</a> / {esc(post["title"])}</div><article class="blog-article"><header class="page-hero"><div class="eyebrow">{esc(post["category"])}</div><h1>{esc(post["title"])}</h1><p class="post-meta">Keith Ornbaum · <time datetime="{esc(post["date"])}">{esc(post["date"])}</time></p></header><div class="article-body">{body}</div><p class="back"><a class="text-link" href="../index.html">← All posts</a></p></article>'
    (folder / 'index.html').write_text(page(post['title'], post['summary'], article, 'blog', 2))
    post_cards.append(f'<article class="doc"><span class="pill">{esc(post["category"])}</span><p class="post-meta"><time datetime="{esc(post["date"])}">{esc(post["date"])}</time></p><h3><a href="{esc(slug)}/index.html">{esc(post["title"])}</a></h3><p>{esc(post["summary"])}</p><a class="text-link" href="{esc(slug)}/index.html">Read post ↗</a></article>')
intro = (ROOT / 'content/blog.html').read_text()
collection = '<div class="docs">' + ''.join(post_cards) + '</div>' if posts else '<div class="blog-empty"><span class="pill">Getting started</span><h3>The first post is still ahead.</h3><p>There are no published posts yet. In the meantime, explore ClearWorth and the work behind this portfolio.</p><a class="button" href="../projects/index.html">Explore projects ↗</a></div>'
(ROOT / 'blog/index.html').write_text(page('Blog', 'Project stories, practical lessons, and perspectives on software, enterprise GIS, data, and automation from Keith Ornbaum.', intro + '<section class="section blog-posts" aria-labelledby="posts-heading"><div class="section-head"><div><div class="eyebrow">From the notebook</div><h2 id="posts-heading">Latest posts.</h2></div></div>' + collection + '</section>', 'blog', 1))
