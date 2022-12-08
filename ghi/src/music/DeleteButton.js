import React from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../accounts/auth.js";

function DeleteButton(props) {
    let { playlist_id } = useParams();
    const { token } = useAuthContext()

    const handleDelete = async (e) => {
        e.preventDefault();
        const url = `${process.env.REACT_APP_MUSIC}/api/playlists/${playlist_id}`
        const fetchConfig = {
            method: "delete",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {

            props.setIsDeleted(true)
        }
    }

    return (
        <button onClick={handleDelete}>Delete</button>
    )
}
export default DeleteButton
