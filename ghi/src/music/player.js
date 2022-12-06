import { NavLink } from 'react-router-dom'
import React from "react";
import { useState } from "react";
import RecommendationsForm from "./RecommendationsForm";

// import "../css/Player.css"

const uri = [
    "5yJM62iiVwUZnfTaNjYbiB",
    "5S5iEaEeqQncFvtEaTDwNe",
    "46rvY1HSdviEjKKFweKWbI",

]
// const songs = ${uri}?utm_source=oembed

// const handleSubmit = async (e) => {
//     e.preventDefault();
//     const data = { genre }
//     const url = "https://open.spotify.com/embed/track/"
//     const uri = [
//         "5yJM62iiVwUZnfTaNjYbiB",
//         "5S5iEaEeqQncFvtEaTDwNe",
//         "46rvY1HSdviEjKKFweKWbI",
//         // will actually need to pass this in from a stored state
//     ]
//     navigate("/playlist");
//     const fetchConfig = {
//         method: "post",
//         body: JSON.stringify(data),
//         headers: {
//             "Content-Type": "application/json",
//         },
//     };

console.log(RecommendationsForm.response);

function SongPlayer() {
    return (
        <div className='container-sm border border-secondary rounded bold justify-content-center'>
            <h1 className='text-center'>
                Jam Pack'd Player
            </h1>

            <div className='container-sm border border-secondary rounded justify-content-center'>
                <h6 className="text-center">Player contents....</h6>

                <iframe title="Current Song" className='container-sm justify-content-center'
                    src="https://open.spotify.com/embed/track/5S5iEaEeqQncFvtEaTDwNe?utm_source=oembed" >
                </iframe>

                {/* Buttons */}
                <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                    <button class="btn btn-danger me-md-2" type="button">Skip</button>

                    <button class="btn btn-primary" type="button">Like</button>
                </div>
                <br />
                <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                    <button class="btn btn-success me-md-2" type="button">Done/Make Playlist</button>
                </div>

            </div>
            <div className="text-center">Text 2</div>

        </div >
    )
}


export default SongPlayer;



