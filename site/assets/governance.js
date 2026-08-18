(() => {
  const button = document.querySelector('[data-menu-button]');
  const nav = document.querySelector('[data-chapter-nav]');
  if (!button || !nav) return;
  button.addEventListener('click', () => {
    const open = nav.dataset.open === 'true';
    nav.dataset.open = String(!open);
    button.setAttribute('aria-expanded', String(!open));
  });

  const active = nav.querySelector('.chapter-link.active');
  if (active) active.scrollIntoView({ block: 'nearest' });

  const pager = document.querySelector('[data-chapter-pager]');
  if (!pager) return;
  const previous = pager.querySelector('[data-chapter-prev]');
  const next = pager.querySelector('[data-chapter-next]');
  document.addEventListener('keydown', (event) => {
    if (window.matchMedia('(max-width: 52rem)').matches) return;
    if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    const target = event.target;
    if (target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target instanceof HTMLSelectElement || target.isContentEditable) return;
    const link = event.key === 'ArrowLeft' ? previous : event.key === 'ArrowRight' ? next : null;
    if (!link) return;
    event.preventDefault();
    window.location.assign(link.href);
  });
})();
