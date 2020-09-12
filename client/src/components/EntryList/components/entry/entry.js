/* React Imports */
import React from "react";

function Delete({ onDelete }) {
  return (
    <div data-testid="delete" onClick={onDelete}>
      -
    </div>
  );
}

function Entry({ desc, amount, onDelete }) {
  // Changing format of amount, E.g 40000 => $40,000
  const amount_format = `$${amount.toLocaleString()}`;
  return (
    <div className="">
      <div data-testid={desc}>{desc}</div>
      <div data-testid={amount}>{amount_format}</div>
      <Delete onDelete={onDelete} />
    </div>
  );
}

export default Entry;
