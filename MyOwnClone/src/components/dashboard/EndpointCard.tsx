import { type FC } from "react";
import Link from "next/link";

type Accent = "lavender" | "rose" | "sky" | "amber" | "mint";

interface PreviewItem {
  label: string;
  muted?: boolean;
  icon?: string;
}

interface EndpointCardProps {
  title: string;
  description: string;
  accent: Accent;
  previewItems: PreviewItem[];
  href: string;
}

export const EndpointCard: FC<EndpointCardProps> = ({
  title,
  description,
  accent,
  previewItems,
  href,
}) => {
  const firstWord = title.split(" ")[0];

  return (
    <div className={`endpoint-card endpoint-card--${accent}`}>
      {/* Col izquierda: texto + CTA */}
      <div className="flex flex-col justify-between min-w-0">
        <div>
          <h3 className="text-[15px] font-semibold text-[var(--text-primary)] leading-tight">
            {title}
          </h3>
          <p className="text-[11px] text-[var(--text-secondary)] mt-1 leading-relaxed">
            {description}
          </p>
        </div>
        <Link
          href={href}
          className="self-start mt-3 rounded-full bg-white/80 backdrop-blur border border-[var(--border-soft)] px-3 py-1.5 text-[11px] font-medium text-[var(--text-primary)] hover:bg-white transition-colors shadow-sm"
        >
          Explore {firstWord} API
        </Link>
      </div>

      {/* Col derecha: lista preview */}
      <div className="flex flex-col gap-1.5 min-w-0">
        {previewItems.slice(0, 4).map((item, i) => (
          <div
            key={i}
            className={`flex items-center gap-1.5 text-[11px] truncate ${
              item.muted
                ? "text-[var(--text-muted)]"
                : "text-[var(--text-secondary)]"
            }`}
          >
            <span className="text-[var(--text-muted)] shrink-0 text-xs">
              {item.icon ?? "⌕"}
            </span>
            <span className="truncate">{item.label}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
