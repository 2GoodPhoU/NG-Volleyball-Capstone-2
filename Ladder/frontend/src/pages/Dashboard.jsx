
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';


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
              <div key={team.id} className="division-box" >
                <Link to={`/team/${team.id}`} style={{ color: 'var(--color-white)' }}>
                  <strong>{team.name}</strong> - Created by: {team.captain_username}
                </Link>
              </div>
            ))}
        </div>
        <Link to="/createteam">
        <button className="btn btn-primary">Create Team</button>
      </Link>
    </div>
  );
};

export default Dashboard;
      