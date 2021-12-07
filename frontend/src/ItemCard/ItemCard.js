import React from 'react';
import { Container } from './ItemCard.styles';
import { Card, CardActions, CardContent, Button, Typography, Avatar, Grid } from '@material-ui/core';

export const ItemCard = (props) => {
    console.log(props.title)
    return (
        <Card>
            <CardContent>
                <Grid container alignItems="center" direction="column">

                <Avatar style={{width: "50px", height: "50px"}} src={props.url}/>
                <Typography vartian="h5" component="h2">{props.title}</Typography>
                <select>
                {props.available.length > 0 && props.available.map((each) => (
                        <option>{each}</option>
                    ))}
                </select>
                <Button variant="contained" color="primary">Submit</Button>
                </Grid>
            </CardContent>
        </Card>
    )
}