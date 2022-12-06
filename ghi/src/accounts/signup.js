import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useToken, useAuthContext } from "./auth"

function SignupComponent() {
  const navigate = useNavigate();
  const [, , signup] = useToken()
  const { token } = useAuthContext

  let [full_name, setFullName] = useState();
  let [password, setPassword] = useState();
  let [username, setUsername] = useState();

  const submitHandler = async (e) => {
    e.preventDefault();
    await signup(full_name, username, password);
    // if (token) {
    //   console.log("token", token)

    // } else {
    //   console.log("word")
    // }

    // navigate("/accounts/account")

  };

  return (
    <div>
      <center>
        <h2>Sign Up for JamPack'd</h2>
        <form onSubmit={submitHandler}>
          Full Name: <input
            type="text"
            name="full_name"
            placeholder="John Doe"
            value={full_name}
            onChange={(event) => setFullName(event.target.value)}
          />
          <br />
          Email Address <input
            type="text"
            name="username"
            placeholder="john@doe.com"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
          />
          <br />
          Password: <input
            type="password"
            name="password"
            placeholder="ilikepizza123"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
          <br />
          <input type="submit" name="submit" />
        </form>
      </center>
    </div>
  );
};


export default SignupComponent;
