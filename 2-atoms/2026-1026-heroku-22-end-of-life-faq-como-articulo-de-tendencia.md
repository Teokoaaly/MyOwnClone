---
id: 2026-1026-heroku-22-end-of-life-faq-como-articulo-de-tendencia
type: atom
certainty: tentative
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]", "[[2026-1026-heroku-metodos-de-despliegue-git-github-docker-terraform-y-autodespliegue-en-push]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
Entre los **cinco** artículos de "Trending articles" de la home de soporte de Heroku figura **"Heroku-22 End-of-Life FAQ"** — con identificador de artículo `NQNCQTEJ`. Es decir, **la página de soporte de una plataforma en producción tiene entre sus cinco contenidos más leídos el FAQ de fin de vida de una generación de runtime**, no un artículo de precios, no uno de despliegue y no uno de límites de uso. El identificador de artículo (`NQNCQTEJ`) y el de "Before opening a support ticket" (`JYBXPRFN`) son **códigos opacos de Salesforce Knowledge**, no slugs legibles.

## Why It Matters
El vault ha medido dos generaciones de espacio de cómputo en Heroku —**Cedar** y **Fir**, con la advertencia explícita de que los dynos Private/Shield de una no valen para la otra ([[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]])— y ahora aparece una **tercera línea temporal**, la de las generaciones de *runtime* (Heroku-22), con su propio ciclo de EOL. Y lo relevante no es el nombre: es que **Heroku publica el EOL como contenido de soporte de primer nivel**, con un FAQ dedicado entre los más leídos.
Eso fija un patrón de **coste de descarte** que el vault no tenía cuantificado: en un PaaS, la plataforma decide cuándo un runtime deja de ser soportado, y el cliente que quiera seguir en él tiene que migrar dentro de una ventana que Heroku define. Es exactamente el riesgo que en el producto propio se evita por completo, porque el stack es nginx + Postgres + Redis autoalojados ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y **nadie puede declarar EOL sobre él**. Y el vector de entrada de esa ventana es el mismo que publica el marketing de despliegue: Heroku ofrece Git, GitHub, Docker y Terraform con autodespliegue en cada push ([[2026-1026-heroku-metodos-de-despliegue-git-github-docker-terraform-y-autodespliegue-en-push]]), es decir, **la app se crea contra un runtime por defecto que el proveedor controla** ([[2026-1026-heroku-changelog-de-runtimes-ruby-3-4-12-opjdk-y-dotnet]]).
El detalle estructural de los identificadores opacos (`NQNCQTEJ`) confirma que **todo el portal es una instancia de Salesforce Knowledge**, con la misma capa legal y de producto que el pie de página declara.

Nota: la captura **no** reproduce el contenido del FAQ de EOL: no hay fecha de fin de vida de Heroku-22, ni sustituto recomendado, ni lista de apps afectadas. El átomo queda en `tentative` por eso.
