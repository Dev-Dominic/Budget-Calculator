/* Everything relating to the User object */

const categories = ["income", "savings", "expenses"];

function userCreate() {
  // Creates new user object and appends each category from categories into it
  // and create a new object to house entries
  let newUser = {};
  categories.forEach((category) => {
    newUser[category] = {};
  });
  return newUser;
}

export { categories };
export default userCreate;
