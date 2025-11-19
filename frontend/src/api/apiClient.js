import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:8000"
});

export const getFollowerHistory = async () => {
  const res = await api.get("/api/twitch/followers");
  return res.data;
};

export const getForecast = async () => {
  const res = await api.get("/api/twitch/forecast");
  return res.data;
};
