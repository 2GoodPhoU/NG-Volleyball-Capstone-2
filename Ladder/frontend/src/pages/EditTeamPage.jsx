// pages/EditTeamPage.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EditTeamPage = () => {
  const [name, setName] = useState('');
  const [captainName, setCaptainName] = useState('');
  const teamId = 1; // Hardcoded team ID for testing

  useEffect(() => {
    // Fetch existing team data based on the hardcoded teamId
    axios.get(`http://localhost:8000/team/${teamId}/`)
      .then((response) => {
        const existingTeam = response.data;
        setName(existingTeam.name);
        setCaptainName(existingTeam.captain_name);
      })
      .catch((error) => {
        console.error('Error fetching team data:', error);
      });
  }, [teamId]);

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.put(`http://localhost:8000/team/${teamId}/`, { name, captain_name: captainName }, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        console.log('Team updated successfully:', response.data);
      })
      .catch((error) => {
        console.error('Error updating team:', error);
        if (error.response) {
          console.error('Response data:', error.response.data);
          console.error('Response status:', error.response.status);
          console.error('Response headers:', error.response.headers);
        } else if (error.request) {
          console.error('No response received:', error.request);
        } else {
          console.error('Request setup error:', error.message);
        }
      });
  };

  return (
    <div>
      <h1 className="main__title">Edit Team</h1>
      <form className="auth__form" onSubmit={handleSubmit}>
        Team Name:
        <input
          type="text"
          value={name}
          placeholder="Team Name"
          required
          onChange={(e) => setName(e.target.value)}
        />
        Captain Name:
        <input
          type="text"
          value={captainName}
          placeholder="Captain Name"
          onChange={(e) => setCaptainName(e.target.value)}
          required
        />
        <button className="btn btn-primary" type="submit">Update Team</button>
      </form>
    </div>
  );
};

export default EditTeamPage;
