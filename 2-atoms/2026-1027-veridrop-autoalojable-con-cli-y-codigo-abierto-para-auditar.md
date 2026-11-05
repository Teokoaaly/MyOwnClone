---
id: 2026-1027-veridrop-autoalojable-con-cli-y-codigo-abierto-para-auditar
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-informe-publico-anonimo-y-la-key-cifrada-en-la-cola]]", "[[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]", "[[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]]"]
---

## Claim
La FAQ da las **instrucciones de autoalojamiento** del detector: **"Veridrop 完全开源。clone 仓库 → pip install -e .\[web\] → uvicorn web.server:app 即可"**, y un **CLI independiente**: **`relay-detector detect --base-url ... --api-key ... --mode full`**. El repositorio es **`github.com/canarybyte/veridrop`** y la licencia es **AGPL-3.0**, con la **"评分公式公开,可逐行审计"** como argumento explícito frente a un competidor de código cerrado (**"cctest.ai 也声称不上传 key,但代码闭源无法验证"**). La FAQ también documenta el **flujo mínimo de uso**: abrir la página del protocolo, meter `base_url` + `api_key` (el desplegable **lista automáticamente los modelos que esa key puede usar en ese relay**), y obtener el informe en **30-60 segundos**, con **URL permanente compartible (`/r/{job_id}`) y descarga en JPG**.

## Why It Matters
Es la **vía más directa para que el vault tenga su propio verificador de proveedores**, y encaja con la política de infraestructura barata que el vault viene aplicando: autoalojar un detector **AGPL en un VPS de ≤ €4/mes** es una operación de una tarde, y **elimina la dependencia de un tercero que cobra en tokens del usuario**. El argumento es el mismo que el del gateway de referencia del vault, que ya eligió AGPLv3 con atribución en la interfaz ([[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]): **la licencia copyleft delata a un competitor que quiere decir "nuestro código es auditable"**, y en este caso es la prueba que el vault necesitaba para diferenciar dos herramientas que ambas prometen no subir la key.
El dato operativo más útil es el **desplegable que lista los modelos disponibles para esa key en ese relay**, porque resuelve de un plumazo la pregunta que el vault tenía abierta como pendiente en PriceAI —**"模型检测 即将开放"** ([[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]])— y además la que se ha convertido en el malentendido más caro del sector: **0 modelos GPT significa permiso de key, no relay caído**.
Y hay una consecuencia sobre el formato del producto: **el informe es un artefacto descargable en JPG con URL permanente**. Eso significa que **el resultado de una detección es un objeto publicable y citable**, y por tanto que un proveedor de relays podría **publicar su propia detección** como prueba de legitimidad — el mismo movimiento que hizo el módulo 卡网 del sector con sus índices de reputación.

## Nota de verificación
Los comandos, la licencia, la URL del repositorio y los tiempos son literales de la FAQ. La captura **no** publica los requisitos de runtime (versión de Python, dependencias), ni si el CLI puede ejecutarse sin la parte web, ni la licencia exacta de cada dependencia.
