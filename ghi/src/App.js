import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import { useEffect, useState } from 'react';
// import { AuthProvider, useToken, useAuthContext } from './accounts/auth.js';
import './css/App.css';
import MainPage from './mainpage'
import SignupComponent from "./accounts/signup"
import LoginComponent from "./accounts/login"
import LogoutComponent from './accounts/logout';
import SongPlayer from './music/player';

import RecommendationsForm from './music/RecommendationsForm';
import AccountPageComponent from "./accounts/accountpage"

import Navigation from './nav';
// import SpotifyButton from './music/SpotifyExport';
import PlaylistDetail from './music/PlaylistDetail';


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
            <Route path="/accounts/signup" element={<SignupComponent SignupForm={SignupComponent} />} />
            <Route path="/accounts/logout" element={<LogoutComponent LogoutComponent={LogoutComponent} />} />
            <Route path="/accounts/account" element={<AccountPageComponent AccountPageComponent={AccountPageComponent} />} />

          </Route>
          <Route path="music">
            <Route path="/music/recommendations" element={<RecommendationsForm />} />
            <Route path="/music/player" element={<SongPlayer />} />
            <Route path="/music/playlist" element={<PlaylistDetail />} />
          </Route>
          {/* /* <Route path="/new_playlist" element={} */}
        </Routes>
      </div >

    </BrowserRouter >
  );
}

export default App;
