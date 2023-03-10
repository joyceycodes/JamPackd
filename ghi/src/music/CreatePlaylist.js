import React, { useState } from "react";
import { useAuthContext } from "../accounts/auth.js";
import { useNavigate } from "react-router-dom";
import { Audio } from 'react-loader-spinner'

function CreatePlaylist() {
    const { token } = useAuthContext()
    const navigate = useNavigate();
    const [name, setName] = useState("");
    const [comments, setComments] = useState("");
    const [loading, setLoading] = useState(false);
    const songs = JSON.parse(window.localStorage.getItem("uris"))

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true)
        const data = {
            name,
            comments,
            songs,
        }
        const url = `${process.env.REACT_APP_MUSIC}/api/playlists/`

        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)

        if (response.ok) {
            setLoading(false)
            const newPlaylist = await response.json();
            navigate(`/music/playlist/${newPlaylist.id}`)
        }
    }

    if (token) {
        return (
            <div className="row">
                <div className="offset-3 col-6">
                    <div className="shadow p-4 mt-4">
                        <h1>Create Playlist</h1>
                        <form onSubmit={handleSubmit}>
                            <div className="mb-3 form-floating">
                                <input onChange={(e) => setName(e.target.value)} placeholder="Name"
                                    required type="text" name="name" id="name" className="form-control" />
                                <label htmlFor="name">Name</label>
                            </div>
                            <div className="mb-3 form-floating">
                                <textarea onChange={(e) => setComments(e.target.value)} placeholder="Comments" required name="comments" id="comments" className="form-control" rows="5" />
                                <label htmlFor="name">Add your thoughts about this playlist...</label>
                            </div>
                            <button className="btn btn-outline-dark">Submit</button>
                        </form>
                    </div>
                    <div className="d-flex justify-content-center m-3">
                        {loading &&
                            < Audio
                                className="justify-content-center"
                                height="50"
                                width="80"
                                color='blue'
                                ariaLabel='three-dots-loading' />}
                    </div>
                </div >
            </div>
        )
    }
}

export default CreatePlaylist;