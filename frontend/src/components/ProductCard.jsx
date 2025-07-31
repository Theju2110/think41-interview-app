export default function ProductCard({ product }) {
  return (
    <div className="card">
      <h3>{product.name}</h3>
      <p>Brand: {product.brand}</p>
      <p>Price: ₹{product.cost}</p>
    </div>
  );
}
