
import React, { useState } from "react";
import NavbarMenuElement from "../shared/navbarMenuElement";
import "../../styles/navbar.css";

import { useDispatch } from "react-redux";
import { logOut } from "../../redux/reducer"; // Assuming you have a logOut action in Redux


const Navbar = () => {

    const dispatch = useDispatch();

    const handleLogOut = () => {
        // Dispatch the log out action
        dispatch(logOut());

        // Optionally, you can clear authentication tokens or cookies here
        document.cookie = "bearer=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"; // Clear cookie
        alert("Logged out successfully.");
    };
    return (
        <nav className="navbar-container">
            <NavbarMenuElement initialLabel="Home" />
            <NavbarMenuElement initialLabel="About" />

            <NavbarMenuElement initialLabel="Log out" onClick={handleLogOut} />
        </nav >
    )
};


export default Navbar;