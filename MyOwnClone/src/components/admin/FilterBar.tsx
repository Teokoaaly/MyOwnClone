import type { FC, ReactNode } from "react";

interface FilterBarProps {
  /** Fields or other controls rendered inside the bar. */
  children: ReactNode;
  /** Extra classes appended to the outer wrapper. */
  className?: string;
}

/**
 * Container that gives a horizontal row of {@link Field} controls the
 * standard card + responsive flex layout used across admin filter bars.
 */
export const FilterBar: FC<FilterBarProps> = ({ children, className }) => {
  return (
    <div
      className={[
        "card flex flex-col gap-3 sm:flex-row sm:items-end",
        className ?? "",
      ]
        .join(" ")
        .trim()}
    >
      {children}
    </div>
  );
};
