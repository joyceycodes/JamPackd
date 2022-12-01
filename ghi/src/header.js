import React from "react";

export default function Header(props) {
    const { } = props;
    return (
        <div className="row center block">
            <div>
                <img
                    className="div-icon"
                    src=""
                    alt=":)"
                />
            </div>
            <div>
                <a href="#/">
                    <h2>Value to be Changed</h2>
                </a>
            </div>

            <div>
                {/* <a className="link" href="#/cart"> commented out DIV - relevant div to be reimplemented when line 16 is updated
                    Cart{" "}
                    {countCartItems ? (
                        <button className="badge">{countCartItems}</button>
                    ) : (
                        ""
                    )}
                </a> */}
                <p></p>
                <a className="link" href="#/signin">
                    Sign In
                </a>
            </div>
        </div>
    );
}
