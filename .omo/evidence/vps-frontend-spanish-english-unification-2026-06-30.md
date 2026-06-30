Context
- The user reported the live frontend as "antiguo y no aprobado" because
  the Spanish alias /registro still rendered Spanish copy
  ("Crea tu cuenta y empieza a escalarte") while the rest of the UI was
  in English. The /registro route was a legacy alias that pointed to
  the old register-form with hardcoded Spanish copy.

Resolution
- Added /signup as the canonical English signup page (same form, English
  copy: "Create your account and start scaling yourself").
- /registro now is a localized redirect: reads the moc_locale cookie
  set by the manual locale selector and redirects to /signup or
  /es/signup depending on the visitor's preference.
- Mounted the LanguageSelector on the public surfaces:
  - home (page.tsx) — added in the nav-links cluster
  - login (login/page.tsx) — added as an absolute-positioned corner widget
  - signup (signup/page.tsx) — added as an absolute-positioned corner widget
  - dashboard sidebar (layout.tsx) — already wired in the previous slice

Branch / commit
- deploy/maint-mode-plus-wip @ 4f60ff2

Live verification on VPS (HTTPS via nginx)
- GET  https://localhost/                  -> 200 (~235ms)
- GET  https://localhost/login             -> 200
- GET  https://localhost/signup            -> 200
- GET  https://localhost/registro          -> 307
    location: /signup            (no cookie)
    location: /es/signup         (Cookie: moc_locale=es)
- GET  https://localhost/api/me/locale     -> 200
    {"locale":"en","supported":["en","es"],"default":"en","cookie_name":"moc_locale"}
- POST https://localhost/api/me/locale {locale:"es"} -> 200
    Set-Cookie: moc_locale=es; Path=/; Secure; SameSite=lax
- LanguageSelector present in HTML for /, /login, /signup.

Rollback target
- Previous deploy/maint-mode-plus-wip commit: 269a4e5
- Last known-good release: 20260629124000-local-embeddings-dynamic