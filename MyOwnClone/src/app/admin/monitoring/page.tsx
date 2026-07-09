"use client";

import { useState, useEffect } from "react";
import { PageHeader } from "@/components/admin/PageHeader";

interface ServiceDetail {
  status: string;
  latency_ms: number | null;
  details: Record<string, any>;
  error: string | null;
}

interface SystemStatus {
  overall_status: string;
  timestamp: string;
  summary: { total: number; healthy: number; degraded: number; down: number };
  services: Record<string, ServiceDetail>;
}

function StatusDot({ status }: { status: string }) {
  const color = status === "healthy" ? "bg-green-500" : status === "degraded" ? "bg-yellow-500" : status === "down" ? "bg-red-500" : "bg-gray-400";
  return <span className={`inline-block h-2 w-2 rounded-full ${color}`} />;
}

function Row({ label, value }: { label: string; value: any }) {
  return (
    <div className="flex justify-between text-sm py-0.5">
      <span className="text-[var(--text-muted)]">{label}</span>
      <span className="font-mono text-[var(--text-primary)]">{value ?? "—"}</span>
    </div>
  );
}

function ServiceCard({ name, svc }: { name: string; svc: ServiceDetail }) {
  const d = svc.details || {};
  return (
    <div className="card p-4">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-sm font-semibold capitalize">{name}</h3>
        <div className="flex items-center gap-1.5">
          <StatusDot status={svc.status} />
          <span className="text-xs">{svc.status}</span>
          {svc.latency_ms !== null && <span className="text-xs text-[var(--text-muted)]">{svc.latency_ms}ms</span>}
        </div>
      </div>
      <div className="space-y-0.5">
        {name === "os" && <>
          <Row label="CPU" value={`${d.cpu_usage_percent}%`} />
          <Row label="RAM" value={`${d.ram_used_mb}/${d.ram_total_mb} MB (${d.ram_usage_percent}%)`} />
          <Row label="Swap" value={`${d.swap_used_mb}/${d.swap_total_mb} MB`} />
          <Row label="Disk" value={`${d.disk_used_gb}/${d.disk_total_gb} GB (${d.disk_usage_percent}%)`} />
          <Row label="Load" value={`${d.load_1m} / ${d.load_5m} / ${d.load_15m}`} />
          <Row label="Uptime" value={`${d.uptime_days}d`} />
        </>}
        {name === "database" && <>
          <Row label="Connections" value={`${d.active_connections}/${d.max_connections}`} />
          <Row label="Size" value={d.database_size} />
          <Row label="Tables" value={d.table_count} />
          <Row label="Cache Hit" value={`${d.cache_hit_ratio}%`} />
          <Row label="Slow" value={d.slow_queries} />
        </>}
        {name === "redis" && <>
          <Row label="Memory" value={`${d.used_memory_mb} MB`} />
          <Row label="Clients" value={d.connected_clients} />
          <Row label="Commands" value={d.total_commands?.toLocaleString()} />
          <Row label="Hit Rate" value={`${d.hit_rate}%`} />
        </>}
        {name === "ollama" && <>
          <Row label="Models" value={d.loaded_models} />
          {d.models?.map((m: any) => <Row key={m.name} label={m.name} value={`${m.size_gb} GB`} />)}
          <Row label="Embed" value={`${d.embedding_latency_ms}ms / ${d.embedding_dimensions}d`} />
        </>}
        {name === "worker" && <>
          <Row label="Queue" value={d.queue_depth} />
          <Row label="Failed" value={d.failed_jobs} />
          <Row label="Workers" value={d.registered_workers} />
        </>}
        {name === "api" && <>
          <Row label="Memory" value={`${d.memory_mb} MB`} />
          <Row label="CPU" value={`${d.cpu_percent}%`} />
          <Row label="Threads" value={d.threads} />
          <Row label="FDs" value={d.open_fds} />
        </>}
      </div>
      {svc.error && <div className="mt-2 text-xs text-red-500">{svc.error}</div>}
    </div>
  );
}

export default function MonitoringPage() {
  const [data, setData] = useState<SystemStatus | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/admin/system-status");
      if (!res.ok) throw new Error(`Error ${res.status}`);
      setData(await res.json());
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 15000);
    return () => clearInterval(interval);
  }, []);

  if (loading && !data) {
    return (
      <div className="space-y-6">
        <PageHeader title="System Monitoring" subtitle="Loading..." />
        <div className="card p-6">Connecting...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="space-y-6">
        <PageHeader title="System Monitoring" subtitle="Error" />
        <div className="card p-6 text-red-500">{error}</div>
      </div>
    );
  }

  const s = data?.summary;
  const color = data?.overall_status === "healthy" ? "text-green-600" : data?.overall_status === "degraded" ? "text-yellow-600" : "text-red-600";

  return (
    <div className="space-y-6">
      <PageHeader
        title="System Monitoring"
        subtitle={data?.timestamp ? new Date(data.timestamp).toLocaleString() : ""}
        actions={
          <div className="flex items-center gap-3">
            <span className={`text-sm font-bold uppercase ${color}`}>{data?.overall_status}</span>
            <button onClick={fetchData} className="btn-secondary text-xs">Refresh</button>
          </div>
        }
      />

      <div className="grid grid-cols-4 gap-3">
        <div className="card p-3 text-center"><div className="text-lg font-bold text-green-600">{s?.healthy}</div><div className="text-xs text-[var(--text-muted)]">Healthy</div></div>
        <div className="card p-3 text-center"><div className="text-lg font-bold text-yellow-600">{s?.degraded}</div><div className="text-xs text-[var(--text-muted)]">Degraded</div></div>
        <div className="card p-3 text-center"><div className="text-lg font-bold text-red-600">{s?.down}</div><div className="text-xs text-[var(--text-muted)]">Down</div></div>
        <div className="card p-3 text-center"><div className="text-lg font-bold">{s?.total}</div><div className="text-xs text-[var(--text-muted)]">Total</div></div>
      </div>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
        {Object.entries(data?.services ?? {}).map(([name, svc]) => (
          <ServiceCard key={name} name={name} svc={svc} />
        ))}
      </div>
    </div>
  );
}
