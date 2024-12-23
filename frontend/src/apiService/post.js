import axiosInstance from "./axiosInstance";


export const getPosts = async () => {
  const response = await axiosInstance.content.get(`/post/`);
  return response.data;
};

export const getPost = async (id) => {
  const response = await axiosInstance.content.get(`/post/${id}`);
  return response.data;
};

export const createPost = async (userId, content) => {
  const payload = { user_id: userId, content };
  const response = await axiosInstance.content.post(`/post/`, payload);
  return response.data;
};

export const updatePost = async (id, post) => {
  const response = await axiosInstance.content.put(`/post/${id}`, post);
  return response.data;
};

export const deletePost = async (id) => {
  const response = await axiosInstance.content.delete(`/post/${id}`);
  return response.data;
};
