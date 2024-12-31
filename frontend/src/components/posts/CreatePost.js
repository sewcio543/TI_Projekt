import React, { useState } from "react";
import { createPost } from "../../apiService/post";
import { getCookie } from "../../apiService/cookies";
import { getUser } from "../../apiService/user";

const CreatePost = ({ onPostCreated }) => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();


    try {
      const userId = await getCookie("user_id");
      const user = await getUser(userId);
      const post = await createPost(userId, content);
      const newPost = {
        id: post.id,
        content: content,
        user: user,
      }

      onPostCreated(newPost);
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
                You got a problem?!
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