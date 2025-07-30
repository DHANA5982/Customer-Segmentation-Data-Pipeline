import os
from etl.ingest import ingest_data
from etl.clean import clean_data
from etl.transform import transform_data
from etl.utils import profile_data

RAW_PATH = 'D:/GitHub/Customer Segmentation Data Pipeline/data/raw/Customer_churn4.csv'
OUTPUT_PATH = 'D:/GitHub/Customer Segmentation Data Pipeline/data/processed/customer_clean.csv'

def main():
    print("🚀 Starting ETL Pipeline")

    df = ingest_data(RAW_PATH)
    profile_data(df)

    df = clean_data(df)
    df = transform_data(df)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"✅ Pipeline completed. Clean data saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
