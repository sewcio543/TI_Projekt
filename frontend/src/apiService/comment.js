// import axios from "axios";
import axiosInstance from "./axiosInstance";


export const getComments = async () => {
  const response = await axiosInstance.content.get(`/comment/`);
  return response.data;
};

export const getComment = async (id) => {
  const response = await axiosInstance.content.get(`/comment/${id}`);
  return response.data;
};
export const getCommentByPostId = async (postId) => {
  const response = await axiosInstance.content.get(`/comment/post/${postId}`);
  return response.data;
};

export const createComment = async (userId, postId, content) => {
  const payload = {
    user_id: userId,
    post_id: postId,
    content
  }
  const response = await axiosInstance.content.post(`/comment/`, payload);
  return response.data;

};

export const updateComment = async (id, post) => {
  const response = await axiosInstance.content.put(`/comment/${id}`, post);
  return response.data;
};

export const deleteComment = async (id) => {
  const response = await axiosInstance.content.delete(`/comment/${id}`);
  return response.data;
};
