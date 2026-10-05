import pandas as pd

# IMPORTANT: Replace 'your_filename.csv' with the exact name of the file you downloaded 
filename = 'Sample - Superstore.csv'

# Note: Using encoding='latin1' or 'utf-8' helps avoid common reading errors with CSV files
try:
    df = pd.read_csv(filename, encoding='latin1')
    print("--- Successfully loaded the dataset! ---\n")
    
    print("--- First 5 rows of your data ---")
    print(df.head())
    
    print("\n--- Dataset Info (Columns and Data Types) ---")
    print(df.info())
    
    print("\n--- Total rows and columns ---")
    print(df.shape)

except Exception as e:
    print(f"An error occurred: {e}. Make sure the filename matches exactly!")