def clean_data(df):
    print("🔄 Cleaning data...")
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    print(f"✅ Cleaned data: {len(df)} rows remaining")
    return df
