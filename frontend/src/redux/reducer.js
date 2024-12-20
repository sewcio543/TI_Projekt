import { createSlice } from "@reduxjs/toolkit";

const settingsSlice = createSlice(
    {
        name: "settings",
        initialState: {
            isLoggedIn: false,
        },
        reducers: {
            logIn: (state) => {
                state.isLoggedIn = true;
            },
            logOut: (state) => {
                state.isLoggedIn = false;
            }
        }
    }
);

// Export actions to use in components (.actions is genereted automatically by createSlice)
export const { logIn, logOut } = settingsSlice.actions;


// Export reducer to use in store
export default settingsSlice.reducer;