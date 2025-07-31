from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TA**u2710",  # Add your MySQL password if it's set
    database="ecommerce"
)

# Route to test the backend
@app.route('/')
def home():
    return "Welcome to the E-commerce API!"

# Route to get product by ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cursor.fetchone()
    cursor.close()

    if product:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
