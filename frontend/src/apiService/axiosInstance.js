import axios from "axios";
import { getCookie } from "./cookies";


// Set up Axios instance with default settings
const API_URL = "http://localhost:8000";
const token = await getCookie();
const axiosInstance = axios.create({
    baseURL: API_URL,
});


// Attach the token to every request automatically
axiosInstance.interceptors.request.use((config) => {
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default axiosInstance;