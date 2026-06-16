import type { FC, ReactNode } from "react";

interface FieldProps {
  /** Visible label rendered above the control. */
  label: ReactNode;
  /** The control itself (input, select, etc). */
  children: ReactNode;
  /** When true, the field grows to fill the available row width. */
***REMOVED***ll?: boolean;
  /** Optional extra classes appended to the outer wrapper. */
  className?: string;
}

const inputClassName =
  "mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]";

/**
 * Form field wrapper used by the admin filter bars. Renders a label + any
 * control with the standard border / focus styling. Replaces the
 * `stat-label` + `border` + `focus:border-accent-warm` markup previously
 * duplicated on every admin page.
 */
export const Field: FC<FieldProps> = ({ label, children, fill, className }) => {
  return (
    <label className={["block", fill ? "flex-1" : "", className ?? ""].join(" ").trim()}>
      <span className="stat-label">{label}</span>
      {children}
    </label>
  );
};

/**
 * Standard styling for inputs and selects inside a {@link Field}.
 * Re-exported so pages don't need to know the raw class string.
 */
export const fieldControlClass = inputClassName;
