import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./app";

describe("<App />", () => {
  test("renders learn react link", () => {
    render(<App />);
    expect(screen.getByText("Budget Calculator")).toBeInTheDocument();
  });
});
