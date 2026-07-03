import pandas as pd
from sqlalchemy import create_engine

# 1. Read the CSV file from your laptop
print("Reading your CSV file...")
# Make sure this matches your actual CSV file name!
df = pd.read_csv('ipl_stats.csv') 

# 2. Connect to your local PostgreSQL database
# Replace 'your_password' with your actual postgres password
engine = create_engine('postgresql://postgres:dinesh123@localhost:5433/dataengg_db')

# 3. Dump the data straight into the 'raw' schema
print("Loading data into PostgreSQL raw schema...")
df.to_sql('ipl_raw_stats', engine, schema='raw', if_exists='replace', index=False)

print("Success! Your raw data is now safely inside PostgreSQL.")