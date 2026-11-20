// A static, same-origin slide viewer. The original PowerPoint remains unchanged.
(() => {
  for (const viewer of document.querySelectorAll('[data-slide-deck]')) {
    const controls = viewer.querySelector('[data-deck-controls]');
    const previous = viewer.querySelector('[data-deck-previous]');
    const next = viewer.querySelector('[data-deck-next]');
    const select = viewer.querySelector('[data-deck-select]');
    const image = viewer.querySelector('[data-deck-image]');
    const original = viewer.querySelector('[data-deck-original]');
    const caption = viewer.querySelector('[data-deck-caption]');
    const transcript = viewer.querySelector('[data-deck-transcript]');
    const error = viewer.querySelector('[data-deck-error]');
    const fullscreen = viewer.querySelector('[data-deck-fullscreen]');
    let slides = [], index = 0;
    const showError = message => { error.textContent = message; error.hidden = false; };
    image.addEventListener('error', () => showError('This slide image could not load. Try another slide or open the PDF below.'));
    image.addEventListener('load', () => { error.hidden = true; });
    function show(position) {
      index = Math.max(0, Math.min(position, slides.length - 1));
      const slide = slides[index];
      image.src = slide.url;
      image.alt = `Slide ${index + 1} of ${slides.length}: ${slide.title}. Read the slide text below for an accessible version.`;
      original.href = slide.url;
      original.setAttribute('aria-label', `Open full-size image of slide ${index + 1}: ${slide.title}`);
      caption.textContent = `Slide ${index + 1} of ${slides.length}: ${slide.title}`;
      transcript.textContent = slide.text;
      select.value = String(index);
      previous.disabled = index === 0;
      next.disabled = index === slides.length - 1;
      error.hidden = true;
      // Preload only the next image; avoid downloading the entire deck on page load.
      if (slides[index + 1]) { const ahead = new Image(); ahead.src = slides[index + 1].url; }
    }
    previous.addEventListener('click', () => show(index - 1));
    next.addEventListener('click', () => show(index + 1));
    select.addEventListener('change', () => show(Number(select.value)));
    viewer.addEventListener('keydown', event => {
      if (!slides.length || event.altKey || event.ctrlKey || event.metaKey || event.target.closest('button,a,select,input,textarea,summary')) return;
      const positions = { ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: slides.length - 1 };
      if (!(event.key in positions)) return;
      event.preventDefault(); show(positions[event.key]);
    });
    if (typeof viewer.requestFullscreen === 'function') {
      fullscreen.hidden = false;
      fullscreen.addEventListener('click', async () => {
        try {
          if (document.fullscreenElement === viewer) await document.exitFullscreen();
          else await viewer.requestFullscreen();
        } catch { showError('Full-screen viewing is unavailable here. Use Open slide image or Open PDF instead.'); }
      });
      document.addEventListener('fullscreenchange', () => {
        fullscreen.textContent = document.fullscreenElement === viewer ? 'Exit full screen' : 'Full screen';
      });
    }
    const manifest = new URL(viewer.dataset.manifest, document.baseURI);
    fetch(manifest, { signal: AbortSignal.timeout(20000) }).then(response => {
      if (!response.ok) throw Error('Manifest unavailable');
      return response.json();
    }).then(data => {
      if (!Array.isArray(data.slides) || data.slides.length !== Number(viewer.dataset.count)) throw Error('Invalid slide count');
      const imageFolder = new URL('slides/', manifest).pathname;
      slides = data.slides.map(slide => {
        const url = new URL(slide.image, manifest);
        if (url.origin !== manifest.origin || !url.pathname.startsWith(imageFolder) || typeof slide.title !== 'string' || typeof slide.text !== 'string') throw Error('Invalid slide');
        return { url: url.href, title: slide.title, text: slide.text };
      });
      select.replaceChildren(...slides.map((slide, i) => {
        const option = document.createElement('option'); option.value = String(i);
        option.textContent = `${i + 1}. ${slide.title}`; return option;
      }));
      controls.hidden = false;
      show(0);
    }).catch(() => showError('Slide navigation could not load. You can still download the PowerPoint or open the PDF below.'));
  }
})();
