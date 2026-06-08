"use client";

import { type FC } from "react";

interface BarSeries {
  label: string;
  value: number;
  color: string;
}

interface BarChartProps {
  data: Array<{ label: string; values: BarSeries[] }>;
  /** Y-axis unit suffix (e.g. "€" or "c"). */
  unit?: string;
  height?: number;
  /** Max value (auto-calculated if omitted). */
  max?: number;
}

/**
 * A dependency-free SVG bar chart. Each data row can stack multiple series
 * side-by-side. We avoid Recharts to keep the bundle small and the chart
 * rendering predictable in tests.
 */
export const BarChart: FC<BarChartProps> = ({
  data,
  unit = "",
  height = 220,
  max,
}) => {
  if (data.length === 0) {
    return (
      <div
        className="flex h-32 items-center justify-center text-xs text-[var(--text-muted)]"
        style={{ height }}
      >
        Sin datos
      </div>
    );
  }

  const computedMax =
    max ??
    Math.max(
      1,
      ...data.flatMap((row) => row.values.map((v) => v.value)),
    );

  // Use a sensible axis max rounded up to a "nice" number.
  const axisMax = Math.ceil(computedMax * 1.1);

  const rowCount = data.length;
  const barWidth = Math.min(36, 100 / Math.max(rowCount, 1));
  const chartWidth = 600;
  const chartHeight = height - 40; // leave room for labels
  const chartLeft = 40;
  const chartTop = 10;

  return (
    <svg
      viewBox={`0 0 ${chartWidth} ${height}`}
      className="w-full"
      style={{ maxHeight: height }}
      role="img"
    >
      {/* Y-axis grid lines */}
      {[0, 0.25, 0.5, 0.75, 1].map((t, i) => {
        const y = chartTop + chartHeight * (1 - t);
        return (
          <g key={i}>
            <line
              x1={chartLeft}
              x2={chartWidth - 8}
              y1={y}
              y2={y}
              stroke="var(--border-soft)"
              strokeWidth={1}
              strokeDasharray={i === 0 ? "0" : "2,2"}
            />
            <text
              x={chartLeft - 4}
              y={y + 3}
              textAnchor="end"
              fontSize={9}
              fill="var(--text-muted)"
              fontFamily="var(--font-mono)"
            >
              {Math.round(axisMax * t).toLocaleString("es-ES")}
              {unit}
            </text>
          </g>
        );
      })}

      {/* Bars */}
      {data.map((row, rowIdx) => {
        const groupWidth = (chartWidth - chartLeft - 12) / rowCount;
        const groupX = chartLeft + groupWidth * rowIdx + groupWidth / 2;
        const seriesCount = row.values.length;
        const seriesSpacing = 2;

        return (
          <g key={row.label}>
            {row.values.map((v, sIdx) => {
              const totalSeriesWidth = barWidth * seriesCount + seriesSpacing * (seriesCount - 1);
              const seriesX = groupX - totalSeriesWidth / 2 + (barWidth + seriesSpacing) * sIdx;
              const h = axisMax > 0 ? (v.value / axisMax) * chartHeight : 0;
              const y = chartTop + chartHeight - h;
              return (
                <rect
                  key={v.label}
                  x={seriesX}
                  y={y}
                  width={barWidth}
                  height={Math.max(0, h)}
                  fill={v.color}
                  rx={3}
                />
              );
            })}
            <text
              x={groupX}
              y={chartTop + chartHeight + 14}
              textAnchor="middle"
              fontSize={10}
              fill="var(--text-muted)"
            >
              {row.label}
            </text>
          </g>
        );
      })}
    </svg>
  );
};

interface LegendItem {
  label: string;
  color: string;
}

interface ChartLegendProps {
  items: LegendItem[];
}

export const ChartLegend: FC<ChartLegendProps> = ({ items }) => {
  return (
    <div className="flex flex-wrap items-center gap-3 text-[11px] text-[var(--text-muted)]">
      {items.map((item) => (
        <span key={item.label} className="flex items-center gap-1.5">
          <span
            className="h-2.5 w-2.5 rounded-full"
            style={{ background: item.color }}
          />
          {item.label}
        </span>
      ))}
    </div>
  );
};
