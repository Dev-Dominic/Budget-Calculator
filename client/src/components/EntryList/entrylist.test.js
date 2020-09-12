/* React Imports */
import React from "react";
import { render, screen } from "@testing-library/react";

/* Component Import */
import EntryList from "./entrylist";
import Entry from "./components/entry";
import { entries } from "./constants";

describe("<EntryList />", () => {
  // Differs from Entry component test by testing that multiple entries are
  // rendered at the same time
  test("Tests that all entries are rendered", () => {
    render(<EntryList entries={entries} onDelete={() => {}} />);

    entries.forEach((entry) => {
      const { desc, amount, expected_amount } = entry;
      expect(screen.getByTestId(desc).textContent).toBe(desc);
      expect(screen.getByTestId(amount).textContent).toBe(expected_amount);
    });
  });
});
