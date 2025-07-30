def profile_data(df):
    print("\n[Profile] Null values per column:")
    print(df.isnull().sum())

    print("\n[Profile] Data types:")
    print(df.dtypes)

    print("\n[Profile] Duplicate records:", df.duplicated().sum())
