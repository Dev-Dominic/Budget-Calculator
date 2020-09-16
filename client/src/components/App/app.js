// React Imports
import React, { useState } from "react";

// Component Imports
import { Tabs } from "../Tabs";
import { EntryList } from "../EntryList/entrylist";

// Utilies Import
import { allUsers } from "../../utils/request/request";

// Assets Imports
import "./app.css";

function App() {
  const [tab, setTab] = useState("income");
  return (
    <div className="App">
      <h1>Budget Calculator</h1>
    </div>
  );
}

export default App;
