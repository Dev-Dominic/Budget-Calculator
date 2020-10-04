/* React Imports */
import React from "react";
import { render, screen } from "@testing-library/react";

/* Component Import */
import Button from "./button";

describe("<SubmitButton />", () => {
  const buttonText = ["Submit", "Add", "Remove"];
  test.each(buttonText)("Test for button text", (text) => {
    render(<Button onSubmit={() => {}} buttonText={text} />);
    expect(screen.getByText(text)).toBeInTheDocument();
  });
});
