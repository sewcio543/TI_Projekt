import React, { useEffect } from "react";
import { Route, BrowserRouter as Router, Routes, Navigate } from "react-router-dom";
import Feed from "./components/pages/feed";
import Login from "./components/pages/login";
import Signup from "./components/pages/signup";
import CreatePost from "./components/posts/CreatePost";
import PostDetail from "./components/posts/PostDetail";
import PostList from "./components/posts/PostList";
import CreateUser from "./components/users/CreateUser";
import UserDetail from "./components/users/UserDetail";
import UserList from "./components/users/UserList";
import PrivateRoute from "./utils/privateRoute";

// In your index.js or App.js
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  useEffect(() => {
    document.title = "GrudgeHub";
  }, []);

  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/feed" element={<PrivateRoute element={<Feed />} />} />
          <Route
            path="/users/"
            element={<PrivateRoute element={<UserList />} />}
          />
          <Route
            path="/user/:id"
            element={<PrivateRoute element={<UserDetail />} />}
          />
          <Route
            path="/create-user"
            element={<PrivateRoute element={<CreateUser />} />}
          />
          <Route
            path="/post/"
            element={<PrivateRoute element={<PostList />} />}
          />
          <Route
            path="/posts/:id"
            element={<PrivateRoute element={<PostDetail />} />}
          />
          <Route
            path="/create-post"
            element={<PrivateRoute element={<CreatePost />} />}
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
