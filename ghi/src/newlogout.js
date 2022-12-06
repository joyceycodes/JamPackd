import { useAuthContext, useToken } from "./accounts/auth";

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


                    <p className="Verification">Verify Logout</p>
                    <button onClick={checkout} className="logout-btn">Logout</button>


                </div>
            </div>
        )
    } else {
        return (
            <div>
                goodbye
            </div>
        )
    }
}