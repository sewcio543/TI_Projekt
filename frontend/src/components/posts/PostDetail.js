import React, { useEffect, useState } from "react";
import { getPost } from "../../apiService/post";

const PostDetail = ({ match }) => {
    const [post, setPost] = useState(null);

    useEffect(() => {
        const fetchPost = async () => {
            const data = await getPost(match.params.id);
            setPost(data);
        }
        fetchPost();
    }, [match.params.id]);

    if (!post) return <div>Loading...</div>

    return (
        <div>
            <h1>User Detail</h1>
            <p>Conent: {post.conent}</p>
        </div>
    );
};

export default PostDetail;