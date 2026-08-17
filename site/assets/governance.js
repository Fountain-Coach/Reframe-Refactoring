(() => {
  const button = document.querySelector('[data-menu-button]');
  const nav = document.querySelector('[data-chapter-nav]');
  if (!button || !nav) return;
  button.addEventListener('click', () => {
    const open = nav.dataset.open === 'true';
    nav.dataset.open = String(!open);
    button.setAttribute('aria-expanded', String(!open));
  });
})();
