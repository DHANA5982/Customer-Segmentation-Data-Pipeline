def transform_data(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    binary_map = {'Yes': 1, 'No': 0}
    binary_cols = ['partner', 'dependents', 'phoneservice', 'paperlessbilling', 'churn']
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map(binary_map)

    df['seniorcitizen'] = df['seniorcitizen'].astype(int)

    print(f"[Transform] Transformed data. Ready for export.")
    return df
