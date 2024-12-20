
import React, { useState } from "react";
import NavbarMenuElement from "../shared/navbarMenuElement";
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
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container-fluid">
                <NavbarMenuElement initialLabel="Home" className="navbar-brand" />
                <NavbarMenuElement initialLabel="About" className="nav-link" />
                <NavbarMenuElement initialLabel="Log out" onClick={handleLogOut} className="nav-link" />
            </div>
        </nav>
    )
};


export default Navbar;