import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/products')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h2>Product List</h2>
      {products.length === 0 ? <p>Loading...</p> : (
        <ul>
          {products.map(product => (
            <li key={product.id}>
              <Link to={`/products/${product.id}`}>{product.name} - ₹{product.retail_price}</Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProductList;
