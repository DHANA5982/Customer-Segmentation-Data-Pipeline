# scripts/load_to_sqlite.py

import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os

# paths
data_path = 'D:/GitHub/Customer Segmentation Data Pipeline/data/fact_dim_tables'
database_path = 'D:/GitHub/Customer Segmentation Data Pipeline/database/telco_churn.db'

# Load DataFrames
fact = pd.read_csv(os.path.join(data_path, 'fact_df.csv'))
dim_customer = pd.read_csv(os.path.join(data_path, 'dim_customer_df.csv'))
dim_services = pd.read_csv(os.path.join(data_path, 'dim_service_df.csv'))
dim_subscription = pd.read_csv(os.path.join(data_path, 'dim_subscription_df.csv'))

# Connect SQLite database
con = sqlite3.connect('telco_churn.db')
cur = con.cursor()

# Drop tables if reloading (for dev/testing)
cur.execute("DROP TABLE IF EXISTS fact_table")
cur.execute("DROP TABLE IF EXISTS dim_customer_table")
cur.execute("DROP TABLE IF EXISTS dim_services_table")
cur.execute("DROP TABLE IF EXISTS dim_subscription_table")

# Write tables to SQLite
fact.to_sql('fact_table', con, index=False)
dim_customer.to_sql('dim_customer_table', con, index=False)
dim_services.to_sql('dim_services_table', con, index=False)
dim_subscription.to_sql('dim_subscription_table', con, index=False)

con.commit()
con.close()
print("✅ Data loaded into telco_churn.db successfully.")
