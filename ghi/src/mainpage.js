import React from "react";
import './css/App.css';
import LoginPage from "./accounts/login";

// import { Navigate } from "react-router-dom";

// const TitleHandler = React.createClass({
//     componentDidMount: function () {
//         document.title = "Amazing Page";
//     }
// }); URLs for how to set document.title https://github.com/remix-run/react-router/issues/49 https://stackoverflow.com/questions/45311521/how-change-the-title-of-a-page-before-it-loads-jsx



class MainPage extends React.Component {

    render() {
        return (
            <div>
                <header>
                    <title>JamPack'd</title>
                    <p className="JP_title borderstyle">JamPack'd</p>

                    <p className="JP_subtitle borderstyle">Pack'd Full of Tasty Jams!</p>
                    <nav>
                        <ul>
                            <li>
                                <button type="button" className="login-btn fbstyle">Login</button>
                                # redirects to login page OR calls in login modal
                            </li>
                            <li>
                                <button type="button" className="signup-btn fbstyle">Sign Up</button>
                                # redirects to signup page OR calls in signup modal
                            </li>
                        </ul>
                    </nav>

                </header>
            </div>

        )
    }
}

export default MainPage;