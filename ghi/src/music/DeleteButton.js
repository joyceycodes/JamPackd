// import React from "react";
// // import { useLocation } from 'react-router-dom'

// function DeleteButton() {
//     const handleDelete = async (e) => {
//         e.preventDefault();
//         const playlist_id = 123
//         const url = `http://localhost:8003/api/playlists/${playlist_id}`
//         const fetchConfig = {
//             method: "delete",
//         };
//         const response = await fetch(url, fetchConfig)
//         if (response.ok) {
//             const deleted = await response.json();
//             console.log("Deleted", deleted)
//         }
//     }
import React from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../accounts/auth.js";

function DeleteButton(props) {
    let { playlist_id } = useParams();
    const { token } = useAuthContext()

    const handleDelete = async (e) => {
        e.preventDefault();
        const url = `http://localhost:8003/api/playlists/${playlist_id}`
        const fetchConfig = {
            method: "delete",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            // const deleted = await response.json();
            // console.log("Deleted", deleted)
            props.setIsDeleted(true)
        }
    }

    //     return (
    //         <button onClick={handleDelete} >Delete</button>
    //     )
    // }
    // export default DeleteButton
    return (
        <button onClick={handleDelete}>Delete</button>
    )
}
export default DeleteButton