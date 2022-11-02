import { configureStore } from "@reduxjs/toolkit";
import properyReducer from "../features/properties/propertyslice";
import authReducer from "../features/auth/authSlice";

export const store = configureStore({
  reducer: {
    properties: properyReducer,
    auth: authReducer,
  },
});
