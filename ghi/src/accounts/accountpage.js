import { Link } from 'react-router-dom';
import React, { useEffect, useState } from "react";
import { useAuthContext } from "../accounts/auth.js";



export default function AccountPageComponent(props) {
  const [playlists, setPlaylists] = useState([]);
  const { token } = useAuthContext()
  const username = props.username
  console.log("LISTPAGE", username)

  useEffect(() => {
    const playlistDetails = async () => {
      const playlistUrl = `${process.env.REACT_APP_MUSIC}/api/playlists/`;
      const fetchConfig = {
        method: "post",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username })
      };
      const response = await fetch(playlistUrl, fetchConfig);
      if (response.ok) {
        const data = await response.json();
        setPlaylists(data.playlists);
        console.log(data)
      }
    }



    if (token) {
      playlistDetails();
    }
  }, [username, token])


  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Your Jams</th>
        </tr>
      </thead>
      <tbody>
        {playlists.map(pingus => {
          const playlist_id = pingus.id
          return (
            <tr key={pingus.id}>
              <td>
                <Link to={`/music/playlist/${playlist_id}`}>{pingus.name}</Link>
              </td>
            </tr>
          );
        })}
      </tbody>
    </table >
  );
};
