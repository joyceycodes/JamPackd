import { NavLink } from 'react-router-dom';
import LogoutTest from './accounts/newlogout';

function Navigation() {
    return (
        <div>
            <div className="nav-container">
                <div className="nav-tabs is-centered">
                    <ul>
                        <li><button><NavLink to="/">Home Page</NavLink></button></li>
                        <li><button><NavLink to="/accounts/signup">Signup</NavLink></button></li>
                        <li><LogoutTest /></li>
                        <li><button><NavLink to="/accounts/accountpage">My Account</NavLink></button></li>
                        {/* <li><button><NavLink to="/accounts/account">My Account</NavLink></button></li> */}
                        {/* /* <li><NavLink to="/new_playlist">Create a new Playlist</NavLink></li> */}
                        {/* <li><NavLink to="/playlist">My Playlists</NavLink></li> */}
                        {/* there are more to add!!!  */}
                        |
                        <li><button><NavLink to="/music/recommendations">Get Songs!</NavLink></button></li>
                    </ul>
                </div>
            </div>
        </div>
    )
}
export default Navigation;