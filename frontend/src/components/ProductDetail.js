import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/products/${id}`)
      .then(response => response.json())
      .then(data => setProduct(data));
  }, [id]);

  if (!product) return <p>Loading...</p>;

  return (
    <div>
      <h2>{product.name}</h2>
      <p>Brand: {product.brand}</p>
      <p>Category: {product.category}</p>
      <p>Price: ₹{product.retail_price}</p>
      <p>Department: {product.department}</p>
      <p>SKU: {product.sku}</p>
    </div>
  );
}

export default ProductDetail;
