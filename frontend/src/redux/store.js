// store.js
import { configureStore } from '@reduxjs/toolkit';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage'; // localStorage
import settingsReducer from './reducer'; // Path to your reducer file

// Persist config
const persistConfig = {
    key: 'root',
    storage, // You can also use sessionStorage if needed
};

// Persisted reducer
const persistedReducer = persistReducer(persistConfig, settingsReducer);

const store = configureStore({
    reducer: {
        settings: persistedReducer,
    },
});

const persistor = persistStore(store);

export { store, persistor };