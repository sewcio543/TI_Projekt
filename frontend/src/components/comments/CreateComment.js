import React, { useState } from "react";
import { createComment } from "../../apiService/comment";
import { getCookie } from "../../apiService/cookies";

const CreateComment = ({ post, onCommentCreated }) => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userId = await getCookie("user_id");

    try {
      const commentId = await createComment(userId, post.id, content);
      const newComment = {
        id: commentId.id,
        content: content,
        user: post.user,
        post: post,
      }
      onCommentCreated(newComment);
      setContent("");
    } catch (error) {
      if (error.response?.status === 418) {
        alert("Content not allowed (too nice). It's GRUDGEHUB!")
      }
    }
  }

  return (
    <div class="d-flex align-items-center gap-3 p-3">
      <img src={`https://bootdey.com/img/Content/avatar/avatar${post.user.id % 8}.png`} alt="" class="rounded-circle" width="33" height="33" />
      <form onSubmit={handleSubmit} class="d-flex align-items-center gap-3">
        <input
          class="form-control py-8" id="exampleInputtext" aria-describedby="textHelp"
          type="text"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Hate it like you mean it.."
        />
        <button class="btn btn-primary">Comment</button>
      </form>
    </div>
  );
};

export default CreateComment;