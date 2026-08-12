"""
test_pipeline.py
Member 4 — integration tests that check Member 1's generator and
Member 2's scorer work correctly together.

Run from inside the tests/ folder:
    cd tests
    pytest test_pipeline.py -v

These will fail with ImportError until Member 1 pushes generation/generator.py
and Member 2 pushes scoring/scorer.py — that's expected. Once they push,
just re-run pytest, no changes needed here.
"""

import sys
sys.path.append("..")

import pandas as pd
from generation.generator import generate_synthetic
from scoring.scorer import score_fidelity, score_diversity, score_ml_utility

DATA_PATH = "../data/demo_dataset_small.csv"
TARGET_COL = "Class"  # fraud/not-fraud label in the credit card dataset


def load_sample(n=50):
    """Small slice so tests run fast — not meant to test data quality,
    just that the functions execute and return sane shapes."""
    return pd.read_csv(DATA_PATH).head(n)


def test_generation_returns_same_columns():
    real = load_sample()
    synthetic = generate_synthetic(real, n_rows=20, epochs=5)
    assert list(synthetic.columns) == list(real.columns)
    assert len(synthetic) == 20


def test_generation_returns_dataframe():
    real = load_sample()
    synthetic = generate_synthetic(real, n_rows=20, epochs=5)
    assert isinstance(synthetic, pd.DataFrame)
    assert not synthetic.empty


def test_fidelity_score_in_range():
    real = load_sample()
    synthetic = generate_synthetic(real, n_rows=20, epochs=5)
    result = score_fidelity(real, synthetic)
    assert 0 <= result["fidelity_score"] <= 100
    assert "per_column_scores" in result


def test_diversity_score_in_range():
    real = load_sample()
    synthetic = generate_synthetic(real, n_rows=20, epochs=5)
    result = score_diversity(synthetic)
    assert 0 <= result["diversity_score"] <= 100


def test_ml_utility_returns_expected_keys():
    real = load_sample()
    synthetic = generate_synthetic(real, n_rows=20, epochs=5)
    result = score_ml_utility(real, synthetic, target_col=TARGET_COL)
    assert "real_accuracy" in result
    assert "synthetic_accuracy" in result
    assert "gap" in result
    assert 0 <= result["real_accuracy"] <= 1
    assert 0 <= result["synthetic_accuracy"] <= 1


def test_conditional_generation_forces_target_value():
    """Checks Member 1's generate_conditional() actually respects the
    forced column value — important since this is the 'oversample fraud'
    feature the whole demo pitch is built around."""
    from generation.generator import generate_conditional

    real = load_sample(n=200)  # need more rows so both classes are present
    synthetic = generate_conditional(
        real, column=TARGET_COL, value=1, n_rows=10, epochs=5
    )
    assert (synthetic[TARGET_COL] == 1).all()
