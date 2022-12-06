import React, { useState } from "react";

function Player(songs) {
    const [like, setLike] = useState(0);
    const [skip, setSkip] = useState(0);
    const [count, setCount] = useState(0)

    const song = songs.songs

    const handleLike = (e) => {
        // uris.push(song[count])
        return (
            setLike(like + 1),
            setCount(count + 1)
        )
    }

    const handleSkip = (e) => {
        return (setSkip(skip + 1), setCount(count + 1))
    }

    const getPlayer = () => {
        const currentSong = song[count]
        while (song.length > 0) {
            return (
                <iframe title="Current Song" className='container-sm justify-content-center' allow='encrypted-media'
                    src={`https://open.spotify.com/embed/track/${currentSong.uri}?utm_source=oembed`} >
                </iframe>

            )
        }
    }

    return (

        <div className='mt-5 container-sm border border-secondary rounded bold justify-content-center'>
            <h1 className='text-center'>
                Jam Pack'd Player
            </h1>

            <div className='mt-5 container-sm border border-secondary rounded bold justify-content-center'>
                <h6 className="text-center">Player contents....</h6>

                <div>
                    {getPlayer()}
                </div>



                {/* Buttons */}
                <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                    <button className="btn btn-danger me-md-2" type="button" onClick={handleSkip}>Skip</button>
                    <button className="btn btn-primary" type="button" onClick={handleLike}>Like</button>
                </div>
                <br />
                <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                    <button className="btn btn-success me-md-2" type="button">Done/Make Playlist</button>
                    {/* Redirect to PlaylistDetail */}
                </div>

            </div>
            <div className="text-center">Text 2</div>

        </div >


    )

}
export default Player;