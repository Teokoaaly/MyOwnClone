---
id: 2026-1026-heroku-changelog-de-runtimes-ruby-3-4-12-opjdk-y-dotnet
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-soporte-catorce-categorias-con-identificadores-numericos]]", "[[2026-1026-heroku-metodos-de-despliegue-git-github-docker-terraform-y-autodespliegue-en-push]]", "[[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]"]
---

## Claim
La sección **"Changelog"** de la home de soporte de Heroku publica **cuatro entradas, todas sobre versiones de runtime**, con las cifras literales en el propio titular: **".NET 8.0.133, 8.0.427, 9.0.123, 9.0.320, 10.0.114 and 10.0.403 SDKs are now available"** (seis SDK de .NET, tres versiones de 8.x, dos de 9.x y dos de 10.x); **"Default Ruby version for new apps is now 3.4.12"**; **"OpenJDK 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.33 and 1.8.0_512 now available"** (seis JDK, desde **27.0.1** hasta **1.8.0_512**, pasando por 25, 21, 17 y 11); y **"Ruby version 3.4.12 is now available"** — es decir, Ruby 3.4.12 aparece **dos veces**, una como disponible y otra como **default de las apps nuevas**.

## Why It Matters
Es la única evidencia del vault sobre **la cadencia de versiones de runtime de Heroku**, y su forma es reveladora: el changelog no anuncia características, **anuncia números de versión disponibles**, y lo hace con el **default de apps nuevas como métrica separada** ("Default Ruby version for new apps is now 3.4.12"). Eso significa que Heroku publica el **runtime por defecto de una app creada hoy**, no solo el catálogo: es un dato directamente comparable con el stack vivo del producto propio, que corre sobre nginx + Postgres + Redis autoalojados ([[2026-1026-heroku-metodos-de-despliegue-git-github-docker-terraform-y-autodespliegue-en-push]]).
Y el paralelismo estructural con las generaciones de cómputo es exacto: del mismo modo que las familias Private/Shield de Cedar **no valen** para los espacios Fir ([[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]), una app creada con el runtime por defecto de una generación dada **no es portable a la siguiente sin migración**, y quien decide cuándo se cierra la ventana es el proveedor.
El salto de OpenJDK de **1.8.0_512 a 27.0.1** en la misma línea es también una medida del **deuda de compatibilidad heredada**: la plataforma mantiene seis generaciones de JDK simultáneas —de 1.8 a 27— para los despliegues de larga vida, un commitment de mantenimiento que **ningún proveedor de VPS del vault declara** y que es un coste oculto del PaaS.
Y el changelog aparece **dentro del portal de soporte**, no del devcenter: para Heroku, "qué versiones hay disponibles" es materia de soporte, con su propio ritmo de publicación y su propio identificador (`devcenter.heroku.com/changelog-items/3851` a `/3854`).

Nota: la captura **solo** reproduce los titulares; no publica fechas de publicación de cada entrada, ni fecha de fin de soporte de ninguna versión, ni el contenido de los artículos.
