---
id: 2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-api-privada-sin-documentacion]]"]
---

## Claim
La superficie DNS pública de [[myownclone]] medida el 2026-10-22 se ha reducido a **dos hosts**: `myownclone.com` y `www.myownclone.com`, ambos en `212.227.169.99` y con cuerpos HTML byte-idénticos (mismo md5). Los otros siete subdominios del mapa de mayo **no tienen registro DNS**: `app`, `api`, `admin`, `docs`, `status`, `dashboard` y `support` devuelven `NO_DNS`. `http://myownclone.com/` redirige con `301` a `https://`. Esto confirma en negativo la observación previa de que `admin.myownclone.com` no servía app propia: ahora directamente no existe.

## Why It Matters
La superficie de ataque y de marca se ha estrechado de nueve subdominios a dos. Cualquier modelo de amenazas, cualquier cálculo de coste por subdominio y cualquier decisión de marketing que asuma "app.myownclone.com" o "api.myownclone.com" como puntos de entrada reales está desactualizado. También significa que `api.` no es ni un alias ni un host: simplemente no hay API pública en subdominio.

## [FRICTION]
> [[2026-1022-dns-superficie-publica-myownclone]] (escrita hace ~21 semanas) afirma que la superficie DNS está confinada a la red 216.150.x.x con **nueve subdominios** (myownclone.com, api, app, admin, www, dashboard, support, status, docs) mapeados a un pool reducido de IPs.
> Este átomo presiona esa creencia porque en la fecha de captura solo dos de esos nueve resuelven, el resto no tiene registro DNS, y la red es 212.227.169.99 en lugar de 216.150.x.x.
> Ambas no pueden ser completamente correctas: o la infraestructura se reconstruyó entre junio y octubre de 2026, o el escaneo de junio se hizo contra un entorno distinto.
> Marcado para juicio humano, no auto-resuelto.
