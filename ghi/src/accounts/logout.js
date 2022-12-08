// import { useNavigate } from "react-router-dom";
// import { useAuthContext } from "./auth";
// let internalToken = null;

// function LogoutComponent() {
//     const navigate = useNavigate();
//     const { token } = useAuthContext();
//     async function logout() {
//         if (token) {
//             const url = `${process.env.REACT_APP_accounts}/api/accounts/me/token/`;
//             await fetch(url, { method: "delete", credentials: "include" });
//             navigate("/");
//         } else {
//             console.log("No token! C:");
//             navigate("/");
//         }
//     }

//     const submitHandler = (e) => {
//         logout();
//         e.preventDefault();
//     };

//     return (
//         <div className="logout-container">
//             <center>
//                 <form onSubmit={submitHandler}>
//                     <p className="Verification">Verify Logout</p>
//                     <button className="logout-btn">Logout</button>
//                 </form>
//             </center>
//         </div>
//     );
// }
// export default LogoutComponent;
