import axios, { AxiosInstance } from 'axios';

const http: AxiosInstance = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? '' : process.env.VUE_APP_BASE_URL,
  timeout: process.env.VUE_APP_REQUEST_TIMEOUT,
  headers: {
    'Content-type': 'application/json',
  },
  params: { },
});

export default http;
