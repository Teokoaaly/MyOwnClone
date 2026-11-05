---
id: 2026-1026-new-api-limitador-se-recupera-tras-flush-de-redis
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]"]
---

## Claim
**v1.0.0-rc.46** corrige que **el rate limiting dejara de funcionar después de que Redis vaciara sus scripts** (PR #6486, `BradleyZhang`, issue #6412). La corrección **recupera el script de Redis tras el flush**. En la misma versión, un **embedding enviado a Gemini con una imagen o un vídeo se rechaza y no se cobra**, y en **rc.44** los **429 de rate limit de modelo llevan el mismo mensaje de error y la misma línea de log con y sin Redis** (PR #7721).

## Why It Matters
Este es un fallo **de dependencia oculta**: el limitador de Redis guarda **scripts compilados en el propio servidor Redis** para hacer el conteo atómicamente. Si Redis se vacía —un reinicio con datos efímeros, un flush manual, un failover— **los scripts desaparecen y el limitador deja de limitar sin avisar**. El síntoma es el peor posible: **el sistema parece sano y no protege nada**. Un gateway de reventa en ese estado permite que un solo cliente consuma todos los canales.
La lección es estructural y el vault la necesita: **cualquier estado crítico que viva en Redis debe poder regenerarse**, y el gateway debe **distinguir "sin límite" de "límite aplicado"**. Es el mismo eje que el átomo de **secretos compartidos entre nodos** y `TRUSTED_PROXIES` ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]): en una topología multi-nodo con Redis, **Redis no es una caché, es parte del plano de control** ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]).
El segundo detalle —**el mismo mensaje de error con y sin Redis** — importa más de lo que parece: si el mensaje de 429 **cambia** según la topología, entonces **el mensaje de error se convierte en un indicador de topología**, y los clientes de código que deciden reintentar pueden comportarse de forma distinta según el despliegue. Unificar los mensajes es **neutralizar la fuga de topología**.
Y el rechazo sin cobro de embeddings con imagen o vídeo hacia Gemini es una regla de **fail-safe de facturación**: lo que se rechaza no se cobra ([[2026-1026-new-api-uso-en-stream-y-costo-de-generaciones-completadas]]).
