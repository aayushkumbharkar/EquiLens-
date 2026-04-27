import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json'
  }
});

export const analysisService = {
  generate: async (prompt) => {
    const response = await api.post('/analysis/generate', { prompt });
    return response.data;
  },
  evaluate: async (prompt, decision) => {
    const response = await api.post('/analysis/evaluate', { prompt, decision });
    return response.data;
  },
  getHistory: async (skip = 0, limit = 20) => {
    const response = await api.get(`/analysis/history?skip=${skip}&limit=${limit}`);
    return response.data;
  }
};
