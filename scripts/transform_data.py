def transform_data(df):
    print("🔄 Transforming data...")
    df['experience_level'] = df['age'].apply(lambda x: 'Junior' if x < 30 else 'Senior')
    df['department'] = df['department'].str.lower()
    print("✅ Transformation complete")
    return df
