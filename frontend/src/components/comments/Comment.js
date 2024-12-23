const Comment = ({ comment }) => {

    return (
        <div>
            <h5>{comment.user.login}:</h5>
            <p>{comment.content}</p>
        </div>
    );
}

export default Comment;