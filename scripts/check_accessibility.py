"""Dependency-free structural accessibility/link checks for the published pages.

Run after build.py. Browser checks and human evaluation are still required.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'projects/index.html', 'projects/clearworth/index.html',
         'projects/tandem/index.html', 'about/index.html', 'blog/index.html',
         'blog/the-journey-to-clearworth/index.html', '404.html']


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


documents = {p: Document((ROOT / p).read_text()) for p in PAGES}
errors = []
references = 0
for path, doc in documents.items():
    def require(condition, message):
        if not condition:
            errors.append(f'{path}: {message}')

    ids = [a['id'] for _, a in doc.elements if 'id' in a]
    require(not [key for key, n in Counter(ids).items() if n > 1], 'duplicate IDs')
    require(any(t == 'html' and a.get('lang') == 'en' for t, a in doc.elements), 'missing page language')
    require(sum(t == 'h1' for t, _ in doc.elements) == 1, 'expected one h1')
    require(sum(t == 'main' for t, _ in doc.elements) == 1, 'expected one main landmark')
    labels = {a['for'] for t, a in doc.elements if t == 'label' and 'for' in a}
    previous_heading = 0
    for tag, attrs in doc.elements:
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            require(level <= previous_heading + 1, f'heading skips from h{previous_heading} to h{level}')
            previous_heading = level
        if tag == 'img':
            require('alt' in attrs, f'image missing alternative text: {attrs.get("src")}')
        if tag in ['input', 'select', 'textarea'] and attrs.get('type') != 'hidden':
            require(attrs.get('id') in labels or bool(attrs.get('aria-label') or attrs.get('aria-labelledby')), 'unlabelled input')
        require(not (attrs.get('tabindex', '').isdigit() and int(attrs['tabindex']) > 0), 'positive tabindex')
        for attribute in ['aria-labelledby', 'aria-describedby', 'aria-controls', 'aria-details']:
            for target in attrs.get(attribute, '').split():
                require(target in ids, f'{attribute} references missing #{target}')
        for attribute in ['href', 'src', 'poster']:
            value = attrs.get(attribute)
            if not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            target = ROOT / unquote(url.path.lstrip('/')) if url.path.startswith('/') else ROOT / Path(path).parent / unquote(url.path)
            if not url.path:
                target = ROOT / path
            if target.is_dir():
                target /= 'index.html'
            require(target.exists(), f'missing local target {value}')
            references += 1
            if url.fragment and target.suffix == '.html' and target.exists():
                other = Document(target.read_text())
                require(any(a.get('id') == unquote(url.fragment) for _, a in other.elements), f'missing fragment {value}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(PAGES)} pages; {references} local references; headings, language, main landmarks, image alternatives, labels, IDs and ARIA references.')
