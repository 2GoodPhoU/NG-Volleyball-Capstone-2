import React, { useState, useEffect, Component } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
//import './container.css' ;
//import { ranktable } from 'components';
import ranktable from '../components/ranktable'
import CustomizedTables from '../components/ranktable';


const DivisionDetailsPage = () => {
  const [divisionDetails, setDivisionDetails] = useState({});
  const { name } = useParams();

  useEffect(() => {
    const fetchDivisionDetails = async () => {
      try {
        // Fetch division details
        const divisionResponse = await axios.get(`http://localhost:8000/division/${name}/`);
        console.log('Division Details API response:', divisionResponse.data);
        setDivisionDetails(divisionResponse.data);

        // Fetch teams in the division along with their positions
        const teamsResponse = await axios.get(`http://localhost:8000/teamindivision/${name}/`);
        console.log('Teams in Division API response:', teamsResponse.data);
        
        // Create an array to store team details with names
        const teamsWithNames = await Promise.all(teamsResponse.data.map(async team => {
          const teamDetailsResponse = await axios.get(`http://localhost:8000/team/${team.team}/`);
          const teamDetails = teamDetailsResponse.data;
          return { ...team, team_name: teamDetails.name };
        }));
        
        setDivisionDetails(prevState => ({
          ...prevState,
          teams: teamsWithNames
        }));
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
      <h2>Teams in Division</h2>
      <ul>
        {divisionDetails.teams && divisionDetails.teams.map(team => (
          <li key={team.team}>
            Team: {team.team_name}, Position: {team.position}
          </li>
        ))}
      </ul>
      
      <Link to="/joindivision">
        <button className="btn btn-primary">Join Division</button>
      </Link>
  
          <CustomizedTables />

      <article id="container">
    
<section>
    <div>Player 1</div>
    <div>Player 2</div>
    <div>Player 3</div>
    <div>Player 4</div>
    <div>Player 5</div>
    <div>Player 6</div>
    <div>Player 7</div>
    <div>Player 8</div>
</section>

<div class="connecter">
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</div>

<div class="line">
    <div>
    </div><div>
    </div><div>
    </div><div>
    </div>
</div>

<section id="quarterFinals">
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</section>

<div class="connecter" id="conn2">
    <div></div>
    <div></div>
</div>

<div class="line" id="line2">
    <div></div>
    <div></div>
</div>

<section id="semiFinals">
    <div></div>
    <div></div>
</section>

<div class="connecter" id="conn3">
    <div></div>
</div>

<div class="line" id="line3">
    <div></div>
</div>

<section id="final">
<div></div>
</section>

</article>



    </div>
  );
};

export default DivisionDetailsPage;
