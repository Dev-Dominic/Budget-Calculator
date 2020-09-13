/* Testing HTTP request methods */

/* MockAxios */
import mockAxios from "jest-mock-axios";

/* Request Methods Import */
import { create, allUsers } from "./request";

describe("create", () => {
  // Clean up after each test
  afterEach(() => {
    mockAxios.reset();
  });

  // Base testing function for create function
  const createTest = (user, response, err = false) => {
    const [thenFn, catchFn] = [jest.fn(), jest.fn()];

    // Making request to create new user submission with 'create'
    create(user).then(thenFn).catch(catchFn);

    // Testing parameters for axios http request
    expect(mockAxios.post).toHaveBeenCalledWith("/api/create", user);

    // Testing proper response
    mockAxios.mockResponse(response);

    // Testing when request gives an error or not
    if (err === true) {
      expect(thenFn).not.toHaveBeenCalled();
      expect(catchFn).toHaveBeenCalledWith(response);
    } else {
      expect(thenFn).toHaveBeenCalledWith(response);
      expect(catchFn).not.toHaveBeenCalled();
    }
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
      data: {
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
      },
      status: 200,
    };

    createTest(user, response);
  });

  test("Testing invalid user creation", () => {
    const user = {};
    const response = {
      data: {
        user: {},
        message: "Failed",
      },
      status: 400,
    };

    create(user, response, true);
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
      data: {
        user: {},
        message: "Failed",
      },
      status: 400,
    };

    create(user, response, true);
  });
});

describe("allUsers", () => {
  // Clean up after each test
  afterEach(() => {
    mockAxios.reset();
  });

  // Base testing function for create function
  const allUsersTest = (response, err = false) => {
    const [thenFn, catchFn] = [jest.fn(), jest.fn()];

    // Making request to create new user submission with 'create'
    allUsers().then(thenFn).catch(catchFn);

    // Testing parameters for axios http request
    expect(mockAxios.get).toHaveBeenCalledWith("/api/all-users");

    // Testing when request gives an error or not
    if (err === true) {
      expect(thenFn).not.toHaveBeenCalled();
      expect(catchFn).toHaveBeenCalledWith(response);
    } else {
      expect(thenFn).toHaveBeenCalledWith(response);
      expect(catchFn).not.toHaveBeenCalled();
    }
  };

  test("Testing retrieving a list of all users", () => {
    response = {
      data: {
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
      },
    };

    allUsersTest(response);
  });
  test("Testing handling empty user object", () => {
    response = {
      data: {
        users: [],
      },
      status: 200,
    };

    allUsersTest(response);
  });
});
