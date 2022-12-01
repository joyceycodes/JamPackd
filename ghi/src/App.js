import React from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import SignupForm from './accounts/signup';
import './css/App.css';
import MainPage from './mainpage';

const domain = /https:\/\/[^/]+/;
const basename = process.env.PUBLIC_URL.replace(domain, '');

function App() {


  return (
    <div>
      <BrowserRouter basename={basename}>
        <Routes>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </BrowserRouter>
    </div >

  );
}

export default App;
