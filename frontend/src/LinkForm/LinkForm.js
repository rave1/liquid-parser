import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import { Formik, Field, Form } from 'formik';
import axios from 'axios';
import { ItemCard } from '../ItemCard/ItemCard';

export const LinkForm = () => {
  const [products, setProducts] = useState([])
  console.log(products)
  return (
    <>
      <Formik
        initialValues={{
          url: 'https://example.com'
        }}
        onSubmit={(values) => {
          // alert(JSON.stringify(values, null, 2));
          axios.post('http://127.0.0.1:5000/', {
            url: values.url
          }).then(
            res => {
              setProducts(previous => [...previous, res.data.data])
            }
          )
        }}
      >
        <Form>
          <label htmlFor="firstName">Link</label>
          <Field id="url" name="url" placeholder="http://example.com" type="url" />
          <button type="submit">Submit</button>
        </Form>
      </Formik>
      {products.length > 0 && products.map((each) => (
        <ItemCard title={each.title} available={each.available} url={each.url} />
      ))}
    </>


  ) 
}