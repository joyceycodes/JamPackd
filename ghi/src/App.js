import React from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import SignupForm from './accounts/signup';

import './css/App.css';
import MainPage from './mainpage';

function App() {

  // useEffects like below to get data about playlists shown on frontpage?

  // useEffect(() => {
  //   async function getOrderData() {
  //     let url = `${process.env.REACT_APP_API_HOST_MONOLITH}/api/orders`;
  //     let response = await fetch(url);
  //     let data = await response.json();
  //     if (response.ok) {
  //       setOrders(data)
  //     }
  //   }
  //   getOrderData();
  // }, [])



  return (
    <BrowserRouter>
      <div>
        <div className="container">
          <div className="tabs is-centered" style={{ display: "flex" }}>
            <ul>
              <li><NavLink to="/">Home Page</NavLink></li>
              <li><NavLink to="/cart">Shop Produce</NavLink></li>
              <li><NavLink to="/produce-admin">Admin Produce</NavLink></li>
              <li><NavLink to="/orders">Orders</NavLink></li>
              <li><NavLink to="/login">Login</NavLink></li>
              <li><NavLink to="/logout">Logout</NavLink></li>
              <li><NavLink to="/signup">Signup</NavLink></li>
            </ul>
          </div>
        </div>
        <Routes>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
