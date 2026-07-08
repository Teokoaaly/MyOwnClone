"use client";

import { useState, useEffect } from "react";
import { PageHeader } from "@/components/admin/PageHeader";

interface IngestionStatus {
  total_chunks: number;
  chunks_with_embedding: number;
  chunks_pending_embedding: number;
  total_sources: number;
  sources_by_status: Record<string, number>;
  embedding_model: string;
  embedding_dimensions: number;
}

export default function MonitoringPage() {
  const [data, setData] = useState<IngestionStatus | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/admin/ingestion-status");
      if (!res.ok) throw new Error(`Error ${res.status}`);
      const json = await res.json();
      setData(json);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  if (loading && !data) {
    return (
      <div className="space-y-6">
        <PageHeader title="System Monitoring" subtitle="Real-time system status" />
        <div className="card p-6">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="space-y-6">
        <PageHeader title="System Monitoring" subtitle="Real-time system status" />
        <div className="card p-6 text-red-500">Error: {error}</div>
      </div>
    );
  }

  const pct = data
    ? Math.round((data.chunks_with_embedding / Math.max(data.total_chunks, 1)) * 100)
    : 0;

  return (
    <div className="space-y-6">
      <PageHeader
        title="System Monitoring"
        subtitle="Real-time ingestion and embedding status"
        actions={
          <button onClick={fetchData} className="btn-secondary text-xs">
            Refresh
          </button>
        }
      />

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
        <div className="card p-4">
          <div className="stat-label">Total Chunks</div>
          <div className="stat-value mt-1">{data?.total_chunks ?? 0}</div>
        </div>
        <div className="card p-4">
          <div className="stat-label">With Embedding</div>
          <div className="stat-value mt-1 text-green-600">{data?.chunks_with_embedding ?? 0}</div>
        </div>
        <div className="card p-4">
          <div className="stat-label">Pending Embedding</div>
          <div className="stat-value mt-1 text-yellow-600">{data?.chunks_pending_embedding ?? 0}</div>
        </div>
        <div className="card p-4">
          <div className="stat-label">Total Sources</div>
          <div className="stat-value mt-1">{data?.total_sources ?? 0}</div>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
        <div className="card p-4">
          <div className="stat-label">Embedding Model</div>
          <div className="mt-2 font-mono text-sm">{data?.embedding_model ?? "N/A"}</div>
          <div className="text-xs text-gray-500">{data?.embedding_dimensions ?? 0} dimensions</div>
        </div>
        <div className="card p-4">
          <div className="stat-label">Sources by Status</div>
          <div className="mt-2 space-y-1">
            {Object.entries(data?.sources_by_status ?? {}).map(([status, count]) => (
              <div key={status} className="flex justify-between text-sm">
                <span className="capitalize">{status}</span>
                <span className="font-mono">{count}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="card p-4">
        <div className="stat-label">Embedding Progress</div>
        <div className="mt-2">
          <div className="h-4 w-full overflow-hidden rounded-full bg-gray-200">
            <div
              className="h-full bg-green-500 transition-all duration-500"
              style={{ width: `${pct}%` }}
            />
          </div>
          <div className="mt-1 text-xs text-gray-500">
            {data?.chunks_with_embedding ?? 0} / {data?.total_chunks ?? 0} chunks embedded ({pct}%)
          </div>
        </div>
      </div>
    </div>
  );
}
