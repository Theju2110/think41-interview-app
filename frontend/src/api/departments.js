// frontend/src/api/departments.js

const BASE_URL = 'http://localhost:5000/api';

export async function fetchDepartment(id) {
  const res = await fetch(`${BASE_URL}/departments/${id}`);
  if (!res.ok) throw new Error('Failed to fetch department');
  return await res.json();
}

export async function fetchDepartmentProducts(id) {
  const res = await fetch(`${BASE_URL}/departments/${id}/products`);
  if (!res.ok) throw new Error('Failed to fetch department products');
  return await res.json();
}
