from src.ingestion import load_data
from src.etl import clean_data
from src.fraud_detection import detect_fraud
from src.database import save_to_db

df = load_data("data/raw_transactions.csv")
df = clean_data(df)
df = detect_fraud(df)

save_to_db(df)

print("Pipeline executed successfully")
