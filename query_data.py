import pandas as pd
from sqlalchemy import create_engine

# Database credentials
db_user = 'postgres'
db_password = 'Kaju2284!' 
db_host = 'localhost'
db_port = '5432'
db_name = 'smart_retail'

try:
    # Connect to PostgreSQL
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    # Write a SQL query to find the top 5 most profitable product categories
    query = """
        SELECT "Category", SUM("Sales") as Total_Sales, SUM("Profit") as Total_Profit
        FROM superstore_sales
        GROUP BY "Category"
        ORDER BY Total_Profit DESC;
    """
    
    # Run the query and load results directly into a Pandas DataFrame
    df_result = pd.read_sql(query, engine)
    
    print("--- Top Categories by Profit (Queried from PostgreSQL) ---")
    print(df_result)

except Exception as e:
    print(f"An error occurred: {e}")