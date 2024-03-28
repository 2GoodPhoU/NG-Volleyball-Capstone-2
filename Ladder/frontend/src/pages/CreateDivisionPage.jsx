import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import axios from 'axios';

const CreateDivisionPage = () => {
  const { userInfo } = useSelector((state) => state.auth);
  const [userData, setUserData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    username: '', // Add username field to the state
    profile_pic: null,
  });

  useEffect(() => {
    // Fetch existing user data when the component mounts
    axios.get(`http://localhost:8000/user/${userInfo.id}/`)
      .then((response) => {
        const existingUserData = response.data;
        setUserData(existingUserData);
      })
      .catch((error) => {
        console.error('Error fetching user data:', error);
      });
  }, [userInfo.id]);

  const handleUsernameChange = (newUsername) => {
    // Update only the username in the local state
    setUserData((prevUserData) => ({
      ...prevUserData,
      username: newUsername,
    }));
  };

  const handleProfilePicChange = (e) => {
    // Update the profile_pic in the local state
    setUserData((prevUserData) => ({
      ...prevUserData,
      profile_pic: e.target.files[0],
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Create FormData to include existing profile_pic
    const formData = new FormData();
    formData.append('first_name', userData.first_name);
    formData.append('last_name', userData.last_name);
    formData.append('email', userData.email);
    formData.append('username', userData.username); // Add username
    formData.append('profile_pic', userData.profile_pic);

    // Send the updated user data back to the server
    axios.put(`http://localhost:8000/user/${userInfo.id}/`, formData)
      .then((response) => {
        console.log('Profile updated successfully:', response.data);
      })
      .catch((error) => {
        console.error('Error updating profile:', error);
        // Handle errors as needed
      });
  };

  return (
    <div className="container auth__container">
      <h1 className='main__title'>Edit Your Profile</h1>
      <p>Hello {userInfo.first_name}, your ID is {userInfo.id}</p>

      <form className="auth__form" onSubmit={handleSubmit}>
        {/* Display existing user data in input fields */}
        <div>
          {/* Input for username */}
          Username:
          <input
            type="text"
            value={userData.username}
            onChange={(e) => handleUsernameChange(e.target.value)}
          />
        </div>
        <div>
          {/* Input for profile_pic */}
          Profile Picture:
          <input
            type="file"
            accept="image/*"
            onChange={handleProfilePicChange}
          />
        </div>
        <button className="btn btn-primary" type="submit">
          Create Division
        </button>
      </form>
    </div>
  );
};

export default CreateDivisionPage;
