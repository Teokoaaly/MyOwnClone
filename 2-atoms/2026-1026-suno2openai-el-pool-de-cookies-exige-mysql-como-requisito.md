---
id: 2026-1026-suno2openai-el-pool-de-cookies-exige-mysql-como-requisito
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]", "[[2026-1023-midjourney-proxy-edicion-plus-ampliada]]"]
---

## Claim
La persistencia de las cookies **no es una opción del pool: es un prerrequisito de instalación**. Los *Prerequisites* del README exigen **Docker y MySQL version >= 5.7**, y el despliegue pasa por cuatro variables de conexión obligatoria —`SQL_NAME`, `SQL_PASSWORD`, `SQL_IP`, `SQL_DK` (puerto, por defecto 3306)— más `BASE_URL` (por defecto `https://studio-api.suno.ai`), `SESSION_ID`, `USER_NAME`, `COOKIES_PREFIX` y `AUTH_KEY`. El modo `docker-compose` exige además **renombrar `env.example` a `.env`** y rellenar esos mismos campos, y la nota de despliegue pide abrir el **puerto 8000 en el grupo de seguridad** y usar proxy HTTPS si el front-end lo usa. La propia descripción del proyecto lo formula sin rodeos: *"save the cookie as a database to realize the cookie pool call"*.

## Why It Matters
El vault ya tiene medido el patrón de estado volátil en este tipo de puente: en `midjourney-proxy` el almacén de tareas es **`in_memory` por defecto**, con Redis como alternativa, y reiniciar el proceso pierde el trabajo ([[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]). Aquí **no existe el modo sin base de datos**: un operador sin MySQL no puede ni arrancar el pool.
Eso invierte la lectura de "la persistencia es una función premium". En el sector Discord→API la persistencia del pool es literalmente **la edición de pago** —la edición plus declara *"账号池持久化，动态维护"* como su característica ([[2026-1023-midjourney-proxy-edicion-plus-ampliada]])—, mientras que aquí **la persistencia viene de serie en el MIT de 275 estrellas**, sin nada que pagar. La consecuencia operativa es que **el coste de este gateway es el de un servidor con base de datos**, no el de un contenedor aislado: hay que decidir MySQL, sus credenciales y su ciclo de vida.
Y para el producto propio la lección es de **hosting**: un upstream que exige base de datos no se despliega en un contenedor efímero ni se factura por uso de API; exige una máquina o un plan que mantenga MySQL, lo que lo convierte en un **upstream autoalojado** y no en un canal de relay.

## [FRICTION]
> [[2026-1023-midjourney-proxy-edicion-plus-ampliada]] (escrita el 2026-10-23) afirma, generalizando sobre "este tipo de proxy", que **"la gestión del pool de cuentas es la línea de producto premium"** y que el núcleo abierto queda atrás mientras "la plus sigue".
> Este átomo presiona esa generalización con un contraejemplo publicado del mismo sector y del mismo arquetipo (proxy de plataforma sin API oficial): en `Suno2openai` la gestión de pool —**cookies persistidas en base de datos, rotadas, con endpoint de refresco y de borrado**— está **en el núcleo abierto bajo licencia MIT**, y la única función de pago que el README menciona es un **front-end** (*"Explore development of official-like frontend pages"*, hoy en "Future Plans"). Si la persistencia del pool es el premium del arquetipo, aquí el premium sería el front-end, no el pool.
> Ambas no pueden ser la misma regla de sector: o "el pool persistente es el premium" describe a `midjourney-proxy` y no al arquetipo, o describe al arquetipo y este repo es la excepción. Marcado para juicio humano, no auto-resuelto: **el vault no ha medido precios, facturación ni uso real de ninguna de las dos ediciones**, y no puede saber si el MIT de aquí está simplemente porque su autor no comercializó la capa operativa.
