import sys
import os

# Add project root (parent of api/) to sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from config.db_config import db_config

app = Flask(__name__)
CORS(app)

# Use db_config dict for connection parameters
db = mysql.connector.connect(**db_config)
cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return "Backend is running"

@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute("SELECT id, name, retail_price FROM products LIMIT 20")
    products = cursor.fetchall()
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
