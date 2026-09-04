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

  const button = document.querySelector('[data-nav-toggle], [data-menu-button]');
  const nav = document.querySelector('[data-site-rail], [data-chapter-nav]');
  if (!nav) return;
  const canonical = document.querySelector('link[rel="canonical"]');
  const pagePath = canonical ? new URL(canonical.href).pathname : window.location.pathname;

  // Keep the chapter rail complete when a checked-in publication snapshot is
  // extended by a new chapter. The route itself remains a static, typed Store
  // projection; this only repairs the shared navigation presentation.
  const finalFlow = nav.querySelector('a[href="/chapters/reframe-app-flow-governance/"]');
  const chapters = [
    ['126', '/chapters/126-fountain-coach-organization-web-projection/', 'The Fountain Coach Organization Web Projection'],
    ['127', '/chapters/127-estate-template-publishing-path/', 'The Estate Template Is the Publishing Path'],
    ['128', '/chapters/128-deployed-estate-webkit-mirror-authority/', 'The Deployed Estate Is a Read-Only WebKit Mirror Authority']
  ];
  for (const [number, href, title] of chapters) {
    if (nav.querySelector(`a[href="${href}"]`)) continue;
    const link = document.createElement('a');
    link.className = 'chapter-link';
    link.href = href;
    link.innerHTML = `<span>${number}</span><span>${title}</span>`;
    if (finalFlow) nav.insertBefore(link, finalFlow); else nav.appendChild(link);
  }

  if (button) {
    button.addEventListener('click', () => {
      const open = nav.dataset.open === 'true';
      nav.dataset.open = String(!open);
      button.setAttribute('aria-expanded', String(!open));
    });
  }

  const index = document.querySelector('.index-grid');
  if (index) {
    for (const [number, href, title] of chapters.slice(1)) {
      if (index.querySelector(`a[href="${href}"]`)) continue;
      const link = document.createElement('a');
      link.href = href;
      link.innerHTML = `<span>${number}</span><span>${title}</span>`;
      index.appendChild(link);
    }
  }

  const current = nav.querySelector(`a[href="${pagePath}"]`);
  if (current) {
    nav.querySelectorAll('.chapter-link.active').forEach((link) => link.classList.remove('active'));
    nav.querySelectorAll('[aria-current="page"]').forEach((link) => link.removeAttribute('aria-current'));
    current.classList.add('active');
    current.setAttribute('aria-current', 'page');
  }
  const active = nav.querySelector('.chapter-link.active');
  if (active) active.scrollIntoView({ block: 'nearest' });

  const pager = document.querySelector('[data-chapter-pager]');
  if (!pager) return;
  if (pagePath === chapters[0][1] && !pager.querySelector('[rel="next"]')) {
    const link = document.createElement('a');
    link.className = 'chapter-pager-link chapter-pager-next';
    link.dataset.chapterNext = '';
    link.rel = 'next';
    link.href = chapters[1][1];
    link.setAttribute('aria-label', `Next chapter: ${chapters[1][2]}`);
    link.innerHTML = `<span><small>NEXT CHAPTER</small>${chapters[1][2]}</span><span aria-hidden="true">→</span>`;
    pager.appendChild(link);
  }
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
