
import React, { useState } from "react";
const NavbarMenuElement = ({ initialLabel, onClick }) => {

    const [label, setLabel] = useState(initialLabel || "Default");

    return (
        <div className="navbar-button-container">
            <button onClick={onClick}>
                <h1>{label}</h1>
            </button>
        </div>
    )
};


export default NavbarMenuElement;