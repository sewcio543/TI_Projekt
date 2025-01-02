import React, { useState } from "react";
import axios from "axios";

import { useDispatch } from "react-redux";
import { logIn } from "../../redux/reducer";
import { useNavigate } from "react-router-dom";
import { verifyUser } from "../../apiService/user";

import image from "./../../images/hate-speech.jpg";

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const dispatch = useDispatch();

    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                "http://localhost:8000/token",
                new URLSearchParams({
                    username,
                    password,
                }),
                {
                    headers: { "Content-Type": "application/x-www-form-urlencoded" },
                }
            );

            const { access_token } = response.data;

            // Save the token to a session cookie
            document.cookie = `bearer=${access_token}; path=/;`;
            dispatch(logIn());

            await verifyUser(access_token);

            // Redirect to home page
            navigate("/feed");

        } catch (error) {
            console.error("Error logging in:", error);
            alert("Login failed. Please check your credentials.");
        }
    };


    return (
        <div
            style={{
                backgroundImage: `url(${image})`,
                backgroundSize: "cover",
                backgroundPosition: "center",
                height: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            <div style={{ position: "absolute", top: "3vh", right: "3vw" }}>
                <h1 className="display-1" style={{ fontWeight: "bold" }}>GrudgeHub</h1>
            </div>
            <div className="container" style={{ width: "30%" }}>
                <div className="card">
                    <div className="card-body">
                        <h1 className="card-title text-center">Login</h1>
                        <form onSubmit={handleLogin}>
                            <div className="form-group">
                                <label htmlFor="username">Username</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="username"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    placeholder="Enter username"
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="password">Password</label>
                                <input
                                    type="password"
                                    className="form-control"
                                    id="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    placeholder="Enter password"
                                />
                            </div>
                            <button type="submit" className="btn btn-primary btn-block w-100 mt-4">Login</button>
                        </form>
                        <button
                            type="button"
                            className="btn btn-link btn-block mt-3"
                            onClick={() => { window.location.href = "/signup"; }}
                        >
                            Signup
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );

};

export default Login;