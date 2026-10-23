---
id: 2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]"]
---

## Claim
El apartado **"快速启动"** (arranque rápido) ofrece **tres vías de despliegue**, dos de ellas sin servidor propio: **"Railway: 基于Railway平台，不需要自己的服务器"** (si Railway no funciona, se puede usar **Zeabur**), y **"Docker: 在服务器或本地使用Docker启动"**. El apartado **"本地开发"** fija el stack: **"依赖java17和maven"**, la configuración vive en **`src/main/application.yml`**, se arranca el `main` de **`ProxyApplication`** y la imagen se construye con **`docker build . -t midjourney-proxy`** (para ello hay que quitar el `VOLUME` comentado en el Dockerfile). El repositorio incluye `Dockerfile`, `docker/`, `docs/` y `pom.xml`.

## Why It Matters
Es un dato de coste y de tiempo de puesta en marcha: **el proxy se puede levantar sin comprar infraestructura**, en Railway o Zeabur, con un `docker build`. Es la operación mínima para poner en pie el puente Discord→API ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]) sin comprar un servidor. Contraste directo con el suelo de infraestructura del vault, donde el plan más barato de Hetzner Cloud es **€5,99/mes sin IVA** y no cabe en el presupuesto de referencia de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): un proxy de esta clase puede costar **0 € de servidor** si se acepta un PaaS.
El stack también es una señal: **Java 17 + Maven + `application.yml`** es un stack backend convencional y mainstream, no una tecnología beta. Para el vault, que ya usa Python/Flask y Next.js ([[2026-1022-myownclone-dos-repos-flask-nextjs]]), la decisión relevante es que una integración con un proveedor sin API oficial **no exige un lenguaje exótico**: el trabajo real está en el estado, las cuentas y la resiliencia ([[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]), no en la implementación.
Detalle operativo que importa: la persistencia de tareas en Redis ([[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]) es un requisito adicional que en un PaaS puede implicar un servicio de backing aparte.

## Nota de verificación
El README **no publica precios** de Railway ni de Zeabur, ni menciona si el proyecto tiene plan gratuito o de pago en esas plataformas. El vault no puede derivar un coste mensual de hosting a partir de esta fuente.
