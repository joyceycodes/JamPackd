
import DeleteButton from "./DeleteButton";

import React from "react";
import SpotifyButton from "./SpotifyExport";


function PlaylistDetail() {
    const pres_songs = localStorage.getItem("pres_songs");
    // const songs = JSON.parse(pres_songs);
    // const songs = pres_songs.map(song => {
    //     return (
    //         song.uri
    //     )
    // })

    return (

        <>
            {/* {console.log(songs)} */}
            {/* {console.log(pres_songs)} */}

            <div className='mt-5 container-sm border 
            border-secondary rounded bold justify-content-center'>

                <h1 className="text-center">My Playlist</h1>
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
                            <tr>
                                <td>
                                    {/* {pres_songs} */}
                                    {/* {pres_songs.title}
                                <iframe title="Current Song" className='container-sm justify-content-center' allow='encrypted-media'
                                    src={`https://open.spotify.com/embed/track/${song.uri}?utm_source=oembed`} >
                                </iframe> */}

                                    {pres_songs?.map(song => {
                                        return (
                                            <tr key={song.uri}>
                                                <td> {song.uri} </td>
                                            </tr>
                                        )
                                    })}


                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>

            {/* <SpotifyButton />
            <DeleteButton /> */}
        </>
    )
}

export default PlaylistDetail;