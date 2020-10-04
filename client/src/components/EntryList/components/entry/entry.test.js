/* React Imports */
import React from "react";
import { render, screen } from "@testing-library/react";

/* Component Imports */
import Entry from "./entry";
import { entries } from "../../constants";

describe("<Entry />", () => {
  test.each(entries)(
    "Tests that the props passed to entry are rendered",
    (entry) => {
      const { desc, amount, expectedAmount } = entry;
      // Rendering Entry
      render(
        <Entry desc={desc} amount={amount} index={1} onDelete={() => {}} />
      );

      // Testing proper rendering of entry
      expect(screen.getByTestId(`${desc}-1`).textContent).toBe(desc);
      expect(screen.getByTestId(`${amount}-1`).textContent).toBe(
        expectedAmount
      );

      // Checks that delete button is rendered
      expect(screen.getByTestId("delete")).toBeInTheDocument();
    }
  );
});
