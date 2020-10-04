/* React Imports */
import React from "react";

function Button({ onSubmit, buttonText }) {
  return (
    <div className="">
      <button data-testid={buttonText} onClick={onSubmit}>
        {buttonText}
      </button>
    </div>
  );
}

export default Button;
