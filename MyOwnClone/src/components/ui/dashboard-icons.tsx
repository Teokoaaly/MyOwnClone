import type { IconProps } from "@phosphor-icons/react";
import type React from "react";
import {
  Archive,
  ArrowSquareOut,
  ArrowsCounterClockwise,
  Books,
  Brain,
  CalendarDots,
  ChartBar,
  ChartLineUp,
  ChatCenteredDots,
  ChatTeardropText,
  CheckCircle,
  ClipboardText,
  CreditCard,
  Envelope,
  EnvelopeSimple,
  FileArrowUp,
  FileDoc,
  GlobeHemisphereWest,
  GraduationCap,
  HighlighterCircle,
  Info,
  Key,
  Lightbulb,
  LinkSimple,
  MicrophoneStage,
  PaperPlaneRight,
  PencilSimple,
  Robot,
  ShoppingBagOpen,
  SlidersHorizontal,
  Sparkle,
  TrendUp,
  Trash,
  WarningCircle,
  Wrench,
  X,
  XCircle,
} from "@phosphor-icons/react/ssr";

export type DashboardIcon = React.ComponentType<IconProps>;

export const NavIcons = {
  resumen: ChartBar,
  biblioteca: Books,
  cerebro: Brain,
  inbox: Envelope,
  productos: ShoppingBagOpen,
  reuniones: CalendarDots,
  analiticas: TrendUp,
  facturacion: CreditCard,
  configuracion: SlidersHorizontal,
  apiKeys: Key,
  impersonation: ArrowsCounterClockwise,
  courtesy: Sparkle,
} as const;

export const ShortcutIcons = {
  upload: FileArrowUp,
  memory: Brain,
  inbox: EnvelopeSimple,
  analytics: ChartLineUp,
} as const;

export const ContentTypeIcons = {
  pdf: FileDoc,
  youtube: LinkSimple,
  text: PencilSimple,
  web: GlobeHemisphereWest,
  interview: MicrophoneStage,
  fallback: Archive,
} as const;

export const SiloIcons = {
  teach: GraduationCap,
  support: ChatCenteredDots,
  sales: ShoppingBagOpen,
} as const;

export const ToneIcons = {
  formal: ClipboardText,
  informal: ChatTeardropText,
  cercano: Sparkle,
  tecnico: Wrench,
} as const;

export const LanguageIcons = {
  es: GlobeHemisphereWest,
  en: GlobeHemisphereWest,
} as const;

export const StatusIcons = {
  all: Envelope,
  pending: ArrowsCounterClockwise,
  sent: CheckCircle,
  discarded: Trash,
} as const;

export const UiIcons = {
  rocket: ArrowSquareOut,
  hint: Lightbulb,
  success: CheckCircle,
  warning: WarningCircle,
  draft: PencilSimple,
  ai: Robot,
  send: PaperPlaneRight,
  save: FileArrowUp,
  discard: Trash,
  close: X,
  good: CheckCircle,
  bad: XCircle,
  info: Info,
  highlight: HighlighterCircle,
};
