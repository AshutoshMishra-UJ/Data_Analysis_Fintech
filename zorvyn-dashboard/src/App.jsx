import React, { useState, useMemo } from "react";
import {
  AreaChart, Area, BarChart, Bar, PieChart, Pie, Cell,
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, Legend, RadarChart, Radar,
  PolarGrid, PolarAngleAxis, PolarRadiusAxis
} from "recharts";

import {
  yoyTrends, quarterlyTrends, txnTypeSplit,
  topStates, brandShare, kpis, stateList,
  p2pVsMerchant, brandYoY,
} from "./data/dashboardData";

// ═══════════════════════════════════════════════════════
// Custom Tooltip
// ═══════════════════════════════════════════════════════
const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div className="custom-tooltip">
      <div className="custom-tooltip-label">{label}</div>
      {payload.map((p, i) => (
        <div key={i} className="custom-tooltip-row">
          <span style={{ color: p.color || "#8b9cbf" }}>{p.name}</span>
          <span className="custom-tooltip-value">
            {typeof p.value === "number" ? p.value.toLocaleString() : p.value}
          </span>
        </div>
      ))}
    </div>
  );
};

// ═══════════════════════════════════════════════════════
// KPI Card
// ═══════════════════════════════════════════════════════
const KpiCard = ({ icon, label, value, sub, badge, badgeType, iconBg, delay = 0 }) => (
  <div className="kpi-card fade-up" style={{ animationDelay: `${delay}ms` }}>
    <div className="kpi-icon" style={{ background: iconBg }}>{icon}</div>
    <div className="kpi-body">
      <div className="kpi-label">{label}</div>
      <div className="kpi-value gradient-text">{value}</div>
      {sub && <div className="kpi-sub">{sub}</div>}
      {badge && (
        <span className={`kpi-badge ${badgeType || "up"}`}>{badge}</span>
      )}
    </div>
  </div>
);

// ═══════════════════════════════════════════════════════
// Chart Cards
// ═══════════════════════════════════════════════════════
const ChartCard = ({ title, subtitle, tag, dotColor, children }) => (
  <div className="chart-card fade-up">
    <div className="chart-header">
      <div>
        <div className="chart-title">
          <span className="chart-title-dot" style={{ background: dotColor || "#6366f1" }} />
          {title}
        </div>
        {subtitle && <div className="chart-subtitle">{subtitle}</div>}
      </div>
      {tag && <span className="chart-tag">{tag}</span>}
    </div>
    {children}
  </div>
);

