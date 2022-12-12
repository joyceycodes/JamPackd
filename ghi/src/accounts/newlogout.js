import { useAuthContext, useToken } from "./auth";
import { NavLink } from 'react-router-dom';


export default function LogoutTest() {
  const { token } = useAuthContext()

  const [, logout] = useToken()
  const checkout = async e => {
    e.preventDefault()
    await logout()
    console.log("logged out")
  }

  if (token) {
    return (
      <div>
        <div className="nav-tabs">
          <button type="button" className="btn btn-light"><NavLink to="/accounts/accountpage">My Playlists</NavLink></button>
          <button type="button" style={{ color: "light-blue", margin: "8px", }} className="btn btn-light" onClick={checkout}>Logout</button>
        </div>
      </div >
    )
  } else {
    return (
      <div className="nav-tabs">
        <button type="button" className="btn btn-light"><NavLink to="/accounts/login">Login</NavLink></button>
        <button type="button" className="btn btn-light"><NavLink to="/accounts/signup">Signup</NavLink></button>
      </div>
    )
  }
}
