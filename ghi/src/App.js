import { BrowserRouter, NavLink, Routes, Route } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import { AuthProvider, useToken, useAuthContext } from './accounts/auth.js';
import './css/App.css';
import MainPage from './mainpage'
import SignupComponent from "./accounts/signup"
import LoginComponent from "./accounts/login"
import LogoutComponent from './accounts/logout';
// import AccountPageComponent from "./accounts/accountpage"



const domain = /https:\/\/[^/]+/;
const basename = process.env.PUBLIC_URL.replace(domain, '');

function App() {

  return (
    <BrowserRouter>
      <div>
        <div className="nav-container">
          <div className="nav-tabs is-centered">
            <ul>
              <li><button><NavLink to="/">Home Page</NavLink></button></li>
              <li><button><NavLink to="/signup">Signup</NavLink></button></li>
              <li><button><NavLink to="/login">Login</NavLink></button></li>
              <li><button><NavLink to="/account">My Account</NavLink></button></li>
              {/* /* <li><NavLink to="/new_playlist">Create a new Playlist</NavLink></li> */}
              {/* <li><NavLink to="/playlists">My Playlists</NavLink></li> */}
              {/* there are more to add!!!  */}
            </ul>
          </div>
        </div>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/login" element={<LoginComponent LoginComponent={LoginComponent} />} />
          <Route path="/signup" element={<SignupComponent SignupComponent={SignupComponent} />} />
          <Route path="/logout" element={<LogoutComponent LogoutComponent={LogoutComponent} />} />
          {/* <Route path="/account" element={<AccountPageComponent AccountPageComponent={AccountPageComponent} />} /> */}
          {/* <Route path="/new_playlist" element={} */}
        </Routes>
      </div>
    </BrowserRouter >
  );
}

export default App;
