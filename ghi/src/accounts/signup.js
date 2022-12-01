import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SignupComponent() {
    const navigate = useNavigate();
    async function signup(full_name, email, password) {
        const url = `${process.env.REACT_APP_accounts}/api/accounts`;
        console.log("heloooooooo", url)
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
        if (response.ok) {

            navigate("/accountpage");
        }
        return false;
    };

    let [full_name, setFullName] = useState();
    let [password, setPassword] = useState();
    let [email, setEmail] = useState();

    const submitHandler = (e) => {
        e.preventDefault();
        signup(full_name, email, password);

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
