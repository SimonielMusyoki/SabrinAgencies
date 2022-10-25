import React from "react";
import About from "../components/Home/About";
import Faqs from "../components/Home/Faqs";
import Options from "../components/Home/Options";
import Banner from "../components/Home/Banner";

function Homepage() {
  return (
    <div className="main">
      <Banner />
      <About />
      <Options />
      <Faqs />
    </div>
  );
}

export default Homepage;
