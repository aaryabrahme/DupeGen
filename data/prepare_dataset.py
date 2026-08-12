"""
prepare_dataset.py
Member 4 — Data prep for the Kaggle "Credit Card Fraud Detection" dataset
(mlg-ulb/creditcardfraud).

Run this from inside the data/ folder:
    cd data
    python prepare_dataset.py

Before running: download creditcard.csv from
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
and place it in this same data/ folder.
"""

import pandas as pd

RAW_FILE = "creditcard.csv"

# ---- Load ----
df = pd.read_csv(RAW_FILE)
print("Raw shape:", df.shape)
print(df["Class"].value_counts())
print("Fraud rate: {:.3f}%".format(df["Class"].mean() * 100))

# ---- Light cleaning ----
# This dataset has no ID columns and (famously) zero missing values,
# but we run the same checks the team guide expects so the pipeline
# is robust if you swap in a different Kaggle dataset later.

# Drop any obvious ID-like columns (none expected here, but safe to keep)
df = df.drop(columns=[c for c in df.columns if "id" in c.lower()], errors="ignore")

# Drop rows with too many missing values (threshold: keep rows with
# at least 70% of columns populated)
df = df.dropna(thresh=len(df.columns) * 0.7)

# Fill any remaining small gaps in numeric columns with the median
df = df.fillna(df.median(numeric_only=True))

print("\nCleaned shape:", df.shape)
print(df.dtypes)
print("Missing values per column:\n", df.isnull().sum().sum(), "total")

# ---- Save the full cleaned dataset (for final scoring / reporting) ----
df.to_csv("demo_dataset_clean.csv", index=False)
print("\nSaved demo_dataset_clean.csv —", df.shape)

# ---- Save a smaller demo-sized sample (for fast live generation) ----
# CTGAN training on 284k rows takes way too long for a live demo.
# We take: all fraud rows (only 492, keep every one) + a random slice
# of normal rows, so the imbalance story is still visible but small
# enough to train on in under a minute.
fraud = df[df["Class"] == 1]
normal = df[df["Class"] == 0].sample(n=2000, random_state=42)

demo_sample = pd.concat([fraud, normal]).sample(frac=1, random_state=42).reset_index(drop=True)
demo_sample.to_csv("demo_dataset_small.csv", index=False)

print("Saved demo_dataset_small.csv —", demo_sample.shape,
      "(", demo_sample['Class'].sum(), "fraud rows,",
      (demo_sample['Class'] == 0).sum(), "normal rows )")
print("\nUse demo_dataset_small.csv for fast local testing / live demo.")
print("Use demo_dataset_clean.csv for the final, most convincing scoring numbers.")
