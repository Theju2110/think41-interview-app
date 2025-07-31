from flask import Flask, jsonify
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.db_config import DB_CONFIG

app = Flask(__name__)

# Create MySQL connection
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route('/')
def index():
    return "Welcome to Think41 API!"


# -------------------- PRODUCTS ENDPOINTS --------------------

@app.route('/products')
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)


@app.route('/products/<int:product_id>')
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404


# -------------------- DEPARTMENT ENDPOINTS --------------------

@app.route('/api/departments')
def get_departments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(departments)


@app.route('/api/departments/<int:department_id>')
def get_department_by_id(department_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departments WHERE id = %s", (department_id,))
    department = cursor.fetchone()
    cursor.close()
    conn.close()
    if department:
        return jsonify(department)
    else:
        return jsonify({'error': 'Department not found'}), 404


@app.route('/api/departments/<int:department_id>/products')
def get_products_by_department(department_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.* FROM products p
        JOIN departments d ON p.department_id = d.id
        WHERE d.id = %s
    """, (department_id,))
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    if products:
        return jsonify(products)
    else:
        return jsonify({'error': 'No products found for this department'}), 404


# -------------------- MAIN --------------------

if __name__ == '__main__':
    app.run(debug=True)
