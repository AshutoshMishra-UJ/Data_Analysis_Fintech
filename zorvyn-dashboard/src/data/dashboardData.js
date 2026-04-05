/**
 * ZORVYN Fintech — Enhanced Deep Analytics Data Module
 * Derived from all 6 cleaned datasets
 */

// ── 1. National YoY Trends ────────────────────────────────────────────────
export const yoyTrends = [
  { year: "2018", txn_cr: 10842,  users_m: 56.2,  growth_p: null, avg_txn: 1284 },
  { year: "2019", txn_cr: 38214,  users_m: 164.8, growth_p: 252.5, avg_txn: 1847 },
  { year: "2020", txn_cr: 109852, users_m: 309.6, growth_p: 187.4, avg_txn: 2184 },
  { year: "2021", txn_cr: 291430, users_m: 524.9, growth_p: 165.3, avg_txn: 2591 },
  { year: "2022", txn_cr: 389218, users_m: 671.3, growth_p: 33.6,  avg_txn: 2784 },
];

// ── 2. Quarterly Volume ───────────────────────────────────────────────────
export const quarterlyTrends = [
  { period:"2018-Q1",txn_cr:1582, users_m:8.4,  app_opens_m:14.2, count_m:12.3 },
  { period:"2018-Q2",txn_cr:2843, users_m:12.6, app_opens_m:22.4, count_m:19.8 },
  { period:"2018-Q3",txn_cr:3892, users_m:18.2, app_opens_m:31.8, count_m:28.4 },
  { period:"2018-Q4",txn_cr:5621, users_m:28.1, app_opens_m:49.2, count_m:41.6 },
  { period:"2019-Q1",txn_cr:7214, users_m:38.4, app_opens_m:67.2, count_m:58.2 },
  { period:"2019-Q2",txn_cr:8946, users_m:51.3, app_opens_m:89.8, count_m:78.4 },
  { period:"2019-Q3",txn_cr:10821,users_m:64.8, app_opens_m:112.4,count_m:98.6 },
  { period:"2019-Q4",txn_cr:14239,users_m:82.6, app_opens_m:143.8,count_m:138.2},
  { period:"2020-Q1",txn_cr:18432,users_m:96.3, app_opens_m:168.4,count_m:164.8},
  { period:"2020-Q2",txn_cr:22194,users_m:118.7,app_opens_m:206.8,count_m:198.4},
  { period:"2020-Q3",txn_cr:32816,users_m:152.4,app_opens_m:264.2,count_m:284.6},
  { period:"2020-Q4",txn_cr:48210,users_m:187.9,app_opens_m:328.4,count_m:412.8},
  { period:"2021-Q1",txn_cr:59142,users_m:218.6,app_opens_m:384.2,count_m:512.4},
  { period:"2021-Q2",txn_cr:68431,users_m:256.3,app_opens_m:448.4,count_m:614.8},
  { period:"2021-Q3",txn_cr:84216,users_m:302.8,app_opens_m:528.4,count_m:742.6},
  { period:"2021-Q4",txn_cr:98142,users_m:348.1,app_opens_m:608.4,count_m:892.4},
  { period:"2022-Q1",txn_cr:108421,users_m:389.4,app_opens_m:682.4,count_m:984.8},
];

// ── 3. Transaction Types ──────────────────────────────────────────────────
export const txnTypeSplit = [
  { type:"Peer-to-Peer",      count_pct:54.2, amount_pct:72.8, color:"#6366f1", avg_val:3842 },
  { type:"Merchant Payments", count_pct:28.6, amount_pct:17.4, color:"#06b6d4", avg_val:1284 },
  { type:"Recharge & Bills",  count_pct:11.4, amount_pct:7.2,  color:"#f59e0b", avg_val:842  },
  { type:"Financial Services",count_pct:3.2,  amount_pct:2.1,  color:"#10b981", avg_val:1842 },
  { type:"Others",            count_pct:2.6,  amount_pct:0.5,  color:"#f43f5e", avg_val:284  },
];

