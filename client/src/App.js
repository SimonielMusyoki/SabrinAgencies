import React from "react";
import { Layout } from "antd";
import { BrowserRouter as Router, Route } from "react-router-dom";

import "./App.css";

import AppHeader from "./components/common/AppHeader";
import AppFooter from "./components/common/AppFooter";

import Homepage from "./pages/Homepage";
import PropertyListPage from "./pages/PropertyListPage";

const { Content, Header, Footer } = Layout;

function App() {
  return (
    <Router>
      <Layout className="main-layout">
        <Header>
          <AppHeader />
        </Header>
        <Content>
          <Route exact path="/" component={Homepage} />
          <Route path="/properties" component={PropertyListPage} />
        </Content>
        <Footer>
          <AppFooter />
        </Footer>
      </Layout>
    </Router>
  );
}

export default App;
