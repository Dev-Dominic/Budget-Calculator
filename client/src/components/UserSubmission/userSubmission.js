/* React Imports */
import React from "react";

function TotalGroup({ title, total, data_testid }) {
  const total_format = `$${parseInt(total).toLocaleString()}`;
  return (
    <div className="">
      <h4 className="">{title}</h4>
      <p className="" data-testid={data_testid}>
        {total_format}
      </p>
    </div>
  );
}

function UserSubmission({ userID, totals, message }) {
  return (
    <div className="">
      <div className="">
        <h4>UserID:</h4>
        <p className="" data-testid={userID}>
          {userID}
        </p>
      </div>
      <div className="">
        <TotalGroup
          title={"Total Income"}
          total={totals["totalIncome"]}
          data_testid={"totalIncome"}
        />
        <TotalGroup
          title={"Total Savings"}
          total={totals["totalSavings"]}
          data_testid={"totalSavings"}
        />
        <TotalGroup
          title={"Total Expenses"}
          total={totals["totalExpenses"]}
          data_testid={"totalExpenses"}
        />
      </div>
      <p className="" data-testid={message}>
        {message}
      </p>
    </div>
  );
}

export default UserSubmission;
