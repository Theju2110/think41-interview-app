import axios from 'axios';

const API_BASE = 'http://127.0.0.1:5000'; // Make sure backend is running

export const getProducts = () => axios.get(`${API_BASE}/products`);
export const getProductById = (id) => axios.get(`${API_BASE}/products/${id}`);
