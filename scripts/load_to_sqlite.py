# scripts/load_to_sqlite.py

import pandas as pd
from sqlalchemy import create_engine
import os

# paths
data_path = 'D:/GitHub/Customer Segmentation Data Pipeline/data/fact_dim_tables'
database_path = 'D:/GitHub/Customer Segmentation Data Pipeline/database/telco_churn.db'

# Load DataFrames
fact = pd.read_csv(os.path.join(data_path, 'fact_df.csv'))
dim_customer = pd.read_csv(os.path.join(data_path, 'dim_customer_df.csv'))
dim_services = pd.read_csv(os.path.join(data_path, 'dim_service_df.csv'))
dim_subscription = pd.read_csv(os.path.join(data_path, 'dim_subscription_df.csv'))

# Create SQLite connection
engine = create_engine(f'sqlite:///{database_path}')

# Write tables to SQLite
fact.to_sql('fact_table', con=engine, if_exists='replace', index=False)
dim_customer.to_sql('dim_customer_table', con=engine, if_exists='replace', index=False)
dim_services.to_sql('dim_services_table', con=engine, if_exists='replace', index=False)
dim_subscription.to_sql('dim_subscription_table', con=engine, if_exists='replace', index=False)

print("✅ Data loaded into telco_churn.db successfully.")
