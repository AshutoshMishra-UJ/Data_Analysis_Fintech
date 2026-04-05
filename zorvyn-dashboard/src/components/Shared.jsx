/**
 * ZORVYN Fintech — Shared UI Primitives
 */
import React from "react";

export const COLORS = {
  c1:"#6366f1",c2:"#06b6d4",c3:"#f59e0b",c4:"#10b981",
  c5:"#f43f5e",c6:"#8b5cf6",c7:"#ec4899",c8:"#3b82f6",
};

export const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div style={{
      background:"rgba(13,18,32,0.97)", border:"1px solid rgba(99,179,237,0.28)",
      borderRadius:10, padding:"10px 14px", fontSize:12,
      boxShadow:"0 8px 32px rgba(0,0,0,0.5)", minWidth:160,
    }}>
      <div style={{fontWeight:600,color:"#f0f6ff",marginBottom:6}}>{label}</div>
      {payload.map((p,i)=>(
        <div key={i} style={{display:"flex",justifyContent:"space-between",gap:16,color:"#8b9cbf",marginBottom:2}}>
          <span style={{color:p.color||"#8b9cbf"}}>{p.name}</span>
          <span style={{fontWeight:600,color:"#06b6d4"}}>
            {typeof p.value==="number" ? p.value.toLocaleString() : p.value}
          </span>
        </div>
      ))}
    </div>
  );
};

export const ChartCard = ({ title, subtitle, tag, dotColor, children, style={} }) => (
  <div className="chart-card fade-up" style={style}>
    <div className="chart-header">
      <div>
        <div className="chart-title">
          <span className="chart-title-dot" style={{background:dotColor||"#6366f1"}}/>
          {title}
        </div>
        {subtitle && <div className="chart-subtitle">{subtitle}</div>}
      </div>
      {tag && <span className="chart-tag">{tag}</span>}
    </div>
    {children}
  </div>
);

export const KpiCard = ({ icon, label, value, sub, badge, badgeType, iconBg, delay=0 }) => (
  <div className="kpi-card fade-up" style={{animationDelay:`${delay}ms`}}>
    <div className="kpi-icon" style={{background:iconBg}}>{icon}</div>
    <div className="kpi-body">
      <div className="kpi-label">{label}</div>
      <div className="kpi-value gradient-text">{value}</div>
      {sub && <div className="kpi-sub">{sub}</div>}
      {badge && <span className={`kpi-badge ${badgeType||"up"}`}>{badge}</span>}
    </div>
  </div>
);

export const SectionTitle = ({ title, sub }) => (
  <div style={{marginBottom:16,marginTop:8}}>
    <h2 style={{fontFamily:"'Space Grotesk',sans-serif",fontSize:18,fontWeight:700,
      background:"linear-gradient(135deg,#f0f6ff,#8b9cbf)",WebkitBackgroundClip:"text",
      WebkitTextFillColor:"transparent",letterSpacing:"-0.3px"}}>
      {title}
    </h2>
    {sub && <p style={{fontSize:12,color:"#4a5568",marginTop:2}}>{sub}</p>}
  </div>
);
