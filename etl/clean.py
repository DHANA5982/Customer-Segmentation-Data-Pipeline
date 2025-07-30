import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(0, inplace=True)
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()
    print(f"[Clean] Cleaned data. Remaining rows: {df.shape[0]}")
    return df
