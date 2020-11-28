import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";

import Navbar from "./components/Navigation/navbar";
import CategoryDetail from "./components/Category/CategoryDetail";
import PostDetail from "./components/Posts/PostDetail";


function App() {

  return (
    <div className="App">
        <Router>
            <Navbar />
            <Switch>
                <Route path="/blogpost/:id" exact component={PostDetail} />
                <Route path="/category/:id" exact component={CategoryDetail} />
            </Switch>
        </Router>
    </div>
  );
}

export default App;
