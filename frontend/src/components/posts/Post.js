import { useState } from "react"
import { useEffect } from "react";
import CreateComment from "../comments/CreateComment";
import CommentList from "../comments/ListComment";
import { getCommentByPostId } from "../../apiService/comment";

const Post = ({ post }) => {

    const [comments, setComments] = useState([]);

    useEffect(() => {
        const fetchComments = async () => {
            const data = await getCommentByPostId(post.id);
            setComments(data);
        }
        fetchComments();
    }, []);

    // Function to handle adding a new comment
    const addComment = (newComment) => {
        setComments((prevComments) => [...prevComments, newComment]);
    };

    return (
        <div>
            <h3>{post.user.login}</h3>
            <p>{post.content}</p>

            <CommentList comments={comments} />
            <CreateComment post={post} onCommentCreated={addComment} />

        </div>
    );
}

export default Post;