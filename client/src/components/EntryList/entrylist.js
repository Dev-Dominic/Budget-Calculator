/* React Imports */
import React from "react";

/* Computer Imports */
import Entry from "./components/entry/entry";

function EntryList({ entries, onDelete }) {
  return (
    <div className="">
      {entries.map(({ desc, amount }, index) => (
        <Entry
          desc={desc}
          amount={amount}
          key={`entry-${index}`}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default EntryList;
