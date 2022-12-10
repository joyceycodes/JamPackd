import { NavLink } from 'react-router-dom';
import LogoutTest from './accounts/newlogout';

function Navigation() {
  return (
    <div>
      <div className="logo-container"><img className="JP_logo" src="https://i.imgur.com/HxIEBd3.png"></img></div>
      <div className="nav-container">
        <div className="nav-tabs">
          <ul>
            <li><button><NavLink to="/">Home Page</NavLink></button></li>
            <li><LogoutTest /></li>
            <li><button><NavLink to="/music/recommendations">Get Songs!</NavLink></button></li>
          </ul>
        </div>
      </div>
    </div>
  )
}
export default Navigation;