import React, { useEffect, useState } from "react";
// import { useLocation } from 'react-router-dom'

function SpotifyButton() {
    const [url, setUrl] = useState('')

    const getAuthUrl = async (e) => {

        e.preventDefault();

        const endpointUrl = "http://localhost:8003/login"
        const fetchConfig = {
            method: "get",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(endpointUrl, fetchConfig)
        if (response.ok) {
            const data = await response.json()
            // window.location.replace(data)
            window.location.href = data
            window.onload = localStorage.setItem("code", window.location.href)
            return data
        }
    }

    // }

    const getAccessToken = async (e) => {
        // e.preventDefault();
        const currentUrl = window.location.href
        setUrl(currentUrl)
        if (currentUrl.includes('http://localhost:3000/music/playlist?code=')) {

            const playlistUrl = "http://localhost:8003/music/playlist"

            const fetchConfig = {
                method: "post",
                headers: {
                    "Content-Type": "application/json",
                },
                body: currentUrl,
            }
            console.log(fetchConfig)
            const response = await fetch(playlistUrl, fetchConfig)
            if (response.ok) {
                const data = await response.json()
                console.log(data)
                return response
            }
        } else {
            setUrl(currentUrl)
        }

    }


    const getUserId = async (e) => {
        e.preventDefault();
        const url = "http://localhost:8003/user"
        const fetchConfig = {
            method: "get",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            const data = await response.json()
            console.log(data)
        }
    }
    // const createPlaylist = async (e, token) => {
    //     e.preventDefault();
    //     let uris = [
    //         "spotify:track:5Z3GHaZ6ec9bsiI5BenrbY",
    //     ]

    //     const playlistUrl = "http://localhost:8003/playlist"

    //     const fetchConfig = {
    //         method: "post",
    //         body: JSON.stringify(uris),
    //         headers: {
    //             "Content-Type": "application/json",
    //         },
    //     }
    //     console.log(fetchConfig)
    //     const response = await fetch(playlistUrl, fetchConfig)
    //     if (response.ok) {
    //         console.log(response)
    //     }
    // }

    const runFunctions = async (e) => {
        try {
            await getAuthUrl(e);
            // await getAccessToken(e);
            await getUserId(e);
        }
        catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        getAccessToken();
    }, [setUrl]);

    return (
        <button onClick={runFunctions}>Export to Spotify</button>
    )

}

export default SpotifyButton;
