import React, { useState } from "react";
import axios from "axios";

import { useDispatch } from "react-redux";
import { logIn } from "../../redux/reducer";
import { useNavigate } from "react-router-dom";
import { verifyUser } from "../../apiService/user";

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
        <div>
            <h1>Login</h1>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;