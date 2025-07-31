// src/components/DepartmentsList.jsx
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { fetchDepartments } from '../api/departments';
import Loader from './Loader';

export default function DepartmentsList() {
  const [departments, setDepartments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDepartments()
      .then(data => {
        setDepartments(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load departments', err);
        setLoading(false);
      });
  }, []);

  if (loading) return <Loader />;

  return (
    <div className="my-4">
      <h2 className="text-xl font-bold mb-2">Departments</h2>
      <ul className="flex flex-wrap gap-2">
        {departments.map(dept => (
          <li key={dept.id}>
            <Link to={`/departments/${dept.id}`} className="px-3 py-1 border rounded hover:bg-gray-100">
              {dept.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
