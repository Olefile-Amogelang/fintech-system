def clean_data(df):
    df = df.dropna()
    df['transaction_amount'] = df['transaction_amount'].astype(float)
    return df