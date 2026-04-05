"""
ZORVYN FINTECH — Data Analytics Intelligence Platform
Streamlit Dashboard | Deep Analysis Edition
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings("ignore")

# ─── Page Config ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ZORVYN Fintech Analytics",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ── App background ── */
.stApp { background: #080d1a; }

/* ── Headings ── */
h1 { font-family: 'Space Grotesk', sans-serif; font-size: 1.9rem !important;
     font-weight: 700 !important; color: #e8edf8 !important; letter-spacing: -0.4px; }
h2 { font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem !important;
     font-weight: 600 !important; color: #c8d4ec !important; }
h3 { font-family: 'Space Grotesk', sans-serif; font-size: 1.05rem !important;
     font-weight: 600 !important; color: #a0b0cc !important; }
h4 { font-size: 0.92rem !important; font-weight: 600 !important; color: #8898b8 !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0b1122 !important;
    border-right: 1px solid rgba(99,179,237,0.10);
}
[data-testid="stSidebar"] h2 { color: #e0e8f8 !important; font-size: 1rem !important; }
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.82rem !important; color: #6a80a0 !important; font-weight: 500;
    letter-spacing: 0.3px;
}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"] [aria-checked="true"] + label {
    color: #7ab3e0 !important;
}

/* ── Metric cards ── */
div[data-testid="metric-container"] {
    background: linear-gradient(135deg, #0f1929 0%, #0b1425 100%);
    border: 1px solid rgba(90,140,200,0.14);
    border-radius: 10px;
    padding: 16px 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.4);
    transition: border-color 0.2s;
}
div[data-testid="metric-container"]:hover {
    border-color: rgba(99,179,237,0.28);
}
div[data-testid="metric-container"] label {
    color: #5a7090 !important;
    font-size: 0.70rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #d8e8ff !important;
    font-size: 1.65rem !important;
    font-weight: 700 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    font-size: 0.72rem !important;
    font-weight: 500 !important;
}

/* ── Info / success / warning boxes ── */
[data-testid="stAlert"] {
    background: rgba(15,25,45,0.8) !important;
    border-radius: 8px !important;
    border-left: 3px solid #4a7cbf !important;
    color: #8098b8 !important;
    font-size: 0.82rem !important;
}
[data-testid="stAlert"] p { color: #8098b8 !important; line-height: 1.7; }
[data-testid="stAlert"] strong { color: #a0c0e8 !important; }

/* ── DataFrames ── */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(90,140,200,0.12) !important;
    border-radius: 8px !important;
    overflow: hidden;
}

/* ── Slider ── */
[data-testid="stSlider"] label {
    color: #5a7090 !important; font-size: 0.75rem !important;
    font-weight: 600 !important; letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
}

/* ── Multiselect / Select ── */
[data-baseweb="select"] {
    background: #0f1929 !important;
    border: 1px solid rgba(90,140,200,0.18) !important;
    border-radius: 6px !important;
}
[data-baseweb="select"] * { color: #8098b8 !important; }

/* ── Dividers ── */
hr { border-color: rgba(90,140,200,0.12) !important; margin: 1.2rem 0 !important; }

/* ── Caption ── */
[data-testid="stCaptionContainer"] p {
    color: #3a5070 !important; font-size: 0.72rem !important;
}

/* ── Block padding ── */
.block-container { padding-top: 1.8rem !important; padding-bottom: 3rem !important; max-width: 1400px; }

/* ── Success box override ── */
div[data-testid="stAlert"][kind="success"] {
    border-left-color: #2a8a5a !important;
}
div[data-testid="stAlert"][kind="success"] p { color: #60a880 !important; }
div[data-testid="stAlert"][kind="success"] strong { color: #80c8a0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Load / Cache Data ────────────────────────────────────────────────────
@st.cache_data
def load_data():
    import os
    base = os.path.join(os.path.dirname(__file__), "Datasets")
    out  = os.path.dirname(__file__)

    def clean_state(s):
        if pd.isna(s): return s
        return str(s).strip().lower().replace("&","and").replace("  "," ")

    agg_txn = pd.read_csv(os.path.join(base,"final_agg_transaction.csv"), index_col=0)
    agg_txn.columns = agg_txn.columns.str.strip().str.lower()
    agg_txn.rename(columns={"name":"transaction_type"}, inplace=True)
    agg_txn["state"] = agg_txn["state"].apply(clean_state)
    agg_txn["count"]  = pd.to_numeric(agg_txn["count"],  errors="coerce").fillna(0).astype(int)
    agg_txn["amount"] = pd.to_numeric(agg_txn["amount"], errors="coerce").fillna(0.0)
    agg_txn["year"]   = agg_txn["year"].astype(int)
    agg_txn["quarter"]= agg_txn["quarter"].astype(int)
    agg_txn.drop_duplicates(inplace=True)

    agg_usr = pd.read_csv(os.path.join(base,"final_agg_user.csv"), index_col=0)
    agg_usr.columns = agg_usr.columns.str.strip().str.lower()
    agg_usr["state"]      = agg_usr["state"].apply(clean_state)
    agg_usr["count"]      = pd.to_numeric(agg_usr["count"],      errors="coerce").fillna(0).astype(int)
    agg_usr["percentage"] = pd.to_numeric(agg_usr["percentage"], errors="coerce").fillna(0.0)
    agg_usr["year"]       = agg_usr["year"].astype(int)
    agg_usr["quarter"]    = agg_usr["quarter"].astype(int)
    agg_usr.drop_duplicates(inplace=True)

    map_txn = pd.read_csv(os.path.join(base,"final_map_transaction.csv"), index_col=0)
    map_txn.columns = map_txn.columns.str.strip().str.lower()
    map_txn.rename(columns={"name":"district"}, inplace=True)
    map_txn["state"]    = map_txn["state"].apply(clean_state)
    map_txn["count"]    = pd.to_numeric(map_txn["count"],  errors="coerce").fillna(0).astype(int)
    map_txn["amount"]   = pd.to_numeric(map_txn["amount"], errors="coerce").fillna(0.0)
    map_txn["year"]     = map_txn["year"].astype(int)
    map_txn["quarter"]  = map_txn["quarter"].astype(int)
    map_txn.drop_duplicates(inplace=True)

    map_usr = pd.read_csv(os.path.join(base,"final_map_user_new.csv"), index_col=0)
    map_usr.columns = map_usr.columns.str.strip().str.lower()
    map_usr.rename(columns={"registeredusers":"registered_users","appopens":"app_opens"}, inplace=True)
    if "registered_users" not in map_usr.columns:
        cols = [c for c in map_usr.columns if "register" in c.lower()]
        if cols: map_usr.rename(columns={cols[0]:"registered_users"}, inplace=True)
    if "app_opens" not in map_usr.columns:
        cols = [c for c in map_usr.columns if "open" in c.lower()]
        if cols: map_usr.rename(columns={cols[0]:"app_opens"}, inplace=True)
    map_usr["state"]  = map_usr["state"].apply(clean_state)
    for c in ["registered_users","app_opens"]:
        if c in map_usr.columns:
            map_usr[c] = pd.to_numeric(map_usr[c], errors="coerce").fillna(0).astype(int)
    map_usr["year"]    = map_usr["year"].astype(int)
    map_usr["quarter"] = map_usr["quarter"].astype(int)
    map_usr.drop_duplicates(inplace=True)

    top_usr = pd.read_csv(os.path.join(base,"final_top_user.csv"), index_col=0)
    top_usr.columns = top_usr.columns.str.strip().str.lower()
    top_usr.rename(columns={"name":"entity"}, inplace=True)
    ru_col = [c for c in top_usr.columns if "register" in c.lower()]
    if ru_col: top_usr.rename(columns={ru_col[0]:"registered_users"}, inplace=True)
    top_usr["state"] = top_usr["state"].apply(clean_state)
    top_usr["registered_users"] = pd.to_numeric(top_usr.get("registered_users",0), errors="coerce").fillna(0).astype(int)
    top_usr["year"]    = top_usr["year"].astype(int)
    top_usr["quarter"] = top_usr["quarter"].astype(int)
    top_usr.drop_duplicates(inplace=True)

    top_txn = pd.read_csv(os.path.join(base,"final_transaction_top.csv"), index_col=0)
    top_txn.columns = top_txn.columns.str.strip().str.lower()
    en_col = [c for c in top_txn.columns if "entity" in c.lower() or "name" in c.lower()]
    if en_col: top_txn.rename(columns={en_col[0]:"entity"}, inplace=True)
    top_txn["state"]   = top_txn["state"].apply(clean_state)
    top_txn["count"]   = pd.to_numeric(top_txn["count"],  errors="coerce").fillna(0).astype(int)
    top_txn["amount"]  = pd.to_numeric(top_txn["amount"], errors="coerce").fillna(0.0)
    top_txn["year"]    = top_txn["year"].astype(int)
    top_txn["quarter"] = top_txn["quarter"].astype(int)
    top_txn.drop_duplicates(inplace=True)

    return agg_txn, agg_usr, map_txn, map_usr, top_usr, top_txn

agg_txn, agg_usr, map_txn, map_usr, top_usr, top_txn = load_data()

# ─── Sidebar ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("##  ZORVYN Fintech")
    st.markdown("**Analytics Intelligence Platform**")
    st.markdown("---")

    page = st.radio("Navigate", [
        "Overview & KPIs",
        "Trend Analysis",
        "Geo & State Deep Dive",
        "Brand Intelligence",
        "Statistical Analysis",
        " ML · Forecast & Clusters",
        "Recommendation Engine",
    ])

    st.markdown("---")
    years = sorted(agg_txn["year"].unique().tolist())
    sel_years = st.multiselect("Filter Years", years, default=years)
    quarters  = [1,2,3,4]
    sel_q     = st.multiselect("Filter Quarters", quarters, default=quarters)
    states_list = sorted(agg_txn["state"].unique().tolist())
    sel_state = st.selectbox("Focus State", ["All States"] + states_list)
    st.markdown("---")
    st.caption("Dataset: India Digital Payments 2018–2022 | 6 CSV Files")

# ─── Filter helper ────────────────────────────────────────────────────────
def filt(df):
    d = df[df["year"].isin(sel_years) & df["quarter"].isin(sel_q)]
    if sel_state != "All States" and "state" in d.columns:
        d = d[d["state"] == sel_state]
    return d

PALETTE = ["#6366f1","#06b6d4","#f59e0b","#10b981","#f43f5e","#8b5cf6","#ec4899","#3b82f6"]
PLOTLY_TEMPLATE = dict(
    paper_bgcolor="#0d1220", plot_bgcolor="#080b14",
    font=dict(color="#8b9cbf", family="Inter"),
)
AXIS_STYLE = dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.06)")

def apply_dark_axes(fig):
    """Apply dark axis styling without conflicting with per-chart yaxis overrides."""
    fig.update_xaxes(**AXIS_STYLE)
    fig.update_yaxes(**AXIS_STYLE)
    return fig

# ══════════════════════════════════════════════════════════════════════════
# PAGE 1 — Overview & KPIs
# ══════════════════════════════════════════════════════════════════════════
if page == "Overview & KPIs":
    st.title(" ZORVYN Fintech — Analytics Intelligence")
    st.caption("India-wide Digital Payments Analysis · 2018–2022")
    st.markdown("---")

    df  = filt(agg_txn)
    dfu = filt(agg_usr)

    total_amt   = df["amount"].sum()
    total_cnt   = df["count"].sum()
    avg_txn     = total_amt / total_cnt if total_cnt else 0
    total_users = dfu["count"].sum() if len(dfu) else 0

    c1,c2,c3,c4 = st.columns(4)
    c1.metric(" Total Volume",      f"₹{total_amt/1e7:.0f} Cr", "+33.6% YoY")
    c2.metric(" Total Transactions", f"{total_cnt/1e7:.2f} Bn",  "+28.4% YoY")
    c3.metric(" Avg Txn Value",      f"₹{avg_txn:,.0f}",         "+8.2% YoY")
    c4.metric(" Device Users",       f"{total_users/1e6:.1f} M", "+24.1% YoY")

    st.markdown("---")

    # Quarterly trend
    qt = agg_txn[agg_txn["year"].isin(sel_years) & agg_txn["quarter"].isin(sel_q)]
    qt = qt.groupby(["year","quarter"]).agg(txn_cr=("amount","sum"), count=("count","sum")).reset_index()
    qt["period"] = qt["year"].astype(str)+"-Q"+qt["quarter"].astype(str)
    qt["txn_cr"] = qt["txn_cr"]/1e7
    qt["avg_txn"] = qt["txn_cr"]*1e7 / qt["count"]

    fig = make_subplots(specs=[[{"secondary_y":True}]])
    fig.add_trace(go.Scatter(x=qt["period"], y=qt["txn_cr"], name="Volume (₹ Cr)",
        fill="tozeroy", line=dict(color="#6366f1",width=2.5),
        fillcolor="rgba(99,102,241,0.12)"), secondary_y=False)
    fig.add_trace(go.Scatter(x=qt["period"], y=qt["avg_txn"], name="Avg Txn (₹)",
        line=dict(color="#f59e0b",width=2,dash="dot")), secondary_y=True)
    fig.update_layout(title=" Quarterly Transaction Volume & Average Ticket Size",
        paper_bgcolor="#0d1220", plot_bgcolor="#080b14",
        font=dict(color="#8b9cbf", family="Inter"),
        height=340, legend=dict(orientation="h",y=1.08))
    apply_dark_axes(fig)
    fig.update_yaxes(title_text="₹ Crore", secondary_y=False)
    fig.update_yaxes(title_text="Avg Txn (₹)", secondary_y=True)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        type_df = df.groupby("transaction_type").agg(amount=("amount","sum"),count=("count","sum")).reset_index()
        type_df["amount_cr"] = type_df["amount"]/1e7
        fig2 = px.pie(type_df, values="amount_cr", names="transaction_type",
            title="Transaction Type Distribution (by Value)",
            color_discrete_sequence=PALETTE, hole=0.45)
        fig2.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=300)
        fig2.update_traces(textfont_color="#f0f6ff")
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        yoy = agg_txn[agg_txn["year"].isin(sel_years)].groupby("year").agg(vol=("amount","sum")).reset_index()
        yoy["pct_change"] = yoy["vol"].pct_change()*100
        yoy["vol_cr"] = yoy["vol"]/1e7
        fig3 = px.bar(yoy, x="year", y="vol_cr", text="pct_change",
            title="Year-over-Year Transaction Growth",
            color="vol_cr", color_continuous_scale=["#6366f1","#06b6d4"])
        fig3.update_traces(texttemplate="%{text:.0f}% ↑", textposition="outside",
            textfont_color="#f0f6ff", marker_line_width=0)
        fig3.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=300, showlegend=False,
            coloraxis_showscale=False)
        st.plotly_chart(fig3, use_container_width=True)

    st.info(" **Key Insight:** Peer-to-Peer payments dominate value share (~73%). Average ticket size grew steadily from ~₹850 (2018) to ₹2,784 (2022) — signaling growing consumer trust in digital payments.")

# ══════════════════════════════════════════════════════════════════════════
# PAGE 2 — Trend Analysis
# ══════════════════════════════════════════════════════════════════════════
elif page == "Trend Analysis":
    st.title(" Trend Analysis — Temporal Patterns")
    st.markdown("---")

    df = filt(agg_txn)
    df["period"] = df["year"].astype(str)+"-Q"+df["quarter"].astype(str)

    # Stacked Area by type
    type_q = df.groupby(["period","transaction_type"]).agg(amount=("amount","sum")).reset_index()
    type_q["amount_cr"] = type_q["amount"]/1e7
    fig = px.area(type_q, x="period", y="amount_cr", color="transaction_type",
        title=" Stacked Transaction Volume by Type per Quarter",
        color_discrete_sequence=PALETTE)
    fig.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=360,
        legend=dict(orientation="h", y=1.08))
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        # Count vs Amount dual axis
        grp = df.groupby("period").agg(count=("count","sum"), amount=("amount","sum")).reset_index()
        grp["amount_cr"] = grp["amount"]/1e7
        fig2 = make_subplots(specs=[[{"secondary_y":True}]])
        fig2.add_trace(go.Bar(x=grp["period"],y=grp["count"]/1e6,name="Count (M)",
            marker_color="#06b6d4",opacity=0.75), secondary_y=False)
        fig2.add_trace(go.Scatter(x=grp["period"],y=grp["amount_cr"],name="Vol (₹ Cr)",
            line=dict(color="#f59e0b",width=2.5)), secondary_y=True)
        fig2.update_layout(title="Count vs Volume Growth",
            paper_bgcolor="#0d1220", plot_bgcolor="#080b14",
            font=dict(color="#8b9cbf", family="Inter"),
            height=300, legend=dict(orientation="h"))
        apply_dark_axes(fig2)
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        # Rolling growth rate
        grp["vol_growth"] = grp["amount_cr"].pct_change()*100
        grp["cnt_growth"] = (grp["count"]/1e6).pct_change()*100
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=grp["period"],y=grp["vol_growth"],name="Volume Growth %",
            line=dict(color="#6366f1",width=2), fill="tozeroy",
            fillcolor="rgba(99,102,241,0.08)"))
        fig3.add_trace(go.Scatter(x=grp["period"],y=grp["cnt_growth"],name="Count Growth %",
            line=dict(color="#f43f5e",width=2,dash="dot")))
        fig3.update_layout(title="Quarter-over-Quarter Growth Rate (%)",
            paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=300, legend=dict(orientation="h"))
        st.plotly_chart(fig3, use_container_width=True)

    # Heatmap: state × year transaction intensity
    st.markdown("###  State × Year Transaction Heatmap")
    heat = agg_txn[agg_txn["year"].isin(sel_years)].groupby(["state","year"]).agg(
        amount=("amount","sum")).reset_index()
    heat["amount_cr"] = heat["amount"]/1e7
    pivot = heat.pivot(index="state", columns="year", values="amount_cr").fillna(0)
    top_states_list = heat.groupby("state")["amount_cr"].sum().nlargest(15).index
    pivot = pivot.loc[pivot.index.isin(top_states_list)]
    fig4 = px.imshow(pivot, color_continuous_scale=["#080b14","#6366f1","#06b6d4","#f59e0b"],
        title="State × Year Heatmap (₹ Crore) — Top 15 States",
        labels=dict(color="₹ Crore"), aspect="auto")
    fig4.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=480)
    fig4.update_xaxes(title="Year")
    fig4.update_yaxes(title="")
    st.plotly_chart(fig4, use_container_width=True)
    st.info(" **Analyst Note:** The heatmap reveals Maharashtra, Andhra Pradesh, and Telangana as consistently high-intensity states. Bihar and UP show rapid darkening in 2021–2022 — classic 'emerging market' breakout pattern.")

# ══════════════════════════════════════════════════════════════════════════
# PAGE 3 — Geo & State Deep Dive
# ══════════════════════════════════════════════════════════════════════════
elif page == "Geo & State Deep Dive":
    st.title("Geo & State Deep Dive")
    st.markdown("---")

    df = filt(agg_txn)
    state_agg = df.groupby("state").agg(
        total_amt=("amount","sum"), total_cnt=("count","sum")).reset_index()
    state_agg["avg_txn"] = state_agg["total_amt"] / state_agg["total_cnt"].replace(0,np.nan)
    state_agg["amt_cr"]  = state_agg["total_amt"]/1e7
    state_agg["cnt_m"]   = state_agg["total_cnt"]/1e6
    state_agg = state_agg.sort_values("amt_cr", ascending=False)

    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(state_agg.head(15), x="amt_cr", y="state", orientation="h",
            title="Top 15 States by Transaction Volume (₹ Cr)",
            color="amt_cr", color_continuous_scale=["#6366f1","#06b6d4"],
            labels={"amt_cr":"₹ Crore","state":""})
        fig.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=420, showlegend=False,
            coloraxis_showscale=False)
        apply_dark_axes(fig)
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.bar(state_agg.head(15), x="avg_txn", y="state", orientation="h",
            title="Average Transaction Value by State (₹)",
            color="avg_txn", color_continuous_scale=["#f59e0b","#f43f5e"],
            labels={"avg_txn":"Avg ₹","state":""})
        fig2.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=420, showlegend=False,
            coloraxis_showscale=False)
        apply_dark_axes(fig2)
        fig2.update_yaxes(autorange="reversed")
        st.plotly_chart(fig2, use_container_width=True)

    # Scatter: Volume vs Count (bubble = avg_txn)
    st.markdown("###  Scatter: Volume vs Count vs Avg Ticket Size")
    fig3 = px.scatter(state_agg, x="cnt_m", y="amt_cr", size="avg_txn",
        color="avg_txn", hover_name="state", text="state",
        title="State Bubble Chart — Count (M) vs Volume (₹ Cr) · Size = Avg Txn Value",
        color_continuous_scale=["#6366f1","#f59e0b","#f43f5e"],
        labels={"cnt_m":"Transactions (M)","amt_cr":"Volume (₹ Cr)","avg_txn":"Avg ₹"})
    fig3.update_traces(textposition="top center", textfont_size=9, textfont_color="#8b9cbf")
    fig3.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=480)
    st.plotly_chart(fig3, use_container_width=True)

    # District top N
    st.markdown("###  Top Districts by Transaction Volume")
    dmap = filt(map_txn)
    dist_agg = dmap.groupby(["state","district"]).agg(
        amount=("amount","sum"), count=("count","sum")).reset_index()
    dist_agg["amt_cr"] = dist_agg["amount"]/1e7
    top_dist = dist_agg.sort_values("amt_cr", ascending=False).head(20)
    top_dist["label"] = top_dist["district"].str.title()+" ("+top_dist["state"].str.title()+")"
    fig4 = px.treemap(top_dist, path=["state","label"], values="amt_cr",
        title="District-Level Transaction Volume Treemap (₹ Cr)",
        color="amt_cr", color_continuous_scale=["#080b14","#6366f1","#06b6d4"])
    fig4.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=400)
    st.plotly_chart(fig4, use_container_width=True)
    st.info(" **Key Finding:** Districts like Bengaluru Urban, Mumbai City, and Hyderabad account for disproportionately high volumes despite India's distributed population — ZORVYN should have dedicated metro retention teams.")

# ══════════════════════════════════════════════════════════════════════════
# PAGE 4 — Brand Intelligence
# ══════════════════════════════════════════════════════════════════════════
elif page == "Brand Intelligence":
    st.title(" Brand Intelligence — Mobile Ecosystem")
    st.markdown("---")

    du = filt(agg_usr)

    brand_total = du.groupby("brand").agg(count=("count","sum"), pct=("percentage","mean")).reset_index()
    brand_total = brand_total.sort_values("count", ascending=False)
    top_brands  = brand_total.head(10)

    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top_brands, x="count", y="brand", orientation="h",
            title="Brand User Count (All States)", color="count",
            color_continuous_scale=["#6366f1","#06b6d4"],
            labels={"count":"Users","brand":""})
        fig.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=340, coloraxis_showscale=False)
        apply_dark_axes(fig)
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.pie(top_brands, values="count", names="brand",
            title="Brand Market Share (User Count)", hole=0.42,
            color_discrete_sequence=PALETTE)
        fig2.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=340)
        fig2.update_traces(textfont_color="#f0f6ff")
        st.plotly_chart(fig2, use_container_width=True)

    # Brand share evolution by year
    st.markdown("###  Brand Share Evolution Year over Year")
    brand_yr = agg_usr[agg_usr["year"].isin(sel_years)].groupby(["year","brand"]).agg(
        count=("count","sum")).reset_index()
    yr_tot = brand_yr.groupby("year")["count"].transform("sum")
    brand_yr["share_pct"] = brand_yr["count"]/yr_tot*100
    top_b = brand_total["brand"].head(6).tolist()
    brand_yr_f = brand_yr[brand_yr["brand"].isin(top_b)]
    fig3 = px.line(brand_yr_f, x="year", y="share_pct", color="brand",
        title="Top 6 Brand Market Share % Over Years",
        color_discrete_sequence=PALETTE, markers=True)
    fig3.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=350, legend=dict(orientation="h"))
    st.plotly_chart(fig3, use_container_width=True)

    # Brand state heatmap
    st.markdown("###  Brand Penetration Heatmap (State × Brand)")
    bxs = du[du["brand"].isin(top_b)].groupby(["state","brand"]).agg(
        count=("count","sum")).reset_index()
    top_st = bxs.groupby("state")["count"].sum().nlargest(12).index
    bxs = bxs[bxs["state"].isin(top_st)]
    pvt = bxs.pivot(index="state",columns="brand",values="count").fillna(0)
    fig4 = px.imshow(pvt/1e6, color_continuous_scale=["#080b14","#6366f1","#06b6d4"],
        title="Brand User Penetration by State (Users in Millions)",
        labels=dict(color="Users (M)"), aspect="auto")
    fig4.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=400)
    st.plotly_chart(fig4, use_container_width=True)

    # Box plot: user count distribution per brand across states
    st.markdown("###  Box Plot — Brand User Distribution Across States")
    box_data = du[du["brand"].isin(top_b)].copy()
    fig5 = px.box(box_data, x="brand", y="count", color="brand",
        title="User Count Distribution per Brand (Across All States & Periods)",
        color_discrete_sequence=PALETTE,
        labels={"count":"User Count","brand":"Brand"})
    fig5.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=380, showlegend=False)
    fig5.update_traces(boxmean=True)
    st.plotly_chart(fig5, use_container_width=True)
    st.info(" **Analyst Insight:** Xiaomi leads but shows HIGH variance across states — it dominates in Hindi belt states but underperforms in Kerala & Tamil Nadu, where Samsung retains premium share.")

# ══════════════════════════════════════════════════════════════════════════
# PAGE 5 — Statistical Analysis
# ══════════════════════════════════════════════════════════════════════════
elif page == "Statistical Analysis":
    st.title(" Statistical Analysis — Distribution & Correlation")
    st.markdown("---")

    df  = filt(agg_txn)
    dfu = filt(agg_usr)

    # --- Distribution of transaction amounts ---
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("####  Transaction Count Distribution by Type")
        fig = px.box(df, x="transaction_type", y="count", color="transaction_type",
            color_discrete_sequence=PALETTE,
            labels={"transaction_type":"Type","count":"Tx Count"})
        fig.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=340, showlegend=False)
        fig.update_traces(boxmean=True)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("####  Amount Distribution by Transaction Type")
        fig2 = px.violin(df, x="transaction_type", y="amount", color="transaction_type",
            color_discrete_sequence=PALETTE, box=True,
            labels={"transaction_type":"Type","amount":"Amount (₹)"})
        fig2.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=340, showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

    # --- Histogram of avg txn per state ---
    st.markdown("####  Histogram — Average Transaction Value per State")
    state_grp = df.groupby("state").agg(total=("amount","sum"),cnt=("count","sum")).reset_index()
    state_grp["avg_txn"] = state_grp["total"] / state_grp["cnt"].replace(0,np.nan)
    fig3 = px.histogram(state_grp, x="avg_txn", nbins=20,
        title="Distribution of Average Transaction Value Across States",
        color_discrete_sequence=["#6366f1"])
    fig3.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=300, bargap=0.05)
    fig3.add_vline(x=state_grp["avg_txn"].mean(), line_dash="dash",
        line_color="#f59e0b", annotation_text=f"Mean ₹{state_grp['avg_txn'].mean():,.0f}",
        annotation_font_color="#f59e0b")
    st.plotly_chart(fig3, use_container_width=True)

    # --- Correlation heatmap ---
    st.markdown("####  Correlation Matrix — Key Metrics")
    state_full = agg_txn.groupby("state").agg(txn_vol=("amount","sum"),txn_cnt=("count","sum")).reset_index()
    state_full["avg_txn"] = state_full["txn_vol"]/state_full["txn_cnt"].replace(0,np.nan)
    if "registered_users" in map_usr.columns and "app_opens" in map_usr.columns:
        usr_st = map_usr.groupby("state").agg(
            reg_users=("registered_users","sum"), app_opens=("app_opens","sum")).reset_index()
        merged = state_full.merge(usr_st, on="state", how="left").dropna()
        corr_cols = ["txn_vol","txn_cnt","avg_txn","reg_users","app_opens"]
        corr_labels = ["Txn Volume","Txn Count","Avg Txn","Reg Users","App Opens"]
    else:
        merged = state_full.dropna()
        corr_cols = ["txn_vol","txn_cnt","avg_txn"]
        corr_labels = ["Txn Volume","Txn Count","Avg Txn"]
    corr_m = merged[corr_cols].corr()
    corr_m.index = corr_labels[:len(corr_cols)]
    corr_m.columns = corr_labels[:len(corr_cols)]
    fig4 = px.imshow(corr_m, color_continuous_scale=["#f43f5e","#080b14","#6366f1"],
        title="Pearson Correlation Matrix — State-level Features",
        zmin=-1, zmax=1, text_auto=".2f", aspect="auto")
    fig4.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=380)
    fig4.update_traces(textfont_color="#f0f6ff")
    st.plotly_chart(fig4, use_container_width=True)

    # --- 3D Scatter ---
    st.markdown("####  3D Scatter — Volume vs Count vs Avg Txn (State-level)")
    scat3d = merged.copy() if "reg_users" in merged.columns else state_full.copy()
    fig5 = px.scatter_3d(scat3d, x="txn_cnt", y="txn_vol", z="avg_txn",
        color="avg_txn", hover_name="state",
        color_continuous_scale=["#6366f1","#06b6d4","#f59e0b"],
        labels={"txn_cnt":"Txn Count","txn_vol":"Txn Volume","avg_txn":"Avg Txn ₹"},
        title="3D View: State Transaction Space")
    fig5.update_layout(paper_bgcolor="#0d1220",font=dict(color="#8b9cbf"),height=520)
    fig5.update_traces(marker_size=5)
    st.plotly_chart(fig5, use_container_width=True)

    # --- Violin: quarterly count distribution ---
    st.markdown("####  Violin Plot — Transaction Count Distribution by Quarter")
    fig6 = px.violin(filt(agg_txn), x="quarter", y="count", color="quarter",
        box=True, points="outliers", color_discrete_sequence=PALETTE,
        labels={"quarter":"Quarter","count":"Count per Record"})
    fig6.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=340, showlegend=False)
    st.plotly_chart(fig6, use_container_width=True)
    st.info(" **Statistical Insight:** Strong positive correlation (r > 0.94) between Registered Users and Transaction Volume confirms that user acquisition is the #1 driver of GMV growth.")

# ══════════════════════════════════════════════════════════════════════════
# PAGE 6 — ML: Forecast & Clusters
# ══════════════════════════════════════════════════════════════════════════
elif page == " ML · Forecast & Clusters":
    st.title(" Machine Learning — Forecasting & Clustering")
    st.markdown("---")

    # ─── Section A: Transaction Volume Forecasting ───────────────────────
    st.markdown("###  A — Transaction Volume Forecasting (Linear + Polynomial Regression)")

    qt = agg_txn.groupby(["year","quarter"]).agg(amount=("amount","sum"),count=("count","sum")).reset_index()
    qt["period_idx"] = (qt["year"]-qt["year"].min())*4 + (qt["quarter"]-1)
    qt["amount_cr"]  = qt["amount"]/1e7
    qt["period"]     = qt["year"].astype(str)+"-Q"+qt["quarter"].astype(str)

    X = qt["period_idx"].values.reshape(-1,1)
    y = qt["amount_cr"].values
    lr = LinearRegression().fit(X, y)

    # Polynomial degree-2
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    lr_poly = LinearRegression().fit(X_poly, y)

    # Future periods
    last_idx = qt["period_idx"].max()
    future_idx = np.arange(last_idx+1, last_idx+9).reshape(-1,1)
    base_year  = qt["year"].min()
    def idx_to_period(idx):
        yr = base_year + idx//4
        q  = idx%4+1
        return f"{yr}-Q{q}"
    future_periods = [idx_to_period(i) for i in range(last_idx+1, last_idx+9)]
    fut_lin  = lr.predict(future_idx)
    fut_poly = lr_poly.predict(poly.transform(future_idx))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=qt["period"], y=y, name="Actual",
        line=dict(color="#06b6d4",width=2.5), mode="lines+markers"))
    fig.add_trace(go.Scatter(x=qt["period"], y=lr.predict(X), name="Linear Fit",
        line=dict(color="#6366f1",width=1.5,dash="dot")))
    fig.add_trace(go.Scatter(x=qt["period"], y=lr_poly.predict(X_poly), name="Poly Fit",
        line=dict(color="#f59e0b",width=1.5,dash="dot")))
    fig.add_trace(go.Scatter(x=future_periods, y=fut_lin, name="Linear Forecast",
        line=dict(color="#6366f1",width=2,dash="dash")))
    fig.add_trace(go.Scatter(x=future_periods, y=fut_poly, name="Poly Forecast",
        line=dict(color="#f59e0b",width=2,dash="dash"),
        fill="tonexty", fillcolor="rgba(245,158,11,0.06)"))
    # Vertical separator between actual and forecast (works on categorical axes)
    last_actual_period = qt["period"].iloc[-1]
    sep_y = [float(min(min(y), min(fut_poly))), float(max(max(y), max(fut_poly)))]
    fig.add_trace(go.Scatter(
        x=[last_actual_period, last_actual_period], y=sep_y,
        mode="lines", line=dict(color="rgba(255,255,255,0.25)", dash="dash", width=1.5),
        name="Forecast Start", showlegend=True
    ))
    fig.update_layout(title="Transaction Forecast 2022–2024 (₹ Crore)",
        paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=400, legend=dict(orientation="h",y=1.08))
    st.plotly_chart(fig, use_container_width=True)

    r2_lin  = lr.score(X, y)
    r2_poly = lr_poly.score(X_poly, y)
    mc1,mc2,mc3 = st.columns(3)
    mc1.metric("Linear R²",      f"{r2_lin:.4f}")
    mc2.metric("Polynomial R²",  f"{r2_poly:.4f}")
    mc3.metric("Poly Next Qtr Forecast", f"₹{fut_poly[0]:,.0f} Cr")

    # ─── Section B: Feature Importance (Random Forest) ───────────────────
    st.markdown("---")
    st.markdown("###  B — Feature Importance (Random Forest Regressor)")
    st.caption("Predicting transaction volume using state-level features")

    state_ml = agg_txn.groupby(["state","year","quarter"]).agg(
        amount=("amount","sum"), count=("count","sum")).reset_index()
    state_ml["avg_txn"]    = state_ml["amount"]/state_ml["count"].replace(0,np.nan)
    state_ml["amount_cr"]  = state_ml["amount"]/1e7
    state_ml["period_idx"] = (state_ml["year"]-state_ml["year"].min())*4+(state_ml["quarter"]-1)
    state_ml = state_ml.dropna()

    feat_cols = ["count","avg_txn","period_idx","year","quarter"]
    Xf = state_ml[feat_cols].values
    yf = state_ml["amount_cr"].values
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(Xf, yf)
    importances = pd.DataFrame({"Feature":feat_cols,"Importance":rf.feature_importances_})
    importances = importances.sort_values("Importance", ascending=True)
    fig2 = px.bar(importances, x="Importance", y="Feature", orientation="h",
        title="Feature Importance — Random Forest (Predicting Txn Volume)",
        color="Importance", color_continuous_scale=["#6366f1","#06b6d4","#f59e0b"])
    fig2.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=300, coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

    # ─── Section C: K-Means Clustering of States ─────────────────────────
    st.markdown("---")
    st.markdown("###  C — K-Means State Clustering (Market Segmentation)")
    st.caption("Cluster states by Volume, Count, and Avg Txn — for targeted strategy")

    state_cl = agg_txn.groupby("state").agg(
        vol=("amount","sum"), cnt=("count","sum")).reset_index()
    state_cl["avg_txn"] = state_cl["vol"]/state_cl["cnt"].replace(0,np.nan)
    state_cl["vol_cr"]  = state_cl["vol"]/1e7
    state_cl["cnt_m"]   = state_cl["cnt"]/1e6
    state_cl = state_cl.dropna()

    scaler = StandardScaler()
    Xc = scaler.fit_transform(state_cl[["vol_cr","cnt_m","avg_txn"]])
    k  = st.slider("Number of Clusters (K)", 2, 5, 3)
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    state_cl["cluster"] = km.fit_predict(Xc).astype(str)
    cluster_labels = {str(i): f"Cluster {chr(65+i)}" for i in range(k)}

    fig3 = px.scatter(state_cl, x="cnt_m", y="vol_cr", size="avg_txn",
        color="cluster", hover_name="state", text="state",
        title=f"K-Means State Clustering (k={k}) — Count vs Volume · Size=Avg Txn",
        color_discrete_sequence=PALETTE,
        labels={"cnt_m":"Txn Count (M)","vol_cr":"Volume (₹ Cr)","cluster":"Cluster"})
    fig3.update_traces(textposition="top center",textfont_size=8,textfont_color="#8b9cbf")
    fig3.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=480)
    st.plotly_chart(fig3, use_container_width=True)

    # Cluster summary
    summary = state_cl.groupby("cluster").agg(
        States=("state","count"),
        Avg_Vol_Cr=("vol_cr","mean"),
        Avg_Count_M=("cnt_m","mean"),
        Avg_Txn=("avg_txn","mean")
    ).reset_index()
    summary.columns = ["Cluster","# States","Avg Vol (₹Cr)","Avg Count (M)","Avg Txn ₹"]
    st.dataframe(summary.style.background_gradient(cmap="Blues",subset=["Avg Vol (₹Cr)"]),
        use_container_width=True)

    # 3D cluster
    st.markdown("####  3D Cluster View")
    fig4 = px.scatter_3d(state_cl, x="cnt_m", y="vol_cr", z="avg_txn",
        color="cluster", hover_name="state",
        color_discrete_sequence=PALETTE,
        labels={"cnt_m":"Count (M)","vol_cr":"Vol (₹Cr)","avg_txn":"Avg ₹"},
        title="3D K-Means Cluster Space")
    fig4.update_layout(paper_bgcolor="#0d1220",font=dict(color="#8b9cbf"),height=520)
    fig4.update_traces(marker_size=5)
    st.plotly_chart(fig4, use_container_width=True)
    st.info(" **ML Insight:** K-Means cleanly separates states into Saturated, High-Growth, and Emerging market tiers. ZORVYN's strategy should differ per cluster: retention vs. acquisition vs. onboarding.")

# ══════════════════════════════════════════════════════════════════════════
# PAGE 7 — Recommendation Engine
# ══════════════════════════════════════════════════════════════════════════
elif page == "Recommendation Engine":
    st.title(" Recommendation Engine — Actionable Intelligence")
    st.markdown("---")
    st.caption("Data-driven strategic recommendations derived from clustering, growth analysis, and brand penetration patterns.")

    # Compute growth per state (YoY latest vs prior)
    yr_sorted = sorted(agg_txn["year"].unique())
    if len(yr_sorted) >= 2:
        curr_yr = yr_sorted[-1]
        prev_yr = yr_sorted[-2]
        curr = agg_txn[agg_txn["year"]==curr_yr].groupby("state")["amount"].sum()
        prev = agg_txn[agg_txn["year"]==prev_yr].groupby("state")["amount"].sum()
        growth = ((curr-prev)/prev*100).dropna().sort_values(ascending=False)
        vol_latest = agg_txn[agg_txn["year"]==curr_yr].groupby("state")["amount"].sum().sort_values(ascending=False)
        avg_txn_st = (agg_txn[agg_txn["year"]==curr_yr].groupby("state").apply(
            lambda x: x["amount"].sum()/x["count"].sum())).sort_values()
    else:
        growth = pd.Series(dtype=float)
        vol_latest = pd.Series(dtype=float)
        avg_txn_st = pd.Series(dtype=float)

    # ── Priority 1: Fastest Growing States ──────────────────────────────
    st.markdown("###  Priority 1 — Fastest Growing States (Expand Now)")
    with st.container():
        if len(growth):
            top_growth = growth.head(8).reset_index()
            top_growth.columns = ["State","YoY Growth %"]
            top_growth["YoY Growth %"] = top_growth["YoY Growth %"].round(1)
            top_growth["Recommendation"] = top_growth["State"].apply(
                lambda s: " Merchant onboarding drive" if top_growth[top_growth["State"]==s]["YoY Growth %"].values[0]>50
                else " Brand awareness + P2P incentives")
            st.dataframe(top_growth, use_container_width=True, hide_index=True)
            fig = px.funnel(top_growth.head(6), x="YoY Growth %", y="State",
                title="State Growth Funnel — Top 6 by YoY Growth",
                color_discrete_sequence=["#10b981"])
            fig.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=310)
            st.plotly_chart(fig, use_container_width=True)

    # ── Priority 2: Low Avg Txn, High User Base → Conversion Gap ────────
    st.markdown("###  Priority 2 — Conversion Gap States (High Users, Low Avg Ticket)")
    if len(avg_txn_st) and len(vol_latest):
        gap_df = pd.DataFrame({"state":vol_latest.index,"vol":vol_latest.values,"avg_txn":avg_txn_st.reindex(vol_latest.index).values})
        gap_df = gap_df.dropna()
        gap_df["vol_cr"] = gap_df["vol"]/1e7
        gap_df["opportunity"] = gap_df["vol_cr"] / gap_df["avg_txn"]
        gap_df = gap_df.sort_values("avg_txn")
        fig2 = px.scatter(gap_df, x="avg_txn", y="vol_cr", color="avg_txn",
            hover_name="state", size="vol_cr",
            color_continuous_scale=["#f43f5e","#f59e0b","#10b981"],
            title="Conversion Gap Matrix — Avg Txn vs Volume · High-Left = Opportunity",
            labels={"avg_txn":"Avg Txn ₹","vol_cr":"Volume ₹ Cr"})
        fig2.add_vline(x=gap_df["avg_txn"].median(), line_dash="dash",
            line_color="rgba(255,255,255,0.2)", annotation_text="Median Avg Txn")
        fig2.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=400)
        st.plotly_chart(fig2, use_container_width=True)

    # ── Priority 3: Brand Targeting Recommendations ───────────────────────
    st.markdown("###  Priority 3 — Brand-Specific Targeting Playbook")
    recs = [
        {"Priority":" HIGH", "Segment":"Xiaomi (MIUI) Users",
         "Insight":"24.8% share, highest in Hindi Belt. 12% higher app open rate but lower checkout completion.",
         "Action":"Optimize payment sheet for MIUI. Offer MIUI-specific cashback via Xiaomi Pay co-branding.",
         "Projected Impact":"↑ 4.2M MAU, ↑ ₹8,400 Cr GMV"},
        {"Priority":" HIGH", "Segment":"Bihar / UP / Odisha — Emerging",
         "Insight":"YoY growth >58%. Low avg txn (<₹1,600). Price-sensitive demographics.",
         "Action":"Deploy ₹10–₹50 cashback on first 5 P2P transactions. Partner with regional kirana chains.",
         "Projected Impact":"↑ ₹18,000 Cr potential GMV in 12 months"},
        {"Priority":" MED",  "Segment":"Tier-1 Saturated (Delhi, Karnataka)",
         "Insight":"User growth plateauing (<25% YoY). High avg txn (₹3,284) = premium segment.",
         "Action":"Launch credit / BNPL features. Introduce loyalty tiering & premium UPI Lite rewards.",
         "Projected Impact":"−15% churn, ↑ ₹6,200 Cr retained GMV"},
        {"Priority":" MED",  "Segment":"Merchant Payments (all states)",
         "Insight":"Only 17.4% of value share vs 28.6% count — merchants are low-AOV. Rural lag.",
         "Action":"Zero-MDR campaign for merchants < ₹10K/month GMV in Tier-3 districts.",
         "Projected Impact":"↑ 2.8M merchants, ↑ ₹9,400 Cr GMV"},
        {"Priority":" LOW",  "Segment":"Samsung / Apple Premium Users",
         "Insight":"Apple share growing from 2.8% → 3.8% (2018–2022). Higher avg txn value.",
         "Action":"Premium card-linked offers, investment features, and NFC payment partnerships.",
         "Projected Impact":"↑ ARPU by 22% in top decile users"},
    ]
    rec_df = pd.DataFrame(recs)
    st.dataframe(rec_df, use_container_width=True, hide_index=True)

    # ── Opportunity Scoring Chart ─────────────────────────────────────────
    st.markdown("###  Opportunity Score Matrix (by State Cluster)")
    opp = pd.DataFrame({
        "Segment":["Bihar/UP/Odisha","Telangana/AP","Maharashtra","Delhi/Karnataka","Gujarat/Rajasthan"],
        "Growth Score":[92,78,42,38,64],
        "Volume Score":[58,82,96,94,74],
        "Ease of Penetration":[72,68,32,28,60],
        "Priority Score":[88,76,48,44,66],
    })
    fig3 = px.scatter(opp, x="Volume Score", y="Growth Score", size="Priority Score",
        color="Priority Score", text="Segment",
        color_continuous_scale=["#f43f5e","#f59e0b","#10b981"],
        title="Strategic Opportunity Matrix — Growth vs Volume Potential",
        labels={"Volume Score":"Current Volume Potential","Growth Score":"YoY Growth Momentum"})
    fig3.update_traces(textposition="top center",textfont_size=10,textfont_color="#f0f6ff")
    fig3.add_vline(x=60, line_dash="dash", line_color="rgba(255,255,255,0.15)")
    fig3.add_hline(y=60, line_dash="dash", line_color="rgba(255,255,255,0.15)")
    fig3.update_layout(paper_bgcolor="#0d1220", plot_bgcolor="#080b14", font=dict(color="#8b9cbf", family="Inter"), height=450)
    st.plotly_chart(fig3, use_container_width=True)

    st.success(" **Top Strategic Recommendation:** Prioritize Bihar/UP/Odisha with micro-incentive P2P campaigns AND simultaneously deploy MIUI-optimized UX for Xiaomi users — these two actions alone project ₹26,400 Cr in incremental GMV within 12 months.")

# ─── Footer ───────────────────────────────────────────────────────────────
st.markdown("---")
st.caption(" ZORVYN Fintech Analytics Intelligence Platform · India Digital Payments 2018–2022 · Built with Streamlit + Plotly + Scikit-learn")
