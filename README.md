    
    sudo apt install nodejs
    sudo apt install npm
    
    
    npx create-react-app mainapp-ui
    
    npm start
    npm run build
    
    collectstatic
    runserver
    
    pip install djangorestframework
    npm install axios
    
    npm install --save bootstrap


















    
    
postman

    HEADERS
        Content-Type: application/json
    
    BODY (raw, json)        
        {
            "name": "Trash",
            "slug": "trash"
        }


for api test

    import React, { useState, useEffect } from 'react';
    const [people, setPeople] = useState([])
    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/test-api/"
        }).then(response => {
            setPeople(response.data)
        })
    }, [])
    
    
    <ul>
        {people.map(p => (
            <li key={p.id}>{p.name}</li>
        ))}
    </ul>

    
get data

    const [categories, setCategories] = useState([])

    useEffect(() => {
        axios({
            method: "GET",
            url: 'http://127.0.0.1:8000/api/category/'
        }).then(responce => {
            setCategories(responce.data)
        })
    }, [])
    console.log(categories)


React Router Dom

    npm install --save react-router-dom
    
    app.js
        import {BrowserRouter as Router, Switch, Route} from "react-router-dom";

    
    navbar.js
        import { Link } from "react-router-dom";
        <Link to={{ pathname: `/category/${c.id}`, fromDashboard: false }}>{c.name}</Link>
        <a className="nav-link" href="#" key={c.id}>{c.name}</a>