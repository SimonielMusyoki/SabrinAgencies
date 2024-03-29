import React, { useEffect } from "react";
import { Col, Container, Row } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { toast } from "react-toastify";
import Spinner from "../components/Spinner";
import Property from "../components/Property";
import { getProperties, reset } from "../features/properties/propertyslice";
import Title from "../components/Title";

const PropertiesPage = () => {
  const { properties, isLoading, isError, message } = useSelector(
    (state) => state.properties
  );
  const dispatch = useDispatch();

  useEffect(() => {
    if (isError) {
      toast.error(message);
    }
    dispatch(getProperties());
  }, [dispatch, isError, message]);

  if (isLoading) {
    return <Spinner />;
  }

  return (
    <>
      <Title title="Real Estate properties" />
      <Container>
        <Row>
          <Col className="mg-top text-center">
            <h1>Our Properties Catalog</h1>
            <hr className="hr-text" />
          </Col>
        </Row>
        {
          <>
            <Row className="mt-3">
              {properties.map((property) => (
                <Col key={property.id} sm={12} md={6} lg={4} xl={3}>
                  <Property property={property} />
                </Col>
              ))}
            </Row>
          </>
        }
      </Container>
    </>
  );
};

export default PropertiesPage;
