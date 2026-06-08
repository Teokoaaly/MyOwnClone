import { type FC } from "react";
import Link from "next/link";

interface OnboardingBannerProps {
  completedSteps?: number;
  totalSteps?: number;
}

export const OnboardingBanner: FC<OnboardingBannerProps> = ({
  completedSteps = 0,
  totalSteps = 4,
}) => {
  const progressPercent = Math.round((completedSteps / totalSteps) * 100);

  return (
    <div
      className="relative overflow-hidden rounded-2xl border border-[var(--border-soft)] p-6 md:p-8 mt-6"
      style={{
        background: `
          radial-gradient(circle at 15% 50%, rgba(249, 115, 22, 0.12), transparent 50%),
          radial-gradient(circle at 85% 30%, rgba(236, 72, 153, 0.08), transparent 45%),
          var(--surface-2)
        `,
      }}
    >
      <div className="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        {/* Left: text */}
        <div>
          <h3 className="text-base font-semibold text-[var(--text-primary)]">
            Finish your AI workspace setup
          </h3>
          <p className="mt-1 text-sm text-[var(--text-muted)] max-w-md">
            Connect your first source, create a clone, train memory, and publish.
          </p>

          {/* Progress bar */}
          <div className="mt-4 flex items-center gap-3">
            <div className="h-1.5 flex-1 max-w-[180px] bg-[var(--border-medium)] rounded-full overflow-hidden">
              <div
                className="h-full rounded-full transition-all duration-500"
                style={{
                  width: `${progressPercent}%`,
                  background: "linear-gradient(90deg, #F97316, #FB923C)",
                }}
              />
            </div>
            <span className="text-xs text-[var(--text-muted)] font-mono tabular-nums">
              {completedSteps}/{totalSteps} steps
            </span>
          </div>
        </div>

        {/* Right: CTAs */}
        <div className="flex flex-wrap gap-2 shrink-0">
          <Link
            href="/biblioteca"
            className="btn-primary"
          >
            Complete setup
          </Link>
          <Link
            href="/configuracion"
            className="btn-secondary"
          >
            View guide
          </Link>
        </div>
      </div>
    </div>
  );
};