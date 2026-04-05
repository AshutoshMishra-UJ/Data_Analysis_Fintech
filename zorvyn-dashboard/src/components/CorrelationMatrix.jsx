/**
 * ZORVYN — Correlation Matrix Heatmap
 * Visual: color-coded r² grid
 */
import React from "react";
import { corrMatrix } from "../data/dashboardData";
import { ChartCard } from "./Shared";

const getRColor = (r) => {
  const abs = Math.abs(r);
  if (abs >= 0.9) return r > 0 ? "#6366f1" : "#f43f5e";
  if (abs >= 0.75) return r > 0 ? "#8b5cf6" : "#f87171";
  if (abs >= 0.6)  return r > 0 ? "#06b6d4" : "#fb923c";
  return "#1e2840";
};

const getTextColor = (r) => Math.abs(r) > 0.7 ? "#f0f6ff" : "#8b9cbf";

export default function CorrelationMatrix() {
  const { features, matrix } = corrMatrix;
  const size = features.length;

  return (
    <ChartCard
      title="Feature Correlation Matrix"
      subtitle="Pearson r coefficients — predictive power between key metrics"
      tag="ANALYTICS" dotColor="#8b5cf6"
    >
      <div style={{ overflowX: "auto" }}>
        <table style={{ width: "100%", borderCollapse: "separate", borderSpacing: 3, marginTop: 4 }}>
          <thead>
            <tr>
              <th style={{ width: 110, textAlign: "left", fontSize: 10, color: "#4a5568", paddingBottom: 6 }}></th>
              {features.map(f => (
                <th key={f} style={{
                  fontSize: 9, fontWeight: 700, color: "#8b9cbf",
                  textAlign: "center", letterSpacing: "0.5px", paddingBottom: 6,
                  maxWidth: 70, wordBreak: "break-word",
                }}>
                  {f.split(" ").map((w, i) => <span key={i}>{w}<br /></span>)}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {matrix.map((row, ri) => (
              <tr key={ri}>
                <td style={{
                  fontSize: 10, color: "#8b9cbf", fontWeight: 600,
                  paddingRight: 8, whiteSpace: "nowrap",
                }}>
                  {features[ri]}
                </td>
                {row.map((val, ci) => (
                  <td key={ci} style={{
                    background: getRColor(val),
                    color: getTextColor(val),
                    textAlign: "center",
                    fontSize: 11, fontWeight: 700,
                    padding: "8px 4px",
                    borderRadius: 6,
                    minWidth: 48,
                    transition: "transform 0.15s",
                    cursor: "default",
                    border: ri === ci ? "2px solid rgba(255,255,255,0.15)" : "none",
                    opacity: ri === ci ? 0.7 : 1,
                  }}
                    title={`${features[ri]} × ${features[ci]}: r = ${val.toFixed(2)}`}
                  >
                    {val.toFixed(2)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Legend */}
      <div style={{ display: "flex", gap: 12, marginTop: 12, flexWrap: "wrap" }}>
        {[
          { c: "#6366f1", label: "Strong +ve (≥ 0.9)" },
          { c: "#06b6d4", label: "Moderate +ve (≥ 0.6)" },
          { c: "#f43f5e", label: "Strong –ve" },
          { c: "#1e2840", label: "Weak / None" },
        ].map(({ c, label }) => (
          <div key={label} style={{ display: "flex", alignItems: "center", gap: 6 }}>
            <span style={{ width: 12, height: 12, borderRadius: 3, background: c, display: "inline-block" }} />
            <span style={{ fontSize: 10, color: "#4a5568" }}>{label}</span>
          </div>
        ))}
      </div>

      <p style={{ marginTop: 10, fontSize: 11, color: "#4a5568", lineHeight: 1.6 }}>
        <strong style={{ color: "#8b5cf6" }}>Analyst Note:</strong> App Opens and Registered Users show r=0.96 correlation —
        strong evidence that platform engagement drives transaction conversion. This pair forms the <strong style={{ color: "#06b6d4" }}>co-feature backbone</strong> of any predictive model built on this dataset.
      </p>
    </ChartCard>
  );
}
