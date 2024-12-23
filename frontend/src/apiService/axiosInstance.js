import axios from "axios";
import { getCookie } from "./cookies";

class AxiosInstance {
  constructor() {
    this.token = null;
    this.people = axios.create({
      baseURL: "http://localhost:8002",
    });
    this.content = axios.create({
      baseURL: "http://localhost:8001",
    });
    this.identity = axios.create({
      baseURL: "http://localhost:8000",
    });
  }

  async initialize() {
    this.token = await getCookie("bearer");
    this.updateToken(this.token);
  }

  updateToken(token) {
    this.token = token;

    const interceptRequest = (config) => {
      if (this.token) {
        config.headers.Authorization = `Bearer ${this.token}`;
        console.log("Intercepted Bearer token:", this.token);
      }
      return config;
    };

    this.people.interceptors.request.use(interceptRequest);
    this.content.interceptors.request.use(interceptRequest);
    this.identity.interceptors.request.use(interceptRequest);
    console.log(`Updated axios instance with token ${this.token}`);
  }
}

const axiosInstance = new AxiosInstance();
await axiosInstance.initialize();

export default axiosInstance;
