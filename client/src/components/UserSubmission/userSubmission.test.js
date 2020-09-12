/* React Imports */
import React from "react";
import { render, screen } from "@testing-library/react";

/* Components Imports */
import UserSubmission from "./userSubmission";

describe("<UserSubmission />", () => {
  test("Tests that user sumbissions are rendered properly", () => {
    const [userID, totals, expectedTotals, message] = [
      "507f191e810c19729de860ea",
      { totalIncome: 2000000, totalSavings: 30000, totalExpenses: 250000 },
      {
        totalIncome: "$2,000,000",
        totalSavings: "$30,000",
        totalExpenses: "$250,000",
      },
      "You have a handle of your budget",
    ];
    render(
      <UserSubmission userID={userID} totals={totals} message={message} />
    );

    // Testing for each rendered prop
    expect(screen.getByTestId(userID)).toBeInTheDocument();
    expect(screen.getByTestId(userID).textContent).toBe(userID);

    expect(screen.getByTestId(message)).toBeInTheDocument();
    expect(screen.getByTestId(message).textContent).toBe(message);

    // Testing that each total was rendered and has been converted to conrrency
    // format
    for (const total in totals) {
      expect(screen.getByTestId(total)).toBeInTheDocument();
      expect(screen.getByTestId(total).textContent).toBe(expectedTotals[total]);
    }
  });
});
