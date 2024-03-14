// pages/CreateTeamPage.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux'; // Assuming you have a Redux store

const CreateTeamPage = () => {
  const [name, setName] = useState('');
  const { userInfo } = useSelector((state) => state.auth);

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post(
        'http://localhost:8000/team/',
        { name, captain: userInfo.id }, // Use the logged-in user's ID as the captain
        {
          headers: {
            'Content-Type': 'application/json',
            // Add your authentication headers if needed
            // Authorization: `Bearer ${yourAuthToken}`,
          },
        }
      )
      .then((response) => {
        console.log('Team created successfully:', response.data);
      })
      .catch((error) => {
        console.error('Error creating team:', error);
        // Handle errors
      });
  };

  return (
    <div>
      <h1 className="main__title">Create Team</h1>
      <form className="auth__form" onSubmit={handleSubmit}>
        Team Name:
        <input
          type="text"
          value={name}
          placeholder="Team Name"
          required
          onChange={(e) => setName(e.target.value)}
        />
        <button className="btn btn-primary" type="submit">
          Create Team
        </button>
      </form>
    </div>
  );
};

export default CreateTeamPage;
