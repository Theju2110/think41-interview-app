import mysql.connector
from config.db_config import db_config


# Sample data (replace with your actual product data)
products = [
    {"name": "Shampoo", "price": 10.0, "department": "Beauty"},
    {"name": "Football", "price": 25.0, "department": "Sports"},
    {"name": "Lipstick", "price": 12.0, "department": "Beauty"},
    {"name": "Tennis Racket", "price": 50.0, "department": "Sports"},
]

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

# Step 1: Insert unique departments
departments = list(set(p["department"] for p in products))
department_ids = {}

for dept in departments:
    cursor.execute("INSERT IGNORE INTO departments (name) VALUES (%s)", (dept,))
    db.commit()
    cursor.execute("SELECT id FROM departments WHERE name = %s", (dept,))
    department_ids[dept] = cursor.fetchone()[0]

# Step 2: Update products table (if not already updated)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        price FLOAT,
        department_id INT,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
""")

# Step 3: Insert products with department_id
for product in products:
    dept_id = department_ids[product["department"]]
    cursor.execute(
        "INSERT INTO products (name, price, department_id) VALUES (%s, %s, %s)",
        (product["name"], product["price"], dept_id)
    )

db.commit()
cursor.close()
db.close()
