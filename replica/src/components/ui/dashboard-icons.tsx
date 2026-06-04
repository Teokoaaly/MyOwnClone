import type { IconProps } from "@phosphor-icons/react";
import {
  ArchiveBox,
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
} from "@phosphor-icons/react";

export type DashboardIcon = (props: IconProps) => JSX.Element;

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
  fallback: ArchiveBox,
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
