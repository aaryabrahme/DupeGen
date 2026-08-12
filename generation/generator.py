import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer


def generate_synthetic(real_df: pd.DataFrame, n_rows: int, epochs: int = 100) -> pd.DataFrame:
    """
    Takes a real dataset and returns a synthetic dataset with the same
    columns, generated to statistically resemble the real data.

    real_df : the real seed data (pandas DataFrame)
    n_rows  : how many synthetic rows to generate
    epochs  : how long to train the generator (higher = better quality, slower)
    """
    # Step 1: Auto-detect column types (numeric, categorical, etc.)
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(real_df)

    # Step 2: Create and train the synthetic data generator
    synthesizer = CTGANSynthesizer(metadata, epochs=epochs, verbose=True)
    synthesizer.fit(real_df)

    # Step 3: Generate new synthetic rows
    synthetic_df = synthesizer.sample(num_rows=n_rows)

    return synthetic_df


# Quick manual test — only runs when you execute this file directly
if __name__ == "__main__":
    real_data = pd.read_csv("../data/sample.csv")
    synthetic_data = generate_synthetic(real_data, n_rows=200, epochs=50)
    print(synthetic_data.head())
    synthetic_data.to_csv("../data/synthetic_test_output.csv", index=False)
    print("Saved synthetic_test_output.csv — open it and compare to sample.csv")

from sdv.sampling import Condition

def generate_conditional(real_df: pd.DataFrame, column: str, value, n_rows: int, epochs: int = 100) -> pd.DataFrame:
    """
    Generates synthetic rows where a specific column is forced to a
    specific value — e.g. column='is_fraud', value=1, to oversample fraud cases.
    """
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(real_df)

    synthesizer = CTGANSynthesizer(metadata, epochs=epochs)
    synthesizer.fit(real_df)

    condition = Condition(num_rows=n_rows, column_values={column: value})
    synthetic_df = synthesizer.sample_from_conditions([condition])

    return synthetic_df