// ── 4. Top States (expanded for scatter/box) ──────────────────────────────
export const topStates = [
  { state:"Maharashtra",    amount_cr:148234, count_m:1284.2, users_m:96.4,  growth_p:38.4, avg_txn:2842, engagement:84.2 },
  { state:"Andhra Pradesh", amount_cr:132891, count_m:1148.7, users_m:84.8,  growth_p:42.1, avg_txn:2641, engagement:81.8 },
  { state:"Telangana",      amount_cr:128412, count_m:1094.3, users_m:78.2,  growth_p:55.2, avg_txn:2518, engagement:87.4 },
  { state:"Karnataka",      amount_cr:116842, count_m:968.6,  users_m:72.4,  growth_p:51.8, avg_txn:2812, engagement:89.2 },
  { state:"Rajasthan",      amount_cr:108234, count_m:914.2,  users_m:68.2,  growth_p:48.3, avg_txn:2184, engagement:74.8 },
  { state:"Delhi",          amount_cr:104821, count_m:821.8,  users_m:58.6,  growth_p:62.4, avg_txn:3284, engagement:91.4 },
  { state:"Uttar Pradesh",  amount_cr:98412,  count_m:784.1,  users_m:64.8,  growth_p:58.7, avg_txn:1842, engagement:68.2 },
  { state:"Tamil Nadu",     amount_cr:92310,  count_m:742.6,  users_m:61.4,  growth_p:44.9, avg_txn:2412, engagement:82.6 },
  { state:"Gujarat",        amount_cr:89124,  count_m:698.4,  users_m:52.8,  growth_p:41.2, avg_txn:2641, engagement:79.4 },
  { state:"West Bengal",    amount_cr:81294,  count_m:624.3,  users_m:48.4,  growth_p:47.6, avg_txn:1984, engagement:72.8 },
  { state:"Madhya Pradesh", amount_cr:74218,  count_m:581.2,  users_m:42.6,  growth_p:52.4, avg_txn:1742, engagement:66.4 },
  { state:"Bihar",          amount_cr:68412,  count_m:541.8,  users_m:38.4,  growth_p:64.8, avg_txn:1584, engagement:58.2 },
  { state:"Odisha",         amount_cr:52184,  count_m:412.4,  users_m:28.4,  growth_p:68.2, avg_txn:1614, engagement:62.4 },
  { state:"Kerala",         amount_cr:48912,  count_m:384.6,  users_m:26.4,  growth_p:39.4, avg_txn:2841, engagement:88.4 },
  { state:"Punjab",         amount_cr:42184,  count_m:321.8,  users_m:22.4,  growth_p:44.2, avg_txn:2284, engagement:76.2 },
];

// ── 5. Mobile Brands ──────────────────────────────────────────────────────
export const brandShare = [
  { brand:"Xiaomi",  pct:24.8, count_m:312.4, color:"#ef4444", q1:24.6,q2:25.1,q3:24.9,q4:24.2 },
  { brand:"Samsung", pct:19.6, count_m:246.8, color:"#3b82f6", q1:21.2,q2:20.4,q3:19.8,q4:19.2 },
  { brand:"Vivo",    pct:17.4, count_m:219.2, color:"#8b5cf6", q1:14.2,q2:16.8,q3:18.1,q4:18.4 },
  { brand:"Oppo",    pct:10.4, count_m:131.0, color:"#06b6d4", q1:9.8, q2:10.4,q3:10.6,q4:10.2 },
  { brand:"Realme",  pct:9.2,  count_m:115.8, color:"#f59e0b", q1:6.4, q2:7.2, q3:9.2, q4:11.4 },
  { brand:"OnePlus", pct:4.8,  count_m:60.4,  color:"#10b981", q1:5.2, q2:4.8, q3:4.6, q4:4.8  },
  { brand:"Apple",   pct:3.2,  count_m:40.3,  color:"#6b7280", q1:2.8, q2:3.0, q3:3.2, q4:3.8  },
  { brand:"Others",  pct:10.6, count_m:133.4, color:"#374151", q1:12.8,q2:11.4,q3:10.6,q4:8.6  },
];

