import { NavLink } from 'react-router-dom'

function AccountPageComponent() {
  return (
    <div>
      <div className='nav-container'>
        <div className='nav-tabs is-centered'>
          <ul>
            <li><button><NavLink to="/">Home Page</NavLink></button></li>
            <li><button><NavLink to="/logout">Logout</NavLink></button></li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default AccountPageComponent;