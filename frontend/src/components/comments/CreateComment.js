import React, { useState } from "react";
import { createComment } from "../../apiService/comment";
import { getCookie } from "../../apiService/cookies";

const CreateComment = ({ postId }) => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userId = await getCookie("user_id");

    try {
      await createComment(userId, postId, content);
      setContent("");
    } catch (error) {
      if (error.response?.status === 418) {
        alert("Content not allowed (too nice). It's GRUDGEHUB!")
      }
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Hate it like you mean it.."
        />
        <button type="submit">Comment</button>
      </form>
    </div>
  );
};

export default CreateComment;