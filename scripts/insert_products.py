import pandas as pd
import mysql.connector
import os
import sys

# Add the parent directory to the path so we can import from config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.db_config import db_config

# Load the CSV file
csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.csv')
df = pd.read_csv(csv_file)

# Replace NaNs with None (NULL in SQL)
df = df.where(pd.notnull(df), None)

# Connect to MySQL
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO products (
            id, cost, category, name, brand,
            retail_price, department, sku, distribution_center_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for index, row in df.iterrows():
        cursor.execute(insert_query, (
            row['id'],
            row['cost'],
            row['category'],
            row['name'],
            row['brand'],
            row['retail_price'],
            row['department'],
            row['sku'],
            row['distribution_center_id']
        ))

    connection.commit()
    print("✅ All rows inserted successfully.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()