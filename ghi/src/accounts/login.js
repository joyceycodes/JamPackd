import { useNavigate } from "react-router-dom";
import { useToken } from "./auth";
import { useState } from "react";

function LoginComponent() {
  let navigate = useNavigate();
  let [, login] = useToken();
  let [username, setUsername] = useState();
  let [password, setPassword] = useState();

  const submitHandler = (e) => {
    login(username, password);
    e.preventDefault();
    navigate("/accounts/accountpage");
  };

  return (
    <div>
      <center>
        <h1>Welcome! Login using your username and password</h1>
        <form onSubmit={submitHandler}>
          <input
            type="text"
            name="username"
            placeholder="Email"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
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