import React from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../accounts/auth.js";

function UpdateButton() {
    let { playlist_id } = useParams();
    const { token } = useAuthContext()

    const handleUpdate = async (e) => {
        e.preventDefault();
        const url = `http://localhost:8003/api/playlists/${playlist_id}`
        const fetchConfig = {
            method: "put",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            // const Updated = await response.json();
            // console.log("Updated", Updated)

        }
    }

    return (
        <button onClick={handleUpdate}>Update</button>
    )
}
export default UpdateButton