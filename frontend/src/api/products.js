const BASE_URL = 'http://localhost:5000/api';

export async function fetchProduct(id) {
  const res = await fetch(`${BASE_URL}/products/${id}`);
  if (!res.ok) throw new Error('Failed to fetch product');
  return await res.json();
}
