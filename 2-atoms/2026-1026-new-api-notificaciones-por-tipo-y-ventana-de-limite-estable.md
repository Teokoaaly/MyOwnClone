---
id: 2026-1026-new-api-notificaciones-por-tipo-y-ventana-de-limite-estable
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]"]
---

## Claim
Dos arreglos de **rate limiting de notificaciones** y de **correo** en releases consecutivos:

- **rc.45**: se añade un **interruptor por tipo de notificación** (códigos de verificación, reset de contraseña, binding de email, aviso de saldo bajo); el aviso de **saldo bajo está activo por defecto**, y los tres primeros **se envían cuando SMTP está configurado**. **rc.46** corrige que la ventana del límite de notificaciones **se reiniciaba cada hora**: ahora una ventana **de más de 60 minutos dura el tiempo configurado** (PR #7877).
- **rc.46**: se incorpora **Resend como proveedor de correo**, en lugar de SMTP, con **dirección de remitente y nombre de remitente configurados por separado** (PR #7880). **rc.46** también repara el **límite de tasa después de que Redis vacía sus scripts** (issue #6412, PR #6486).

## Why It Matters
El arreglo de la **ventana horaria** es un caso de bug de producción clásico: un limitador con ventana "cada hora" en realidad es "cada N minutos desde el primer disparo", y quien lo pidió **pierde el límite real** en la práctica. El vault ya tiene documentado el caso hermano de límites contados por nodo sin Redis compartido ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]); aquí el mismo Redis aparece como **dependencia frágil** que puede dejar el límite **inoperante** después de un `FLUSH`, un detalle de operación que un self-hoster no detectaría hasta que hubiera un abuso.
La incorporación de **Resend** importa porque el correo es **infraestructura de alta y de recuperación** en todo el sector que el vault estudia: verification codes, reset de contraseña y binding de email ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]). Poder **desacoplarse de SMTP** y usar una API HTTP con remitente explícito es una mejora de fiabilidad real — y el matiz de que los tres tipos de notificación **dependen de que SMTP esté configurado** es una dependencia escondida que conviene tener en el radar.
La lección para el vault: **cada dependencia de infraestructura heredada (SMTP) es un punto único de fallo silencioso**, y la alternativa por API HTTP con remitente separado es el camino de salida.
