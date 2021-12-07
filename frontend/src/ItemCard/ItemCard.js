import React, { useState } from 'react';
import axios from 'axios';
import { Container, FormInput } from './ItemCard.styles';
import { Card, CardActions, CardContent, Button, Typography, Avatar, Grid, makeStyles, TextField } from '@material-ui/core';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

const useStyles = makeStyles((theme) => ({
    formControl: {
      margin: theme.spacing(1),
      minWidth: 120,
    },
    selectEmpty: {
      marginTop: theme.spacing(2),
    },
    root: {
        minWidth: 275,
        margin: 10,
      },
      bullet: {
        display: 'inline-block',
        margin: '0 2px',
        transform: 'scale(0.8)',
      },
      title: {
        fontSize: 14,
      },
      pos: {
        marginBottom: 12,
      },
  }));
  

export const ItemCard = (props) => {
    console.log(props.title)
    
    const classes = useStyles();
    const [select, setSelect] = useState(props.available[0])
    const [quant, setQuant] = useState(0)
    const [product, setProducts] = useState([{
        name: '',
        flavour: '',
        quantity: quant
    }])
    console.log(product)

    const handleChange = (event) => {
        setSelect(event.target.value);
        setProducts({
            name: props.title,
            flavour: event.target.value,
            quantity: quant
        })
    }

    const handleSubmit = () => {
        setProducts({
            name: props.title,
            flavour: select,
            quantity: quant
        })
    }

    const sendProduct = () => {
        axios.post('http://127.0.0.1:5000/save', {product})
    }

    return (
        <Card className={classes.root}>
            <CardContent>
                <Grid container alignItems="center" direction="column">
                    <Avatar style={{width: "150px", height: "150px"}} src={props.url}/>
                </Grid>
                <Typography vartian="h5" component="h2">{props.title}</Typography>
                    <FormInput>
                        <FormControl variant="filled" className={classes.formControl} size="small">
                            <InputLabel id="demo-simple-select-filled-label">Available</InputLabel>
                            <Select
                            labelId="demo-simple-select-filled-label"
                            id="demo-simple-select-filled"
                            value={select}
                            onChange={handleChange}
                            >
                                {props.available.length > 0 && props.available.map((each) => (
                                    <MenuItem value={each}>{each}</MenuItem>
                                ))}
                            </Select>
                            <TextField id="filled-basic" label="Quantity" variant="filled" value={quant} onChange={(event) => setQuant(event.target.value)} />
                            <Button variant="contained" color="primary" type="submit" onClick={handleSubmit}>Submit</Button>
                        </FormControl>
                    </FormInput>
                    <Button variant="contained" color="primary" type="submit" onClick={sendProduct}>state</Button>
            </CardContent>
        </Card>
    )
}