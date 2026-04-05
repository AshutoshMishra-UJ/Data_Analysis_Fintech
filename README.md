# ZORVYN Fintech — Data Analytics Intelligence Platform

> A professional, end-to-end data analysis project built for **ZORVYN Fintech** using India's digital payment ecosystem data (2018–2022).

---

## Project Overview

This project analyzes India's aggregated digital payment and user transaction data across **6 structured datasets**, delivering deep business intelligence through an interactive Streamlit dashboard.

**Problem Statement:** *Market Expansion & Geo-Spatial Transaction Trends Analysis* — helping ZORVYN Fintech identify high-growth geographies, dominant transaction patterns, mobile brand penetration, and data-driven expansion opportunities.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Data Cleaning | Python, Pandas, NumPy |
| Visualization | Plotly (interactive charts) |
| ML & Analytics | Scikit-learn (K-Means, Random Forest, Regression) |
| Dashboard | Streamlit |
| Language | Python 3.10+ |

---

## Datasets (6 CSV files)

| File | Description |
|---|---|
| `final_agg_transaction.csv` | Aggregated transactions by state, year, quarter, type |
| `final_agg_user.csv` | User counts by mobile brand |
| `final_map_transaction.csv` | District-level transaction mapping |
| `final_map_user_new.csv` | District-level user registration & app opens |
| `final_top_user.csv` | Top user statistics by state/pincode |
| `final_transaction_top.csv` | Top transaction statistics by state/pincode |

---

## Dashboard Pages

1. **Overview & KPIs** — Total volume, transaction count, avg ticket size, YoY growth
2. **Trend Analysis** — Stacked area charts, heatmaps, QoQ growth rates
3. **Geo & State Deep Dive** — State rankings, bubble charts, district treemaps
4. **Brand Intelligence** — Brand share, YoY evolution, box plots, penetration heatmap
5. **Statistical Analysis** — Box plots, violin plots, correlation matrix, 3D scatter
6. **ML: Forecast & Clusters** — Linear/polynomial forecasting, Random Forest feature importance, K-Means clustering (interactive k), 3D cluster view
7. **Recommendation Engine** — Data-driven market expansion playbook, conversion gap matrix, opportunity scoring

---

## How to Run

```bash
# 1. Install dependencies
pip install streamlit plotly pandas numpy scikit-learn

# 2. Run the dashboard
streamlit run dashboard.py
```

Open **http://localhost:8501** in your browser.

---

## Key Business Insights

- **Peer-to-Peer payments** dominate at ~73% of total transaction value nationally
- **Maharashtra, Andhra Pradesh, and Telangana** are the top 3 states by volume
- **Xiaomi holds ~25% mobile brand share** across all years — largest single device segment
- **Bihar, UP, and Odisha** show the highest YoY growth (>58%) — prime expansion targets
- Strong **r = 0.97 correlation** between registered users and transaction volume — user acquisition is the #1 GMV driver
- **K-Means clustering** cleanly segments India's states into Saturated, High-Growth, and Emerging market tiers

---

## Project Structure

```
Zorvyn_Data_Analyst/
├── Datasets/                  # Raw source CSV files
│   ├── final_agg_transaction.csv
│   ├── final_agg_user.csv
│   ├── final_map_transaction.csv
│   ├── final_map_user_new.csv
│   ├── final_top_user.csv
│   └── final_transaction_top.csv
├── dashboard.py               # Main Streamlit dashboard (7 pages)
├── data_cleaning.py           # Data cleaning & preprocessing pipeline
├── requirements.txt           # Python dependencies
└── README.md
```

---

## Author

Ashutosh Mishra
.
