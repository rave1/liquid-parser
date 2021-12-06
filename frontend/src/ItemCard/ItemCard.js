import React from 'react';
import ReactDOM from 'react-dom';
import { Formik, Field, Form } from 'formik';
import axios from 'axios';


export const ItemCard = (props) => {
    console.log(props.title)
    return (
        <div>
            <h1>{props.title}</h1>
            <ul>
                {props.available.length > 0 && props.available.map((each) => (
                    <li>{each}</li>
                ))}
            </ul>
        </div>
    )
}