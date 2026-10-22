---
id: 2026-1022-cookie-next-locale-sin-httponly-ni-secure
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-sin-headers-de-seguridad]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]"]
---
## Claim
La cookie `NEXT_LOCALE` de [[myownclone]] se emite sin los flags `HttpOnly` ni `Secure`.

## Why It Matters
Una cookie de locale accesible desde JavaScript es una vía trivial para exfiltración vía XSS: sin `HttpOnly` puede leerse desde cualquier script inyectado, y sin `Secure` puede transmitirse en claro sobre conexiones no HTTPS. Es el único hallazgo de cookie del informe y encaja con el patrón de ausencia de hardening de [[2026-1022-sin-headers-de-seguridad]] y [[2026-1022-ausencia-csp-xss-sin-mitigacion]]: no hay mitigación en la capa de transporte, ni de contenido, ni de cookie. Su contenido es el locale ES/EN que el producto usa para el i18n routing descrito en [[2026-1022-i18n-es-first-jurisdiccion-es]], así que el impacto directo sobre datos es bajo, pero el indicador de disciplina de seguridad es lo que importa.
