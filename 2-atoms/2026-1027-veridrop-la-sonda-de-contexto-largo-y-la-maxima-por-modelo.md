---
id: 2026-1027-veridrop-la-sonda-de-contexto-largo-y-la-maxima-por-modelo
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]]", "[[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]]", "[[2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra]]"]
---

## Claim
VeriDrop ofrece **dos niveles de sonda de contexto largo**, ambos pagados por la key del usuario. El nivel de **profundidad** lanza **"额外发 32k → 100k → 200k tokens 探针"** para comprobar si el relay **兑现 la context window anunciada** (*"识别截断 / 路由到小窗口模型"*), y **"失败立即停"**. El nivel **extremo** va **"按模型上限等比探测(如 1M 模型测 32k → 500k → 950k)"** y su objetivo declarado es **"catch「宣传 1M 实际只给 200k」这类高端中转站欺诈,标准档完全测不到"**. Para **GPT-6 Astra** los números concretos publicados son: **máximo de entrada 922k**, con **sonda 32k → 461k → 875.9k**. La FAQ confirma que el contexto largo es un ítem aparte y **de pago** (*"1 项用户主动付费启用的长上下文检测"*), y que la **detección regular no lo activa por defecto**.

## Why It Matters
Es la **dimensión de capacidad** del fraude de relays, y es la que el vault no tenía: hasta ahora sus átomos cubren **modelo** (¿es el que dice?) y **tokens** (¿cuenta bien?), pero no **ventana de contexto**. Y la ventana de contexto es donde el fraude es más rentable y más invisible: **un relay puede servir un modelo de 200k y anunciarlo como de 1M**, y ninguna petición de chat cotidiana lo detecta porque nadie escribe 900k tokens en un día normal. El detector lo llama explícitamente **fraude de gama alta** —el tipo que solo aparece en relays caros, que son los que el vault querría usar.
El mecanismo de la sonda es lo que hace la idea reutilizable: **no es un test de longitud sino una escalera de longitudes creciente con parada al primer fallo** (32k → 100k → 200k, o 32k → 500k → 950k proporcional al techo). El primer umbral que pasa es la cota real. Es el mismo tipo de prueba que el vault ya aplica en su propio stack —descubrir el límite real de un proveedor por Incremento en lugar de por Documentation— y por eso es portable al producto: **un campo `max_tokens` declarado que nadie ha sondeado no es una capacidad, es una afirmación**.
Y hay un punto de diseño que encaja con el vault: **la sonda se factura aparte y no entra en el total**, como el ítem de pago desligado de la tabla de pesos de [[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]] y con su precio medido en [[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]]. Es exactamente la separación que el vault recomienda para las magnitudes heterogéneas.

## Nota de verificación
Cifras literales de la página OpenAI. La captura **no** publica el criterio de "fallo" de una sonda (si es error de la API, truncamiento medido o reintento), ni el número de tokens de salida usados para forzar la longitud, ni los umbrales deContexto de los otros ocho modelos de la lista.
