import { useNavigate } from "react-router-dom";
import { useToken } from "./auth";
import { useState } from "react";
import { Audio } from 'react-loader-spinner'

function LoginComponent() {
  const navigate = useNavigate();
  const [login] = useToken();
  const [loading, setLoading] = useState(false);
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();

  const submitHandler = async (e) => {
    e.preventDefault();
    setLoading(true);
    await login(username, password)
    setLoading(false)
    navigate("/accounts/accountpage");
  };

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Welcome! Login using your email and password:</h1>
          <form onSubmit={submitHandler}>
            <div className="mb-3 form-floating">
              <input
                type="text"
                name="username"
                placeholder="Email"
                id="email"
                value={username}
                className="form-control"
                onChange={(event) => setUsername(event.target.value)}
              />
              <label htmlFor="email">Email</label>
            </div>
            <div className="mb-3 form-floating">
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={password}
                className="form-control"
                onChange={(event) => setPassword(event.target.value)}
              />
              <label htmlFor="password">Password</label>
            </div>
            <button className="btn btn-outline-dark" disabled={loading}>Submit</button>
            {loading &&
              < Audio
                className="justify-content-center"
                height="50"
                width="80"
                color='blue'
                ariaLabel='three-dots-loading' />}
          </form>
        </div>
      </div >
    </div>
  );

}

export default LoginComponent;