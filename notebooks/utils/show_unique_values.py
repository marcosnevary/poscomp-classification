import pandas as pd


def show_unique_values(df: pd.DataFrame) -> None:
    for column in df.columns:
        print(f"{column}: {df[column].unique()}")
