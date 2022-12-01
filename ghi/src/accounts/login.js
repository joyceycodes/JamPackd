import { useNavigate } from "react-router-dom";
import { useToken } from "./auth";
import { useState } from "react";

function LoginComponent() {
  let navigate = useNavigate();
  let [token, login] = useToken();
  console.log(token);

  let [email, setEmail] = useState();
  let [password, setPassword] = useState();

  const submitHandler = (e) => {
    login(email, password);
    e.preventDefault();
    navigate("/accountpage");
    // redirect to homepage loggedin, not "/"
  };

  return (
    <div>
      <center>
        <h1>Welcome! Login using your email and password</h1>
        <form onSubmit={submitHandler}>
          <input
            type="text"
            name="email"
            placeholder="Email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
          <br />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
          <br />
          <input type="submit" name="submit" />
        </form>
      </center>
    </div>
  );
}
export default LoginComponent;


// const submitLogin = async () => {
//   const requestOptions = {
//     method: "POST",

//     headers: {
//       "Content-Type": "application/x-www-form-urlencoded",
//       "Authorization": `Bearer ${fastapi_token}`
//     },
//     credentials: "include",
//     body: JSON.stringify(
//       `grant_type=&email=${email}&password=${password}&scope=&client_id=&client_secret=`
//     ),
//   };

//   const response = await fetch(
//     `${process.env.REACT_APP_ACCOUNTS_HOST}/token`,
//     requestOptions
//   );
//   const data = await response.json();
//   if (!response.ok) {
//     setErrorMessage(data.detail);
//   } else {
//     localStorage.setItem("Email", email);
//     setToken(data.access_token);
//     navigate("/accountpage");
//   }
// };

// const submitHandler = (e) => {
//   login(email, password);
//   e.preventDefault();
//   submitLogin();
//   navigate("/accountpage");
//   // redirect to homepage loggedin, not "/"
// };