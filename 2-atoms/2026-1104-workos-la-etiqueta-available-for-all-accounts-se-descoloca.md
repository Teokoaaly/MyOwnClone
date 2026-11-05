---
id: 2026-1104-workos-la-etiqueta-available-for-all-accounts-se-descoloca
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1103-workos-inventario-de-funciones-de-authkit]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]", "[[2026-1104-workos-precios-estables-en-cinco-capturas]]"]
---

## Claim
La captura del **2026-11-04** de workos.com/pricing coloca la etiqueta **"Available for all accounts"** en la línea **505**, dentro del tramo del banner enterprise (justo después del "Powered by WorkOS" y del logo de Clay) y **antes** del encabezado "## Batteries included" — es decir, **descolada de la lista de funciones**. En la captura del **11-03** la misma etiqueta estaba **adherida a la función "Social Auth"** ("### Social Auth / Authentication with Microsoft, Google, and more / Available for all accounts"), y la captura cruda del **10-31** **no la traía en ninguna parte**. En el 11-04 ninguna de las diez funciones de AuthKit (Social Auth, Email + Password, Magic Auth, MFA, Email verification, Organization auth policies, JIT provisioning, Passkeys, RBAC, CLI Authentication) lleva marca de disponibilidad.

## Why It Matters
Es un **delta de render puro** que importa porque el vault ya usó la posición de la etiqueta como evidencia de que Social Auth es una capacidad transversal, no una función premium: [[2026-1103-workos-inventario-de-funciones-de-authkit]] anota en su verificación que "el único ítem con marca explícita de disponibilidad es 'Social Auth — Available for all accounts'". Con el 11-04, esa afirmación literal deja de ser sostenible: la etiqueta existe en la página, pero **su anclaje al ítem se ha perdido en el render**, y en la captura del 10-31 no aparecía en absoluto. La conclusión de fondo (que el inventario de AuthKit **no tiene línea de precio propia** y que la única que lo monetiza es el MAU, en [[2026-1104-workos-precios-estables-en-cinco-capturas]]) **no cambia**.

Operativamente, la lección es de higiene de fuente: el vault no debe colgar una afirmación sobre la granularidad de un badge comercial de una posición que el extractor mueve entre capturas. La afirmación segura es la más débil: **"la página incluye en algún punto la etiqueta 'Available for all accounts'"**, sin atribuirle una función concreta.

## [FRICTION]
> [[2026-1103-workos-inventario-de-funciones-de-authkit]] afirma, en su nota de verificación, que "el único ítem con marca explícita de disponibilidad es 'Social Auth — Available for all accounts'; los restantes se listan sin indicación de plan ni de precio".
> Este átomo presiona esa creencia en un punto concreto: en la captura del **2026-11-04** la etiqueta **ya no está adherida a Social Auth** sino flotando en la línea 505, antes de "Batteries included", y ninguna función aparece marcada; en la del **10-31** la etiqueta no aparece en absoluto.
> Ambas no pueden ser simultáneamente correctas: o la etiqueta pertenece estructuralmente a Social Auth (y el extractor del 11-04 la descoló al reordenar el DOM), o pertenece a la sección "Batteries included" en su conjunto (y entonces el 11-03 la asoció por error al ítem contiguo). Marcado para juicio humano, no auto-resuelto. **Ninguna de las dos lecturas altera precios ni la lista de funciones**, que es lo que el átomo sostiene.

## Nota de verificación
sources/2026-11-04-workos-pricing.md: "Powered by WorkOS" (501), imagen clay-logo-dark (503), "Available for all accounts" (505), "## Batteries included" (507), y "### Social Auth / Authentication with Microsoft, Google, and more" (511-513) sin etiqueta. sources/2026-11-03-workos-pricing.md, líneas 197-201: "### Social Auth / Authentication with Microsoft, Google, and more / Available for all accounts". sources/2026-10-31-workos-pricing.md, líneas 376-392: "Powered by WorkOS / Batteries included / Google Microsoft signing / ### Social Auth / Authentication with Microsoft, Google, and more" — sin la etiqueta.
