(() => {
  const search = document.querySelector('#project-search');
  const filter = document.querySelector('#project-category');
  if (!search || !filter) return;
  const cards = [...document.querySelectorAll('[data-project]')];
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-results');
  const update = () => {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    for (const card of cards) {
      const matches = card.dataset.search.includes(query) && (filter.value === 'all' || card.dataset.category === filter.value);
      card.hidden = !matches;
      if (matches) visible++;
    }
    count.textContent = `${visible} project${visible === 1 ? '' : 's'} shown`;
    empty.hidden = visible !== 0;
  };
  search.addEventListener('input', update);
  filter.addEventListener('change', update);
  document.querySelector('#reset-search').addEventListener('click', () => { search.value = ''; filter.value = 'all'; update(); search.focus(); });
  update();
})();
