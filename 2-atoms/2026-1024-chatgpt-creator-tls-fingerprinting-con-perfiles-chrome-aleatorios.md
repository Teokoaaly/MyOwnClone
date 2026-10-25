---
id: 2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]"]
---

## Claim
Una de las siete features declaradas es **"TLS Fingerprinting — Randomized Chrome TLS profiles to avoid detection"**. La estructura de archivos le da un módulo propio: `internal/chrome/profiles.go  # Chrome TLS profile randomization`, consumido por `internal/register/client.go  # HTTP client with TLS fingerprinting`. El README también declara **"Proxy Support — Optional HTTP/SOCKS proxy for all requests"**, y la sección de configuración confirma que la variable de entorno **`PROXY` sobrescribe el valor del proxy del archivo de configuración**. El README es explícito sobre el propósito declarado: el perfil TLS se aleatoriza **"to avoid detection"**.

## Why It Matters
Este es el **mecanismo de elusión de primer orden del sector**, y es distinto del que el thread venía documentando. Todo lo que había en el thread era elusión de **red y de identidad**: IP que coincida con el país del número, VPN, proxy ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]), sesiones rotating o sticky ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]). Aquí aparece la capa que está **por debajo de la IP**: la huella TLS del cliente.
La consecuencia es precisa y no es trivial: **cambiar de IP no basta si el cliente HTTP sigue siendo el mismo**. Un fingerprint TLS identificable es una señal estable que sobrevive al cambio de proxy, y el propio autor del bot lo ha colocado como feature de primer nivel en un repositorio con 338 estrellas. Eso significa que el coste real de un flujo de alta a escala no es solo el del proxy por gigabyte, sino también el de **construir o untruear un cliente que no se parezca a Go por defecto**.
Para el vault, esto cierra el círculo con el resto del thread en un punto que ya estaba abierto: la §8 del thread decía que **el número de altas, no el de bytes, es lo que escala**; esta fuente añade que el proxy por sí solo no desactiva la detección, y que hay una capa de software entre el proxy y el registro.
Y es el mismo tipo de razonamiento que el vault ya aplicó al captcha —"elegir por el tipo de captcha que aparece en el destino" en vez de por precio—: aquí el criterio de selección sería el del **tipo de señal de detección que aparece en el destino**, no el del país del proxy.

## Nota de verificación
El README declara la feature y el árbol de archivos confirma los dos módulos. La captura **no revela qué librería o biblioteca se usa** para la aleatorización de perfiles TLS (el `go.mod` no está capturado), ni los valores de los perfiles, ni su número. El vault no puede afirmar que la aleatorización sea eficaz contra la detección actual de OpenAI.
