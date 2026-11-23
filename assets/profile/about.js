const viewer = document.querySelector('#screenshot');
const fullImage = viewer.querySelector('img');
document.querySelectorAll('.shot').forEach(button => {
  button.addEventListener('click', () => {
    const preview = button.querySelector('img');
    viewer.querySelector('#viewer-title').textContent = button.dataset.title;
    fullImage.src = preview.currentSrc || preview.src;
    fullImage.alt = preview.alt;
    viewer.querySelector('#viewer-caption').textContent = preview.alt;
    viewer.showModal();
  });
});
