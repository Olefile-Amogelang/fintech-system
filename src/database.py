import sqlite3

def save_to_db(df):
    conn = sqlite3.connect("transactions.db")
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    conn.close()