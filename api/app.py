from flask import Flask, jsonify
import mysql.connector
from config.db_config import db_config

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_all_products():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return jsonify(products)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        if product:
            return jsonify(product)
        else:
            return jsonify({'message': 'Product not found'}), 404
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
