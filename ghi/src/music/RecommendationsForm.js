import React from "react";
import { useState } from "react";
import Player from "./Player.js";

function RecommendationsForm() {

    const [genre, setGenre] = useState("");
    // const [recommendations, SetReccs] = useState({});

    const [songs, setSongs] = useState([]);


    const genres = [
        "acoustic",
        "afrobeat",
        "alt-rock",
        "alternative",
        "ambient",
        "anime",
        "black-metal",
        "bluegrass",
        "blues",
        "bossanova",
        "brazil",
        "breakbeat",
        "british",
        "cantopop",
        "chicago-house",
        "children",
        "chill",
        "classical",
        "club",
        "comedy",
        "country",
        "dance",
        "dancehall",
        "death-metal",
        "deep-house",
        "detroit-techno",
        "disco",
        "disney",
        "drum-and-bass",
        "dub",
        "dubstep",
        "edm",
        "electro",
        "electronic",
        "emo",
        "folk",
        "forro",
        "french",
        "funk",
        "garage",
        "german",
        "gospel",
        "goth",
        "grindcore",
        "groove",
        "grunge",
        "guitar",
        "happy",
        "hard-rock",
        "hardcore",
        "hardstyle",
        "heavy-metal",
        "hip-hop",
        "holidays",
        "honky-tonk",
        "house",
        "idm",
        "indian",
        "indie",
        "indie-pop",
        "industrial",
        "iranian",
        "j-dance",
        "j-idol",
        "j-pop",
        "j-rock",
        "jazz",
        "k-pop",
        "kids",
        "latin",
        "latino",
        "malay",
        "mandopop",
        "metal",
        "metal-misc",
        "metalcore",
        "minimal-techno",
        "movies",
        "mpb",
        "new-age",
        "new-release",
        "opera",
        "pagode",
        "party",
        "philippines-opm",
        "piano",
        "pop",
        "pop-film",
        "post-dubstep",
        "power-pop",
        "progressive-house",
        "psych-rock",
        "punk",
        "punk-rock",
        "r-n-b",
        "rainy-day",
        "reggae",
        "reggaeton",
        "road-trip",
        "rock",
        "rock-n-roll",
        "rockabilly",
        "romance",
        "sad",
        "salsa",
        "samba",
        "sertanejo",
        "show-tunes",
        "singer-songwriter",
        "ska",
        "sleep",
        "songwriter",
        "soul",
        "soundtracks",
        "spanish",
        "study",
        "summer",
        "swedish",
        "synth-pop",
        "tango",
        "techno",
        "trance",
        "trip-hop",
        "turkish",
        "work-out",
        "world-music",
    ]

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = { genre }
        const url = "http://localhost:8003/recommendations"
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            const recommendations = await response.json();
            // console.log(recommendations)
            setSongs(recommendations)
            // sessionStorage.setItem("recommendations", recommendations)
        }
    }

    // example_url = "https://open.spotify.com/embed/track/5S5iEaEeqQncFvtEaTDwNe?utm_source=oembed"

    const url_pre = "https://open.spotify.com/embed/track/"

    const url_post = "?utm_source=oembed"

    // values passed in from the response after getting genres
    var uris = [
        "5S5iEaEeqQncFvtEaTDwNe",
        "reterrg"]


    var song_count = 0
    const em_link = (url_pre + uris[song_count] + url_post);







    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Start jammin'!</h1>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <select onChange={(e) => setGenre(e.target.value)} required id="genre" name="genre" className="form-select">
                                <option value="">Select a genre</option>
                                {genres.map(genre => {
                                    return (
                                        <option value={genre} key={genre}>
                                            {genre}
                                        </option>
                                    )
                                })}
                            </select>
                        </div>
                        <button className="btn btn-outline-dark">Submit</button>
                        {/* Try to make it so the player doesn't show until after the button is pressed" */}
                    </form>

                    {/* <div >
                        <iframe title="something" src="https://open.spotify.com/embed/playlist/5a2OuIJ1kEttA8X3PaewlI?utm_source=oembed" allowfullscreen allow="clipboard-write; encrypted-media; fullscreen; picture-in-picture;">
                        </iframe>
                    </div> */}



                </div>
                <br />
                <div className='container-sm border border-secondary rounded bold justify-content-center'>
                    <h1 className='text-center'>
                        Jam Pack'd Player
                    </h1>

                    <div className='container-sm border border-secondary rounded justify-content-center'>
                        <h6 className="text-center">Player contents....</h6>



                        <iframe title="Current Song" className='container-sm justify-content-center' allow="encrypted-media"
                            src={em_link} >
                        </iframe>

                        {/* Buttons */}
                        <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                            <button className="btn btn-danger me-md-2" type="button">Skip</button>
                            {/* if button is pressed song_count ++ 1 */}

                            <button className="btn btn-primary" type="button">Like</button>
                            {/* if button is pressed song_count ++ 1 AND Add song to liked category*/}

                        </div>
                        <br />
                        <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                            <button className="btn btn-success me-md-2" type="button">Done/Make Playlist</button>
                            {/* Redirect to PlaylistDetail */}
                        </div>

                    </div>
                    <div className="text-center">Text 2</div>

                </div >
            </div >
            <br />
            <Player songs={songs} />


        </div>
    )
}

export default RecommendationsForm;