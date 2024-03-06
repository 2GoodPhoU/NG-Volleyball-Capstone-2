import React, {Component} from "react";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Input from "@mui/material/Input";

export default class LoginPage extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return<Grid container spacing={1}>
            <Grid item xs={12} align = "center">
                <Typography component='h4' variant='h4'>
                    Login
                </Typography>
            </Grid>
            <Grid item xs={12} align = "center">
                <FormControl fullWidth color='success' required='true'>
                <InputLabel>Username: </InputLabel>
                <Input /> 
                </FormControl> 
                <FormControl fullWidth color='success' required='true' variant='filled'>
                <InputLabel>Password: </InputLabel>
                <Input /> 
                </FormControl> 
            </Grid>
        </Grid>
    }
}
