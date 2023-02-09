import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Player(songs) {
    const navigate = useNavigate();
    const [like, setLike] = useState(0);
    const [skip, setSkip] = useState(0);
    const [count, setCount] = useState(0)
    const [likedSongs, setLikedSongs] = useState([])

    const song = songs.songs

    const handleLike = (e) => {
        return (
            setLike(like + 1),
            setCount(count + 1),
            setLikedSongs(likedSongs => [...likedSongs, song[count]])
        )
    }

    const handleSkip = (e) => {
        return (setSkip(skip + 1), setCount(count + 1))
    }

    const getPlayer = () => {
        const currentSong = song[count]
        while (count < song.length)
            return (
                <div>

                    <iframe title="Current Song" className='container-sm justify-content-center' allow='encrypted-media'
                        src={`https://open.spotify.com/embed/track/${currentSong.uri}?utm_source=oembed`} >
                    </iframe>

                    <div className="d-grid gap-1 d-md-flex justify-content-md-center">
                        <button className="btn btn-danger me-md-2" type="button" onClick={handleSkip}>Skip</button>
                        <button className="btn btn-primary me-md-2" type="button" onClick={handleLike}>Like</button>
                    </div>
                    <br />

                </div>
            )
    }


    const handleSubmit = () => {
        window.localStorage.setItem("uris", JSON.stringify(likedSongs))
        navigate("/music/playlist/new")
    }

    while (song.length > 0) {
        return (
            <div className='mt-4 mb- 2 container-sm border border-secondary rounded bold justify-content-center'>
                <h1 className='text-center'>
                    Jam Pack'd Player
                </h1>

                <div className='mt-5 container-sm border border-secondary rounded bold justify-content-center'>
                    <br />
                    {/* <h6 className="text-center">Player contents....</h6> */}

                    <div>
                        {getPlayer()}
                    </div>

                    <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                        <button className="btn btn-success me-md-2" type="button" onClick={handleSubmit}>Done/Make Playlist</button>
                    </div>
                    <br />
                </div>
                <br />
            </div >
        )
    }
}
export default Player;