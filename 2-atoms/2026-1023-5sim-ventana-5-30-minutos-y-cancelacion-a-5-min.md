---
id: 2026-1023-5sim-ventana-5-30-minutos-y-cancelacion-a-5-min
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-openai-chatgpt-pricing.md]
links: ["[[2026-1023-5sim-reembolso-hasta-15-minutos]]", "[[2026-1023-5sim-openai-tasa-entrega-65-de-100]]", "[[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]"]
---

## Claim
La ventana operativa de un número virtual para OpenAI está acotada por el proveedor: "once you purchase a virtual number, you can receive unlimited SMS messages for a certain website or app within **5-30 minutes**"; "If a SMS is not delivered within **five minutes**, in some cases the order will be canceled automatically"; y "Some service/country/operator combos can provide you with only **one SMS** message". Es decir: el número vive entre 5 y 30 minutos, puede auto-cancelarse a los cinco, y algunas combinaciones país-operador solo admiten un único mensaje.

## Why It Matters
Esto convierte la "tasa de entrega" en una métrica de ventana, no de stock: el resultado de un pedido depende de que el SMS llegue **dentro de los primeros minutos**, con un 44 % de probabilidad de que no llegue ([[2026-1023-5sim-openai-tasa-entrega-65-de-100]]). Un flujo automatizado que reintenta tiene que decidir en qué momento abandona la orden, y el proveedor toma esa decisión por él a los cinco minutos — con el reembolso correspondiente ([[2026-1023-5sim-reembolso-hasta-15-minutos]]). Y el límite de "un solo SMS" en algunas combinaciones es un recordatorio de que el servicio no garantiza siquiera la posibilidad de reintentar el paso de verificación sobre el mismo número ([[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]).


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo acota la ventana operativa de 5sim (5-30 minutos, cancelación automática a los cinco) y la conecta con la tasa de entrega como métrica de ventana.

OnlineSim añade dos precisiones que el vault no tenía para ningún proveedor:
(1) la ventana **depende del país**: "you get a virtual number for a short time **from 10 minutes to 1 hour**. The exact time depends on the selected country" — y la restricción "**only from a single selected website or app**" ([[2026-1026-onlinesim-ventana-de-10-minutos-a-1-hora-segun-pais]]).
(2) la **misma página da tres ventanas incompatibles**: "10 minutes to 1 hour" (FAQ), "15-minute Number" (nombre de la tarifa) y "for 15 minutes" (bullet). Es decir, la duración efectiva de una orden es **un dato de la página que publica el proveedor**, y hay que leerla servicio a servicio — igual que la cobertura.

Y el matiz nuevo: OnlineSim **no declara ningún plazo de reembolso** ni de auto-cancelación, solo la ventana de alquiler por país ([[2026-1026-onlinesim-reembolso-al-saldo-al-cerrar-el-numero]]). En 5sim el plazo de auto-cancelación a los 5 minutos es lo que hace el reembolso automático una consecuencia de la expiración de la orden; sin plazo, no se puede acotar el coste temporal de un reintento.
