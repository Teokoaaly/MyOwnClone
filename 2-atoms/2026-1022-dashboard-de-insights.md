---
id: 2026-1022-dashboard-de-insights
type: atom
certainty: tentative
sources: [raw/articles/myownclone-founder-transcript.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[ai-clones]]", "[[emprenda-aprendiendo]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]"]
---

## Claim
[[myownclone]] incluye un panel de "aprendizajes" con cuatro salidas: feedbacks que dejan los usuarios, preguntas más frecuentes (para dar más contexto al clon o para detectar nuevos cursos), un análisis del avatar de la audiencia que se construye guardando memoria sobre los interlocutores, y una lista de gaps de conocimiento —preguntas que el clon no supo responder.
> "vas viendo los feedbacks que te dejan, vas viendo las preguntas más frecuentes que te hacen por si quieres darle más contexto… Oye, me preguntan mucho sobre este tema. Eso te permite, por ejemplo, pensar en nuevos cursos… tener insights de quién es el avatar de tu audiencia… se va guardando memoria sobre la gente que va hablando contigo… una parte que te dice los gaps de conocimiento. Oye, te han preguntado sobre esto y tu clon no ha sabido responder."

## Why It Matters
Convierte el tráfico del clon en inteligencia de producto: preguntas no contestadas y feedback son la hoja de ruta de qué grabar/formar, y el perfil de audiencia es un input para designing la oferta. Es la pieza que convierte el panel en un bucle de mejora y en el sitio donde el guardarrail anti-alucinación se monetiza (un gap es contenido que falta). En [[ai-clones]] aparece listada como "insights de audiencia", y [[emprenda-aprendiendo]] es el dataset real donde estos signals se generaron. El recon de bundles confirma que el panel existe y es navegable: `/admin/learning` con cuatro subpáginas exactas — `/audience`, `/feedback`, `/gaps` y `/questions` (y sus alias ES `/audiencia`, `/preguntas`), es decir, una implementación 1:1 de las cuatro salidas descritas por el founder — ver [[2026-1022-admin-rutas-bilingues-sin-subdominio]].
