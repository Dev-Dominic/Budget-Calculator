/* Testing Imports */
import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";

/* Component */
import Tabs from "./tabs";

/* Test Tabs */
const _tabs = ["income", "savings", "expenses", "all"];

describe("<Tabs />", () => {
  test("Test that each tab is present", () => {
    render(<Tabs tabs={_tabs} active={0} onChangeTab={() => {}} />);

    _tabs.forEach((_tab) => expect(screen.getByText(_tab)).toBeInTheDocument());
  });

  // Tabs 'active' prop takes an integer, thus _tabs needed to converted to a
  // list of indexes to represent what current tab is active, can be used to
  // retrieve associated title from '_tabs'
  test.each(_tabs.map((e, index) => index))(
    "Tests active tab element: %s element",
    (tabIndex) => {
      render(<Tabs tabs={_tabs} active={tabIndex} onChangeTab={() => {}} />);

      // Checking that current 'tabIndex' contains 'active' class
      expect(screen.getByTestId(_tabs[tabIndex])).toHaveClass("active");

      // Checking that every other tab element does not have active class
      for (let i = 0; i < _tabs.length; i++) {
        if (i === tabIndex) continue;
        expect(screen.getByTestId(_tabs[i])).not.toHaveClass("active");
      }
    }
  );
});
