import React, { useState } from "react";
import axios from "axios";

import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { verifyUser } from "../../apiService/user";
import { signUp } from "../../redux/reducer";
import { createUser } from "../../apiService/user";

const Signup = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const dispatch = useDispatch();

    const navigate = useNavigate();

    const handleSignup = async (e) => {
        e.preventDefault();
        try {
            const user = {
                login: username,
                password: password
            }
            const { user_id } = await createUser(user);
            console.log("Craeted user id", user_id);

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
            await verifyUser(access_token);



            // Save the token, user_id to a session cookie
            document.cookie = `bearer=${access_token}; path=/;`;
            document.cookie = `user_id=${user_id}; path=/;`;
            dispatch(signUp());

            await (access_token);

            // Redirect to home page
            navigate("/feed");

        } catch (error) {
            console.error("Error logging in:", error);
            alert(`Signup failed. ${error.response.data.detail}`);
        }
    };

    return (
        <div>
            <h1>Signup</h1>
            <form onSubmit={handleSignup}>
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
                <button type="submit">Signup</button>
                <button type="button" onClick={() => { window.location.href = "/login"; }}>Login</button>
            </form>
        </div>
    );
};

export default Signup;