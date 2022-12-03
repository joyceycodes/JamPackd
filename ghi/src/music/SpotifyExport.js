import React from "react";


function SpotifyButton() {

    const handleExport = async (e) => {

        e.preventDefault();

        const url = "http://localhost:8003/login"
        const fetchConfig = {
            method: "get",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            const data = await response.json()
            window.location.replace(data)
        }

    }

    return (
        <button onClick={handleExport}>Export to Spotify</button>
    )
}

export default SpotifyButton;