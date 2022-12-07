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


                    <button onClick={checkout} className="logout-btn">Logout</button>


                </div>
            </div>
        )
    } else {
        return (
            <div>
                <button><NavLink to="/accounts/login">Login</NavLink></button>
            </div>
        )
    }
}