---
id: 2026-1026-bitlaunch-linux-o-windows-con-ubuntu-desktop-y-windows-rdp
type: atom
certainty: solid
sources: [sources/2026-10-25-bitlaunch-home.md]
links: ["[[2026-1024-evoxt-os-windows-rdp-y-linux]]", "[[2026-1024-flokinet-sin-windows-ni-virtualizacion-anidada]]", "[[2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso]]"]
---

## Claim
BitLaunch ofrece "a huge range of operating systems, from Linux to Windows Desktop and Server" y, si se quiere experiencia gráfica, "launch **Ubuntu Desktop** or a **Windows RDP**". El pie añade páginas de sistema operativo y variante: **Ubuntu VPS, Debian VPS, CentOS VPS, Ubuntu Desktop VPS, Windows RDP, Fedora, Rocky Linux, OpenBSD, FreeBSD** y **Linux VPS** genérico. La home **no publica coste de licencia de Windows**, ni requisitos de RAM por SO, ni si Ubuntu Desktop es una imagen con escritorio completo.

## Why It Matters
El vault ya tiene el eje del catálogo de SO como **variable que separa proveedores**, no como detalle: Evoxt lista Windows, Ubuntu, Debian, CentOS, AlmaLinux, Rocky, Fedora y SUSE sin versiones ni coste de licencia Windows ([[2026-1024-evoxt-os-windows-rdp-y-linux]]), HostBrr declara una lista extensa que su propia FAQ reduce a cinco ([[2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso]]), y FlokiNET **no ofrece Windows en VPS** — solo Linux/BSD, con Windows reservado a dedicado ([[2026-1024-flokinet-sin-windows-ni-virtualizacion-anidada]]). BitLaunch añade el extremo más amplio: **incluye Windows Desktop además de Windows Server y una imagen de escritorio Linux (Ubuntu Desktop)**, lo que abre un caso de uso que el corpus no tenía — escritorio remoto como producto — pero sin publicar lo que ese caso cuesta. Para un producto como MyOwnClone, la combinación relevante no es el escritorio sino que **Windows RDP implica coste de licencia no publicado**, que es una partida recurrente que el thread de hosting barato ya no considera marginal (egreso, backup e IPv4 sí lo eran).

## Nota de verificación
La captura **no publica** coste de licencia de Windows, RAM mínima por SO, si Windows Desktop y Windows Server son el mismo producto con distinto plan, ni el precio del addon Ubuntu Desktop. No se afirma ninguno de esos datos.

## Nota de extensión 2026-10-26 — rutas de conexión por SO
Fuente: `sources/2026-10-25-bitlaunch-bitcoin-vps.md`. La página de producto Bitcoin VPS añade la **ficha de conexión por sistema operativo**, que la home no tenía: para un VPS Linux desde Windows se usa **PuTTY** (enlazado al artículo "how to connect to SSH with PuTTY"); para un VPS Windows hace falta una **app RDP**, que en Windows es **integrada** ("built-in"), en Linux se recomienda **Remmina** y en macOS la app **Microsoft Remote Desktop** del App Store. Confirma además que el producto "Windows or Linux" del titular coincide con el catálogo de la home, y que el "Windows RDP" de la home se documenta aquí como una conexión RDP estándar, sin diferencias de producto declaradas.

Lo que esta extensión **no cambia**: el átomo original sigue intacto — no se publica coste de licencia de Windows, RAM mínima por SO, ni si Ubuntu Desktop es imagen con escritorio completo. Lo que **añade** es el detalle operativo de cliente: el corpus ya tenía el caso de uso de escritorio remoto ([[2026-1024-evoxt-os-windows-rdp-y-linux]], [[2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso]]) pero no la ruta de acceso, que es el dato que un stack automatizado necesita para decidir si el acceso es programable (RDP en Windows es local; Remmina y Microsoft Remote Desktop son clientes de escritorio, no librerías headless).
