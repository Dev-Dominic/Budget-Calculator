/* Testing UserCreate function utility */

import userCreate, { categories } from "./userCreate";

describe("userCreate", () => {
  test("Tests that all categories are created for the user object", () => {
    const user = userCreate();
    categories.forEach((category) => {
      // Checking that each category exists and that it is instantiated with an
      // empty object
      expect(user).toHaveProperty(category);
      expect(user[category]).toEqual({});
    });
  });
});
