---
id: 2026-1104-workos-annual-credits-se-describe-de-dos-formas-distintas
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1031-workos-annual-credits-frente-a-pay-as-you-go]]", "[[2026-1104-workos-precios-estables-en-cinco-capturas]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]"]
---

## Claim
La página de precios de WorkOS describe el plan **Annual Credits con dos listas distintas en la misma captura**, y ambas se contradicen entre sí. La **tarjeta superior** "## Annual Credits" (junto a "Pay as you go") lista: "Everything in **Pay as you go**, plus... / Pre-pay credit discounts / **99.99% uptime SLA** / Guided migration and onboarding / Guaranteed support SLA". El **banner inferior** "Annual credits — Need a flexible plan tailored to your business requirements?" lista: "Everything in **Pay as you go**, plus... / Pre-pay credit discounts / Guided migration and onboarding / Guaranteed support SLA / **Dedicated Slack channel**". Es decir: la tarjeta superior incluye el **SLA de uptime del 99,99%** y no el Slack; el banner inferior incluye el **Slack dedicado** y no el SLA de uptime. Y "Dedicated Slack channel" **ya figura** como característica inclusiva de "Pay as you go" en la tarjeta de arriba.

## Why It Matters
Es una **contradicción interna de la página**, no entre capturas, y toca la definición del plan enterprise del vault. La conclusión de [[2026-1031-workos-annual-credits-frente-a-pay-as-you-go]] —que Annual Credits es el plan enterprise con SLA de uptime 99,99%, prepago de créditos, onboarding guiado y SLA de soporte garantizado— sigue siendo correcta para la tarjeta superior, pero el banner inferior **presenta el mismo plan sin el SLA de uptime** y **con un extra que el propio Pay as you go ya incluye**. Es decir: en la versión de la página que el extractor del 11-04 capturó, **el SLA de uptime del 99,99% no es un atributo estable de Annual Credits**.

Operativamente importa porque el SLA de uptime es lo que justifica pagar un plan enterprise frente a "Pay as you go": si el documento comercial inferior no lo incluye, el vault no puede afirmar que Annual Credits difiere de pay-as-you-go por el uptime. Y el banner inferior es precisamente el que deriva a "Schedule a call" (`/contact-sales`), es decir, el punto donde el precio no está publicado. La lección metodológica para el vault: **cuando una página define el mismo plan en dos bloques, hay que citarlos por separado** en lugar de fundirlos en una lista única.

## [FRICTION]
> [[2026-1031-workos-annual-credits-frente-a-pay-as-you-go]] afirma, en su Claim, que Annual Credits incluye "**SLA de 99,99% de uptime**, migración y onboarding guiados y **SLA de soporte garantizado** y canal de Slack dedicado", fundiendo en un mismo listado la tarjeta superior y el banner inferior.
> Este átomo presiona esa creencia en dos puntos: (a) el banner inferior **no** menciona el SLA de uptime del 99,99%, de modo que ese atributo solo está en la tarjeta superior; y (b) el "canal de Slack dedicado" que el átomo atribuye a Annual Credits aparece en la página como inclusivo **de Pay as you go** (tarjeta superior) y como extra del banner inferior, nunca como una ventaja que la página atribuya solo a Annual Credits.
> Ambas no pueden ser completamente correctas: o la página cambió entre el 11-03 y el 11-04 (el banner inferior no aparece en el volcado del 11-03), o la página mantiene dos definiciones divergentes de Annual Credits desde al menos el 10-31. Marcado para juicio humano, no auto-resuelto. **El precio de Annual Credits sigue sin publicarse en ninguna de las dos listas**, así que esa conclusión no se ve afectada.

## Nota de verificación
sources/2026-11-04-workos-pricing.md: tarjeta "## Annual Credits" en líneas 34-48 (con "99.99% uptime SLA" en la línea 44, sin "Dedicated Slack channel") y banner "Annual credits" en líneas 445-460 (sin SLA de uptime, con "Dedicated Slack channel" en la línea 459); tarjeta "## Pay as you go" líneas 15-29 con "Dedicated Slack channel" en la línea 27. La captura del 11-03 (lines 15-45) solo contiene la tarjeta superior. La captura del 10-31 contiene ambos bloques (líneas 21-29 y 337-347).
