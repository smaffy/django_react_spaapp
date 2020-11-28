
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';


function CategoryDetail({match}) {

    const [category, setCategory] = useState([])
    const id = match.params.id

    useEffect(() => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8000/api/category/${id}/`
        }).then(response => {
            setCategory(response.data)
        })
    }, [id])

  return (
    <div>
        Category with id {category.id}
        <p>Category: <strong>{category.name}</strong></p>
    </div>
  );
}

export default CategoryDetail;
