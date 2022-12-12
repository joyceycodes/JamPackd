import { NavLink } from 'react-router-dom';
import LogoutTest from './accounts/newlogout';

function Navigation() {
  return (
    <div className='background'>
      <div className="logo-container"><NavLink to="/"><img className="JP_logo" src="https://i.imgur.com/HxIEBd3.png" alt="JamPackd Logo"></img></NavLink></div>
      <div className="nav-container">
        <div className="nav-tabs">
          <ul>
            <li><LogoutTest /></li>
            <li><button type="button" className="btn btn-light"><NavLink to="/music/recommendations">Get Songs!</NavLink></button></li>
          </ul>
        </div>
      </div>
    </div>
  )
}
export default Navigation;