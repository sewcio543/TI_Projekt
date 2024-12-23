const Comment = ({ comment }) => {

    return (
        <div>
            <p>{comment.id}. {comment.content} for post {comment.post.id}</p>
        </div>
    );
}

export default Comment;