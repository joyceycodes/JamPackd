import { useNavigate } from "react-router-dom";
import { useAuthContext } from "./auth";
let internalToken = null;
console.log(internalToken);

function LogoutComponent() {
    const navigate = useNavigate();
    const { token } = useAuthContext();
    console.log(token)
    async function logout() {
        if (token) {
            console.log(token)
            // console.log("token found");
            // const url = `${process.env.REACT_APP_accounts}/api/accounts/me/token/`;
            // await fetch(url, { method: "delete", credentials: "include" });
            // // internalToken = null;
            // setToken(null);
            // navigate("/");
        } else {
            console.log("No token");
            navigate("/");
        }
    }

    const submitHandler = (e) => {
        logout();
        e.preventDefault();
    };

    return (
        <div className="logout-container">
            <center>
                <form onSubmit={submitHandler}>
                    <p className="Verification">Verify Logout</p>
                    <button className="logout-btn">Logout</button>
                </form>
            </center>
        </div>
    );
}
export default LogoutComponent;
