---
id: 2026-1028-openai-register-config-output
type: atom
certainty: solid
sources: [sources/2026-10-28-openai-register-cli-proxy.md]
links: ["[[2026-1022-api-privada-sin-documentacion]]", "[[2026-1023-5sim-openai-tabla-visible-8-filas]]"]
---
## Claim
OpenAI Register requires .env environment configuration for mail setup (Gmail IMAP), output directory for tokens, and network settings (OPENAI_SSL_VERIFY, SKIP_NET_CHECK). Registration outputs include per-email token JSON files in tokens/ and a consolidated accounts.txt file with format `email----password`.

## Why It Matters
The .env file serves as the single configuration point for all mail, proxy, and network parameters needed by the registration tool. Proper setup of MAIL_DOMAIN, IMAP_SERVER, IMAP_PORT, EMAIL_USER, and EMAIL_PASS (Google App Password) is essential for automated verification code retrieval. The token output directory and accounts.txt provide persistent records of created accounts and their credentials, enabling later consumption by downstream workflows or CLIProxyAPI integration. The tool warns that .env and config.yaml must not be committed to version control due to exposed secrets.

## [FRICTION]
> El atom asume que el usuario tiene una cuenta Gmail y ha generado una aplicación password. [[2026-1024-veridrop-cobertura-de-protocolos-por-relay]] no aborda directamente la configuración de mail para registro de OpenAI, pero la nota sobre gestión de expectativas se aplica: los usuarios que esperan verificación instantánea sin configuración de IMAP quedarán satisfechos solo con entrada manual de códigos, lo que reduce el valor de la automatización. La ruta de menor fricción es configurar Gmail IMAP con aplicación password, pero esto requiere haber habilitado 2FA y generado un password de aplicación en Google, lo que añade una barrera de entrada inicial no cubierta en la documentación mínima del proyecto. Ambas afirmaciones no pueden ser completamente correctas sin conocer el estado de la cuenta de correo del operador. Marcado para juicio humano, no auto-resuelto.