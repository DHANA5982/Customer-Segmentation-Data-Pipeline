import pandas as pd

raw_df = pd.read_csv('D:/GitHub/Customer Segmentation Data Pipeline/data//raw/Customer_churn4.csv')

raw_df.isnull().sum()
raw_df['TotalCharges'] = pd.to_numeric(raw_df['TotalCharges'], errors='coerce')
raw_df['TotalCharges'].isnull().sum()
raw_df['TotalCharges'].fillna(0, inplace=True)

raw_df.duplicated().sum()
for col in raw_df.select_dtypes(include='object').columns:
    print(f'{col}, unique values: {raw_df[col].nunique()}')

clean_df = raw_df.drop_duplicates()
clean_df.to_csv('D:/GitHub/Customer Segmentation Data Pipeline/data/processed/cleaned_df.csv', index=False)