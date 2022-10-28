import { configureStore } from "@reduxjs/toolkit";
import properyReducer from "../features/properties/propertyslice";

export const store = configureStore({
  reducer: {
    properties: properyReducer,
  },
});
