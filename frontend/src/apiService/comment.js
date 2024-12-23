import axios from "axios";


export const getComments = async () => {
  const response = await axios.content.get(`/comment/`);
  return response.data;
};

export const getComment = async (id) => {
  const response = await axios.content.get(`/comment/${id}`);
  return response.data;
};

export const createComment = async (post) => {
  const response = await axios.content.post(`/comment/`, post);
  return response.data;
};

export const updateComment = async (id, post) => {
  const response = await axios.content.put(`/comment/${id}`, post);
  return response.data;
};

export const deleteComment = async (id) => {
  const response = await axios.content.delete(`/comment/${id}`);
  return response.data;
};
