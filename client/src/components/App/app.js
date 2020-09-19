// React Imports
import React, { useState } from "react";

// Component Imports
import { Tabs } from "../Tabs";
import { EntryList } from "../EntryList/entrylist";

// Utilities Import
import { create, allUsers } from "../../utils/request";
import { userCreate, categories } from "../../utils/userCreate";

// Assets Imports
import "./app.css";

const tabs = [...categories, "all"];

function App() {
  const [tab, setTab] = useState(0);
  const [user, setUser] = useState(userCreate());
  const [dest, setDest] = useState();
  const [amount, setAmount] = useState();
  return (
    <div className="App">
      <h1>Budget Calculator</h1>
      <div className="">
        <input data-testid="desc" placeholder="Description" />
        <input data-testid="amount" placeholder="Amount" />
      </div>
    </div>
  );
}

export default App;
