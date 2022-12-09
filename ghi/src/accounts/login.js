import { useNavigate } from "react-router-dom";
import { useToken } from "./auth";
import { useState } from "react";

function LoginComponent(props) {
  const navigate = useNavigate();
  const [login] = useToken();

  // const [username, setUsername] = useState();
  const [password, setPassword] = useState();

  const submitHandler = async (e) => {
    e.preventDefault();
    await login(props.username, password)
    navigate("/accounts/accountpage");
  };

  return (
    <div>
      <center>
        <h1>Welcome! Login using your email and password</h1>
        <form onSubmit={submitHandler}>
          <input
            type="text"
            name="username"
            placeholder="Email"
            value={props.username}
            onChange={(event) => props.setUsername(event.target.value)}
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