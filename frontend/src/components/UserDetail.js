import React, { useEffect, useState } from "react";
import { getUser } from "../apiService/user";

const UserDetail = ({ match }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      const data = await getUser(match.params.id);
      setUser(data);
    };
    fetchUser();
  }, [match.params.id]);

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>User Detail</h1>
      <p>Login: {user.login}</p>
    </div>
  );
};

export default UserDetail;
