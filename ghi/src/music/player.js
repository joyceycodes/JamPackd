// import { NavLink } from 'react-router-dom'

function SongPlayer() {
    return (
        <div className='container-sm border border-secondary rounded justify-content-center'>
            <h1 className='text-center'>
                Jam Pack'd Player
            </h1>
            <div className='container-sm border border-secondary rounded justify-content-center'>

                <h6 className="text-center">Player contents....</h6>

                <iframe className='container-sm border border-secondary rounded justify-content-center' src="https://open.spotify.com/embed/track/1LDeuD3jbSpHucsd0nOt6t?utm_source=oembed">
                </iframe>

            </div>



            <div></div>
            <div></div>
            <div className="text-center">Text 2</div>

        </div>
    )
}

export default SongPlayer;



