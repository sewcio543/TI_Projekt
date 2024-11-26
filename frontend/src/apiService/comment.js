import axios from "axios";

const API_URL = "http://localhost:8000";

export const getComments = async () => {
    const response = await axios.get(`${API_URL}/comment/`);
    return response.data;
}

export const getComment = async (id) => {
    const response = await axios.get(`${API_URL}/comment/${id}`);
    return response.data;
}

export const createComment = async (post) => {
    const response = await axios.post(`${API_URL}/comment/`, post);
    return response.data;
}

export const updateComment = async (id, post) => {
    const response = await axios.put(`${API_URL}/comment/${id}`, post);
    return response.data;
}

export const deleteComment = async (id) => {
    const response = await axios.delete(`${API_URL}/comment/${id}`);
    return response.data;
}