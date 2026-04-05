/**
 * ZORVYN — Scatter Plot: Users vs Transaction Volume
 * Bubble size = YoY Growth %, Color = cluster
 * Relevance: Identifies high-opportunity state clusters for expansion
 */
import React, { useState } from "react";
import {
  ScatterChart, Scatter, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Cell, ReferenceLine,
} from "recharts";
import { scatterUserAmount, stateClusters } from "../data/dashboardData";
import { ChartCard } from "./Shared";

const clusterColors = { 0: "#6366f1", 1: "#10b981", 2: "#f59e0b" };
const clusterLabels = { 0: "Saturated", 1: "High-Growth", 2: "Emerging" };

const getCluster = (name) => {
  const found = stateClusters.find(s => s.state === name);
  return found ? found.cluster : 2;
};

const BubbleTooltip = ({ active, payload }) => {
  if (!active || !payload?.length) return null;
  const d = payload[0]?.payload;
  if (!d) return null;
  const cluster = getCluster(d.name);
  return (
    <div style={{
      background: "rgba(13,18,32,0.97)", border: `1px solid ${clusterColors[cluster]}44`,
      borderRadius: 10, padding: "10px 14px", fontSize: 12,
      boxShadow: "0 8px 32px rgba(0,0,0,0.5)",
    }}>
      <div style={{ fontWeight: 700, color: "#f0f6ff", marginBottom: 6 }}>{d.name}</div>
      <div style={{ color: "#8b9cbf" }}>Registered Users: <span style={{ color: "#06b6d4", fontWeight: 600 }}>{d.x.toFixed(1)}M</span></div>
      <div style={{ color: "#8b9cbf" }}>Txn Volume: <span style={{ color: "#06b6d4", fontWeight: 600 }}>₹{d.y.toFixed(0)}K Cr</span></div>
      <div style={{ color: "#8b9cbf" }}>YoY Growth: <span style={{ color: "#10b981", fontWeight: 600 }}>+{d.z}%</span></div>
      <div style={{ color: "#8b9cbf" }}>Engagement: <span style={{ color: "#f59e0b", fontWeight: 600 }}>{d.engagement}%</span></div>
      <div style={{ marginTop: 6 }}>
        <span style={{
          background: `${clusterColors[cluster]}22`, color: clusterColors[cluster],
          padding: "2px 8px", borderRadius: 999, fontSize: 10, fontWeight: 700,
        }}>
          {clusterLabels[cluster]} Market
        </span>
      </div>
    </div>
  );
};

export default function ScatterPlot() {
  const [highlight, setHighlight] = useState(null);

  return (
    <ChartCard
      title="State Opportunity Scatter Analysis"
      subtitle="Users (M) vs Transaction Volume — bubble size = YoY growth"
      tag="SCATTER · CLUSTERING" dotColor="#10b981"
    >
      {/* Cluster legend */}
      <div style={{ display: "flex", gap: 16, marginBottom: 12, flexWrap: "wrap" }}>
        {Object.entries(clusterColors).map(([k, c]) => (
          <div key={k}
            style={{ display: "flex", alignItems: "center", gap: 6, cursor: "pointer",
              opacity: highlight === null || highlight === +k ? 1 : 0.4, transition: "opacity 0.2s" }}
            onMouseEnter={() => setHighlight(+k)} onMouseLeave={() => setHighlight(null)}>
            <span style={{ width: 10, height: 10, borderRadius: "50%", background: c, display: "inline-block" }} />
            <span style={{ fontSize: 11, color: "#8b9cbf" }}>{clusterLabels[k]} Markets</span>
          </div>
        ))}
        <span style={{ fontSize: 10, color: "#4a5568", marginLeft: "auto" }}>Bubble size ∝ YoY Growth %</span>
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <ScatterChart margin={{ top: 4, right: 24, bottom: 8, left: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
          <XAxis type="number" dataKey="x" name="Users (M)"
            tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false}
            label={{ value: "Registered Users (M)", fill: "#4a5568", fontSize: 10, offset: -4, position: "insideBottom" }}
          />
          <YAxis type="number" dataKey="y" name="Txn Vol (₹K Cr)"
            tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} axisLine={false}
            label={{ value: "Txn Vol (₹K Cr)", fill: "#4a5568", fontSize: 10, angle: -90, position: "insideLeft" }}
          />
          <Tooltip content={<BubbleTooltip />} />
          <ReferenceLine x={60} stroke="rgba(99,102,241,0.2)" strokeDasharray="4 4" />
          <ReferenceLine y={100} stroke="rgba(99,102,241,0.2)" strokeDasharray="4 4" />
          <Scatter data={scatterUserAmount} name="States">
            {scatterUserAmount.map((d, i) => {
              const cluster = getCluster(d.name);
              const col = clusterColors[cluster];
              const r = 6 + (d.z / 12);
              const faded = highlight !== null && highlight !== cluster;
              return (
                <Cell key={i}
                  fill={col} fillOpacity={faded ? 0.15 : 0.75}
                  stroke={col} strokeWidth={faded ? 0 : 1.5}
                  r={r}
                />
              );
            })}
          </Scatter>
        </ScatterChart>
      </ResponsiveContainer>

      {/* Quadrant labels */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginTop: 12 }}>
        {[
          { icon: "⚠️", label: "Low Users, High Volume", desc: "Niche premium markets (e.g., Kerala, Delhi)", color: "#f59e0b" },
          { icon: "🏆", label: "High Users, High Volume", desc: "Core revenue states – retain & upsell", color: "#6366f1" },
          { icon: "🌱", label: "Low Users, Low Volume", desc: "Greenfield expansion opportunity", color: "#10b981" },
          { icon: "📈", label: "High Users, Low Volume", desc: "Conversion optimization needed (Avg Txn low)", color: "#06b6d4" },
        ].map(q => (
          <div key={q.label} style={{
            background: "rgba(255,255,255,0.02)", borderRadius: 8, padding: "8px 10px",
            borderLeft: `2px solid ${q.color}33`,
          }}>
            <div style={{ fontSize: 11, fontWeight: 600, color: q.color }}>{q.icon} {q.label}</div>
            <div style={{ fontSize: 10, color: "#4a5568", marginTop: 2 }}>{q.desc}</div>
          </div>
        ))}
      </div>
    </ChartCard>
  );
}
