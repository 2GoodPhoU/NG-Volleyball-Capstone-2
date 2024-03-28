import React, { Component } from "react";
import { Fragment } from 'react';
import * as React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LadderPage from "./Ladder";
import LoginPage from "./Login";
import { CssBaseline } from "@mui/material/CssBaseline";
import { Box } from "@mui/material/Box";
import { Container } from "@mui/material/Container";

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
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Router>
    );
  }
}
