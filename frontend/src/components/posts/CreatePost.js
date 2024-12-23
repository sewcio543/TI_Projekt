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
      <div className="card shadow-none border">
        <div className="card-body">
          <form onSubmit={handleSubmit}>
            <div className="form-floating mb-3">
              <textarea
                className="form-control"
                placeholder="Leave a comment here"
                id="floatingTextarea2"
                value={content}
                onChange={(e) => setContent(e.target.value)}
              ></textarea>
              <label htmlFor="floatingTextarea2" className="p-7">
                Share your thoughts
              </label>
            </div>
            <div className="d-flex align-items-center gap-2">
              <button type="submit" className="btn btn-primary ms-auto">
                Post
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default CreatePost;