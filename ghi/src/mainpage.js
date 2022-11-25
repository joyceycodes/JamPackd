import React from "react";
import './css/App.css';

// import { Navigate } from "react-router-dom";

class MainPage extends React.Component {
    render() {
        return (
            <div>
                <header>
                    <p className="JP_title borderstyle">JamPack'd</p>

                    <p className="JP_subtitle borderstyle">Pack'd Full of Tasty Jams!</p>
                    <nav>
                        <ul>
                            <li>
                                <button type="button" className="login-btn fbstyle">Login</button>
                            </li>
                            <li>
                                <button type="button" className="signup-btn fbstyle">Sign Up</button>
                            </li>
                        </ul>
                    </nav>

                </header>
            </div>

        )
    }
}

export default MainPage;