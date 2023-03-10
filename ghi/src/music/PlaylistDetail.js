import DeleteButton from "./DeleteButton";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../accounts/auth.js";
import { useNavigate } from "react-router-dom";

function PlaylistDetail() {
    const navigate = useNavigate();
    const { playlist_id } = useParams();
    const { token } = useAuthContext()
    const [isDeleted, setIsDeleted] = useState(false);
    const [playlist, setPlaylist] = useState({})

    useEffect(() => {
        const getPlaylist = async () => {

            const url = `${process.env.REACT_APP_MUSIC}/api/playlists/${playlist_id}`

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
                setPlaylist(playlistDetails)
            }
        }
        if (token) {
            getPlaylist();
        }
        setIsDeleted();
    }, [playlist_id, token])

    const handleUpdate = () => {
        navigate(`/music/playlist/update/${playlist_id}`)

    }


    return (
        <>
            <div className='container-sm 
            border-secondary rounded bold justify-content-center'>

                <h1 className="text-center m-4">{playlist.name}</h1>
                <p className="text-center">{playlist.comments}</p>
                <div className="d-flex justify-content-center row">
                    <button type="button" className="btn btn-light m-2 col-4" onClick={handleUpdate}>Update</button>
                    <br />
                    <DeleteButton setIsDeleted={setIsDeleted} />
                    <div class="w-100"></div>
                    <div className={isDeleted ? "alert alert-danger mb-0 mt-3 col-5" : "alert alert-success d-none mb-0"} id="delete-message">
                        Playlist has been deleted.
                    </div>
                </div>
                <div className='mt-3 container-sm border 
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
                            {playlist.songs?.map(song => {
                                return (
                                    <tr key={song.uri}>
                                        <td>{song.name}</td>
                                        <td>{song.artist}</td>
                                        <td>
                                            <iframe title="Current Song" className='container-sm justify-content-center' allow='encrypted-media'
                                                src={`https://open.spotify.com/embed/track/${song.uri}?utm_source=oembed`} >
                                            </iframe>
                                        </td>
                                    </tr>
                                )
                            })}
                        </tbody>

                    </table>
                </div>
            </div>


        </>
    )
}


export default PlaylistDetail;
