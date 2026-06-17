export type PublicPlanId = "free" | "pro" | "enterprise";

export interface PublicPlanFeature {
  label: string;
  included: boolean;
}

export interface PublicPlan {
  id: PublicPlanId;
  name: string;
  badge: string;
  description: string;
  monthly: number | null;
  annual: number | null;
  billing: string;
  cta: string;
  href: string;
  featured?: boolean;
  features: PublicPlanFeature[];
}

export const PUBLIC_PRICING_PLANS: PublicPlan[] = [
  {
    id: "free",
    name: "Free",
    badge: "Starter",
    description: "Perfect to explore and prototype.",
    monthly: 0,
    annual: 0,
    billing: "No card required",
    cta: "Get started",
    href: "/registro",
    features: [
      { label: "1 AI clone", included: true },
      { label: "Basic knowledge base", included: true },
      { label: "Public chat", included: true },
      { label: "Community support", included: true },
      { label: "Inbox AI triage", included: false },
      { label: "API access", included: false },
    ],
  },
  {
    id: "pro",
    name: "Pro",
    badge: "Most popular",
    description: "For creators and growing businesses.",
    monthly: 64.9,
    annual: 778.8,
    billing: "Monthly billing",
    cta: "Choose Pro",
    href: "/planes",
    featured: true,
    features: [
      { label: "5 AI clones", included: true },
      { label: "Unlimited knowledge", included: true },
      { label: "Inbox AI triage", included: true },
      { label: "Product catalog", included: true },
      { label: "Full analytics", included: true },
      { label: "Priority support", included: true },
    ],
  },
  {
    id: "enterprise",
    name: "Enterprise",
    badge: "Scale",
    description: "For teams with advanced needs.",
    monthly: null,
    annual: null,
    billing: "Tailored contract",
    cta: "Contact sales",
    href: "mailto:hello@myownclone.com",
    features: [
      { label: "Unlimited clones", included: true },
      { label: "API access", included: true },
      { label: "Team management", included: true },
      { label: "Custom integrations", included: true },
      { label: "Dedicated support", included: true },
    ],
  },
];

export const PUBLIC_PRICING_COMPARISON = [
  ["AI clones", "1", "5", "Unlimited"],
  ["Knowledge base", "Basic", "Unlimited", "Unlimited"],
  ["Public chat", "Yes", "Yes", "Yes"],
  ["Inbox AI triage", "No", "Yes", "Yes"],
  ["Product catalog", "No", "Yes", "Yes"],
  ["Analytics", "Basic", "Full", "Advanced"],
  ["API access", "No", "No", "Yes"],
  ["Support", "Community", "Priority", "Dedicated"],
] as const;

export function formatPublicPlanPrice(value: number | null) {
  if (value === null) return "Custom";
  if (value === 0) return "$0";

  return `$${value.toLocaleString("en-US", {
    minimumFractionDigits: value % 1 ? 2 : 0,
    maximumFractionDigits: 2,
  })}`;
}

export function normalizePublicPlanId(value: string | null | undefined): PublicPlanId | null {
  if (!value) return null;
  const normalized = value.toLowerCase();

  if (normalized === "free" || normalized === "basic") return "free";
  if (normalized === "pro") return "pro";
  if (normalized === "enterprise" || normalized === "scale") return "enterprise";

  return null;
}

export function getPublicBillingLabel(plan: PublicPlan, annual: boolean) {
  if (plan.monthly === null) return plan.billing;
  if (!annual) return plan.billing;
  return "Annual equivalent from dashboard price";
}
