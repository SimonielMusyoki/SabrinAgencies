import React from "react";
import { Row, Container, Col } from "react-bootstrap";

function Footer() {
  return (
    <footer>
      <Container>
        <Row>
          <Col className="py-3">
            Copyright &copy; Real Estate {new Date().getFullYear()}
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
