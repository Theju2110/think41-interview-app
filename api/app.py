from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TA**u2710",
    database="ecommerce"
)
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
