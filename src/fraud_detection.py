def detect_fraud(df):
    df['fraud_flag'] = 0

    df.loc[df['transaction_amount'] > 10000, 'fraud_flag'] = 1

    df['transaction_count'] = df.groupby('user_id')['transaction_id'].transform('count')
    df.loc[df['transaction_count'] > 5, 'fraud_flag'] = 1

    return df