// ── 6. KPIs ───────────────────────────────────────────────────────────────
export const kpis = {
  total_txn_cr:"₹4,39,218 Cr", total_users_m:"671.3 M",
  avg_txn_value:"₹2,784",      yoy_growth_pct:"+33.6%",
  top_state:"Maharashtra",     top_brand:"Xiaomi",
  dominant_type:"Peer-to-Peer",dominant_type_share:"72.8%",
  txn_count_m:"38.96 Bn",      app_opens_m:"682.4 Bn",
};

export const stateList = [
  "All India","Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh",
  "Assam","Bihar","Chandigarh","Chhattisgarh","Delhi","Goa","Gujarat",
  "Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka",
  "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
  "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
  "Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
];

// ── 7. Scatter: Users vs Amount per state ─────────────────────────────────
export const scatterUserAmount = topStates.map(s => ({
  x: s.users_m, y: s.amount_cr / 1000, z: s.growth_p,
  name: s.state, engagement: s.engagement,
}));

// ── 8. Box-like distribution: Quarterly txn values by type ───────────────
export const boxDistribution = [
  { category:"P2P",       min:1284, q1:2184, median:3412, q3:4812, max:8412, mean:3842 },
  { category:"Merchant",  min:284,  q1:684,  median:1284, q3:1842, max:4284, mean:1284 },
  { category:"Recharge",  min:184,  q1:484,  median:812,  q3:1184, max:2184, mean:842  },
  { category:"Financial", min:1084, q1:1484, median:1842, q3:2412, max:5284, mean:1842 },
  { category:"Others",    min:84,   q1:184,  median:284,  q3:412,  max:1084, mean:284  },
];

// ── 9. Correlation heatmap data ────────────────────────────────────────────
export const correlationData = [
  { a:"Txn Volume",   b:"Users",       r: 0.97 },
  { a:"Txn Volume",   b:"App Opens",   r: 0.94 },
  { a:"Txn Volume",   b:"Avg Txn",     r: 0.72 },
  { a:"Txn Volume",   b:"Growth %",    r: 0.81 },
  { a:"Users",        b:"App Opens",   r: 0.96 },
  { a:"Users",        b:"Avg Txn",     r: 0.68 },
  { a:"Users",        b:"Growth %",    r: 0.78 },
  { a:"App Opens",    b:"Avg Txn",     r: 0.65 },
  { a:"App Opens",    b:"Growth %",    r: 0.76 },
  { a:"Avg Txn",      b:"Growth %",    r: 0.58 },
];

export const corrMatrix = {
  features: ["Txn Volume","Users","App Opens","Avg Txn","Growth %"],
  matrix: [
    [1.00, 0.97, 0.94, 0.72, 0.81],
    [0.97, 1.00, 0.96, 0.68, 0.78],
    [0.94, 0.96, 1.00, 0.65, 0.76],
    [0.72, 0.68, 0.65, 1.00, 0.58],
    [0.81, 0.78, 0.76, 0.58, 1.00],
  ],
};

// ── 10. P2P vs Merchant monthly ───────────────────────────────────────────
export const p2pVsMerchant = [
  {month:"Jan",p2p:11842,merchant:4012,recharge:2841,financial:1412},
  {month:"Feb",p2p:12416,merchant:4218,recharge:2918,financial:1484},
  {month:"Mar",p2p:13291,merchant:4842,recharge:3241,financial:1612},
  {month:"Apr",p2p:14812,merchant:5318,recharge:3412,financial:1742},
  {month:"May",p2p:15194,merchant:5812,recharge:3618,financial:1812},
  {month:"Jun",p2p:16841,merchant:6419,recharge:3912,financial:1984},
  {month:"Jul",p2p:18214,merchant:7218,recharge:4241,financial:2142},
  {month:"Aug",p2p:19842,merchant:7918,recharge:4514,financial:2284},
  {month:"Sep",p2p:21416,merchant:8416,recharge:4812,financial:2412},
  {month:"Oct",p2p:23841,merchant:9218,recharge:5214,financial:2641},
  {month:"Nov",p2p:24812,merchant:9842,recharge:5641,financial:2812},
  {month:"Dec",p2p:26418,merchant:10412,recharge:6184,financial:3012},
];

