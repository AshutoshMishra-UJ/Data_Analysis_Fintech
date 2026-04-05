"""
============================================================
  ZORVYN FINTECH — Data Cleaning & Preprocessing Pipeline
  Dataset: India Digital Payments (PhonePe Pulse)
  Author: ZORVYN Data Intelligence Team
============================================================
"""

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

# ─── Paths ───────────────────────────────────────────────
BASE = os.path.join(os.path.dirname(__file__), "Datasets")
OUT  = os.path.dirname(__file__)

# ─── Helper: Standardize State Names ─────────────────────
def clean_state(s):
    if pd.isna(s): return s
    return (str(s).strip().lower()
            .replace("&", "and")
            .replace("  ", " "))

# ─── Helper: Standardize District Names ──────────────────
def clean_district(s):
    if pd.isna(s): return s
    s = str(s).strip().lower()
    for suffix in [" district", " dist."]:
        s = s.replace(suffix, "")
    return s.strip().replace("  ", " ")

# ═══════════════════════════════════════════════════════════
#  1. AGGREGATED TRANSACTIONS
#     Cols: name, state, year, quarter, count, amount
# ═══════════════════════════════════════════════════════════
print("📦 Loading aggregated transactions...")
agg_txn = pd.read_csv(os.path.join(BASE, "final_agg_transaction.csv"), index_col=0)
agg_txn.columns = agg_txn.columns.str.strip().str.lower()
agg_txn.rename(columns={"name": "transaction_type"}, inplace=True)
agg_txn["state"]            = agg_txn["state"].apply(clean_state)
agg_txn["transaction_type"] = agg_txn["transaction_type"].str.strip()
agg_txn["count"]            = pd.to_numeric(agg_txn["count"],  errors="coerce").fillna(0).astype(int)
agg_txn["amount"]           = pd.to_numeric(agg_txn["amount"], errors="coerce").fillna(0.0)
agg_txn["year"]             = agg_txn["year"].astype(int)
agg_txn["quarter"]          = agg_txn["quarter"].astype(int)
agg_txn.drop_duplicates(inplace=True)
print(f"   ✅ agg_txn: {agg_txn.shape}")

# ═══════════════════════════════════════════════════════════
#  2. AGGREGATED USERS
#     Cols: brand, count, percentage, state, year, quarter
# ═══════════════════════════════════════════════════════════
print("📦 Loading aggregated users...")
agg_usr = pd.read_csv(os.path.join(BASE, "final_agg_user.csv"), index_col=0)
agg_usr.columns = agg_usr.columns.str.strip().str.lower()
agg_usr["state"]      = agg_usr["state"].apply(clean_state)
agg_usr["brand"]      = agg_usr["brand"].str.strip()
agg_usr["count"]      = pd.to_numeric(agg_usr["count"],      errors="coerce").fillna(0).astype(int)
agg_usr["percentage"] = pd.to_numeric(agg_usr["percentage"], errors="coerce").fillna(0.0)
agg_usr["year"]       = agg_usr["year"].astype(int)
agg_usr["quarter"]    = agg_usr["quarter"].astype(int)
agg_usr.drop_duplicates(inplace=True)
print(f"   ✅ agg_usr: {agg_usr.shape}")

# ═══════════════════════════════════════════════════════════
#  3. MAP TRANSACTIONS (district-level)
#     Cols: name, state, year, quarter, count, amount
# ═══════════════════════════════════════════════════════════
print("📦 Loading map transactions...")
map_txn = pd.read_csv(os.path.join(BASE, "final_map_transaction.csv"), index_col=0)
map_txn.columns = map_txn.columns.str.strip().str.lower()
map_txn.rename(columns={"name": "district"}, inplace=True)
map_txn["state"]    = map_txn["state"].apply(clean_state)
map_txn["district"] = map_txn["district"].apply(clean_district)
map_txn["count"]    = pd.to_numeric(map_txn["count"],  errors="coerce").fillna(0).astype(int)
map_txn["amount"]   = pd.to_numeric(map_txn["amount"], errors="coerce").fillna(0.0)
map_txn["year"]     = map_txn["year"].astype(int)
map_txn["quarter"]  = map_txn["quarter"].astype(int)
map_txn.drop_duplicates(inplace=True)
print(f"   ✅ map_txn: {map_txn.shape}")

