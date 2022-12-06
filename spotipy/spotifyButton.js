// import React, { useEffect, useState } from "react";
// // import { useLocation } from 'react-router-dom'

// function SpotifyButton() {
//     const [url, setUrl] = useState('')

//     const getAuthUrl = async (e) => {

//         e.preventDefault();

//         const endpointUrl = "http://localhost:8003/login"
//         const fetchConfig = {
//             method: "get",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//         };
//         const response = await fetch(endpointUrl, fetchConfig)
//         if (response.ok) {
//             const data = await response.json()
//             // window.location.replace(data)
//             // sessionStorage.setItem("code", window.location.href)
//             window.location.href = data
//             return data
//         }
//     }

//     // }

//     const getAccessToken = async (e) => {
//         // e.preventDefault();
//         const currentUrl = window.location.href
//         setUrl(currentUrl)
//         if (currentUrl.includes('http://localhost:3000/music/playlist?code=')) {

//             const playlistUrl = "http://localhost:8003/music/playlist"

//             const fetchConfig = {
//                 method: "post",
//                 headers: {
//                     "Content-Type": "application/json",
//                 },
//                 body: currentUrl,
//             }
//             console.log(fetchConfig)
//             const response = await fetch(playlistUrl, fetchConfig)
//             if (response.ok) {
//                 const data = await response.json()
//                 console.log(data)
//                 return response
//             }
//         } else {
//             setUrl(currentUrl)
//         }

//     }


//     const getUserId = async (e) => {
//         e.preventDefault();
//         const url = "http://localhost:8003/user"
//         const fetchConfig = {
//             method: "get",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//         };
//         const response = await fetch(url, fetchConfig)
//         if (response.ok) {
//             const data = await response.json()
//             console.log(data)
//         }
//     }
//     // const createPlaylist = async (e, token) => {
//     //     e.preventDefault();
//     //     let uris = [
//     //         "spotify:track:5Z3GHaZ6ec9bsiI5BenrbY",
//     //     ]

//     //     const playlistUrl = "http://localhost:8003/playlist"

//     //     const fetchConfig = {
//     //         method: "post",
//     //         body: JSON.stringify(uris),
//     //         headers: {
//     //             "Content-Type": "application/json",
//     //         },
//     //     }
//     //     console.log(fetchConfig)
//     //     const response = await fetch(playlistUrl, fetchConfig)
//     //     if (response.ok) {
//     //         console.log(response)
//     //     }
//     // }

//     const runFunctions = async (e) => {
//         try {
//             await getAuthUrl(e);
//             // await getAccessToken(e);
//             await getUserId(e);
//         }
//         catch (error) {
//             console.log(error)
//         }
//     }

//     useEffect(() => {
//         getAccessToken();
//     }, [setUrl]);

//     return (
//         <button onClick={runFunctions}>Export to Spotify</button>
//     )

// }

// export default SpotifyButton;

/* OPTION 2 
import React, { useState, useEffect } from "react";

const authEndpoint = 'https://accounts.spotify.com/authorize';
// Replace with your app's client ID, redirect URI and desired scopes
const clientId = "26c21b44542b466295adedc6ee996cb2";
const redirectUri = "http://localhost:3000/music/playlist";
const scopes = [
    "playlist-modify-private", "playlist-modify-public",
];


function SpotifyButton() {
    const [token, setToken] = useState('')
        const hash = window.location.hash
        let token = window.localStorage.getItem("token")
        // how to get token from url (when we have a hashtag and no token)
        if (!token && hash) {
            token = hash.substring(1).split("&").find(elem => elem.startsWith("access_token")).split("=")[1]
            // set hash token to an empty string
            window.location.hash = ""
            // save token to local storage
            window.localStorage.setItem("token", token)
        }
        setToken(token)
    }, [])


    return (
        <div className="App">

            <a
                className="btn btn-outline-dark"
                href={`${authEndpoint}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopes.join("%20")}&response_type=code&show_dialog=true`}
            >
                Login to Spotify
            </a>

            {/* {this.state.token && (
                    <iframe title="Current Song" className='container-sm justify-content-center'
                        src="https://open.spotify.com/embed/track/4U4h7WNNyvhpdaDgHSdD4j?utm_source=oembed" >
                    </iframe>
                    // Spotify Player Will Go Here In the Next Step
                )} 
        </div >
    ); 
    }

export default SpotifyButton;
    */