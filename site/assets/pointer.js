(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('[data-theme-toggle]');
  const iconOnlyButton = document.querySelector('[data-icon-only-toggle]');
  const navButton = document.querySelector('[data-nav-toggle]');
  const rail = document.querySelector('[data-site-rail]');
  const themeKey = 'benedikt-pointer-theme';
  const iconOnlyKey = 'benedikt-pointer-icon-only';
  const themes = ['auto', 'light', 'dark'];

  const currentTheme = () => root.dataset.theme || 'auto';

  const describeTheme = (theme) => {
    if (theme === 'light') return 'Theme: light. Activate to use dark theme.';
    if (theme === 'dark') return 'Theme: dark. Activate to follow the system theme.';
    return 'Theme: auto. Activate to use light theme.';
  };

  const applyTheme = (theme) => {
    if (theme === 'auto') delete root.dataset.theme;
    else root.dataset.theme = theme;
    if (themeButton) {
      themeButton.textContent = `Theme: ${theme}`;
      themeButton.setAttribute('aria-label', describeTheme(theme));
    }
  };

  if (themeButton) {
    applyTheme(currentTheme());
    themeButton.addEventListener('click', () => {
      const next = themes[(themes.indexOf(currentTheme()) + 1) % themes.length];
      applyTheme(next);
      try {
        if (next === 'auto') localStorage.removeItem(themeKey);
        else localStorage.setItem(themeKey, next);
      } catch (_) {}
    });
  }

  const applyIconOnly = (enabled) => {
    root.dataset.iconOnly = enabled ? 'true' : 'false';
    if (iconOnlyButton) {
      iconOnlyButton.setAttribute('aria-pressed', String(enabled));
      iconOnlyButton.setAttribute('aria-label', enabled ? 'Show navigation labels' : 'Show icons only');
      iconOnlyButton.textContent = enabled ? 'Labels' : 'Icon only';
    }
  };

  let savedIconOnly = false;
  try { savedIconOnly = localStorage.getItem(iconOnlyKey) === 'true'; } catch (_) {}
  applyIconOnly(savedIconOnly);
  if (iconOnlyButton) {
    iconOnlyButton.addEventListener('click', () => {
      const next = root.dataset.iconOnly !== 'true';
      applyIconOnly(next);
      try {
        if (next) localStorage.setItem(iconOnlyKey, 'true');
        else localStorage.removeItem(iconOnlyKey);
      } catch (_) {}
    });
  }

  if (navButton && rail) {
    navButton.addEventListener('click', () => {
      const isOpen = rail.classList.toggle('is-open');
      navButton.setAttribute('aria-expanded', String(isOpen));
    });
    rail.querySelectorAll('a[href^="#"]').forEach((link) => {
      link.addEventListener('click', () => {
        rail.classList.remove('is-open');
        navButton.setAttribute('aria-expanded', 'false');
      });
    });
  }

})();
