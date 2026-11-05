---
id: 2026-1026-github-search-ningun-repo-publico-indexa-la-verificacion-de-edad-en-el-alta
type: atom
certainty: tentative
sources: [sources/2026-10-25-github-search-chatgpt-age-verification.md]
links: ["[[2026-1026-github-search-cero-resultados-para-la-consulta-de-edad-y-cumpleanos]]", "[[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]", "[[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]"]
---

## Claim
La consulta del 2026-10-25 se formuló para probar si existe tooling público que resuelva **la verificación de edad en el alta de cuentas de ChatGPT**, y la respuesta es `total_count: 0`. En consecuencia, **el vault no tiene ninguna fuente pública sobre el control de edad** en el alta de cuentas de IA: el único punto del vault donde la edad legal aparece documentada es el **L1 de NoOnes** —"We ask for your date of birth to confirm your legal age", un peldaño de KYC de un exchange cripto que habilita operar y tener saldo ([[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]])—, es decir, en un dominio que **no es el del registro de cuentas de IA**. Y el flujo de alta que el vault sí tiene medido, los nueve pasos HTTP del bot `chatgpt-creator` (CSRF → signup → OTP → callback), **no contiene ningún paso de edad, de fecha de nacimiento ni de comprobación de edad** ([[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]).

## Why It Matters
El thread documenta las cuatro patas del alta —correo, captcha, proxy, SMS/KYC— y hasta ahora no tenía una quinta porque nadie la buscó: la **verificación de edad**. La captura del 2026-10-25 es la primera que la interroga y devuelve cero, lo que deja el vault en una posición incómoda y precisa: **el control de edad no es una partida documentada de la economía del alta**. Tres lecturas posibles, y la fuente **no permite elegir entre ellas**:
1. El alta por la vía que el vault midió (email + OTP, sin teléfono) **no pide fecha de nacimiento**, porque la verificación de edad ocurre en un momento distinto —posterior, en la primera sesión o en la compra de suscripción— y ese paso no está en el flujo de nueve pasos;
2. Existe, pero **no es pública**: vive en el circuito cerrado que el thread ya describe (canales chinos, gateways autoalojados, marketplaces), igual que la capacidad de producción de cuentas vive fuera del repositorio público ([[2026-1026-github-search-cero-resultados-para-la-consulta-de-edad-y-cumpleanos]]);
3. El control de edad **no existe como fricción operativa** en la vía medida, y por eso nadie escribe código público para él.
El dato que conecta las tres con lo que el vault ya sabe es que **el KYC humano revendido cuesta ¥10.28 con una unidad en stock** —tres órdenes de magnitud por encima del código de SMS ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]])—: si la edad tuviera un coste de verificación real en el alta, el mercado chino lo publicaría como fila. El vault **no lo ha buscado**, y esa búsqueda es una captura pendiente, no un hueco que se pueda rellenar con inferencia.

## Nota de verificación
La fuente de este átomo es el JSON de 9 líneas con `total_count: 0`; todo lo que se afirma sobre la ausencia es **una lectura de ese cero acotada a la conjunción de seis términos**. La afirmación sobre el flujo de nueve pasos y la de NoOnes **no proceden de esta captura**: proceden de átomos existentes con sus propias fuentes ([[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]], [[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]) y se usan aquí como contexto, no como dato de esta fuente. El vault **no ha buscado** en PriceAI, en lzt.market ni en GitHub la fila de KYC/edad; la mención a ¥10.28 es un dato ya atomizado ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]) citado como pista de búsqueda pendiente, no como medición de esta captura.