# ═══════════════════════════════════════════════════════════
#  4. MAP USERS (district-level)
#     Cols: index(district), registeredUsers, appOpens, state, year, quarter
# ═══════════════════════════════════════════════════════════
print("📦 Loading map users...")
map_usr = pd.read_csv(os.path.join(BASE, "final_map_user_new.csv"), index_col=0)
map_usr.columns = map_usr.columns.str.strip().str.lower()
map_usr.rename(columns={"index": "district",
                         "registeredusers": "registered_users",
                         "appopens": "app_opens"}, inplace=True)
map_usr["state"]            = map_usr["state"].apply(clean_state)
map_usr["district"]         = map_usr["district"].apply(clean_district)
map_usr["registered_users"] = pd.to_numeric(map_usr["registered_users"], errors="coerce").fillna(0).astype(int)
map_usr["app_opens"]        = pd.to_numeric(map_usr["app_opens"],        errors="coerce").fillna(0).astype(int)
map_usr["year"]             = map_usr["year"].astype(int)
map_usr["quarter"]          = map_usr["quarter"].astype(int)
map_usr.drop_duplicates(inplace=True)
print(f"   ✅ map_usr: {map_usr.shape}")

# ═══════════════════════════════════════════════════════════
#  5. TOP USERS
#     Cols: name, registeredUsers, state, year, quarter
# ═══════════════════════════════════════════════════════════
print("📦 Loading top users...")
top_usr = pd.read_csv(os.path.join(BASE, "final_top_user.csv"), index_col=0)
top_usr.columns = top_usr.columns.str.strip().str.lower()
top_usr.rename(columns={"name": "entity",
                         "registeredusers": "registered_users"}, inplace=True)
top_usr["state"]            = top_usr["state"].apply(clean_state)
top_usr["entity"]           = top_usr["entity"].astype(str).str.strip()
top_usr["registered_users"] = pd.to_numeric(top_usr["registered_users"], errors="coerce").fillna(0).astype(int)
top_usr["year"]             = top_usr["year"].astype(int)
top_usr["quarter"]          = top_usr["quarter"].astype(int)
top_usr.drop_duplicates(inplace=True)
print(f"   ✅ top_usr: {top_usr.shape}")

# ═══════════════════════════════════════════════════════════
#  6. TOP TRANSACTIONS
#     Cols: entityName, state, year, quarter, count, amount
# ═══════════════════════════════════════════════════════════
print("📦 Loading top transactions...")
top_txn = pd.read_csv(os.path.join(BASE, "final_transaction_top.csv"), index_col=0)
top_txn.columns = top_txn.columns.str.strip().str.lower()
top_txn.rename(columns={"entityname": "entity"}, inplace=True)
top_txn["state"]   = top_txn["state"].apply(clean_state)
top_txn["entity"]  = top_txn["entity"].astype(str).str.strip()
top_txn["count"]   = pd.to_numeric(top_txn["count"],  errors="coerce").fillna(0).astype(int)
top_txn["amount"]  = pd.to_numeric(top_txn["amount"], errors="coerce").fillna(0.0)
top_txn["year"]    = top_txn["year"].astype(int)
top_txn["quarter"] = top_txn["quarter"].astype(int)
top_txn.drop_duplicates(inplace=True)
print(f"   ✅ top_txn: {top_txn.shape}")

# ═══════════════════════════════════════════════════════════
#  BUILD MASTER CLEANED DATASET
#  Pivot: state × year × quarter aggregates
# ═══════════════════════════════════════════════════════════
print("\n🔧 Building master cleaned dataset...")

# Total transactions per state/year/quarter
state_txn = (agg_txn
             .groupby(["state", "year", "quarter"])
             .agg(total_txn_count=("count", "sum"),
                  total_txn_amount=("amount", "sum"))
             .reset_index())

# Total registered users per state/year/quarter (from map_usr)
state_usr = (map_usr
             .groupby(["state", "year", "quarter"])
             .agg(total_registered_users=("registered_users", "sum"),
                  total_app_opens=("app_opens", "sum"))
             .reset_index())

# Dominant transaction type per state/year/quarter
dominant_type = (agg_txn
                 .sort_values("count", ascending=False)
                 .groupby(["state", "year", "quarter"])
                 .first()[["transaction_type"]]
                 .reset_index())

# Top mobile brand per state/year/quarter
top_brand = (agg_usr
             .sort_values("count", ascending=False)
             .groupby(["state", "year", "quarter"])
             .first()[["brand"]]
             .reset_index()
             .rename(columns={"brand": "top_brand"}))

