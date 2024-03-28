import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

const JoinDivisionPage = () => {
  const [userTeams, setUserTeams] = useState([]);
  const [selectedTeam, setSelectedTeam] = useState('');
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

  const handleTeamSelect = (event) => {
    setSelectedTeam(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Logic to submit the selected team to join a division
      const response = await axios.post(`http://localhost:8000/team-in-division/join_division/${selectedTeam}/`);
      console.log('Join division response:', response.data);
      // Handle success or display a message to the user
    } catch (error) {
      console.error('Error joining division:', error);
      // Handle errors
    }
  };

  return (
    <div>
      <h1>{userInfo.first_name} Teams</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="teamSelect">Select a Team to Join Division: <br/></label>
        <select id="teamSelect" value={selectedTeam} onChange={handleTeamSelect}>
          <option value="">Select a Team</option>
          {userTeams.map((team) => (
            <option key={team.id} value={team.id}>{team.name}</option>
          ))}
        </select>
        <br/>
        <button className="btn btn-primary">Join Division</button>
      </form>
      <br/>
      <Link to="/createteam">
        <button className="btn btn-primary">Create Team</button>
      </Link>    </div>
  );
};

export default JoinDivisionPage;
