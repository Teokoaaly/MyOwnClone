---
id: 2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]]", "[[2026-1027-veridrop-el-campo-model-no-es-prueba-y-la-estabilidad-se-mide-por-el-cv-de-tokens]]", "[[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]"]
---

## Claim
La FAQ da **cinco indicadores duros** para elegir relay, y son todos verificables con la propia key: **① thinking signature ≥ 100**; **② número de problemas graves de protocolo = 0**; **③ coherencia del `usage` entre stream y non-stream**; **④ el campo id de modelo coincide con el modelo solicitado** (**"model_consistency pass"**); **⑤ el CV de `completion_tokens` en varias peticiones < 0.10** (estabilidad). Y da el criterio de cribado recomendado: buscar en la 红黑榜 los relays **con muchas detecciones, mediana alta y sin problemas graves**, luego comparar el multiplicador, y **por último correr una detección propia con la key** (*"只看价格,或者只看一次高分,都不可可靠"*).

## Why It Matters
Es el **criterio de compra ejecutable** del sector, y es notable que **ninguno de los cinco criterios sea un precio**: uno es criptográfico, dos son de integridad de protocolo, uno de estabilidad estadística y uno de coherencia de identidad. Es decir, **el sitio competidor está diciendo que el precio es la última variable, no la primera**, y que el filtro correcto es un **AND de cinco condiciones**, no un score.
Los dos criterios que el vault no tenía son el ① y el ⑤: **"la firma criptográfica llega a 100"** es un umbral binario y concluyente (no un score), y **el CV < 0,10** es una **cifra de tolerancia**, no una dirección. Juntas, definen una **spec de calidad mínima** —que se solapa con la regla de veto de [[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]]— que el vault podría escribir como contrato de aceptación para sus proveedores de `OPENAI_API_BASE`: *cero problemas graves, coherencia stream/no-stream, identidad de modelo, y varianza de contador por debajo del 10 %*.
Y el orden del cribado —**detección → precio → verificación propia**— invierte el orden natural del comprador (precio primero) y es el mismo patrón de "comprueba el precio solo después de saber que lo que compras es real" que el vault ya tenía para el módulo 卡网 ([[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]). La frase final del vault sobre el que **"no publishes ni el número de detecciones ni el denominador"** se ve aquí respondida: el criterio de la FAQ es explícitamente **"检测次数多、中位分高、没有严重问题"**, es decir, **el número de detecciones vuelve a ser la primera condición**.

## Nota de verificación
Los cinco indicadores y el orden del cribado son literales de la FAQ. La captura **no** publica el número mínimo de detecciones que la FAQ considera suficiente ("检测次数多" no está cuantificado).
