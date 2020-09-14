/* Holds all requests need for project */

import axios from "axios";

async function create(params) {
  const result = await axios.post("/api/create", params);
  const { user, message } = result.data;

  return { user, message };
}

async function allUsers() {
  return;
}

export { create, allUsers };