// ═══════════════════════════════════════════════════════
// Main App
// ═══════════════════════════════════════════════════════
export default function App() {
  const [activeYear, setActiveYear]   = useState("All");
  const [activeState, setActiveState] = useState("All India");
  const [activeQ, setActiveQ]         = useState("All");

  const years = ["All", "2018", "2019", "2020", "2021", "2022"];
  const quarters = ["All", "Q1", "Q2", "Q3", "Q4"];

  // Filter quarterly trend based on year selection
  const filteredQuarterly = useMemo(() => {
    if (activeYear === "All") return quarterlyTrends;
    return quarterlyTrends.filter(d => d.period.startsWith(activeYear));
  }, [activeYear]);

  // Max value for ranking bars
  const maxAmount = Math.max(...topStates.map(s => s.amount_cr));

  return (
    <div className="app-shell">
      {/* Animated Grid Background */}
      <div className="grid-bg" />

      {/* ─── Header ─────────────────────────────────────── */}
      <header className="header">
        <div className="header-brand">
          <div className="brand-logo">Z</div>
          <div>
            <div className="brand-name">ZORVYN <span>Fintech</span></div>
          </div>
          <span className="header-badge">Analytics Intelligence</span>
        </div>

        <div className="header-live">
          <div className="live-dot" />
          <span>India Digital Payments · 2018 – 2022</span>
        </div>
      </header>

      {/* ─── Page ──────────────────────────────────────── */}
      <main className="page">

        {/* ── FILTER BAR ─────────────────────────────── */}
        <div className="filter-bar">
          <span className="filter-label">Year</span>
          <div className="filter-group">
            {years.map(y => (
              <button key={y} className={`filter-chip ${activeYear === y ? "active" : ""}`}
                onClick={() => setActiveYear(y)}>{y}</button>
            ))}
          </div>
          <div className="filter-divider" />
          <span className="filter-label">Quarter</span>
          <div className="filter-group">
            {quarters.map(q => (
              <button key={q} className={`filter-chip ${activeQ === q ? "active" : ""}`}
                onClick={() => setActiveQ(q)}>{q}</button>
            ))}
          </div>
          <div className="filter-divider" />
          <span className="filter-label">State</span>
          <select className="filter-select" value={activeState}
            onChange={e => setActiveState(e.target.value)}>
            {stateList.map(s => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>

        {/* ── KPI CARDS ──────────────────────────────── */}
        <div className="kpi-grid">
          <KpiCard delay={0}
            icon="💸" label="Total Transaction Volume"
            value={kpis.total_txn_cr}
            sub="Across all states · 2022 Q1"
            badge="↑ 33.6% YoY" badgeType="up"
            iconBg="linear-gradient(135deg,rgba(99,102,241,.25),rgba(6,182,212,.15))"
          />
          <KpiCard delay={80}
            icon="👥" label="Registered Users"
            value={kpis.total_users_m}
            sub="Cumulative unique users"
            badge="↑ 28.1% YoY" badgeType="up"
            iconBg="linear-gradient(135deg,rgba(16,185,129,.25),rgba(6,182,212,.15))"
          />
          <KpiCard delay={160}
            icon="📊" label="Total Transactions"
            value={kpis.txn_count_m}
            sub="Transaction count · 2022 Q1"
            badge="Peer-to-Peer Dominant" badgeType="up"
            iconBg="linear-gradient(135deg,rgba(245,158,11,.25),rgba(244,63,94,.1))"
          />
          <KpiCard delay={240}
            icon="📱" label="Avg Transaction Value"
            value={kpis.avg_txn_value}
            sub="Per transaction average"
            badge="#1 Brand: Xiaomi" badgeType="up"
            iconBg="linear-gradient(135deg,rgba(139,92,246,.25),rgba(236,72,153,.1))"
          />
        </div>

        {/* ── SECTION 1: Area + Donut ───────────────── */}
        <div className="chart-grid chart-grid-3" style={{ marginBottom: 20 }}>

          <ChartCard
            title="Quarterly Transaction Trends"
            subtitle={`₹ Crore volume over time · ${activeYear === "All" ? "2018–2022" : activeYear}`}
            tag="TEMPORAL" dotColor="#6366f1"
          >
            <ResponsiveContainer width="100%" height={280}>
              <AreaChart data={filteredQuarterly} margin={{ top: 4, right: 8, bottom: 0, left: 0 }}>
                <defs>
                  <linearGradient id="grad1" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#6366f1" stopOpacity={0.4} />
                    <stop offset="100%" stopColor="#6366f1" stopOpacity={0} />
                  </linearGradient>
                  <linearGradient id="grad2" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#06b6d4" stopOpacity={0.3} />
                    <stop offset="100%" stopColor="#06b6d4" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                <XAxis dataKey="period" tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} />
                <YAxis tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} axisLine={false}
                  tickFormatter={v => `${(v/1000).toFixed(0)}K`} />
                <Tooltip content={<CustomTooltip />} />
                <Area type="monotone" dataKey="txn_cr" name="Vol (₹ Cr)"
                  stroke="#6366f1" strokeWidth={2.5} fill="url(#grad1)" dot={false} />
                <Area type="monotone" dataKey="users_m" name="Users (M)"
                  stroke="#06b6d4" strokeWidth={2} fill="url(#grad2)" dot={false} />
              </AreaChart>
            </ResponsiveContainer>
            <div className="legend">
              {[["#6366f1","Transaction Volume (₹ Cr)"],["#06b6d4","Registered Users (M)"]].map(([c,l])=>(
                <div key={l} className="legend-item"><span className="legend-dot" style={{background:c}}/>{l}</div>
              ))}
            </div>
          </ChartCard>

          <ChartCard
            title="Transaction Type Split"
            subtitle="By value share (2022)"
            tag="% SHARE" dotColor="#06b6d4"
          >
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie data={txnTypeSplit} dataKey="amount_pct" nameKey="type"
                  cx="50%" cy="50%" innerRadius={52} outerRadius={80}
                  strokeWidth={2} stroke="rgba(8,11,20,0.8)">
                  {txnTypeSplit.map((d, i) => <Cell key={i} fill={d.color} />)}
                </Pie>
                <Tooltip formatter={(v) => `${v}%`} content={<CustomTooltip />} />
              </PieChart>
            </ResponsiveContainer>
            <div className="legend" style={{ marginTop: 0 }}>
              {txnTypeSplit.map(d => (
                <div key={d.type} className="legend-item">
                  <span className="legend-dot" style={{ background: d.color }} />
                  {d.type} <span style={{ color: "#6366f1", fontWeight: 600, marginLeft: 4 }}>{d.amount_pct}%</span>
                </div>
              ))}
            </div>
          </ChartCard>
        </div>

        {/* ── SECTION 2: State Ranking + Line Dual ───── */}
        <div className="chart-grid chart-grid-2" style={{ marginBottom: 20 }}>

          <ChartCard
            title="Top 10 States by Transaction Value"
            subtitle="All-India cumulative (₹ Crore)"
            tag="GEO RANKING" dotColor="#f59e0b"
          >
            <table className="rank-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>State</th>
                  <th style={{ width: 80 }}>Bar</th>
                  <th style={{ textAlign: "right" }}>₹ Crore</th>
                  <th style={{ textAlign: "right" }}>Growth</th>
                </tr>
              </thead>
              <tbody>
                {topStates.map((s, i) => (
                  <tr key={s.state}>
                    <td className="rank-num">{i + 1}</td>
                    <td className="rank-state">{s.state}</td>
                    <td className="rank-bar-cell">
                      <div className="rank-bar-track">
                        <div className="rank-bar-fill"
                          style={{ width: `${(s.amount_cr / maxAmount) * 100}%` }} />
                      </div>
                    </td>
                    <td className="rank-amount">{s.amount_cr.toLocaleString()}</td>
                    <td style={{ textAlign: "right" }}>
                      <span className="kpi-badge up" style={{ marginTop: 0 }}>+{s.growth_p}%</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </ChartCard>

          <ChartCard
            title="P2P vs Merchant Payments (2021)"
            subtitle="Monthly transaction count (₹ Crore)"
            tag="TREND" dotColor="#10b981"
          >
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={p2pVsMerchant} margin={{ top: 4, right: 8, bottom: 0, left: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                <XAxis dataKey="month" tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} />
                <YAxis tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} axisLine={false}
                  tickFormatter={v => `${(v / 1000).toFixed(0)}K`} />
                <Tooltip content={<CustomTooltip />} />
                <Line type="monotone" dataKey="p2p"      name="Peer-to-Peer"      stroke="#6366f1" strokeWidth={2.5} dot={false} />
                <Line type="monotone" dataKey="merchant" name="Merchant Payments"  stroke="#f59e0b" strokeWidth={2}   dot={false} />
              </LineChart>
            </ResponsiveContainer>
            <div className="legend">
              {[["#6366f1","Peer-to-Peer (₹ Cr)"],["#f59e0b","Merchant (₹ Cr)"]].map(([c,l])=>(
                <div key={l} className="legend-item"><span className="legend-dot" style={{background:c}}/>{l}</div>
              ))}
            </div>
          </ChartCard>
        </div>

        {/* ── SECTION 3: Brand Bar + Brand Line ──────── */}
        <div className="chart-grid chart-grid-2" style={{ marginBottom: 20 }}>

          <ChartCard
            title="Mobile Brand Market Share"
            subtitle="User distribution across all states (2022 Q1)"
            tag="BRANDS" dotColor="#8b5cf6"
          >
            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={brandShare} layout="vertical"
                margin={{ top: 4, right: 8, bottom: 0, left: 48 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" horizontal={false} />
                <XAxis type="number" tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false}
                  tickFormatter={v => `${v}%`} />
                <YAxis type="category" dataKey="brand" tick={{ fill: "#8b9cbf", fontSize: 12 }} tickLine={false} width={56} />
                <Tooltip content={<CustomTooltip />} formatter={(v) => `${v}%`} />
                <Bar dataKey="pct" name="Market Share %" radius={[0, 6, 6, 0]}>
                  {brandShare.map((d, i) => <Cell key={i} fill={d.color} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </ChartCard>

          <ChartCard
            title="Brand Share Evolution (2018–2022)"
            subtitle="% of users by year for top 5 brands"
            tag="EVOLUTION" dotColor="#ec4899"
          >
            <ResponsiveContainer width="100%" height={260}>
              <LineChart data={brandYoY} margin={{ top: 4, right: 8, bottom: 0, left: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                <XAxis dataKey="year" tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} />
                <YAxis tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} axisLine={false}
                  tickFormatter={v => `${v}%`} />
                <Tooltip content={<CustomTooltip />} formatter={(v) => `${v}%`} />
                {["Xiaomi","Samsung","Vivo","Oppo","Realme"].map((b, i) => {
                  const colors = ["#ef4444","#3b82f6","#8b5cf6","#06b6d4","#f59e0b"];
                  return <Line key={b} type="monotone" dataKey={b} name={b}
                    stroke={colors[i]} strokeWidth={2} dot={false} />;
                })}
              </LineChart>
            </ResponsiveContainer>
            <div className="legend">
              {[["#ef4444","Xiaomi"],["#3b82f6","Samsung"],["#8b5cf6","Vivo"],["#06b6d4","Oppo"],["#f59e0b","Realme"]].map(([c,l])=>(
                <div key={l} className="legend-item"><span className="legend-dot" style={{background:c}}/>{l}</div>
              ))}
            </div>
          </ChartCard>
        </div>

        {/* ── SECTION 4: YoY Growth Bar ───────────────── */}
        <div className="chart-grid chart-grid-full" style={{ marginBottom: 20 }}>
          <ChartCard
            title="Year-over-Year National Transaction Growth"
            subtitle="Total digital payment volume (₹ Crore) across India"
            tag="YoY GROWTH" dotColor="#f43f5e"
          >
            <ResponsiveContainer width="100%" height={240}>
              <BarChart data={yoyTrends} margin={{ top: 4, right: 24, bottom: 0, left: 0 }}>
                <defs>
                  <linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#6366f1" stopOpacity={1} />
                    <stop offset="100%" stopColor="#06b6d4" stopOpacity={1} />
                  </linearGradient>
                  <linearGradient id="barGrad2" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#f59e0b" stopOpacity={1} />
                    <stop offset="100%" stopColor="#f43f5e" stopOpacity={1} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                <XAxis dataKey="year" tick={{ fill: "#4a5568", fontSize: 11 }} tickLine={false} />
                <YAxis yAxisId="left" tick={{ fill: "#4a5568", fontSize: 10 }} tickLine={false} axisLine={false}
                  tickFormatter={v => `${(v / 1000).toFixed(0)}K`} />
                <YAxis yAxisId="right" orientation="right" tick={{ fill: "#4a5568", fontSize: 10 }}
                  tickLine={false} axisLine={false} tickFormatter={v => `${v}M`} />
                <Tooltip content={<CustomTooltip />} />
                <Bar yAxisId="left" dataKey="txn_cr"  name="Volume (₹ Cr)" fill="url(#barGrad)"  radius={[6,6,0,0]} />
                <Bar yAxisId="right" dataKey="users_m" name="Users (M)"     fill="url(#barGrad2)" radius={[6,6,0,0]} />
              </BarChart>
            </ResponsiveContainer>
            <div className="legend">
              {[["url(#barGrad)","Transaction Volume (₹ Cr)"],["url(#barGrad2)","Registered Users (M)"]].map(([c,l])=>(
                <div key={l} className="legend-item">
                  <span className="legend-dot" style={{background:c==="url(#barGrad)"?"#6366f1":"#f59e0b"}}/>
                  {l}
                </div>
              ))}
            </div>
          </ChartCard>
        </div>

        {/* ── SECTION 5: Radar + Insights Box ────────── */}
        <div className="chart-grid chart-grid-2" style={{ marginBottom: 20 }}>

          <ChartCard
            title="Transaction Category Radar"
            subtitle="Count % vs Value % comparison"
            tag="RADAR" dotColor="#f59e0b"
          >
            <ResponsiveContainer width="100%" height={260}>
              <RadarChart data={txnTypeSplit}>
                <PolarGrid stroke="rgba(255,255,255,0.06)" />
                <PolarAngleAxis dataKey="type" tick={{ fill: "#8b9cbf", fontSize: 10 }} />
                <PolarRadiusAxis angle={30} domain={[0, 80]} tick={{ fill: "#4a5568", fontSize: 9 }} />
                <Radar name="Count %" dataKey="count_pct" stroke="#6366f1" fill="#6366f1" fillOpacity={0.25} strokeWidth={2} />
                <Radar name="Value %" dataKey="amount_pct" stroke="#f59e0b" fill="#f59e0b" fillOpacity={0.2}  strokeWidth={2} />
                <Tooltip content={<CustomTooltip />} />
              </RadarChart>
            </ResponsiveContainer>
            <div className="legend">
              {[["#6366f1","Transaction Count %"],["#f59e0b","Transaction Value %"]].map(([c,l])=>(
                <div key={l} className="legend-item"><span className="legend-dot" style={{background:c}}/>{l}</div>
              ))}
            </div>
          </ChartCard>

          {/* Insights Panel */}
          <div className="chart-card fade-up" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            <div className="chart-header" style={{ marginBottom: 4 }}>
              <div className="chart-title">
                <span className="chart-title-dot" style={{ background: "#10b981" }} />
                🔍 ZORVYN Key Insights
              </div>
              <span className="chart-tag">STRATEGIC</span>
            </div>

            {[
              { color: "#6366f1", icon: "📈", title: "Explosive P2P Growth",
                body: "Peer-to-peer payments dominate at 72.8% of total value. UP, Bihar & West Bengal show the fastest 12-month CAGR — prime expansion targets." },
              { color: "#06b6d4", icon: "📱", title: "Xiaomi Dominates FinTech Entry",
                body: "Xiaomi leads with ~25% market share consistently from 2018–2022, making it the single largest device segment. ZORVYN should tailor UX for MIUI." },
              { color: "#f59e0b", icon: "🌏", title: "Tier-2 City Surge",
                body: "Districts outside state capitals (e.g. Papum Pare in Arunachal) show 300%+ YoY growth. ZORVYN's next push should target rural + semi-urban nodes." },
              { color: "#10b981", icon: "🏆", title: "Maharashtra Leads, South Rising",
                body: "Maharashtra holds #1 in volume but Telangana (+55%), Karnataka (+52%) are growing fastest — signaling Southeast India as the high-priority market." },
            ].map((ins, i) => (
              <div key={i} style={{
                background: "rgba(255,255,255,0.02)", border: "1px solid rgba(255,255,255,0.05)",
                borderRadius: 12, padding: "12px 14px",
                borderLeft: `3px solid ${ins.color}`,
              }}>
                <div style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 4 }}>
                  <span style={{ fontSize: 14 }}>{ins.icon}</span>
                  <span style={{ fontWeight: 600, fontSize: 12, color: ins.color }}>{ins.title}</span>
                </div>
                <p style={{ fontSize: 11, color: "#8b9cbf", lineHeight: 1.6, margin: 0 }}>{ins.body}</p>
              </div>
            ))}
          </div>
        </div>

      </main>

      {/* ─── Footer ──────────────────────────────────── */}
      <footer className="footer">
        © 2024 ZORVYN Fintech Intelligence Platform · Dataset: India Digital Payments (2018–2022) ·
        Built with React + Recharts
      </footer>
    </div>
  );
}
