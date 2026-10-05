import pandas as pd
from sqlalchemy import create_engine

# 1. CSV filename
csv_filename = 'Sample - Superstore.csv' 

# 2. PostgreSQL credentials 
# (Default username is usually 'postgres', and password is the one you set during installation)
db_user = 'postgres'
db_password = 'Kaju2284!' 
db_host = 'localhost'
db_port = '5432'
db_name = 'smart_retail'

try:
    print("Loading CSV file...")
    df = pd.read_csv(csv_filename, encoding='latin1')
    
    # Create the connection engine to PostgreSQL
    print("Connecting to PostgreSQL...")
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    # Send the dataframe to a SQL table named 'superstore_sales'
    print("Uploading data to the 'superstore_sales' table...")
    df.to_sql('superstore_sales', engine, if_exists='replace', index=False)
    
    print("\n--- Success! Data successfully loaded into PostgreSQL! ---")

except Exception as e:
    print(f"An error occurred: {e}")