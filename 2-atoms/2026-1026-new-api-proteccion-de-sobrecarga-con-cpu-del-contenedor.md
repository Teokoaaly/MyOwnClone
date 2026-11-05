---
id: 2026-1026-new-api-proteccion-de-sobrecarga-con-cpu-del-contenedor
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1023-new-api-stack-go-gin-react19-y-electron]]"]
---

## Claim
**v1.0.0-rc.45** corrige la **protección contra sobrecarga** en contenedores: antes leía **el CPU y la memoria equivocados**; ahora usa **los del propio contenedor**, y **solo rechaza peticiones si los valores siguen altos durante unos 15 segundos seguidos** (PR #7317, `ax2`). La misma versión incorpora **continuidad y frescura** en la detección. En **rc.42** los **archivos de build del frontend ya no cuentan contra el rate limit de página**, así que una carga en frío **no devuelve 429** a la siguiente sesión en la misma IP.

## Why It Matters
El defecto era **tráfico de container mal leído**: en un despliegue en Docker/Kubernetes, el proceso ve **cgroup limits**, no los del host. Un sentinel de sobrecarga que lee el CPU del host ve "todo bien" mientras el contenedor está ahogándose, o al revés. Es un fallo que **solo aparece en producción** y que nadie reproduce en desarrollo.
La **ventana de 15 segundos de continuidad** es la corrección conceptual: un pico de un segundo **no debe** provocar rechazo de peticiones. Un gateway que rechaza por picos transitorios **se auto-sabotea** — el cliente ve errores y reintenta, lo que **aumenta** la carga justo cuando el sistema está saturado. Es la misma disciplina de fail-closed que aparece en el resto de la captura, pero aplicada al lado del **coste de servicio** y no al del dinero ([[2026-1026-new-api-reintento-de-tarea-reserva-el-sobrante-y-no-sale-si-no-alcanza]]).
El arreglo del **rate limit de página** es el complemento honesto: los ficheros de build del frontend son **estáticos**, no son peticiones de API, y contarlos como tráfico de usuario hacía que **un cliente que recarga la consola quemara su propio límite** antes de usar el producto. Para un gateway desplegado en contenedor ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]) esto es la diferencia entre un 429 fantasma y un servicio usable. Y el principio general —**medir el recurso correcto**— es el mismo que ya se había marcado en el modelo de variables de entorno del gateway ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]): leer el CPU del host en vez de los cgroups es el mismo error de fondo que leer una variable no inyectada.
