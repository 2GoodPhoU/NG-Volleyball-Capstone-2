import React, { Component } from "react";
import ResponsiveAppBar from "./ResponsiveAppBar";
import { CssBaseline } from "@mui/material";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";

export default class LadderPage extends Component {
    constructor(props) {
        super(props);
    }
    
    render() {
        return (
                <ResponsiveAppBar></ResponsiveAppBar>
        );
    }
}
