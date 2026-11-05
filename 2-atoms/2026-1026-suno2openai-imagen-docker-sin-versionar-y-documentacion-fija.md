---
id: 2026-1026-suno2openai-imagen-docker-sin-versionar-y-documentacion-fija
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1023-new-api-escala-adopcion-y-traduccion]]", "[[2026-1026-github-search-suno-ventanas-de-desarrollo-largas-y-no-volcadas]]"]
---

## Claim
El canal de distribución documentado es **una imagen de Docker Hub, `wlhtea/suno2openai:latest`**, sin versión: el `docker run` de ejemplo publica **`-p 8000:8000` y `-p 8501:8501`** con `--restart=always`, mientras que el acceso documentado es **solo por `http://localhost:8000`** —el puerto 8501 se mapea pero **no se explica en ninguna parte del README**. La sección de despliegue por `docker-compose` lleva su propia marca temporal: **"Update Time: 2024/4/7 18:18"**, es decir **más de dos meses antes del último commit del repositorio (19 de enero de 2025)** y tres años antes de la captura.

## Why It Matters
Dos datos operativos que el vault no tenía para esta categoría. El primero: **el puerto 8501 abierto y sin documentar** es exactamente el tipo de superficie que el vault ya sabe medir —en `new-api` el README advierte que `latest` sigue las builds publicadas y puede cambiar, y que hay que **fijar versión desde Releases, leer las notas de upgrade y hacer backup antes de actualizar** ([[2026-1023-new-api-escala-adopcion-y-traduccion]]). Aquí **no hay Releases de las que fijar** y el `docker run` documentado **arrastra `latest`**, así que un operador que copie el README obtiene una versión que no puede fijar, de un proyecto con 464 commits y último cambio hace 21 meses respecto a la captura.
El segundo dato es más fino y es de **deriva documental**: la guía de despliegue por `docker-compose` lleva fecha propia de abril de 2024, **anterior al último commit** —igual que el vault ya vio en `midjourney-proxy`, donde el README se actualizó en agosto de 2025 y el código quedó congelado en junio de 2024 ([[2026-1026-github-search-suno-ventanas-de-desarrollo-largas-y-no-volcadas]]). La diferencia es que aquí el README es **más viejo que el código**, no al revés: es decir, **quien lea la guía puede estar ejecutando un procedimiento que el autor ya cambió**. La regla operativa que esto sugiere para el vault es que **un README auto-declarado con fecha es un dato en sí mismo, y hay que contrastarlo con `pushed_at` antes de tratarlo como procedimiento vigente**.
