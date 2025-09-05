import pandas as pd
from utils.variables import PROCESSED_DATA_PATH


def save_dataframe(df: pd.DataFrame, file_name: str) -> None:
    df.to_csv(PROCESSED_DATA_PATH / f"{file_name}.csv", index=False)
