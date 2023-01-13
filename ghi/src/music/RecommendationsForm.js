import React from "react";
import { useState } from "react";
import { useAuthContext } from "../accounts/auth";
import Player from "./Player.js";
import { Audio } from 'react-loader-spinner'

function RecommendationsForm() {
    const { token } = useAuthContext()
    const [loading, setLoading] = useState(false);
    const [genre, setGenre] = useState("");
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
        setLoading(true);
        const data = { genre }
        const url = `${process.env.REACT_APP_MUSIC}/recommendations`
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            setLoading(false)
            const recommendations = await response.json();
            setSongs(recommendations)
        }
    }

    if (token) {
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
                        </form>
                        {loading &&
                            < Audio
                                className="justify-content-center"
                                height="50"
                                width="80"
                                color='blue'
                                ariaLabel='three-dots-loading' />}
                    </div>

                    <br />
                    <Player songs={songs} />
                </div>
                <br />
                <br />
            </div >
        )
    }
}

export default RecommendationsForm;
