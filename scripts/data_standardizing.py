import pandas as pd

clean_df = pd.read_csv('D:/GitHub/Customer Segmentation Data Pipeline/data//processed/cleaned_df.csv')

# Remane columns
clean_df.columns = clean_df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert binary fields
binary_map = {'Yes': 1, 'No': 0}
clean_df['partner'] = clean_df['partner'].map(binary_map)
clean_df['dependents'] = clean_df['dependents'].map(binary_map)

processed_df = clean_df.copy()
processed_df.to_csv('D:/GitHub/Customer Segmentation Data Pipeline/data/processed/processed_df.csv', index=False)