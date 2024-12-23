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
        <div class="card" style={{ padding: "10px", margin: "10px" }}>
            <div class="card-body border-bottom">
                <div class="d-flex align-items-center gap-3">
                    <img src={`https://bootdey.com/img/Content/avatar/avatar${post.user.id % 8}.png`} alt="" class="rounded-circle" width="40" height="40"></img>
                    <h6 class="fw-semibold mb-0 fs-4">{post.user.login}</h6>
                    {/* <span class="fs-2"><span class="p-1 bg-light rounded-circle d-inline-block"></span> 15 min ago</span> */}
                </div>
                <p class="text-dark my-3">
                    {post.content}
                </p>
                <div class="d-flex align-items-center my-3">
                    <div class="d-flex align-items-center gap-2">
                        <a class="text-white d-flex align-items-center justify-content-center bg-primary p-2 fs-4 rounded-circle" href="javascript:void(0)" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Like">
                            <i class="fa fa-thumbs-up"></i>
                        </a>
                        <span class="text-dark fw-semibold">67</span>
                    </div>
                    <div class="d-flex align-items-center gap-2 ms-4">
                        <a class="text-white d-flex align-items-center justify-content-center bg-secondary p-2 fs-4 rounded-circle" href="javascript:void(0)" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Comment">
                            <i class="fa fa-comments"></i>
                        </a>
                        <span class="text-dark fw-semibold">2</span>
                    </div>
                </div>
            </div>
            <div class="position-relative">
                <CommentList comments={comments} />
                <CreateComment post={post} onCommentCreated={addComment} />
            </div>
        </div>
    );
}

export default Post;