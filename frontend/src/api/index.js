import axios from "axios";

const API_URL = "http://localhost:8000/api";

export function getPokemonListing({ sort = "id", order = "ASC", page = 1 }) {
  return axios.get(
    `${API_URL}/pokemon?sort=${sort}&order=${order}&page=${page}`
  );
}

export function getPokemon(poke) {
  return axios.get(`${API_URL}/pokemon/${poke}`);
}

export function getEvolutionListing({ sort = "id", order = "ASC", page = 1 }) {
  return axios.get(
    `${API_URL}/evolutions?sort=${sort}&order=${order}&page=${page}`
  );
}

export function getEvolution(id) {
  return axios.get(`${API_URL}/evolutions/${id}`);
}

export function getTypeListing({ sort = "id", order = "ASC", page = 1 }) {
  return axios.get(`${API_URL}/types?sort=${sort}&order=${order}&page=${page}`);
}

export function getType(id) {
  return axios.get(`${API_URL}/types/${id}`);
}

export function getTestResults() {
  return axios.get(`${API_URL}/tests`);
}

export function getSearchResults(term) {
  return axios.post(`${API_URL}/search`, null, { params: { q: term } });
}
