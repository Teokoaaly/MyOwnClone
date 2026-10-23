---
id: 2026-1023-hetzner-apps-un-clic-gratuitas-incluidas
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
Cada servidor cloud incluye **apps de un clic gratuitas** listas en minutos, y la página lista explícitamente: **Coolify, Docker CE, GitLab CE, Grafana, Jitsi Meet, Nextcloud, Owncast, PhotoPrism, Prometheus, RustDesk, WireGuard y Wordpress**, con enlaces a la documentación de cada una. La captura los describe como "free, high-quality one-click apps" y aclara que el software popular (Docker, WordPress, Nextcloud, GitLab) se puede instalar "sin la molestia de la configuración".

## Why It Matters
Es el atajo de puesta en marcha del que habla el vault: la infraestructura viva de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] es un VPS propio con nginx delante de una app Next.js — exactamente el montaje que Coolify (self-hosted PaaS sobre Docker) automatiza. Dos consecuencias: (1) **cero coste de licencia** para un stack que ya incluye Docker, Prometheus y Grafana, que son exactamente las piezas de observabilidad que el vault tiene como coste abierto en [[2026-1022-posthog-integracion-pesada-sentry]]; (2) **cero coste de horas de configuración**, lo que importa cuando el modelo de producto es "mínima versión viable que funciona muy bien" ([[2026-1022-mvp-salir-al-mercado-pronto]]). Coolify en particular es el atajo que convierte el VPS de €5,99/mes ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) en un entorno de despliegue tipo Vercel propio, sin pasar por un hyperscaler.

## Nota de verificación
La captura no publica el número de apps disponibles en total, ni requisitos de recursos (RAM/CPU) por app, ni si Coolify o las apps de un clic se pueden instalar en un plan CPX02 de 1 vCPU.
