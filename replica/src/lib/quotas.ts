import "server-only";

export type PlanName = "basic" | "pro" | "scale" | "enterprise" | "trial";

interface PlanLimits {
  conversationsPerDay: number;
  emailsPerMonth: number;
  sources: number;
  storageMb: number;
  clones: number;
  teamMembers: number;
}

const PLAN_LIMITS: Record<PlanName, PlanLimits> = {
  trial: {
    conversationsPerDay: 50,
    emailsPerMonth: 20,
    sources: 5,
    storageMb: 100,
    clones: 1,
    teamMembers: 1,
  },
  basic: {
    conversationsPerDay: 200,
    emailsPerMonth: 100,
    sources: 20,
    storageMb: 1000,
    clones: 1,
    teamMembers: 1,
  },
  pro: {
    conversationsPerDay: 1000,
    emailsPerMonth: 500,
    sources: 100,
    storageMb: 5000,
    clones: 3,
    teamMembers: 3,
  },
  scale: {
    conversationsPerDay: 5000,
    emailsPerMonth: 2000,
    sources: 500,
    storageMb: 25000,
    clones: 10,
    teamMembers: 10,
  },
  enterprise: {
    conversationsPerDay: 50000,
    emailsPerMonth: 10000,
    sources: 2000,
    storageMb: 100000,
    clones: 50,
    teamMembers: 50,
  },
};

export function getPlanLimits(plan: PlanName): PlanLimits {
  return PLAN_LIMITS[plan];
}

export function checkLimit(
  plan: PlanName,
  resource: keyof PlanLimits,
  current: number
): { allowed: boolean; limit: number } {
  const limit = PLAN_LIMITS[plan][resource];
  return { allowed: current < limit, limit };
}
