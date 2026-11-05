---
id: 2026-1023-hetzner-apps-un-clic-gratuitas-incluidas
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
Cada servidor cloud incluye **apps de un clic gratuitas** listas en minutos, y la página lista explícitamente: **Coolify, Docker CE, GitLab CE, Grafana, Jitsi Meet, Nextcloud, Owncast, PhotoPrism, Prometheus, RustDesk, WireGuard y Wordpress**, con enlaces a la documentación de cada una. La captura los describe como "free, high-quality one-click apps" y aclara que el software popular (Docker, WordPress, Nextcloud, GitLab) se puede instalar "sin la molestia de la configuración".

## Why It Matters
Es el atajo de puesta en marcha del que habla el vault: la infraestructura viva de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] es un VPS propio con nginx delante de una app Next.js — exactamente el montaje que Coolify (self-hosted PaaS sobre Docker) automatiza. Dos consecuencias: (1) **cero coste de licencia** para un stack que ya incluye Docker, Prometheus y Grafana, que son exactamente las piezas de observabilidad que el vault tiene como coste abierto en [[2026-1022-posthog-integracion-pesada-sentry]]; (2) **cero coste de horas de configuración**, lo que importa cuando el modelo de producto es "mínima versión viable que funciona muy bien" ([[2026-1022-mvp-salir-al-mercado-pronto]]). Coolify en particular es el atajo que convierte el VPS de €5,99/mes ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) en un entorno de despliegue tipo Vercel propio, sin pasar por un hyperscaler.

## Nota de verificación
La captura no publica el número de apps disponibles en total, ni requisitos de recursos (RAM/CPU) por app, ni si Coolify o las apps de un clic se pueden instalar en un plan CPX02 de 1 vCPU.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. La lista de apps de un clic se repite **idéntica en las tres capturas** —**Coolify, Docker CE, GitLab CE, Grafana, Jitsi Meet, Nextcloud, Owncast, PhotoPrism, Prometheus, RustDesk, WireGuard y Wordpress**— con el mismo texto "free, high-quality one-click apps" y sin ninguna app nueva ni retirada en el periodo. La captura del 2026-11-01 añade además, en la sección de recursos del menú, dos entradas de blog sobre Coolify ("One-click self-hosting with coolify" y "Engineering Coolify-v2"), lo que confirma que Coolify es la apuesta de un clic del proveedor, pero **no aporta precio ni requisitos de recursos**: el dato que falta para dimensionar el stack de MyOwnClone sobre el CPX02 de € 5,99/mes ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) sigue sin estar publicado.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. La lista de apps de un clic se repite **con los mismos doce nombres y en el mismo orden**: **Coolify, Docker CE, GitLab CE, Grafana, Jitsi Meet, Nextcloud, Owncast, PhotoPrism, Prometheus, RustDesk, WireGuard y Wordpress**, con el mismo texto "every cloud server comes with free, high-quality one-click apps that are ready to go in just a few minutes" y el mismo enlace a la documentación de apps. **Ninguna app añadida ni retirada** en el periodo. Un matiz de captura menor: en el markdown de esta fecha los **enlaces individuales a la documentación de cada app no aparecen** (los nombres sí, pero sin el href a `docs.hetzner.com/cloud/apps/list/...`), a diferencia del 10-22, el 10-31 y el 11-02 — es un artefacto de renderizado del extractor, no una retirada de las apps. La ausencia que este átomo ya señalaba sigue vigente: la captura **no publica** requisitos de recursos (RAM/CPU) por app, número total de apps disponibles, ni si Coolify o Docker CE caben en un CPX02 de 1 vCPU — el dato que falta para dimensionar el stack de MyOwnClone sobre el plan de € 5,99/mes ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) continúa sin estar publicado. Ver [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]].
