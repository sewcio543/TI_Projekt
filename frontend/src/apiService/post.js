import axiosInstance from "./axiosInstance"

const API_URL = "http://localhost:8000";

export const getPosts = async () => {
    const response = await axiosInstance.get(`${API_URL}/post/`);
    return response.data;
}

export const getPost = async (id) => {
    const response = await axiosInstance.get(`${API_URL}/post/${id}`);
    return response.data;
}

export const createPost = async (userId, content) => {

    const payload = { user_id: userId, content };
    const response = await axiosInstance.post(`${API_URL}/post/`, payload);
    return response.data;
}

export const updatePost = async (id, post) => {
    const response = await axiosInstance.put(`${API_URL}/post/${id}`, post);
    return response.data;
}

export const deletePost = async (id) => {
    const response = await axiosInstance.delete(`${API_URL}/post/${id}`);
    return response.data;
}