# Merge all
master = (state_txn
          .merge(state_usr,    on=["state", "year", "quarter"], how="left")
          .merge(dominant_type, on=["state", "year", "quarter"], how="left")
          .merge(top_brand,     on=["state", "year", "quarter"], how="left"))

# Derived metrics
master["avg_txn_amount"]         = (master["total_txn_amount"] / master["total_txn_count"].replace(0, np.nan)).round(2)
master["period"]                 = master["year"].astype(str) + "-Q" + master["quarter"].astype(str)
master["total_txn_amount_cr"]    = (master["total_txn_amount"] / 1e7).round(4)   # in Crores

# Sort
master.sort_values(["state", "year", "quarter"], inplace=True)
master.reset_index(drop=True, inplace=True)

# Save master
master_path = os.path.join(OUT, "zorvyn_cleaned_data.csv")
master.to_csv(master_path, index=False)
print(f"   ✅ Master saved → {master_path}  [{master.shape}]")

# Save individual cleaned datasets
agg_txn.to_csv(os.path.join(OUT, "clean_agg_transactions.csv"), index=False)
agg_usr.to_csv(os.path.join(OUT, "clean_agg_users.csv"),         index=False)
map_txn.to_csv(os.path.join(OUT, "clean_map_transactions.csv"),  index=False)
map_usr.to_csv(os.path.join(OUT, "clean_map_users.csv"),         index=False)
top_txn.to_csv(os.path.join(OUT, "clean_top_transactions.csv"),  index=False)
top_usr.to_csv(os.path.join(OUT, "clean_top_users.csv"),         index=False)

print("\n✅ All cleaned datasets saved successfully!")
print("\n📊 Master Dataset Preview:")
print(master.head(5).to_string())

# ═══════════════════════════════════════════════════════════
#  BUSINESS INSIGHTS (Top 3 for ZORVYN stakeholders)
# ═══════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("  ZORVYN FINTECH — KEY BUSINESS INSIGHTS")
print("═"*60)

# INSIGHT 1: Top 10 States by Total Transaction Amount (all time)
print("\n📌 INSIGHT 1: Top 10 States by Total Digital Payment Volume")
top_states = (master
              .groupby("state")["total_txn_amount_cr"]
              .sum()
              .sort_values(ascending=False)
              .head(10)
              .reset_index())
top_states.columns = ["State", "Total Amount (₹ Crore)"]
print(top_states.to_string(index=False))

# INSIGHT 2: Year-over-Year transaction growth
print("\n📌 INSIGHT 2: National Year-over-Year Transaction Growth")
yoy = (master
       .groupby("year")
       .agg(txn_count=("total_txn_count", "sum"),
            txn_amount_cr=("total_txn_amount_cr", "sum"))
       .reset_index())
yoy["count_growth_%"]  = yoy["txn_count"].pct_change().mul(100).round(1)
yoy["amount_growth_%"] = yoy["txn_amount_cr"].pct_change().mul(100).round(1)
print(yoy.to_string(index=False))

# INSIGHT 3: Market Share of Transaction Types (all-India, latest year)
latest_year = agg_txn["year"].max()
print(f"\n📌 INSIGHT 3: Transaction Type Market Share ({latest_year})")
type_share = (agg_txn[agg_txn["year"] == latest_year]
              .groupby("transaction_type")
              .agg(count=("count", "sum"), amount=("amount", "sum"))
              .reset_index())
type_share["amount_share_%"] = (type_share["amount"] / type_share["amount"].sum() * 100).round(2)
type_share["count_share_%"]  = (type_share["count"]  / type_share["count"].sum()  * 100).round(2)
type_share.sort_values("amount_share_%", ascending=False, inplace=True)
print(type_share[["transaction_type", "count_share_%", "amount_share_%"]].to_string(index=False))

# INSIGHT 4: Top Mobile Brands (All India)
print("\n📌 INSIGHT 4: Top Mobile Brands by User Count (All India)")
brand_share = (agg_usr
               .groupby("brand")["count"]
               .sum()
               .sort_values(ascending=False)
               .head(10)
               .reset_index())
total_users = brand_share["count"].sum()
brand_share["share_%"] = (brand_share["count"] / agg_usr["count"].sum() * 100).round(2)
print(brand_share.to_string(index=False))

print("\n✅ Insights generated. Ready for dashboard visualization.\n")
