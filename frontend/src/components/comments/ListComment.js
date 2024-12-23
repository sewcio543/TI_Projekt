import React, { useEffect, useState } from "react";
import { getCommentByPostId } from "../../apiService/comment";
import Comment from "./Comment";

const CommentList = ({ postId }) => {
    const [comments, setComments] = useState([]);

    useEffect(() => {
        const fetchComments = async () => {
            const data = await getCommentByPostId(postId);
            console.log(data);
            setComments(data);
        }
        fetchComments();
    }, []);

    return (
        <div>
            <h3>Comments list</h3>
            <ul>
                {
                    comments.map((comment) => (
                        <Comment key={comment.id} comment={comment} />
                    ))
                }
            </ul>
        </div>
    );
};

export default CommentList;