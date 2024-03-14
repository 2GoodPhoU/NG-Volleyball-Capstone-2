// Assuming you have a Redux store with user information available

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';

const Dashboard = () => {
  const [userTeams, setUserTeams] = useState([]);
  const { userInfo } = useSelector((state) => state.auth);

  useEffect(() => {
    const fetchUserTeams = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/team/user_teams/${userInfo.id}/`);
        console.log('Response:', response.data);
        setUserTeams(response.data);
      } catch (error) {
        console.error('Error fetching user teams:', error);
        // Handle errors
      }
    };
        fetchUserTeams();
    }, [userInfo]);

  return (
    <div>
      <h1 className='main__title'> {userInfo.first_name} Teams</h1>
        <div className="division-container">
            {userTeams.map((team) => (
            <div key={team.id} className="division-box" style={{ color: 'var(--color-white)' }}>
                Team: {team.name} <br />
                Captain: {team.captain_username} 
            </div>
            ))}
        </div>
    </div>
  );
};

export default Dashboard;
      