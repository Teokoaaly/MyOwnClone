/**
 * Inline `<head>` script that runs BEFORE React hydrates. It reads the
 * stored theme from localStorage and applies the `.dark` class on
 * `<html>` so the first paint matches the chosen theme.
 */
export const themeInitScript = `
(function() {
  try {
    var t = localStorage.getItem('myownclone.theme');
    if (!t) {
      t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    if (t === 'dark') document.documentElement.classList.add('dark');
    document.documentElement.style.colorScheme = t;
  } catch (e) {}
})();
`.trim();
