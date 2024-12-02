import { configureStore } from "@reduxjs/toolkit";
import settingsReducer from "./reducer";

// Configure the Redux store. It's bascially a container for current state of the app.
// It holds the state of the app and allows to dispatch actions to change the state
const store = configureStore({
    reducer: {
        settings: settingsReducer,
    },
});

export default store;