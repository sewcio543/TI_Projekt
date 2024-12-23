import React, { useState } from "react";
import { createPost } from "../../apiService/post";
import { getCookie } from "../../apiService/cookies";

const CreatePost = () => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userId = await getCookie("user_id");

    try {
      await createPost(userId, content);
      setContent("");
    } catch (error) {
      if (error.response?.status === 418) {
        alert("Content not allowed (too nice). It's GRUDGEHUB!")
      }
    }
  }

  return (
    <div>
      <h1>Create Post</h1>
      <form onSubmit={handleSubmit}>
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