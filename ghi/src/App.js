import { BrowserRouter, NavLink, Routes, Route } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import { AuthProvider, useToken, useAuthContext } from './accounts/auth.js';
import './css/App.css';
import MainPage from './mainpage'
import SignupForm from "./accounts/signup"
import LoginComponent from "./accounts/login"
import LogoutComponent from './accounts/logout';
import RecommendationsForm from './music/RecommendationsForm';
// import AccountPageComponent from "./accounts/accountpage"

import Navigation from './nav';


const domain = /https:\/\/[^/]+/;
const basename = process.env.PUBLIC_URL.replace(domain, '');

function App() {

  return (
    <BrowserRouter basename={basename}>
      <Navigation />
      < div >
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="accounts">
            <Route path="/accounts/login" element={<LoginComponent LoginComponent={LoginComponent} />} />
            <Route path="/accounts/signup" element={<SignupForm SignupForm={SignupForm} />} />
            <Route path="/accounts/logout" element={<LogoutComponent LogoutComponent={LogoutComponent} />} />
          </Route>
          <Route path="music">
            <Route path="/music/recommendations" element={<RecommendationsForm />} />
          </Route>
          {/* <Route path="/account" element={<AccountPageComponent AccountPageComponent={AccountPageComponent} />} /> */}
          {/* <Route path="/new_playlist" element={} */}
        </Routes>
      </div >

    </BrowserRouter >
  );
}

export default App;
