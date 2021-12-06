import React from 'react';
import { Container } from './ItemCard.styles';
import { Button } from '@material-ui/core';


export const ItemCard = (props) => {
    console.log(props.title)
    return (
        <Container>
            <img src={props.url}/>
            <p>{props.title}</p>
            <select>
            {props.available.length > 0 && props.available.map((each) => (
                    <option>{each}</option>
                ))}
            </select>
            <Button variant="contained" color="primary">Submit</Button>
        </Container>
    )
}