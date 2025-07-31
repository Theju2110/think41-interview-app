import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import DepartmentPage from './pages/DepartmentPage';
import DepartmentList from './components/DepartmentList';

function App() {
  return (
    <Router>
      <div className="app-container">
        <DepartmentList />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/departments/:id" element={<DepartmentPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
