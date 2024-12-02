import React, { useState } from "react";
import Navbar from "../topbar/navbar";


const Feed = () => {


    const fetchFeed = async (e) => {
        e.preventDefault();
        try {
            console.log("Fetching feed page..")
        } catch (error) {
            console.error("Error logging in:", error);
            alert("Login failed. Please check your credentials.");
        }
    };

    return (
        <div>
            <Navbar />
            <h1>Feed</h1>
        </div>
    );
};

export default Feed;