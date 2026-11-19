// The links still open source screenshots when dialog support or JS is absent.
(() => {
  const dialog = document.querySelector('.cf-lightbox');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('img');
  const title = dialog.querySelector('h2');
  const zoom = dialog.querySelector('[data-zoom]');
  const original = dialog.querySelector('[data-original]');
  const media = dialog.querySelector('.cf-lightbox-media');
  let trigger;
  for (const link of document.querySelectorAll('.cf-zoom')) {
    link.addEventListener('click', (event) => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      trigger = link;
      image.src = link.href;
      image.alt = link.querySelector('img').alt;
      title.textContent = link.dataset.caption;
      original.href = link.href;
      dialog.classList.remove('cf-actual-size');
      zoom.textContent = 'Actual size';
      zoom.setAttribute('aria-pressed', 'false');
      dialog.showModal();
      media.scrollTop = media.scrollLeft = 0;
    });
  }
  zoom.addEventListener('click', () => {
    const actual = dialog.classList.toggle('cf-actual-size');
    zoom.textContent = actual ? 'Fit image' : 'Actual size';
    zoom.setAttribute('aria-pressed', String(actual));
  });
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => trigger?.focus());
})();

