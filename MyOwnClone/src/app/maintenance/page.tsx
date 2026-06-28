import { redirect } from "next/navigation";

interface MaintenanceStatus {
  active: boolean;
  message: string;
}

async function getMaintenanceStatus(): Promise<MaintenanceStatus> {
  try {
    const base = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:5001";
    const res = await fetch(`${base}/console/api/myownclone/maintenance/status`, {
      cache: "no-store",
    });
    if (!res.ok) {
      return { active: true, message: "Sistema en mantenimiento" };
    }
    return await res.json();
  } catch {
    return { active: true, message: "Sistema en mantenimiento" };
  }
}

export default async function MaintenancePage() {
  const status = await getMaintenanceStatus();
  if (!status.active) {
    redirect("/");
  }
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "2rem",
        textAlign: "center",
        backgroundColor: "#fef3c7",
      }}
    >
      <h1 style={{ fontSize: "2.5rem", marginBottom: "1rem", color: "#92400e" }}>
        Sistema en mantenimiento
      </h1>
      <p style={{ fontSize: "1.25rem", color: "#78350f", maxWidth: "32rem" }}>
        {status.message || "Estamos haciendo cambios para mejorar tu experiencia. Vuelve pronto."}
      </p>
      <p style={{ marginTop: "2rem", fontSize: "0.875rem", color: "#a16207" }}>
        Si necesitas ayuda urgente, contacta a soporte.
      </p>
    </main>
  );
}
