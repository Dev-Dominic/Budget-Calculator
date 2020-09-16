// React Imports
import React, { useState } from "react";

// Component Imports
import { Tabs } from "../Tabs";
import { EntryList } from "../EntryList/entrylist";

// Utilities Import
import { allUsers } from "../../utils/request";
import { userCreate, categories } from "../../utils/userCreate";

// Assets Imports
import "./app.css";

function App() {
  return (
    <div className="App">
      <h1>Budget Calculator</h1>
    </div>
  );
}

export default App;
