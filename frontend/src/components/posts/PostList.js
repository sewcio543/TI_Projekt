import React, { useEffect, useState } from "react";
import { getPosts } from "../../apiService/post";
import Post from "./Post";

const PostList = ({ posts }) => {
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