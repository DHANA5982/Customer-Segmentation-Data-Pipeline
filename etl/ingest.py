import pandas as pd

def ingest_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print(f"[Ingest] Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
    return df
