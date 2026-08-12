import pandas as pd
import numpy as np

real_df = pd.read_csv("../data/sample.csv")
fake_synthetic_df = real_df.copy()

numeric_cols = fake_synthetic_df.select_dtypes(include=np.number).columns
fake_synthetic_df[numeric_cols] = fake_synthetic_df[numeric_cols] + np.random.normal(0, 1, fake_synthetic_df[numeric_cols].shape)

fake_synthetic_df.to_csv("../data/fake_synthetic_for_testing.csv", index=False)
print("Done! Saved fake_synthetic_for_testing.csv")