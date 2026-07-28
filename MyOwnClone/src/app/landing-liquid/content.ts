import {
  PUBLIC_PRICING_COMPARISON,
  PUBLIC_PRICING_PLANS,
  type PublicPlan,
} from "@/lib/public-pricing";

type SpanishPlanCopy = {
  readonly badge: string;
  readonly description: string;
  readonly billing: string;
  readonly cta: string;
  readonly features: readonly string[];
};

const spanishPlanCopy: Readonly<Record<PublicPlan["id"], SpanishPlanCopy>> = {
  free: {
    badge: "Para empezar",
    description: "Explora y crea tu primer clon.",
    billing: "Sin tarjeta",
    cta: "Crear mi clon",
    features: ["1 clon de IA", "Base de conocimiento inicial", "Chat público", "Soporte comunitario", "Triaje de bandeja", "Acceso API"],
  },
  pro: {
    badge: "Más elegido",
    description: "Para creadores y negocios en crecimiento.",
    billing: "Facturación mensual",
    cta: "Elegir Pro",
    features: ["5 clones de IA", "Conocimiento ilimitado", "Triaje de bandeja", "Catálogo de productos", "Analítica completa", "Soporte prioritario"],
  },
  enterprise: {
    badge: "Escala",
    description: "Para equipos con necesidades avanzadas.",
    billing: "Contrato a medida",
    cta: "Hablar con el equipo",
    features: ["Clones ilimitados", "Acceso API", "Gestión de equipos", "Integraciones personalizadas", "Soporte dedicado"],
  },
};

const spanishComparisonLabels: Readonly<Record<string, string>> = {
  "AI clones": "Clones de IA",
  "Knowledge base": "Base de conocimiento",
  "Public chat": "Chat público",
  "Inbox AI triage": "Triaje de bandeja",
  "Product catalog": "Catálogo de productos",
  Analytics: "Analítica",
  "API access": "Acceso API",
  Support: "Soporte",
};

export const liquidPricingPlans: readonly PublicPlan[] = PUBLIC_PRICING_PLANS.map((plan) => {
  const translation = spanishPlanCopy[plan.id];
  return {
    ...plan,
    badge: translation.badge,
    description: translation.description,
    billing: translation.billing,
    cta: translation.cta,
    features: plan.features.map((feature, index) => ({
      ...feature,
      label: translation.features[index] ?? feature.label,
    })),
  };
});

export const liquidPricingComparison: readonly (readonly string[])[] = PUBLIC_PRICING_COMPARISON.map(
  ([feature, free, pro, enterprise]) => [
    spanishComparisonLabels[feature] ?? feature,
    free === "Yes" ? "Sí" : free === "No" ? "No" : free,
    pro === "Yes" ? "Sí" : pro === "No" ? "No" : pro,
    enterprise === "Yes" ? "Sí" : enterprise === "No" ? "No" : enterprise,
  ],
);

export const liquidPricingCopy = {
  annual: "Anual",
  annualEquivalent: "Equivalente anual",
  compareFeatures: "Comparar planes",
  current: "Actual",
  dashboardPrices: "Precios del panel",
  feature: "Característica",
  monthly: "Mensual",
  pricing: "Planes",
  toggleAnnual: "Cambiar facturación anual",
  year: "/año",
  month: "/mes",
} as const;
