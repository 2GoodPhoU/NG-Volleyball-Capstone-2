import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LadderPage from "./Ladder";
import ProfilePage from "./myProfile";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<p>This is the home page</p>} />
          <Route path="/ladder" element={<LadderPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </Router>
    );
  }
}
