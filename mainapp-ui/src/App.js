import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";

import Navbar from "./components/Navigation/navbar";
import CategoryDetail from "./components/Category/CategoryDetail";


function App() {

  return (
    <div className="App">
        <Router>
            <Navbar />
            <Switch>
                <Route path="/category/:id" exact component={CategoryDetail} />
            </Switch>
        </Router>
    </div>
  );
}

export default App;
