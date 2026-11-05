---
id: 2026-1027-moakt-recreable
type: atom
certainty: tentative
sources: [sources/2026-10-27-moakt.md]
links: ["[[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]", "[[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]"]
---

## Claim
La misma dirección de email temporal puede recrearse en cualquier momento posterior, permitiendo al usuario recuperar o reutilizar una dirección previamente utilizada.

## Why It Matters
Los usuarios no están obligados a aceptar una dirección efímera única: pueden generar nuevamente la dirección exacta cuando la necesiten, apoyando flujos de trabajo que requieren re-registro consistente.

## [FRICTION]
> [[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]] registró que Mail.tm declara "API access" y "a quick way to register disposable mailboxes in bulk", pero sin especificaciones verificables de escala. Este átomo presiona eso porque Moakt menciona que la dirección exacta puede recrearse, mientras que Mail.tm no declara explícitamente ese flujo en su home. La recreación sin API documentada depende de la interfaz web, lo que crea una incertidumbre operativa. Ambas pueden ofrecer la funcionalidad pero con grados de transparencia diferentes. Marcado para juicio humano, no auto-resuelto.