// Progressive enhancement: without JavaScript each image still opens its original.
(() => {
  const dialog = document.querySelector('.cf-lightbox');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('img');
  const title = dialog.querySelector('h2');
  let trigger;
  for (const link of document.querySelectorAll('.cf-zoom')) {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      trigger = link;
      image.src = link.href;
      image.alt = link.querySelector('img').alt;
      title.textContent = link.dataset.caption;
      dialog.showModal();
    });
  }
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => trigger?.focus());
})();
