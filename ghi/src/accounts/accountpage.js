import { Link } from 'react-router-dom';
import React, { useEffect, useState } from "react";
import { useAuthContext } from "../accounts/auth.js";
import { NavLink } from 'react-router-dom';

export default function AccountPageComponent() {
  const [playlists, setPlaylists] = useState([]);
  const { token } = useAuthContext()


  useEffect(() => {
    const playlistDetails = async () => {
      const playlistUrl = `${process.env.REACT_APP_MUSIC}/api/playlists/`;
      const fetchConfig = {
        method: "get",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      };
      const response = await fetch(playlistUrl, fetchConfig);
      if (response.ok) {
        const data = await response.json();
        setPlaylists(data.playlists);
      }
    }
    if (token) {
      playlistDetails();
    }

  }, [token])


  return (
    <div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Your Jams</th>
          </tr>
        </thead>
        <tbody>

          {playlists.map(playlist => {
            const playlist_id = playlist.id
            return (
              <tr key={playlist.id}>
                <td>
                  <Link className="text-decoration-none text-muted" to={`/music/playlist/${playlist_id}`}>{playlist.name}</Link>
                </td>
              </tr>
            );
          })}
          <div>
            <button className="btn btn-outline-dark m-2"><NavLink to="/music/recommendations">Create a new playlist!</NavLink></button>
          </div>
        </tbody>
      </table >
    </div>
  );
};
