---
id: 2026-1026-heroku-metodos-de-despliegue-git-github-docker-terraform-y-autodespliegue-en-push
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-signup.md]
links: ["[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]", "[[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]]"]
---

## Claim
El marketing de despliegue de Heroku declara literalmente: **"We've got all the popular deployment methods covered — think Git, GitHub, Docker, and Terraform. Want to automatically deploy on every git push? We've got you covered!"**. La página también enumera los **servicios de datos gestionados** de la plataforma: **"Heroku Postgres, Heroku Data for Redis, Apache Kafka on Heroku, and more"**, y el claim de DevOps es **"Heroku monitors uptime, performance, and infrastructure concerns, freeing you from the hidden costs and distraction of setting up and managing your own servers and hardware operations."** El titular de la sección de datos es **"Integrated data services"**.

## Why It Matters
Los **cuatro métodos de despliegue** (Git, GitHub, Docker, Terraform) son, uno a uno, cosas que el vault ya tiene resueltas o ha medido por su cuenta: el stack vivo es nginx + Postgres + Redis en un VPS autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), los dos repos son Flask y Next.js ([[2026-1022-myownclone-dos-repos-flask-nextjs]]) y el proxy de imagen se construye con `docker build . -t midjourney-proxy` sobre Java 17 y Maven ([[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]]). Es decir: **la diferencia entre el stack del vault y el de Heroku no es el lenguaje ni el empaquetado, es quién ejecuta el `docker build` y quién sostiene el proceso** — el auto-despliegue en cada `git push` es exactamente la pieza que en el stack propio es trabajo manual.
Y la enumeración de datos gestionados (Postgres, Redis, Kafka) es la que hace el PaaS **sustituible pieza por pieza**: cada uno de esos tres tiene una línea de coste propia en el catálogo de Heroku (Postgres desde $5/mes, Key-Value Mini desde $3/mes, Kafka desde $100/mes) y, por tanto, **cada uno es un punto donde "sin ops" se paga dos veces** — el dyno y el dato.
Hay una observación de posture en el claim de DevOps: **"freeing you from the hidden costs"**. Es marketing, pero nombra la palanca real de la venta enterprise: no es el precio, es **el coste de operar**. Para un producto como [[myownclone]], cuyo stack es nginx + Postgres + Redis en un VPS con 1 GB ([motivo del umbral en [[2026-1024-lowendbox-cuarto-escalon-de-precio-10-dolares-al-ano]]), la conversación con un cliente enterprise no es "tu servidor no aguanta" sino "tú vas a querer 24/7, backups, eixos y alertas sin tener a nadie de guardia" — y ese es exactamente el argumento de venta que Heroku escribe en su landing.
