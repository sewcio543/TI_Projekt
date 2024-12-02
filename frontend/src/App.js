import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import CreateUser from "./components/users/CreateUser";
import UserDetail from "./components/users/UserDetail";
import UserList from "./components/users/UserList";
import CreatePost from "./components/posts/CreatePost";
import PostDetail from "./components/posts/PostDetail";
import PostList from "./components/posts/PostList";
import Login from "./components/pages/login";
import Feed from "./components/pages/feed";
import PrivateRoute from "./utils/privateRoute";

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/login" element={<Login />} />

          <Route path="/" element={<PrivateRoute element={<UserList />} />} />
          <Route path="/user/:id" element={<PrivateRoute element={<UserDetail />} />} />
          <Route path="/create-user" element={<PrivateRoute element={<CreateUser />} />} />
          <Route path="/post/" element={<PrivateRoute element={<PostList />} />} />
          <Route path="/posts/:id" element={<PrivateRoute element={<PostDetail />} />} />
          <Route path="/create-post" element={<PrivateRoute element={<CreatePost />} />} />
          <Route path="/feed" element={<PrivateRoute element={<Feed />} />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;