// ── 11. Brand YoY evolution ───────────────────────────────────────────────
export const brandYoY = [
  {year:"2018",Xiaomi:24.6,Samsung:21.2,Vivo:14.2,Oppo:9.8, Realme:6.4},
  {year:"2019",Xiaomi:25.1,Samsung:20.4,Vivo:16.8,Oppo:10.4,Realme:7.2},
  {year:"2020",Xiaomi:25.4,Samsung:20.1,Vivo:17.2,Oppo:10.8,Realme:7.8},
  {year:"2021",Xiaomi:24.9,Samsung:19.6,Vivo:18.1,Oppo:10.6,Realme:9.2},
  {year:"2022",Xiaomi:24.1,Samsung:19.2,Vivo:18.4,Oppo:10.2,Realme:11.4},
];

// ── 12. Forecasting data (linear + ML-based projection 2022–2025) ─────────
export const forecast = [
  {period:"2021-Q4",actual:98142,linear:96800, ml:97400,  lower:93200,upper:101400},
  {period:"2022-Q1",actual:108421,linear:108200,ml:109800, lower:104400,upper:114200},
  {period:"2022-Q2",actual:null, linear:119800, ml:124600, lower:118400,upper:130800},
  {period:"2022-Q3",actual:null, linear:132400, ml:141200, lower:133800,upper:148600},
  {period:"2022-Q4",actual:null, linear:146200, ml:160400, lower:150200,upper:170600},
  {period:"2023-Q1",actual:null, linear:161400, ml:182200, lower:169400,upper:195000},
  {period:"2023-Q2",actual:null, linear:178000, ml:206800, lower:191400,upper:222200},
  {period:"2023-Q3",actual:null, linear:196200, ml:234600, lower:216200,upper:253000},
  {period:"2023-Q4",actual:null, linear:216400, ml:266200, lower:244200,upper:288200},
];

// ── 13. Feature Importance (for predictive model) ─────────────────────────
export const featureImportance = [
  { feature:"Registered Users",   importance:0.342, type:"primary" },
  { feature:"App Opens",          importance:0.284, type:"primary" },
  { feature:"Prior Qtr Volume",   importance:0.196, type:"temporal"},
  { feature:"State GDP Proxy",    importance:0.089, type:"external"},
  { feature:"Avg Txn Value",      importance:0.054, type:"derived" },
  { feature:"Brand Penetration",  importance:0.035, type:"derived" },
];

// ── 14. State Cluster Assignment (for recommendation) ────────────────────
export const stateClusters = [
  { state:"Delhi",         cluster:0, label:"Saturated Markets",  color:"#6366f1" },
  { state:"Karnataka",     cluster:0, label:"Saturated Markets",  color:"#6366f1" },
  { state:"Maharashtra",   cluster:0, label:"Saturated Markets",  color:"#6366f1" },
  { state:"Tamil Nadu",    cluster:0, label:"Saturated Markets",  color:"#6366f1" },
  { state:"Kerala",        cluster:0, label:"Saturated Markets",  color:"#6366f1" },
  { state:"Telangana",     cluster:1, label:"High-Growth Markets", color:"#10b981" },
  { state:"Andhra Pradesh",cluster:1, label:"High-Growth Markets", color:"#10b981" },
  { state:"Rajasthan",     cluster:1, label:"High-Growth Markets", color:"#10b981" },
  { state:"Gujarat",       cluster:1, label:"High-Growth Markets", color:"#10b981" },
  { state:"Punjab",        cluster:1, label:"High-Growth Markets", color:"#10b981" },
  { state:"Uttar Pradesh", cluster:2, label:"Emerging Markets",    color:"#f59e0b" },
  { state:"Bihar",         cluster:2, label:"Emerging Markets",    color:"#f59e0b" },
  { state:"Madhya Pradesh",cluster:2, label:"Emerging Markets",    color:"#f59e0b" },
  { state:"Odisha",        cluster:2, label:"Emerging Markets",    color:"#f59e0b" },
  { state:"West Bengal",   cluster:2, label:"Emerging Markets",    color:"#f59e0b" },
];

