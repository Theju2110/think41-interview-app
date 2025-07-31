from flask import Flask, jsonify
import mysql.connector
import sys
import os

# Add the project root to the system path so Python can find the 'config' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the database config
from config.db_config import db_config

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Product API'}), 200

@app.route('/products', methods=['GET'])
def get_products():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(products), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)
