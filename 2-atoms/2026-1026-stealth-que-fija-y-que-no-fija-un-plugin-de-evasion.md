---
id: 2026-1026-stealth-que-fija-y-que-no-fija-un-plugin-de-evasion
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]", "[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1026-stealth-modularidad-por-carga-selectiva-y-require-directo-de-una-evasion]]"]
---

## Claim
La sección "Purpose" delimita el alcance del plugin en dos frases: "There are a couple of ways the use of puppeteer can easily be detected by a target website. **The addition of `HeadlessChrome` to the user-agent being only the most obvious one**." Y el objetivo declarado: "The goal of this plugin is to be the definite companion to puppeteer to avoid detection, **applying new techniques as they surface**". La sección "Modularity" añade la razón de la flexibilidad: "As this cat & mouse game is in it's infancy and fast-paced the plugin is kept as flexibile as possible, to support **quick testing and iterations**".

## Why It Matters
Es la **declaración de alcance más honesta del sector**, y es la que permite contrastar capas: el plugin se ocupa de lo que el navegador **revela desde dentro de la página** —el `User-Agent` con `HeadlessChrome` es, según el propio autor, "only the most obvious one"— y nada más.
El vault ya registró que la capa de huella **del cliente HTTP** —huella TLS con perfiles Chrome aleatorizados— es una señal de primer orden que hay que construir a mano ([[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]). Esta captura **no lo contradice, lo delimita**: el plugin de evasión de navegador **no toca el transporte**, solo el contenido de la página. La línea "the most obvious one" es exactamente la respuesta al hecho de que la detección tiene muchas capas y esta cubre las internas.
Y hay un dato de governance que importa para un vault que consume estas herramientas: **el criterio de diseño declarado es "nuevas técnicas a medida que aparecen"** y el mecanismo de mantenimiento es la **velocidad de iteración**, no la cobertura. Eso explica, y a la vez **limita**, por qué la lista de evasiones del changelog es un extracto y no un catálogo: el proyecto optimiza para reaccionar rápido a la señal del día, no para cerrar la superficie entera ([[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]).
La consecuencia operativa para el vault: **instalar este plugin no reduce el modelo de riesgo del pipeline a una sola capa**. Cierra la capa de señales internas del navegador —con cobertura parcial y fecha de referencia antigua— y **deja intactas** las de transporte, IP, cookies y comportamiento. La identidad declarada del cliente (UA, idioma, plataforma, `vendor`) queda fijada por configuración, no resuelta ([[2026-1026-stealth-user-agent-override-y-navigator-vendor-como-capa-de-identidad]]).

Nota de verificación: las tres citas son literales del README. La captura **no** enumera "a couple of ways" más allá del `User-Agent`: no publica la lista completa de vectores de detección que el plugin pretende cubrir.
