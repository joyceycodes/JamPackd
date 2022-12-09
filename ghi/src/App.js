import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './css/App.css';
import MainPage from './mainpage'
import SignupComponent from "./accounts/signup"
import LoginComponent from "./accounts/login"
import RecommendationsForm from './music/RecommendationsForm';
import AccountPageComponent from "./accounts/accountpage"
import Navigation from './nav';
import { useState, useEffect } from 'react'
// import SpotifyButton from './music/SpotifyExport';
import PlaylistDetail from './music/PlaylistDetail';
import CreatePlaylist from './music/CreatePlaylist';
import UpdatePlaylist from './music/UpdatePlaylist';


const domain = /https:\/\/[^/]+/;
const basename = process.env.PUBLIC_URL.replace(domain, '');

function App() {
  const [username, setUsername] = useState();

  useEffect(() => {
    setUsername();
  }, [])

  return (
    <BrowserRouter basename={basename}>
      <Navigation />
      <div >
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="accounts">
            <Route path="/accounts/login" element={<LoginComponent />} />
            <Route path="/accounts/signup" element={<SignupComponent SignupForm={SignupComponent} />} />
            <Route path="/accounts/accountpage" element={<AccountPageComponent AccountPageComponent={AccountPageComponent} />} />
          </Route>
          <Route path="music">
            <Route path="/music/recommendations" element={<RecommendationsForm />} />
            <Route path="/music/playlist/new" element={<CreatePlaylist />} />
            <Route path="/music/playlist/:playlist_id" element={<PlaylistDetail />} />
            <Route path="/music/playlist/update/:playlist_id" element={<UpdatePlaylist />} />
          </Route>
          {/* /* <Route path="/new_playlist" element={} */}
        </Routes >
      </div >

    </BrowserRouter >
  );
}


export default App;
