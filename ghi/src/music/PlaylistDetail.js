
import DeleteButton from "./DeleteButton";

import DeleteButton from "./DeleteButton";
import React, { useState, useEffect } from "react";
// import SpotifyButton from "./SpotifyExport";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../accounts/auth.js";


function PlaylistDetail() {
    let { playlist_id } = useParams();
    const { token } = useAuthContext()
    const [isDeleted, setIsDeleted] = useState(false);
    const [playlist, setPlaylist] = useState({})

    useEffect(() => {
        const getPlaylist = async () => {
            const url = `http://localhost:8003/api/playlists/${playlist_id}`
            const fetchConfig = {
                method: "get",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            };
            const response = await fetch(url, fetchConfig)
            if (response.ok) {
                const playlistDetails = await response.json();
                console.log(playlistDetails)
                setPlaylist(playlistDetails)
            }
        }
        if (token) {
            getPlaylist();
        }
        setIsDeleted();
    }, [playlist_id, token])


    return (
        <>
            <div className='mt-5 container-sm border 
            border-secondary rounded bold justify-content-center'>

                <h1 className="text-center">{playlist.name}</h1>
                <p className="text-center">{playlist.comments}</p>
                {/* <p className="text-center">{playlist.songs}</p> */}
                <div className='mt-5 container-sm border 
            border-secondary rounded bold justify-content-center'>
                    <table className="table table-striped 
                    justify-content-center">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Artist</th>
                                <th>Player</th>
                            </tr>
                        </thead>
                        <tbody>

                            {pres_songs.map(song => {
                                return (
                                    <tr key={song.uri}>
                                        <td> {song.uri} </td>
                                    </tr>
                                )
                            })};
                            <td>
                                {/* {pres_songs} */}
                                {/* {pres_songs.title}
                                <iframe title="Current Song" className='container-sm justify-content-center' allow='encrypted-media'
                                    src={`https://open.spotify.com/embed/track/${pres_songs.uri}?utm_source=oembed`} >
                                </iframe> */}
                            </td>
                        </tbody>
                    </table>
                </div>



            </div>



            {/* {console.log(songs)} */}
            {console.log(pres_songs)}

            <div className='mt-5 container-sm border 
            border-secondary rounded bold justify-content-center'>

                <h1 className="text-center">My Playlist- Pass in Dynamically Later</h1>
                <div className='mt-5 container-sm border 
            border-secondary rounded bold justify-content-center'>
                    <table className="table table-striped 
                    justify-content-center">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Artist</th>
                                <th>Player</th>
                            </tr>
                        </thead>
                        <tbody>

                            {pres_songs.map(song => {
                                return (
                                    <tr key={song.uri}>
                                        <td> {song.uri} </td>
                                    </tr>
                                )
                            })};
                            <td>
                                {/* {pres_songs} */}
                                {/* {pres_songs.title}
                                <iframe title="Current Song" className='container-sm justify-content-center' allow='encrypted-media'
                                    src={`https://open.spotify.com/embed/track/${pres_songs.uri}?utm_source=oembed`} >
                                </iframe> */}
                            </td>
                        </tbody>
                    </table>
                </div>



            </div>



            <SpotifyButton />
        </>
    )
}

export default PlaylistDetail;
