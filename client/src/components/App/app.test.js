import React from "react";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import App from "./app";

describe("<App /> Application Title", () => {
  test("Ensures that App title is rendered", () => {
    render(<App />);
    expect(screen.getByText("Budget Calculator")).toBeInTheDocument();
  });
});

describe("<App /> Adding new items to each category", () => {
  test("Testing that new description and amount fields are updated", () => {
    // Rendering main app
    render(<App />);

    // Adding new description and amount
    const [desc, amount] = [
      screen.getByTestId("desc"),
      screen.getByTestId("amount"),
    ];

    // Adding new values to these input fields
    userEvent.type(desc, "Salary");
    userEvent.type(amount, "150000");

    // Assertions
    expect(desc).toHaveValue("Salary");
    expect(amount).toHaveValue("150000");
  });

  test("Testing that when add button is pressed that entrylist is updated", () => {
    // Rendering main app
    render(<App />);

    // Adding new description and amount
    const [desc, amount, add, entrylist] = [
      screen.getByTestId("desc"),
      screen.getByTestId("amount"),
      screen.getByTestId("add"),
      screen.getByTestId("entrylist"),
    ];

    // Adding new values to these input fields
    userEvent.type(desc, "Salary");
    userEvent.type(amount, "150000");

    // Simulating adding new entry
    userEvent.click(add);

    // Asserting that input field has been cleared
    expect(desc).toHaveValue("");
    expect(amount).toHaveValue("");

    // Asserting that new entry has been added to entrylist
    expect(entrylist).toHave;
  });
});
