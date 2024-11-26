import React, { useState } from "react";
import { createUser } from "../apiService/user";

const CreateUser = () => {
  const [login, setLogin] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createUser({ login });
    setLogin("");
  };

  return (
    <div>
      <h1>Create User</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          placeholder="Login"
        />
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default CreateUser;
