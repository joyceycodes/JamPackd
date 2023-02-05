import { NavLink } from 'react-router-dom';
import LogoutTest from './accounts/newlogout';

function Navigation() {
  return (
    <div className='background'>
      <div className="nav-tabs">
        <ul>
          <NavLink to="/"><img className="JP_logo" src="https://i.imgur.com/HxIEBd3.png" alt="JamPackd Logo"></img></NavLink>
          <LogoutTest />
        </ul>
      </div>
      <div className="nav-container">
      </div>
    </div>

  )
}
export default Navigation;