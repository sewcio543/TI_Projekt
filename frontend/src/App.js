import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import CreateUser from "./components/CreateUser";
import UserDetail from "./components/UserDetail";
import UserList from "./components/UserList";
import CreatePost from "./components/CreatePost";
import PostDetail from "./components/PostDetail";
import PostList from "./components/PostList";
import Login from "./components/pages/login";
import Feed from "./components/pages/feed";

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<UserList />} />
          <Route path="/user/:id" element={<UserDetail />} />
          <Route path="/create-user" element={<CreateUser />} />
          <Route path="/post/" element={<PostList />} />
          <Route path="/posts/:id" element={<PostDetail />} />
          <Route path="/create-post" element={<CreatePost />} />
          <Route path="/login" element={<Login />} />
          <Route path="/feed" element={<Feed />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;