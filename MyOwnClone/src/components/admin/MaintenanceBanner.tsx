"use client";

import { useEffect, useState } from "react";

interface MaintenanceStatus {
  active: boolean;
  message: string;
}

export function MaintenanceBanner() {
  const [status, setStatus] = useState<MaintenanceStatus | null>(null);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    let cancelled = false;
    const check = async () => {
      try {
        const base = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:5001";
        const res = await fetch(`${base}/console/api/myownclone/maintenance/status`, {
          cache: "no-store",
        });
        if (!cancelled && res.ok) {
          setStatus(await res.json());
        }
      } catch {
        // Silent retry
      }
    };
    check();
    const interval = setInterval(check, 60000);
    return () => {
      cancelled = true;
      clearInterval(interval);
    };
  }, []);

  if (!status?.active || dismissed) {
    return null;
  }

  return (
    <div
      role="alert"
      style={{
        backgroundColor: "#fde047",
        color: "#713f12",
        padding: "0.75rem 1rem",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        position: "sticky",
        top: 0,
        zIndex: 1000,
        borderBottom: "1px solid #facc15",
      }}
    >
      <span>
        <strong>Modo mantenimiento activo.</strong> Las escrituras están deshabilitadas para usuarios no-admin.
      </span>
      <button
        onClick={() => setDismissed(true)}
        style={{
          background: "transparent",
          border: "1px solid #713f12",
          color: "#713f12",
          padding: "0.25rem 0.5rem",
          borderRadius: "4px",
          cursor: "pointer",
        }}
      >
        Ocultar 5 min
      </button>
    </div>
  );
}
