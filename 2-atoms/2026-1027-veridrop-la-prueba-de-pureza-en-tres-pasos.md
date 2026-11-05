---
id: 2026-1027-veridrop-la-prueba-de-pureza-en-tres-pasos
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]", "[[2026-1027-veridrop-el-campo-model-no-es-prueba-y-la-estabilidad-se-mide-por-el-cv-de-tokens]]", "[[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]"]
---

## Claim
La FAQ prescribe un **protocolo de prueba de pureza en tres pasos**: **① 验模型** — en Claude, la firma de servidor del thinking signature; en GPT, la presencia de campos foráneos `claude_*` en `usage`; **② 验 token** — *"发受控请求,看输入 token 的涨幅是否合理、流式和非流式用量是否一致"*; **③ 验 capacidad** — *"在长文本里埋 3 处信息看能否找回,再测工具调用 y salida estructurada"*. La FAQ da el protocolo: **el modo standard cubre los pasos ① y ②**, y **el contexto largo hay que marcarlo aparte**.

## Why It Matters
Es la **receta que el vault llevaba tiempo buscando** desde que PriceAI dejó la verificación de modelo en estado "即将开放" ([[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]): tres pasos, tres pruebas, y —esto es lo valioso— **la tercera tiene una construcción concreta**. **Enterrar tres datos en un texto largo y comprobar que el modelo los devuelve** es una prueba de recall que un relay con contexto truncado **no puede pasar**, y es barata: un prompt largo y una pregunta. Es la forma más barata del vault de comprobar la capacidad de contexto sin pagar una sonda de 875k tokens.
El segundo paso también es una construcción reutilizable: **comparar el crecimiento del contador de tokens entre peticiones** y **comparar el `usage` en stream frente a no-stream**. Este último es un control que el gateway de referencia del vault ya tiene que resolver porque cobra distinto por camino ([[2026-1026-new-api-uso-en-stream-y-costo-de-generaciones-completadas]]): **el relay que factura distinto en stream y en no-stream está/secando dos partidas del mismo producto**, y esa incoherencia es la misma que delata al intermediario.
Y hay una lección de alcance: **la capacidad y la identidad se prueban con herramientas distintas y no se pueden sustituir**. Un relay puede tener la firma criptográfica intacta y aun así cortar el contexto.

## Nota de verificación
Los tres pasos y el reparto de cobertura son literales de la FAQ. La captura **no** publica el diseño concreto del prompt de "tres datos enterrados" ni el umbral de crecimiento del token deemed aceptable.
