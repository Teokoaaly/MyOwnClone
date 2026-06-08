# DESIGN SYSTEM — MyOwnClone "Institutional Console"

> Source of truth for visual decisions. Tokens already live in `replica/src/app/globals.css`; this document explains the intent, lists every token, and codifies component rules.

## 1. Identity

- **Name**: Institutional Console
- **Personality**: clear, dense, premium, financial. Light by default, dark as a complete token variant — never a separate design.
- **References (intent, not content to copy)**: Madful'At dashboard, OEME console, Linear/Stripe admin panels.

## 2. Principles (do not break these)

1. Light mode is the default product. Dark is a true variant by tokens, not a redesign.
2. The UI is responsive for real — desktop dense, tablet compact, mobile stacked.
3. Information, not decoration, is the protagonist. Charts, tables, lists, metrics over marketing cards.
4. No landing-page inside the app. No big hero copy, no "Trusted by 200,000+ users" rows, no rotated notification stacks.
5. No card inside a card.
6. No long text explaining the UI.
7. No gradient that hides data.
8. No saturated colors. Accents are accents, not backgrounds.
9. No heavy shadows. Soft, tight, layered.

## 3. Tokens

### 3.1 Surfaces (light default)

```
--bg-page:    #E8E2DD     warm cream outer
--bg-shell:   #FFFFFF     app shell
--bg-sidebar: #FFFFFF
--bg-topbar:  #FFFFFF
--surface-1:  #FFFFFF     card
--surface-2:  #FAFAF9     nested card / hover
--surface-3:  #F5F5F4     deeper hover
```

### 3.2 Surfaces (dark variant via `.dark` class)

```
--bg-page:    #070708
--bg-shell:   #0B0B0C
--bg-sidebar: #101011
--bg-topbar:  #111112
--surface-1:  #121213
--surface-2:  #171718
--surface-3:  #1D1D1F
```

### 3.3 Borders (always present, never hard)

```
--border-soft:   rgba(15, 23, 42, 0.06)   default
--border-medium: rgba(15, 23, 42, 0.10)
--border-strong: rgba(15, 23, 42, 0.16)
```

Dark mode flips the alpha source to `rgba(255, 255, 255, 0.07)` etc.

### 3.4 Text

| Token | Light | Dark |
|---|---|---|
| --text-primary | #1C1917 | #F4F4F5 |
| --text-secondary | #57534E | #A1A1AA |
| --text-muted | #78716C (4.69:1) | #A1A1AA (~6.4:1) |
| --text-faint | #D6D3D1 | #52525B |

### 3.5 Accents (Tailwind theme block)

```
--color-accent-warm:   #EA580C   default CTA, active nav, margin-positive
--color-accent-amber:  #D97706
--color-accent-pink:   #DB2777
--color-accent-blue:   #2563EB
--color-accent-cyan:   #0891B2
--color-accent-violet: #7C3AED
--color-accent-green:  #059669
```

### 3.6 Series (charts)

```
--series-orange: #FB923C
--series-amber:  #FBBF24
--series-pink:   #EC4899
--series-blue:   #2563EB
--series-cyan:   #06B6D4
--series-violet: #8B5CF6
```

### 3.7 Pastels (EndpointCard hero blocks only)

```
--color-pastel-lavender: #F3E8FF
--color-pastel-rose:     #FFE4E6
--color-pastel-sky:      #E0F2FE
--color-pastel-amber:    #FEF3C7
--color-pastel-mint:     #D1FAE5
```

## 4. Typography

- UI / body: `var(--font-dm-sans)` (DM Sans, loaded via `next/font/google`).
- Numbers and code: `var(--font-jetbrains-mono)` (JetBrains Mono).
- Weights: 400, 500, 600, 700. No bold-excessive.
- No negative tracking.
- Numbers in `.stat-value` and `.mono` get `font-variant-numeric: tabular-nums`.
- H1: 24-32px. H2 (card): 16-20px. Body: 14-15px. Label: 11-12px (uppercase + tracking 0.12em via `.section-label`).

## 5. Layout grid

### Desktop (≥1024px)

