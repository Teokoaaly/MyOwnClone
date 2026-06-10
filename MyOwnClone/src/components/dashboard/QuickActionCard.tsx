"use client";

import { type FC } from "react";
import { motion } from "framer-motion";
import type { IconProps } from "@phosphor-icons/react";
import { Link } from "@/i18n/navigation";

interface QuickActionCardProps {
  href: string;
  icon: React.ComponentType<IconProps>;
  label: string;
  description: string;
  /** CSS color for the icon, e.g. "text-[var(--color-accent-warm)]" */
  iconColor?: string;
}

export const QuickActionCard: FC<QuickActionCardProps> = ({
  href,
  icon: Icon,
  label,
  description,
  iconColor = "text-[var(--color-accent-warm)]",
}) => {
  return (
    <Link href={href} className="block group">
      <motion.div
        whileHover={{ y: -2 }}
        transition={{ type: "spring", stiffness: 400, damping: 25 }}
        className="card cursor-pointer transition-all duration-180 group-hover:border-[var(--border-strong)] group-hover:shadow-md"
      >
        {/* Icon */}
        <div className={`mb-3 ${iconColor}`}>
          <Icon className="h-6 w-6" weight="duotone" />
        </div>

        {/* Label */}
        <h3 className="text-sm font-semibold text-[var(--text-primary)] group-hover:text-[var(--color-accent-warm)] transition-colors duration-160">
          {label}
        </h3>

        {/* Description */}
        <p className="mt-1 text-xs text-[var(--text-muted)] leading-relaxed">
          {description}
        </p>
      </motion.div>
    </Link>
  );
};
