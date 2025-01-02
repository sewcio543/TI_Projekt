import React, { useState } from "react";
import axios from "axios";

import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { verifyUser } from "../../apiService/user";
import { signUp } from "../../redux/reducer";
import { createUser } from "../../apiService/user";

import image from "./../../images/hate-speech.jpg";

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
            const my_user = await createUser(user);
            console.log("Craeted user id", my_user.id);
            console.log(my_user);

            // add sleep for 0.5 seconds
            const sleep = (milliseconds) => {
                return new Promise(resolve => setTimeout(resolve, milliseconds))
            }
            await sleep(500);

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
            console.log(access_token);
            // await verifyUser(access_token);



            // Save the token, user_id to a session cookie
            document.cookie = `bearer=${access_token}; path=/;`;
            // document.cookie = `user_id=${user_id}; path=/;`;
            document.cookie = `user_id=${my_user.id}; path=/;`;
            dispatch(signUp());


            await (access_token);

            // Redirect to home page
            navigate("/feed");

        } catch (error) {
            console.error("Error logging in:", error);
            alert(`Signup failed. ${error.response}`);
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
                        <h1 className="card-title text-center">Signup</h1>
                        <form onSubmit={handleSignup}>
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
                            <button type="submit" className="btn btn-primary btn-block w-100 mt-4">Signup</button>
                        </form>
                        <button
                            type="button"
                            className="btn btn-link btn-block mt-3"
                            onClick={() => { window.location.href = "/login"; }}
                        >
                            Login
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Signup;