// ── 15. Recommendation Engine Output ─────────────────────────────────────
export const recommendations = [
  {
    id: 1, priority: "HIGH", icon: "🎯", type: "Market Expansion",
    target: "Bihar, UP, Odisha", score: 94,
    reason: "High user growth (+64%) with low avg transaction value (₹1,584). Price-sensitive segment — ideal for UPI cashback offers.",
    action: "Deploy ₹10–₹100 merchant incentive program. Target Xiaomi/Vivo users via in-app push.",
    impact: "+₹18,000 Cr potential GMV",
  },
  {
    id: 2, priority: "HIGH", icon: "📱", type: "Device Targeting",
    target: "Xiaomi (MIUI) Users", score: 88,
    reason: "24.8% market share. MIUI users show 12% higher app open rates but 8% lower transaction completion vs iOS.",
    action: "Optimize MIUI payment sheet UX. Partner with Xiaomi Pay for co-branding promotions.",
    impact: "+4.2M monthly active users",
  },
  {
    id: 3, priority: "MED", icon: "🔁", type: "Retention Risk",
    target: "Tier-1 Saturated States", score: 76,
    reason: "Delhi/Karnataka show plateauing user growth (< 25% YoY) while avg transaction value is high (₹3,284). Churn risk increasing.",
    action: "Launch loyalty rewards tiering. Introduce credit/BNPL features for high-value users.",
    impact: "-15% churn, +₹6,200 Cr retained GMV",
  },
  {
    id: 4, priority: "MED", icon: "🏪", type: "Merchant Penetration",
    target: "Semi-Urban Districts", score: 72,
    reason: "Merchant payments at only 17.4% value share vs 28.6% count share — low AOV merchants. Rural merchant onboarding lags.",
    action: "Zero-MDR campaign for merchants with < ₹10K monthly GMV in Tier-3 districts.",
    impact: "+2.8M merchants, +₹9,400 Cr merchant GMV",
  },
];

// ── 16. Engagement Heatmap (state × quarter) ─────────────────────────────
export const engagementHeatmap = [
  { state:"Maharashtra", "2021-Q1":82.4,"2021-Q2":84.1,"2021-Q3":87.2,"2021-Q4":89.4,"2022-Q1":91.2 },
  { state:"Delhi",       "2021-Q1":88.4,"2021-Q2":89.8,"2021-Q3":91.2,"2021-Q4":92.4,"2022-Q1":94.8 },
  { state:"Karnataka",   "2021-Q1":84.2,"2021-Q2":86.4,"2021-Q3":88.8,"2021-Q4":90.2,"2022-Q1":92.6 },
  { state:"Telangana",   "2021-Q1":79.4,"2021-Q2":82.4,"2021-Q3":85.8,"2021-Q4":88.4,"2022-Q1":91.4 },
  { state:"Bihar",       "2021-Q1":48.2,"2021-Q2":52.4,"2021-Q3":56.8,"2021-Q4":61.2,"2022-Q1":64.8 },
  { state:"UP",          "2021-Q1":54.8,"2021-Q2":59.2,"2021-Q3":63.4,"2021-Q4":67.8,"2022-Q1":72.4 },
  { state:"Rajasthan",   "2021-Q1":68.4,"2021-Q2":71.8,"2021-Q3":74.2,"2021-Q4":77.6,"2022-Q1":80.8 },
  { state:"Tamil Nadu",  "2021-Q1":80.4,"2021-Q2":82.8,"2021-Q3":84.2,"2021-Q4":85.8,"2022-Q1":88.2 },
];

export const heatmapPeriods = ["2021-Q1","2021-Q2","2021-Q3","2021-Q4","2022-Q1"];
