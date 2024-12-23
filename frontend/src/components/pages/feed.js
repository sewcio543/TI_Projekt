import React, { useState } from "react";
import Navbar from "../topbar/navbar";

import CreatePost from "../posts/CreatePost";
import PostList from "../posts/PostList";
import UserList from "../users/UserList";


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

    // TODO state management for posts (similar as in Post.js)

    return (
        <div>
            <Navbar />
            <div className="container mt-3">
                <h1>Feed</h1>
                <hr />
            </div>
            <div className="container">
                <div className="row">
                    <div className="col-md-2"></div>
                    <div className="col-md-7">
                        <div className="mb-4">
                            <CreatePost />
                        </div>
                        <PostList />
                    </div>
                    <div className="col-md-3">
                        <UserList />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Feed;