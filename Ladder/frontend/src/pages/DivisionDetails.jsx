// DivisionDetailsPage.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const DivisionDetailsPage = () => {
  const [divisionDetails, setDivisionDetails] = useState({});
  const { name } = useParams();

  useEffect(() => {
    const fetchDivisionDetails = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/division/${name}/`);
        console.log('Division Details API response:', response.data);
        setDivisionDetails(response.data);
      } catch (error) {
        console.error('Error fetching division details:', error);
      }
    };

    fetchDivisionDetails();
  }, [name]);

  return (
    <div>
      <h1>{divisionDetails.name} Details</h1>
      <p>Admin: {divisionDetails.admin_email}</p>
      {/* Add more details as needed */}
    </div>
  );
};

export default DivisionDetailsPage;
