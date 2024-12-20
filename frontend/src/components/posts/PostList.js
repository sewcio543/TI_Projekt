import React, { useEffect, useState } from "react";
import { getPosts } from "../../apiService/post";

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
            <ul>
                {
                    posts.map((post) => (
                        <li key={post.id}>{post.content}</li>
                    ))
                }
            </ul>
        </div>
    );
};

export default PostList;