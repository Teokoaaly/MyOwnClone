---
id: 2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md, sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]", "[[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]", "[[2026-1024-veridrop-tercer-estado-edge-y-su-dispersion]]"]
---

## Claim
El veredicto de VeriDrop **no es el score**: los umbrales de score son **≥ 85 = excelente (verde)**, **70-84 = aprobado (verde claro)**, **50-69 = marginal (amarillo)**, **< 50 = no alcanzado (rojo)**, pero **"任意 detector 报严重问题,verdict 会被砍到 marginal"** — un solo detector con problema grave baja el veredicto a *marginal* (círculo amarillo, "存在风险") **aunque el score llegue a 70**. El caso publicado es explícito: **GPT-4o con 75 puntos y veredicto `marginal`**, con la explicación de que "通常意味着接口能用但中转站在做协议转换,实际跑的可能不是真的 GPT 模型". La página OpenAI repite la regla desde el otro lado: **"只要存在 1 条严重问题…整体结论就会降到黄色「小心使用」"**, y traduce el significado: la interfaz funciona, pero **el modelo que corre puede no ser el que se cree**.

## Why It Matters
Es la **primera definición explícita de "problema grave" que el vault tiene para el sector de relays**, y cambia la semántica de una columna de score: un 75 con problemas graves **no es un 75**. El directorio de VeriDrop ya publicaba un tercer estado intermedio ("边缘") que PriceAI no tenía y que hacía incomparables dos métricas de estabilidad ([[2026-1024-veridrop-tercer-estado-edge-y-su-dispersion]]); aquí aparece la regla que lo produce: **el estado marginal no es "poco puntos", es "un eje falló"**.
Para un producto que quiere comprar capacidad, la consecuencia es operativa y dura: **el filtro correcto no es "score ≥ 70" sino "cero problemas graves"**. Es el mismo criterio que la propia FAQ da como indicador duro para elegir relay ("protocol 严重问题数量 = 0"), y es la forma correcta de traducir un veredicto de múltiples ejes a **una regla de decisión binaria** — el requisito que el vault ya Rocket al construir un agregador de precios sin SLA ([[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]).

## Nota de verificación
Umbrales, regla y ejemplo del 75 son literales de las dos fuentes. La captura **no** publica la lista de condiciones que un detector debe cumplir para ser contado como "严重问题", más allá de los ejemplos citados (residuos `claude_*` en `usage`, conversión de protocolo).
