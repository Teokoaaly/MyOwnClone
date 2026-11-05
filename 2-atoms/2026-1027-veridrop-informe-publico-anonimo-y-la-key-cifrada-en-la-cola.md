---
id: 2026-1027-veridrop-informe-publico-anonimo-y-la-key-cifrada-en-la-cola
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-tres-flujos-de-ingreso-y-el-aislamiento-de-la-comision]]", "[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1027-veridrop-la-prueba-de-pureza-en-tres-pasos]]"]
---

## Claim
La FAQ describe el tratamiento de la API key en detalle verificable: **la key no se escribe en claro ni en el informe ni en los logs**; en la **detección asíncrona de producción**, el valor **"经过认证加密的密文"** se guarda **temporalmente en la cola de tareas**, **"worker 执行时只在内存解密"**, y **"任务成功或失败后清空"**; en la **sonda continua activada por el webmaster**, **"专用 key 会以密文保存到撤销为止"**. En el informe solo queda la forma **desenmascarada** (**"sk-y7xU••••••0h"**). El **informe es público y anónimo**: la URL `/r/{job_id}` es **permanente y compartible** (*"任何人拿到链接都能看(匿名、不加密)"*), el informe **no contiene nombre, email ni IP**, y el borrado se pide por **GitHub issue**. Existe además una promesa de **"后续会加 opt-in 的「私有报告」开关"** (aún no implementado).

## Why It Matters
Es el **modelo de confianza por custodia** del competidor, inseparable del modelo de ingresos de [[2026-1027-veridrop-tres-flujos-de-ingreso-y-el-aislamiento-de-la-comision]], y su publicación de la cadena de custodia es el activo más valioso del material: **el usuario entrega una credencial a un tercero y no tiene que creerse la promesa, porque puede leer el diseño**. Las tres propiedades —cifrado autenticado en reposo, descifrado solo en memoria, borrado al terminar— son **exactamente las que el gateway de referencia del vault ya aplica a sus propios secretos** ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]), lo que confirma que **es un estándar de facto y no una excentricidad**.
Pero hay un precio explícito a ese diseño que el vault debe registrar: **el informe es público por defecto**. Es decir, **la evidencia de la calidad de un relay es pública, pero el canal para probarla (la key) es privado**. Y hay una consecuencia operativa inmediata: **no se debe compartir la URL del informe de un relay privado**, porque la URL contiene la base URL enmascarada, la key enmascarada y los resultados — un **inventario de por dónde compra el cliente, visible para cualquiera que tenga el enlace**. El sitio lo dice ("如果你测的是私有中转站不想公开,不要 compartir URL"), pero el diseño por defecto es el contrario.
Y para el producto del vault hay una idea transferible: **el informe público es un activo de reputación del relay**. Un relay cuya detección está publicada es un relay auditable por cualquiera; uno sin informe es una caja negra declarada.

## Nota de verificación
Todas las afirmaciones son literales de la FAQ. La captura **no** publica el algoritmo de cifrado, si el borrado tras fallo está verificado en código, ni la fecha estimada del interruptor de informe privado.
