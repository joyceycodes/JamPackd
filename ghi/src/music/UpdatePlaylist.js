import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../accounts/auth.js";
import { useNavigate } from "react-router-dom";
function UpdatePlaylist() {
    let { playlist_id } = useParams();
    const { token } = useAuthContext()
    const navigate = useNavigate();
    const [name, setName] = useState("");
    const [comments, setComments] = useState("");

    const handleUpdate = async (e) => {
        e.preventDefault();
        const data = {
            name,
            comments,
        }
        const url = `${process.env.REACT_APP_MUSIC}/api/playlists/${playlist_id}`
        const fetchConfig = {
            method: "put",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        };
        const response = await fetch(url, fetchConfig)
        console.log(response)
        if (response.ok) {
            const updatedPlaylist = await response.json();
            console.log(updatedPlaylist)
            navigate(`/music/playlist/${updatedPlaylist.id}`)

        }
    }


    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Update Playlist</h1>
                    <form onSubmit={handleUpdate}>
                        <div className="mb-3 form-floating">
                            <input onChange={(e) => setName(e.target.value)} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
                            <label htmlFor="name">New Playlist Name</label>
                        </div>
                        <div className="mb-3 form-floating">
                            <textarea onChange={(e) => setComments(e.target.value)} placeholder="Comments" required name="comments" id="comments" className="form-control" />
                            <label htmlFor="name">New Playlist Comments</label>
                        </div>
                        <button className="btn btn-outline-dark">Submit</button>
                    </form>
                </div>
            </div >
        </div>
    )
}


export default UpdatePlaylist;