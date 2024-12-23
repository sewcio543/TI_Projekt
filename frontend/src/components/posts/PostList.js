import React, { useEffect, useState } from "react";
import { getPosts } from "../../apiService/post";
import Post from "./Post";

const PostList = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            const data = await getPosts();
            setPosts(data);
        }
        fetchPosts();
    }, []);

    return (
        <div>
            <h1>Posts List</h1>
                {
                    posts.map((post) => (
                        <Post key={post.id} post={post} />
                    ))
                }

        </div>
    );
};

export default PostList;