import { NavLink } from 'react-router-dom';

function Navigation() {
    return (
        <div>
            <div className="nav-container">
                <div className="nav-tabs is-centered">
                    <ul>
                        <li><button><NavLink to="/">Home Page</NavLink></button></li>
                        <li><button><NavLink to="/signup">Signup</NavLink></button></li>
                        <li><button><NavLink to="/login">Login</NavLink></button></li>
                        <li><button><NavLink to="/account">My Account</NavLink></button></li>
                        {/* /* <li><NavLink to="/new_playlist">Create a new Playlist</NavLink></li> */}
                        {/* <li><NavLink to="/playlists">My Playlists</NavLink></li> */}
                        {/* there are more to add!!!  */}
                    </ul>
                </div>
            </div>
        </div>
    )
}
export default Navigation;