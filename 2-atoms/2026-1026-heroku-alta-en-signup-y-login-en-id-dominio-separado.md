---
id: 2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-signup.md]
links: ["[[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]", "[[2026-1023-live-verify-aviso-legal-aun-declara-vercel]]", "[[2026-1024-njal-la-privacidad-whois-y-dns-anycast-incluidos-en-el-registro]]"]
---

## Claim
La captura de `https://signup.heroku.com/` muestra que **el alta y el login viven en dos dominios distintos**: el texto "Already have an account? [Log in](https://id.heroku.com/login)" apunta a **`id.heroku.com`**, no a `signup.heroku.com`. El logotipo de la página es **"Heroku from Salesforce"** y enlaza a `www.heroku.com/home`. Y el formulario de alta **no contiene ningún campo de contraseña ni de confirmación de contraseña**: la captura solo enumera los campos de identidad, país, empresa y consentimiento, y termina en el botón "Verify" del captcha.

## Why It Matters
La separación **`signup.heroku.com` / `id.heroku.com`** es la misma forma que el vault ya midió en su propio producto: superficie de aplicación y superficie de identidad en hosts distintos, con la consecuencia de que **la sesión y el login no viven en el mismo origen que el alta** ([[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]). Aquí la separación es además **corporativa**: la página que capta el alta y la que autentica son de un grupo (Salesforce) que el vault tiene ya registrado en el Aviso Legal como processor declarado de un proveedor que ya no es el real ([[2026-1023-live-verify-aviso-legal-aun-declara-vercel]]).
El dato duro y más útil es **la ausencia del campo de contraseña**: el alta **no crea la credencial en la página**. O bien la credencial se pide en un paso posterior (fuera de la captura), o bien la cuenta se crea sin contraseña y el acceso se resuelve por correo/SSO en `id.heroku.com`. El vault **no puede elegir entre las dos lecturas** con este material — y esa indeterminación es en sí misma el dato: **una alta sin campo de contraseña no es una alta, es una captación de datos que luego se convierte en cuenta en otro host**. Es el mismo patrón de "la superficie de registro publica lo que el proveedor quiere capturar, no lo que el usuario va a autenticar" que el vault registró en el registro de dominios de njalla.la, donde lo publicado (WHOIS, DNS, reenvío) es un bundle de producto y no la mecánica de la cuenta ([[2026-1024-njal-la-privacidad-whois-y-dns-anycast-incluidos-en-el-registro]]).
