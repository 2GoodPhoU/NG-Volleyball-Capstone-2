import { useSelector } from 'react-redux'  
// const { userInfo } = useSelector((state) => state.auth)

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const TeamPage = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await axios.get('http://localhost:8000/team/');
        console.log('Teams API response:', response.data);
        setTeams(response.data);
      } catch (error) {
        console.error('Error fetching Teams:', error);
      }
    };

    fetchTeams();
  }, []);

  return (
    <div>
      <h1 className="main__title" >Teams</h1>
      <div className="division-container">
        {teams.map((team) => (
          <div key={team.name} className="division-box">
            <Link to={`/team/${team.id}`} style={{ color: 'var(--color-white)' }}>
              <strong>{team.name}</strong> - Created by: {team.captain_username}
            </Link>
          </div>
        ))}
      </div>

      <button className="btn btn-primary" type="submit">
          Create Team
        </button>
    </div>
  );
};

export default TeamPage;
