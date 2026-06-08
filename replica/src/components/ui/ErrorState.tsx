"use client";

import type { FC, ReactNode } from "react";

interface ErrorStateProps {
  title?: string;
  message: string;
  action?: ReactNode;
}

export const ErrorState: FC<ErrorStateProps> = ({
  title = "Algo salió mal",
  message,
  action,
}) => {
  return (
    <div
      role="alert"
      className="card border-red-200/60 bg-red-50/40"
    >
      <p className="text-sm font-medium text-red-700">{title}</p>
      <p className="mt-1 text-xs text-red-600">{message}</p>
      {action && <div className="mt-3">{action}</div>}
    </div>
  );
};
