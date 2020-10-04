/* React Imports */
import React from "react";

/* Computer Imports */
import Entry from "./components/entry/entry";

function EntryList({ entries, onDelete }) {
  return (
    <div className="">
      {entries.map(({ desc, amount }, i) => (
        <Entry
          desc={desc}
          amount={amount}
          key={`entry-${i}`}
          index={i}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default EntryList;
