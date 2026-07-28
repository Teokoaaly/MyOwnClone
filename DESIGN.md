# MyOwnClone Liquid Landing Design System

## 1. Atmosphere & Identity

La landing alternativa es un escaparate claro y preciso para un producto de clonación digital. Su firma visual es un cristal líquido azul sobre blanco: capas translúcidas, luz difusa y un orbe propio que comunica inteligencia sin ocultar el contenido.

## 2. Color

| Role | Token | Value | Usage |
| --- | --- | --- | --- |
| Surface | `--liquid-surface` | `#FFFFFF` | Fondo principal |
| Surface soft | `--liquid-surface-soft` | `#F5FAFF` | Bandas y secciones |
| Text strong | `--liquid-ink` | `#10213B` | Titulares y navegación |
| Text muted | `--liquid-muted` | `#51647F` | Cuerpo y ayuda |
| Accent | `--liquid-blue` | `#0084FF` | CTA, foco y enlaces |
| Glow one | `--liquid-glow-one` | `#60B1FF` | Resplandor ambiental |
| Glow two | `--liquid-glow-two` | `#319AFF` | Resplandor ambiental |
| Glass | `--liquid-glass` | `rgba(255,255,255,.30)` | Navegación y superficies de cristal |
| Glass border | `--liquid-glass-border` | `rgba(0,0,0,.10)` | Contorno exterior |
| Glass highlight | `--liquid-glass-highlight` | `rgba(255,255,255,.35)` | Reflejo interior |

El azul es el único acento. La legibilidad no depende del blur y el texto siempre usa `--liquid-ink` o `--liquid-muted`.

## 3. Typography

| Level | Token | Size | Weight | Usage |
| --- | --- | --- | --- | --- |
| Display | `--liquid-display` | `clamp(3rem, 5.2vw, 4.7rem)` | 700 | Hero |
| H2 | `--liquid-h2` | `clamp(2rem, 3.2vw, 3rem)` | 700 | Secciones |
| H3 | `--liquid-h3` | `1.25rem` | 700 | Tarjetas |
| Lead | `--liquid-lead` | `1.125rem` | 400 | Descripción |
| Body | `--liquid-body` | `1rem` | 400 | Texto general |
| Small | `--liquid-small` | `.875rem` | 500 | Etiquetas |

Fustat se usa en marca y titulares. Inter se usa en contenido y controles. El texto no baja de 14 px.

## 4. Spacing & Layout

La unidad base es 4 px. Los espaciados permitidos son `4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96` px. El contenido usa un máximo de 1600 px, 24 px de gutter en escritorio y 16 px en móvil. Los breakpoints son 640, 768, 1024, 1280 y 1536 px.

## 5. Components

### Liquid glass surface

- **Structure:** capa traslúcida, borde fino y reflejo interior.
- **Spacing:** 16 o 24 px, radio 16 px.
- **States:** foco visible azul, hover con cambio de opacidad, activo con escala `.98`.
- **Accessibility:** contraste AA sin blur; objetivos interactivos de mínimo 44 px.
- **Motion:** solo `transform` y `opacity` entre 160 y 260 ms.

### Primary CTA

- **Structure:** enlace o botón azul con icono circular de flecha.
- **States:** default, hover a escala máxima `1.02`, active `.98`, focus visible.
- **Accessibility:** etiqueta inequívoca y contraste AA.

## 6. Motion & Interaction

Los microcambios duran 160 ms y las entradas decorativas 420 ms con `cubic-bezier(.16,1,.3,1)`. El orbe solo transforma y cambia de opacidad. En `prefers-reduced-motion: reduce` se eliminan las animaciones no esenciales y se conserva el contenido estático.

## 7. Depth & Surface

La estrategia es cristal y sombras tonales suaves: borde de 1 px, reflejo inset y sombra azul muy difusa. Los componentes mantienen radio de 16 px; los elementos circulares solo se usan como iconos de CTA.
