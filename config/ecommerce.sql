CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

CREATE TABLE products (
    id INT PRIMARY KEY,
    cost DECIMAL(10, 2),
    category VARCHAR(100),
    name VARCHAR(255),
    brand VARCHAR(100),
    retail_price DECIMAL(10, 2),
    department VARCHAR(100),
    sku VARCHAR(100),
    distribution_center_id INT
);
SELECT * FROM products LIMIT 10;
show tables;
