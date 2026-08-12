import pandas as pd
import numpy as np
from scipy.stats import ks_2samp, chisquare
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


def score_fidelity(real_df: pd.DataFrame, synthetic_df: pd.DataFrame) -> dict:
    per_column_scores = {}

    for col in real_df.columns:
        if col not in synthetic_df.columns:
            continue

        if pd.api.types.is_numeric_dtype(real_df[col]):
            stat, p_value = ks_2samp(real_df[col].dropna(), synthetic_df[col].dropna())
            similarity = p_value
        else:
            real_counts = real_df[col].value_counts(normalize=True)
            synth_counts = synthetic_df[col].value_counts(normalize=True)
            all_categories = set(real_counts.index) | set(synth_counts.index)
            real_freqs = [real_counts.get(cat, 0.0001) for cat in all_categories]
            synth_freqs = [synth_counts.get(cat, 0.0001) for cat in all_categories]
            try:
                stat, p_value = chisquare(synth_freqs, real_freqs)
                similarity = min(p_value, 1.0)
            except Exception:
                similarity = 0.5

        per_column_scores[col] = round(similarity * 100, 1)

    fidelity_score = round(np.mean(list(per_column_scores.values())), 1) if per_column_scores else 0

    return {
        "fidelity_score": fidelity_score,
        "per_column_scores": per_column_scores
    }


def score_diversity(synthetic_df: pd.DataFrame) -> dict:
    numeric_df = synthetic_df.select_dtypes(include=[np.number]).dropna()

    if len(numeric_df) < 5:
        return {"diversity_score": 0, "duplicate_ratio": None}

    scaled = StandardScaler().fit_transform(numeric_df)

    nn = NearestNeighbors(n_neighbors=2)
    nn.fit(scaled)
    distances, _ = nn.kneighbors(scaled)
    nearest_distances = distances[:, 1]

    threshold = np.percentile(nearest_distances, 10)
    duplicate_ratio = round((nearest_distances < threshold).mean(), 3)

    diversity_score = round((1 - duplicate_ratio) * 100, 1)

    return {
        "diversity_score": diversity_score,
        "duplicate_ratio": duplicate_ratio
    }


def score_ml_utility(real_df: pd.DataFrame, synthetic_df: pd.DataFrame, target_col: str) -> dict:
    def prep(df):
        df = df.dropna().copy()
        for col in df.select_dtypes(include="object").columns:
            df[col] = LabelEncoder().fit_transform(df[col].astype(str))
        return df

    real_prepped = prep(real_df)
    synth_prepped = prep(synthetic_df)

    X_real = real_prepped.drop(columns=[target_col])
    y_real = real_prepped[target_col]

    X_train_real, X_test_real, y_train_real, y_test_real = train_test_split(
        X_real, y_real, test_size=0.3, random_state=42
    )

    real_model = RandomForestClassifier(random_state=42)
    real_model.fit(X_train_real, y_train_real)
    real_accuracy = accuracy_score(y_test_real, real_model.predict(X_test_real))

    X_synth = synth_prepped.drop(columns=[target_col])
    y_synth = synth_prepped[target_col]
    synth_model = RandomForestClassifier(random_state=42)
    synth_model.fit(X_synth, y_synth)
    synthetic_accuracy = accuracy_score(y_test_real, synth_model.predict(X_test_real))

    gap = round(real_accuracy - synthetic_accuracy, 3)

    return {
        "real_accuracy": round(real_accuracy, 3),
        "synthetic_accuracy": round(synthetic_accuracy, 3),
        "gap": gap
    }


if __name__ == "__main__":
    real = pd.read_csv("../data/sample.csv")

    # This now points to Member 1's REAL generated data instead of the fake noisy version
    real_synthetic = pd.read_csv("../data/real_synthetic_output.csv")

    print("Fidelity:", score_fidelity(real, real_synthetic))
    print("Diversity:", score_diversity(real_synthetic))
    print("ML Utility:", score_ml_utility(real, real_synthetic, target_col="label"))