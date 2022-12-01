import { useState } from "react";
import { useToken } from "./auth";
import { useNavigate } from "react-router-dom";

function SignupComponent() {
    const navigate = useNavigate();
    const [token, login] = useToken();
    async function signup(email, full_name, password) {
        const url = `${process.env.REACT_APP_accounts}/api/users`;
        const response = await fetch(url, {
            method: "post",
            body: JSON.stringify({
                full_name,
                email,
                password,
            }),
            headers: {
                "content-type": "application/json",
            },
        });
        console.log("TOKEN HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!", token);
        if (response.ok) {
            await login(email, password);
            navigate("/login");
        }
        return false;
    };

    let [full_name, setFullName] = useState();
    let [password, setPassword] = useState();
    let [email, setEmail] = useState();

    const submitHandler = (e) => {
        signup(email, full_name, password);

        e.preventDefault();
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
                        name="email"
                        placeholder="john@doe.com"
                        value={email}
                        onChange={(event) => setEmail(event.target.value)}
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
