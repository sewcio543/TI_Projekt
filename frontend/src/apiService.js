import axios from "axios";

const API_URL = "http://localhost:8000";

export const getUsers = async () => {
  const response = await axios.get(`${API_URL}/user/`);
  return response.data;
};

export const getUser = async (id) => {
  const response = await axios.get(`${API_URL}/user/${id}`);
  return response.data;
};

export const createUser = async (user) => {
  const response = await axios.post(`${API_URL}/user/`, user);
  return response.data;
};

export const updateUser = async (id, user) => {
  const response = await axios.put(`${API_URL}/user/${id}`, user);
  return response.data;
};

export const deleteUser = async (id) => {
  const response = await axios.delete(`${API_URL}/user/${id}`);
  return response.data;
};
