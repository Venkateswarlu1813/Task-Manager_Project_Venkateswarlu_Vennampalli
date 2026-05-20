import axios from "axios";
import Cookies from "js-cookie";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

API.interceptors.request.use(
  (config) => {

    const token = Cookies.get("access");

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },

  (error) => {
    return Promise.reject(error);
  }
);

export default API;