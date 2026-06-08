"use client";

import { type FC } from "react";

export type StatusKind =
  | "active"
  | "normal"
  | "trial"
  | "suspended"
  | "warning"
  | "cancelled"
  | "error"
  | "violet"
  | "default";

interface StatusBadgeProps {
  kind?: StatusKind;
  label?: string;
  /** When provided, overrides the kind-based label and class. */
  className?: string;
}

const KIND_TO_CLASS: Record<StatusKind, string> = {
  active: "badge-active",
  normal: "badge-active",
  trial: "badge-trial",
  suspended: "badge-warning",
  warning: "badge-warning",
  cancelled: "badge-error",
  error: "badge-error",
  violet: "badge-violet",
  default: "badge-trial",
};

const KIND_TO_LABEL: Record<StatusKind, string> = {
  active: "Active",
  normal: "Active",
  trial: "Trial",
  suspended: "Suspended",
  warning: "Warning",
  cancelled: "Cancelled",
  error: "Error",
  violet: "Admin",
  default: "—",
};

/** Maps a raw status string from the API to a `StatusKind`. */
export function statusToKind(raw: string | null | undefined): StatusKind {
  switch ((raw ?? "").toLowerCase()) {
    case "active":
    case "normal":
      return "active";
    case "trial":
      return "trial";
    case "suspended":
    case "warning":
      return "warning";
    case "cancelled":
    case "error":
      return "error";
    case "violet":
    case "admin":
      return "violet";
    default:
      return "default";
  }
}

export const StatusBadge: FC<StatusBadgeProps> = ({
  kind = "default",
  label,
  className,
}) => {
  return (
    <span className={className ?? KIND_TO_CLASS[kind]}>
      {label ?? KIND_TO_LABEL[kind]}
    </span>
  );
};
