from config.db_config import db_config
import sys
import os

# Add parent directory (project root) to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mysql.connector

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Step 1: Get department name-to-id mapping
cursor.execute("SELECT id, name FROM departments")
department_map = {name: id for id, name in cursor.fetchall()}

# Step 2: Get all product ids and departments
cursor.execute("SELECT id, department FROM products")
products = cursor.fetchall()

# Step 3: Update each product with correct department_id
for product_id, department_name in products:
    department_id = department_map.get(department_name)
    if department_id:
        try:
            cursor.execute(
                "UPDATE products SET department_id = %s WHERE id = %s",
                (department_id, product_id)
            )
        except Exception as e:
            print(f"Failed to update product {product_id}: {e}")

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Update complete.")