```
┌──────────────────────────────────────────────────┐
│ Page padding p-3 md:p-6                          │
│  ┌─ shell rounded-22 border shadow-soft ──────┐  │
│  │ ┌── sidebar 220px ──┐ ┌── content ────────┐ │  │
│  │ │ Logo              │ │ Topbar 72px       │ │  │
│  │ │ Search            │ ├───────────────────┤ │  │
│  │ │ Nav sections      │ │ Main p-6          │ │  │
│  │ │  · API PLAYGROUND │ │   grid 12 cols    │ │  │
│  │ │  · MANAGEMENT     │ │   gap-4           │ │  │
│  │ │ User block        │ │                   │ │  │
│  │ └───────────────────┘ └───────────────────┘ │  │
│  └──────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

### Tablet (768-1023px)

- Sidebar collapses to a rail (72px) OR a drawer.
- Topbar stays 64-72px.
- Cards: 2 columns.
- Tabs: horizontal scroll.

### Mobile (<768px)

- No persistent sidebar. Drawer opens from left, same nav order.
- Topbar compact (56px), with hamburger.
- Main padding 16px.
- Cards: 1 column.
- Tables: convert to list rows/cards.
- Charts: fixed height 260-320px with horizontal scroll for tooltips.

## 6. Shell exterior

The app lives inside a rounded shell on a warm cream page. The shell is a frame, not a feature.

```
background: var(--bg-page);   outside the shell
.app-shell {                  the shell itself
  background: var(--bg-shell);
  border-radius: 22px;
  border: 1px solid var(--border-soft);
  box-shadow:
    0 1px 2px rgba(15, 23, 42, 0.04),
    0 24px 64px rgba(15, 23, 42, 0.08);
}
```

## 7. Component rules

### 7.1 Cards

- Radius: 14-18px (use 14 for tight data cards, 18 for hero cards).
- Padding: 16px mobile, 20-24px desktop.
- Border: 1px `var(--border-soft)`, always visible.
- Hover: max `translateY(-1px)` or `-2px`. Never bigger.
- No card inside a card. If you need a sub-grouping, use a divider or a list row, not a nested card.

### 7.2 Buttons

- Primary (`.btn-primary`): pill, near-black solid (`#0C0A09`), white text. Dark-mode inverts.
- Secondary (`.btn-secondary`): pill, white, 1px border `var(--border-medium)`, hover `--surface-2`.
- Border glow (`hover:shadow-[0_0_28px_rgba(249,115,22,0.16)]`) is only for primary CTA on the institutional shell.
- Icon buttons: 32-40px square, hover `--surface-2`, no shadow.
- Disabled: `opacity: 0.4`, no pointer.

### 7.3 Inputs

- Height: 36-40px.
- Border: 1px `var(--border-soft)`; focus: 1px `var(--color-accent-warm)` + soft glow.
- Radius: 8-10px (NOT pill — pill is reserved for buttons).
- Placeholder: `var(--text-muted)`.
- Search bars (topbar, ⌘K) get the search icon left, optional shortcut hint right.

### 7.4 Badges (translucent)

| State | Color | Class |
|---|---|---|
| Active | emerald | `.badge-active` |
| Trial / New | cyan | `.badge-trial` |
| Warning / Suspended | amber | `.badge-warning` |
| Error / Cancelled | red | `.badge-error` |
| Enterprise / Admin | violet | `.badge-violet` (to add) |

Each badge uses a 1px translucent border + 10% alpha fill + solid text color. Light/dark variants already implemented in `globals.css`.

### 7.5 Tables

Desktop:
- Compact rows (36-44px height).
- Header: `var(--surface-2)` background, 11px uppercase muted text.
- Body rows: border-bottom `var(--border-soft)`.
- Numbers right-aligned in mono.
- Hover: `var(--surface-2)` background.

Mobile:
- Render as list rows. Hide non-essential columns. Show 3-5 key fields. Add an action menu icon.

### 7.6 Empty / loading / error states

Empty: icon (32-40px) + short title (1 line, 14-16px) + microcopy (12-13px muted) + optional CTA.
Loading: skeleton with `bg-[var(--surface-2)]` rounded rectangles. No bouncing dots except for in-card micro-loaders.
Error: icon (red, 20px) + title + short reason + a "Try again" button.

### 7.7 Charts

- Recharts (or equivalent) with the `--series-*` palette.
- Grid lines: `var(--border-soft)`, 1px, dashed optional.
- Labels: 11px, `var(--text-muted)`.
- Tooltip: 12px, white card with 1px `var(--border-medium)`.
- Legend: 12px, dot + label, gap 12px.

## 8. Iconography

- Library: `@phosphor-icons/react`, weight `duotone` for nav, `regular` for actions, `bold` for active emphasis.
- 8 namespaces already defined: `NavIcons`, `ShortcutIcons`, `ContentTypeIcons`, `SiloIcons`, `ToneIcons`, `LanguageIcons`, `StatusIcons`, `UiIcons`.
- Always 18-20px in nav, 16-18px in cards, 14-16px in buttons.

## 9. Microinteractions

- Durations: 160-220ms.
- Easings: `ease`, `ease-in-out`. No bouncy springs.
- Hover: `translateY(-1px)`, `background` color shift, or border glow.
- Active: `scale(0.98)` for buttons.
- Focus: 1px `var(--color-accent-warm)` outline with 2px offset.
- Honor `prefers-reduced-motion` (already in globals.css).

## 10. Accessibility

- Color contrast: AA minimum, AAA for primary text.
- Focus visible: every interactive element.
- Keyboard nav: sidebar, topbar, modals, dropdowns all keyboard-navigable.
- Aria: every icon-only button needs `aria-label`; every form field needs a `<label>`.
- Don't rely on color alone (use badges with text, not just colored dots).

## 11. Don'ts (the rules that prevent slop)

- No `bg-black` / `bg-white` in components — use tokens.
- No inline gradient styles in pages — use the `app-shell` class.
- No new colors that don't exist in the accent palette.
- No card-in-card.
- No "FAQs" or "About" copy inside the app shell.
- No emoji.
- No hardcoded "0" in stat cards without a count-up.
- No charts without a y-axis label.
- No "Click here" or "Read more" — use specific actions.
- No magic strings for status — always map to canonical English then translate in the view.
