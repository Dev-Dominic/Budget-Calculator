// React Imports
import React from "react";

// Asserts Imports
import "./tabs.css";

function Tabs({ tabs, active, onChangeTab }) {
  return (
    <div className="">
      {tabs.map((tab, index) => {
        if (index === active)
          return (
            <div
              className="active"
              key={index}
              data-testid={tab}
              onClick={onChangeTab}
            >
              {tab}
            </div>
          );

        return (
          <div className="" key={index} data-testid={tab} onClick={onChangeTab}>
            {tab}
          </div>
        );
      })}
    </div>
  );
}

export default Tabs;
