import axiosInstance from "./axiosInstance";


export const getUsers = async () => {
  const response = await axiosInstance.people.get(`/`);
  return response.data;
};

export const getUser = async (id) => {
  const response = await axiosInstance.people.get(`/${id}`);
  return response.data;
};

export const createUser = async (user) => {
  const response = await axiosInstance.people.post(`/`, user);
  return response.data;
};

export const updateUser = async (id, user) => {
  const response = await axiosInstance.people.put(`/${id}`, user);
  return response.data;
};

export const deleteUser = async (id) => {
  const response = await axiosInstance.people.delete(`/${id}`);
  return response.data;
};

export const verifyUser = async (token) => {
  try {
    // update token, make sure it's request is authorized
    axiosInstance.updateToken(token);
    const response = await axiosInstance.people.get(`this`);
    const { id } = response.data;

    // user_id to a session cookie
    document.cookie = `user_id=${id}; path=/;`;
  } catch (error) {
    alert("Failed to verify user!")
  }
};
