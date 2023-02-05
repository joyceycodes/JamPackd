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
        <div>
          <button type="button" className="btn btn-light m-2"><NavLink to="/accounts/accountpage">My Playlists</NavLink></button>
          <button type="button" className="btn btn-light m-2" onClick={checkout}>Logout</button>
        </div>
      </div >
    )
  } else {
    return (
      <div>
        <button type="button" className="btn btn-light m-2 mt-4"><NavLink to="/accounts/login">Login</NavLink></button>
        <button type="button" className="btn btn-light m-2 mt-4"><NavLink to="/accounts/signup">Signup</NavLink></button>
      </div>

    )
  }
}
