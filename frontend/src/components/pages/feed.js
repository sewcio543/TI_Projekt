import React, { useState } from "react";
import { useEffect } from "react";
import Navbar from "../topbar/navbar";

import CreatePost from "../posts/CreatePost";
import PostList from "../posts/PostList";
import UserList from "../users/UserList";

import { getPosts } from "../../apiService/post";

const Feed = () => {

    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            const data = await getPosts();
            setPosts(data);
        }
        fetchPosts();
    }, []);

    // Function to handle adding a new post
    const addPost = (newPost) => {
        setPosts((prevPosts) => [...prevPosts, newPost]);
    };


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
                            <CreatePost onPostCreated={addPost} />
                        </div>
                        <PostList posts={posts} />
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