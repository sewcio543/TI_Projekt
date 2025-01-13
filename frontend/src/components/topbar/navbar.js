
import React from "react";
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
        document.cookie = "user_id=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"; // Clear user_id cookie
        alert("Logged out successfully.");
    };
    return (
        <nav className="navbar navbar-expand-lg" style={{ backgroundColor: "#d31a32" }}>
            <div className="container-fluid">
                <h1 className="display-1" style={{ fontWeight: "bold" }}>GrudgeHub</h1>
                <div className="ml-auto d-flex">
                    <NavbarMenuElement initialLabel="Log out" onClick={handleLogOut} className="nav-link mx-10" />
                </div>
            </div>
        </nav>
    )
};


export default Navbar;