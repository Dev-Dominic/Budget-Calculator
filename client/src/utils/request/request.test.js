/* Testing HTTP request methods */

/* MockAxios */
import axios from "axios";
import MockAdapter from "axios-mock-adapter";

/* Request Methods Import */
import { create, allUsers } from "./request";

const mock = new MockAdapter(axios);

describe("create", () => {
  // Clean up after each test
  afterEach(() => {
    mock.reset();
  });

  // Base testing function for create function
  const createTest = (user, response, status) => {
    mock.onPost("/api/create").reply(status, response);

    // Needed because the response passed from 'create' would not come until
    // after all synchrounous code is ran.
    const testResponse = ({ user, message }) => {
      expect(user).toEqual(response.user);
      expect(message).toEqual(response.message);
    };

    create(user).then(testResponse).catch(testResponse);
  };

  test("Testing valid user creation", () => {
    const user = {
      firstName: "Dominic",
      lastName: "Henry",
      expense: {
        grocery: 10000,
        utilities: 10000,
        transportation: 5000,
      },
      income: {
        salary: 240000,
      },
      savings: {
        equities: 15000,
        pension: 20000,
        emergency: 50000,
      },
    };

    const response = {
      user: {
        ...user,
        _id: "507f191e810c19729de860ea",
        totalIncome: 240000,
        totalSavings: 85000,
        totalExpenses: 25000,
        statement: "You have a good handle of your budget",
        leftover: 130000,
      },
      message: "Success",
    };

    createTest(user, response, 200);
  });

  test("Testing invalid user creation", () => {
    const user = {};
    const response = {
      user: {},
      message: "Failed",
    };

    createTest(user, response, 400);
  });

  test("Testing when user submission made by existing ipAddress", () => {
    const user = {
      firstName: "Gabrielle",
      lastName: "Clarke",
      expense: {
        grocery: 10000,
      },
      income: {
        salary: 240000,
      },
    };

    const response = {
      user: {},
      message: "Failed",
    };

    createTest(user, response, 400);
  });
});

describe("allUsers", () => {
  // Clean up after each test
  afterEach(() => {
    mock.reset();
  });

  // Base testing function for create function
  const allUsersTest = (response, status) => {
    mock.onGet("/api/create").reply(status, response);
    const users = allUsers();

    expect(response.data.users).toEqual(users);
  };

  test("Testing retrieving a list of all users", () => {
    const response = {
      users: [
        {
          firstName: "Gabrielle",
          lastName: "Clarke",
          expense: {
            grocery: 10000,
          },
          income: {
            salary: 10000,
          },
          _id: "604f191e810c19729de860ea",
          totalIncome: 240000,
          totalExpenses: 25000,
          statement: "Your budget is very tight",
          leftover: 0,
        },
        {
          firstName: "Dominic",
          lastName: "Henry",
          expense: {
            grocery: 10000,
            utilities: 10000,
            transportation: 5000,
          },
          income: {
            salary: 240000,
          },
          savings: {
            equities: 15000,
            pension: 20000,
            emergency: 50000,
          },
          _id: "507f191e810c19729de860ea",
          totalIncome: 240000,
          totalSavings: 85000,
          totalExpenses: 25000,
          statement: "You have a good handle of your budget",
          leftover: 130000,
        },
      ],
    };

    allUsersTest(response, 200);
  });

  test("Testing handling empty user object", () => {
    const response = {
      users: [],
    };

    allUsersTest(response, 200);
  });
});
