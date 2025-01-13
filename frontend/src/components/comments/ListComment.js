import React from "react";
import Comment from "./Comment";

const CommentList = ({ comments }) => {

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