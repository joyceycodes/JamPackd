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
                <div className="logout-container">


                    <button><NavLink to="/accounts/accountpage">My Account</NavLink></button>
                    <button onClick={checkout} className="logout-btn">Logout</button>


                </div>
            </div>
        )
    } else {
        return (
            <div style={{ justifyContent: "space-between" }}>

                <button className="me-4"><NavLink to="/accounts/login">Login</NavLink></button>
                <button className="ms-4"><NavLink to="/accounts/signup">Signup</NavLink></button>
            </div>
        )
    }
}
