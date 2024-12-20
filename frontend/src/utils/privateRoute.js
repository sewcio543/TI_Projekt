import { Navigate } from "react-router-dom";
import { useSelector } from "react-redux";

const PrivateRoute = ({ element }) => {
    const { isLoggedIn } = useSelector((state) => state.settings);

    if (!isLoggedIn) {
        // If not logged in, redirect to login page
        return <Navigate to="/login" />;
    }

    return element;
};

export default PrivateRoute;