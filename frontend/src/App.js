import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import CreateUser from "./components/CreateUser";
import UserDetail from "./components/UserDetail";
import UserList from "./components/UserList";

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<UserList />} />
          <Route path="/user/:id" element={<UserDetail />} />
          <Route path="/create-user" element={<CreateUser />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
