import { useState } from "react"
import CreateComment from "../comments/CreateComment";
import CommentList from "../comments/ListComment";

const Post = ({ post }) => {

    return (
        <div>
            <h3>{post.user.login}</h3>
            <p>id: {post.id}</p>
            <p>{post.content}</p>

            <CommentList postId={post.id} />
            <CreateComment postId={post.id} />

        </div>
    );
}

export default Post;