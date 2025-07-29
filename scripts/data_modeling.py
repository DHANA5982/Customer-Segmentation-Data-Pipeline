import pandas as pd

processed_df = pd.read_csv('D:/GitHub/Customer Segmentation Data Pipeline/data//processed/processed_df.csv')

# Fact table
fact_df = processed_df[[
    'customerid', 'tenure', 'monthlycharges', 'totalcharges', 'churn'
]]
fact_df.to_csv('D:/GitHub/Customer Segmentation Data Pipeline/data/fact_dim_tables/fact_df.csv', index=False)

# Customer dimension
dim_customer = processed_df[[
    'customerid', 'gender', 'seniorcitizen', 'partner', 'dependents'
]]
dim_customer.to_csv('D:/GitHub/Customer Segmentation Data Pipeline/data/fact_dim_tables/dim_customer_df.csv', index=False)

# Services dimension
dim_services = processed_df[[
    'customerid', 'phoneservice', 'multiplelines', 'internetservice',
    'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
    'streamingtv', 'streamingmovies'
]]
dim_services.to_csv('D:/GitHub/Customer Segmentation Data Pipeline/data/fact_dim_tables/dim_service_df.csv', index=False)

# Subscription dimension
dim_subscription = processed_df[[
    'customerid', 'contract', 'paperlessbilling', 'paymentmethod'
]]
dim_subscription.to_csv('D:/GitHub/Customer Segmentation Data Pipeline/data/fact_dim_tables/dim_subscription_df.csv', index=False)