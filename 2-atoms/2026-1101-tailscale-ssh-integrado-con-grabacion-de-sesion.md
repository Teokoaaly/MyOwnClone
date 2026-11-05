---
id: 2026-1101-tailscale-ssh-integrado-con-grabacion-de-sesion
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
Tailscale documenta **"Use Tailscale SSH"** como parte de "Set Up Servers" y, por separado, **"SSH session recording"** dentro de "Logging, Streaming, and Events". La Presence del producto incluye por tanto acceso SSH a los nodos **sin exponer el puerto 22 a Internet** y con registro de sesión como función de logging de primera clase.

## Why It Matters
Cierra el último hueco del requisito "cero puertos públicos" del vault: si el acceso administrativo también va por el tailnet, no hace falta mantener sshd escuchando en la IP pública del VPS que hoy sirve el frontend ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]). Y la grabación de sesión da una trazabilidad que hoy no existe en el stack de observabilidad de MyOwnClone ([[2026-1022-myclone-stack-tecnologico]]), donde Langfuse y Sentry cubren la aplicación pero no el acceso al host. Límite honesto: la captura solo enumera los títulos de las páginas; no dice si la grabación requiere plan de pago, ni si Tailscale SSH sustituye o coexiste con sshd, ni qué política de auditoría aplica.
