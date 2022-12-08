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

//     return (
//         <button onClick={handleDelete} >Delete</button>
//     )
// }
// export default DeleteButton