import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useToken } from "./auth"
import { useAuthContext } from "../accounts/auth.js";
// let internalToken = null;

function SignupComponent() {
  const navigate = useNavigate();
  const [, , signup] = useToken();
  const { token } = useAuthContext();

  let [full_name, setFullName] = useState();
  let [password, setPassword] = useState();
  let [username, setUsername] = useState();

  const submitHandler = async (e) => {
    e.preventDefault();
    await signup(full_name, username, password);
    navigate("/accounts/accountpage")
  };
  if (!token) {

    return (
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Sign Up for JamPack'd</h1>
            <form onSubmit={submitHandler}>
              <div className="mb-3 form-floating">
                <input
                  type="text"
                  name="full_name"
                  placeholder="John Doe"
                  className="form-control"
                  value={full_name}
                  onChange={(event) => setFullName(event.target.value)}
                />
                <label htmlFor="name">Full Name</label>
              </div>
              <div className="mb-3 form-floating">
                <input
                  type="text"
                  name="username"
                  placeholder="john@doe.com"
                  className="form-control"
                  value={username}
                  onChange={(event) => setUsername(event.target.value)}
                />
                <label htmlFor="email">Email</label>
              </div>
              <div className="mb-3 form-floating">
                <input
                  type="password"
                  name="password"
                  placeholder="ilikepizza123"
                  className="form-control"
                  value={password}
                  onChange={(event) => setPassword(event.target.value)}
                />
                <label htmlFor="password">Password</label>
              </div>
              <button className="btn btn-outline-dark">Submit</button>
            </form>
          </div>
        </div >
      </div>
    );
  }
};


export default SignupComponent;
