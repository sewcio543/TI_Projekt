import React, { useState } from "react";
import { createPost } from "../../apiService/post";

const CreatePost = () => {
  const [userId, setUserId] = useState("");
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createPost(userId, content);
      setContent("");
    } catch (error) {
      if (error.response?.status === 418) {
        alert("Content not allowed you fucker. It's GRUDGEHUB!")
      }
    }
  }

  return (
    <div>
      <h1>Create Post</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          placeholder="User ID"
        />
        <input
          type="text"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="You got a problem?!"
        />
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default CreatePost;