import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const TeamDetailsPage = () => {
  const [teamDetails, setTeamDetails] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const { id } = useParams();

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
      </div>
    </div>
  );
};

export default TeamDetailsPage;
