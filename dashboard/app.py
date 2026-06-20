import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("../transactions.db")
df = pd.read_sql("SELECT * FROM transactions", conn)

st.title("Transaction Monitoring Dashboard")

st.metric("Total Transactions", len(df))
st.metric("Fraud Cases", df['fraud_flag'].sum())

st.dataframe(df)
