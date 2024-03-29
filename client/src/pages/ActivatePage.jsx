import React, { useEffect, useState } from "react";
import { Button, Col, Container, Row, Form } from "react-bootstrap";
import { FaCheckCircle } from "react-icons/fa";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate, useParams } from "react-router-dom";
import { toast } from "react-toastify";
import Spinner from "../components/Spinner";
import Title from "../components/Title";
import { activate, reset } from "../features/auth/authSlice";

const ActivatePage = () => {
  const { uid, token } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const { isLoading, isError, isSuccess, message } = useSelector(
    (state) => state.auth
  );

  useEffect(() => {
    if (isError) {
      toast.error(message);
    }
    if (isSuccess) {
      toast.success("Your account has been activated, you can login now");
      navigate("/");
    }
    dispatch(reset());
  }, [isError, isSuccess, message, navigate, dispatch]);

  const submitHandler = () => {
    const userData = { uid, token };
    dispatch(activate(userData));
  };

  return (
    <>
      <Title title="Activate User" />
      <Container>
        <Row>
          <Col className="mg-top text-center">
            <section>
              <h1>
                <FaCheckCircle /> Activate
              </h1>
              <hr className="hr-text" />
            </section>
          </Col>
        </Row>
        {isLoading && <Spinner />}
        <Row className="mt-3">
          <Button
            type="submit"
            variant="outline-success"
            size="lg"
            onClick={submitHandler}
          >
            Activate
          </Button>
        </Row>
      </Container>
    </>
  );
};

export default ActivatePage;
