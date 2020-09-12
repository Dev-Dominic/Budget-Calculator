/* React Imports */
import React from "react";
import { render, screen } from "@testing-library/react";

/* Component Import */
import SubmitButton from "./submitbutton";

describe("<SubmitButton />", () => {
  test("Test for button text", () => {
    render(<SubmitButton onSubmit={() => {}} />);
    expect(screen.getByText("Submit")).toBeInTheDocument();
  });
});
