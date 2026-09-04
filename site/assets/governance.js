(() => {
  fetch('/estate-route-map.json')
    .then((response) => response.json())
    .then((map) => {
      const routes = new Map((map.routes || []).map((route) => [route.id, route]));
      const isLocalPreview = ['127.0.0.1', 'localhost'].includes(window.location.hostname);
      document.querySelectorAll('[data-estate-route]').forEach((link) => {
        const route = routes.get(link.dataset.estateRoute);
        if (!route) return;
        link.href = isLocalPreview && route.previewHref ? route.previewHref : route.href;
        link.setAttribute('aria-label', route.label);
        link.title = route.label;
      });
    })
    .catch(() => {});

  const button = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-site-rail]');
  if (!button || !nav) return;

  // Keep the chapter rail complete when a checked-in publication snapshot is
  // extended by a new chapter. The route itself remains a static, typed Store
  // projection; this only repairs the shared navigation presentation.
  const finalFlow = nav.querySelector('a[href="/chapters/reframe-app-flow-governance/"]');
  const chapter126 = '/chapters/126-fountain-coach-organization-web-projection/';
  const chapter127 = '/chapters/127-estate-template-publishing-path/';
  if (finalFlow && !nav.querySelector(`a[href="${chapter126}"]`)) {
    const link = document.createElement('a');
    link.className = 'chapter-link';
    link.href = chapter126;
    link.innerHTML = '<span>126</span><span>The Fountain Coach Organization Web Projection</span>';
    nav.insertBefore(link, finalFlow);
  }
  const chapter126Link = nav.querySelector(`a[href="${chapter126}"]`);
  if (finalFlow && chapter126Link && !nav.querySelector(`a[href="${chapter127}"]`)) {
    const link = document.createElement('a');
    link.className = 'chapter-link';
    link.href = chapter127;
    link.innerHTML = '<span>127</span><span>The Estate Template Is the Publishing Path</span>';
    finalFlow.parentNode.insertBefore(link, finalFlow);
  }

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
