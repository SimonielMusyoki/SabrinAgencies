import React from "react";
import { Col, Row } from "antd";

const items = [
  {
    key: "1",
    icon: <i className="fas fa-search-location"></i>,
    title: "Simplified Search",
    content:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus dolore deleniti, aliquid velit quidem soluta? Dolor, id. Consequatur praesentium nemo ipsam fugit eveniet velit, quibusdam similique qui illo, maxime obcaecati.",
  },
  {
    key: "2",
    icon: <i className="fas fa-database"></i>,
    title: "Lots of Properties",
    content:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus dolore deleniti, aliquid velit quidem soluta? Dolor, id. Consequatur praesentium nemo ipsam fugit eveniet velit, quibusdam similique qui illo, maxime obcaecati.",
  },
  {
    key: "3",
    icon: <i className="fas fa-globe-africa"></i>,
    title: "Proudly African",
    content:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus dolore deleniti, aliquid velit quidem soluta? Dolor, id. Consequatur praesentium nemo ipsam fugit eveniet velit, quibusdam similique qui illo, maxime obcaecati.",
  },
];

function About() {
  return (
    <div id="about" className="block about-section">
      <div className="fluid-container">
        <div className="title-section">
          <h2>About Us</h2>
          <p>You will find us very interesting!</p>
        </div>
        <div className="content-section">
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto
            corrupti et dignissimos quas cum vero sequi nam nostrum dolorem,
            quidem tempore esse cupiditate libero ad porro magnam odit rem
            iusto!
          </p>
        </div>
        <Row gutter={[16, 16]}>
          {items.map((item) => {
            return (
              <Col md={{ span: 8 }} key={item.key}>
                <div className="content">
                  <div className="icon">{item.icon}</div>
                  <h3>{item.title}</h3>
                  <p>{item.content}</p>
                </div>
              </Col>
            );
          })}
        </Row>
      </div>
    </div>
  );
}

export default About;
