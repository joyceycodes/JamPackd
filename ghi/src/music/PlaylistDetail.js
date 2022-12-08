import React from "react";
import DeleteButton from "./DeleteButton";
import SpotifyButton from "./SpotifyExport";


function PlaylistDetail(props) {

    return (
        <>
            <h1>My Playlist</h1>
            <SpotifyButton />
            <DeleteButton />
        </>
    )
}

export default PlaylistDetail;