
import DeleteButton from "./DeleteButton";

import React, { useState, useEffect } from "react";
import SpotifyButton from "./SpotifyExport";
// import { useParams } from "react-router-dom";


function PlaylistDetail() {
    // const { playlist_id } = useParams();
    const [isDeleted, setIsDeleted] = useState(false);

    useEffect(() => {
        setIsDeleted();
    }, [])

    return (
        <>
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
            <br />
            <DeleteButton setIsDeleted={setIsDeleted} />
            <div className={isDeleted ? "alert alert-success mb-0 mt-3" : "alert alert-success d-none mb-0"} id="delete-message">
                Playlist has been deleted.
            </div>

        </>
    )
}

export default PlaylistDetail;