import { useEffect, useState } from 'react';
import { fetchAllProducts } from '../api/products';
import ProductCard from '../components/ProductCard';
import Loader from '../components/Loader';

export default function HomePage() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAllProducts().then(data => {
      setProducts(data);
      setLoading(false);
    });
  }, []);

  if (loading) return <Loader />;

  return (
    <div>
      <h1>All Products</h1>
      <div className="product-grid">
        {products.map(p => <ProductCard key={p.id} product={p} />)}
      </div>
    </div>
  );
}
