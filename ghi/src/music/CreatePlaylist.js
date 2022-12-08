import React, { useState } from "react";
import { useAuthContext } from "../accounts/auth.js";

function CreatePlaylist() {
    const { token } = useAuthContext()

    const [name, setName] = useState("");
    const [comments, setComments] = useState("");
    const songs = JSON.parse(window.localStorage.getItem("uris"))


    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = {
            name,
            comments,
            songs,
        }

        // console.log(data)
        const url = "http://localhost:8003/api/playlists/"
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
            const newPlaylist = await response.json();
            console.log(newPlaylist)
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
                                <textarea onChange={(e) => setComments(e.target.value)} placeholder="Comments"
                                    required name="comments" id="comments" className="form-control" />
                                <label htmlFor="name">Comments</label>
                            </div>
                            <button className="btn btn-outline-dark">Submit</button>
                        </form>
                    </div>
                </div >
            </div>
        )
    }
}

export default CreatePlaylist;