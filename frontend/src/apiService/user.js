import axiosInstance from "./axiosInstance"

const API_URL = "http://localhost:8000";

export const getUsers = async () => {
  const response = await axiosInstance.get(`${API_URL}/user/`);
  return response.data;
};

export const getUser = async (id) => {
  const response = await axiosInstance.get(`${API_URL}/user/${id}`);
  return response.data;
};

export const createUser = async (user) => {
  const response = await axiosInstance.post(`${API_URL}/user/`, user);
  return response.data;
};

export const updateUser = async (id, user) => {
  const response = await axiosInstance.put(`${API_URL}/user/${id}`, user);
  return response.data;
};

export const deleteUser = async (id) => {
  const response = await axiosInstance.delete(`${API_URL}/user/${id}`);
  return response.data;
};