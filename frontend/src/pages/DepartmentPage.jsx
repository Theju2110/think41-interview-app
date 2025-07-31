import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { fetchDepartment, fetchDepartmentProducts } from '../api/departments';
import ProductCard from '../components/ProductCard';
import Loader from '../components/Loader';

export default function DepartmentPage() {
  const { id } = useParams();
  const [department, setDepartment] = useState(null);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

    Promise.all([
      fetchDepartment(id),
      fetchDepartmentProducts(id)
    ])
      .then(([deptData, productsData]) => {
        setDepartment(deptData);
        setProducts(productsData);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching department or products:', err);
        setError('Unable to load department or products.');
        setLoading(false);
      });
  }, [id]);

  if (loading) return <Loader />;
  if (error) return <p>{error}</p>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">
        {department ? `${department.name} (${products.length} products)` : 'Department'}
      </h1>

      {products.length === 0 ? (
        <p>No products found in this department.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      )}
    </div>
  );
}
