import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';

function App() {
  return (
    <Router>
      <div>
        <h1>Product App</h1>
        <nav>
          <Link to="/products">View Products</Link>
        </nav>
        <Routes>
          <Route path="/products" element={<ProductList />} />
          <Route path="/products/:id" element={<ProductDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
