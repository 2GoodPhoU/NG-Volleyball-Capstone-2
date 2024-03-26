import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { toast } from 'react-toastify'
import { useNavigate} from 'react-router-dom'


const TeamDetailsPage = () => {
  const [teamDetails, setTeamDetails] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const { id } = useParams();
  const { userInfo } = useSelector((state) => state.auth);
  const navigate = useNavigate()


  useEffect(() => {
    const fetchTeamDetails = async () => {
      setLoading(true);
      try {
        console.log('Team ID:', id);
        const response = await axios.get(`http://localhost:8000/team/${id}/`);
        console.log('Team Details API response:', response.data);
        setTeamDetails(response.data);
      } catch (error) {
        console.error('Error fetching team details:', error);
        setError('Error fetching team details. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchTeamDetails();
  }, [id]);

  const handleJoinTeam = async () => {
    try {
      const response = await axios.post(`http://localhost:8000/team/join_team/${id}/${userInfo.id}/`);
      console.log('Join Team API response:', response.data);
      // Update team details after joining
      setTeamDetails(response.data);
      toast.success("Successfully joined")

      navigate("/dashboard")
    } catch (error) {
      console.error('Error joining team:', error);
      setError('Error joining team. Please try again later.');
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>{teamDetails.name} Details</h1>
      <div>
        <h2>Name: {teamDetails.name}</h2>
          <p>Captain: {teamDetails.captain_username}</p>
          <p>Members: <br /></p>
              <ul>
                {teamDetails.member_usernames && teamDetails.member_usernames.map(username => (
                  <li key={username}>{username}</li>
                ))}
              </ul>
          <button className="btn btn-primary" onClick={handleJoinTeam}>Join Team</button>
      </div>
    </div>
  );
};

export default TeamDetailsPage;
