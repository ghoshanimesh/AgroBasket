import { faCaretDown, faEye, faTimes } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import React, { useState, useEffect } from "react"
import { Accordion, Button, Card } from "react-bootstrap"
import { getProgressLog } from "../../services/post"
import "./ViewPostLogComponent.css"

const titleCase = str => {
  return str
    .toLowerCase()
    .split(" ")
    .map(function (word) {
      return word.replace(word[0], word[0].toUpperCase())
    })
    .join(" ")
}

const SingleFarmerLog = eventKey => {
  return (
    <Card className="mb-4">
      <Card.Header className="bg-dark">
        <button href={"/"} type="button" class="btn btn-link mr-2 float-right text-capitalize">
          <FontAwesomeIcon icon={faTimes} size="lg" /> <br /> Close
        </button>
        <Accordion.Toggle
          as={Button}
          variant="link"
          eventKey={eventKey}
          className="float-right text-capitalize"
        >
          <FontAwesomeIcon icon={faEye} size="lg" /> <br /> View
        </Accordion.Toggle>

        <p className="mt-2 mb-2 text-primary">
          Animesh Ghosh
          <span class="text-muted"> (</span>
          <span class="text-muted fs-small">&nbsp; +91 9082879987 &nbsp;</span>
          <span class="text-muted">
            ) <br /> {titleCase("BUXAR")}, Bihar <br />
          </span>
        </p>
        <p class="mt-2 text-white">
          Jowar : 20 units * 1125 Rs. per unit = {20 * 1125} Rs. <br />
          From 1st July, 2021 to 1st September, 2022
        </p>
      </Card.Header>
      <Accordion.Collapse eventKey={eventKey}>
        <Card.Body className="bg-light">
          <Card.Title>Card Title</Card.Title>
          <Card.Text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </Card.Text>
          <Button variant="primary">Go somewhere</Button>
        </Card.Body>
      </Accordion.Collapse>
    </Card>
  )
}

const ViewPostLogComp = ({ id }) => {
  useEffect(() => {
    async function getLog() {
      const res = await getProgressLog({ postId: id })
      console.log(res[0])
    }
    getLog()
  }, [])

  return (
    <section>
      <div className="">
        <div className="container p-4">
        <div class="row mb-2">
        <div className="col-md-12">
            <h5 class="font-weight-bold">Progress Log - Jowar, June</h5>
        </div>
        </div>
          <div className="row mb-3">
            <div className="col-md-12">
              <Accordion defaultActiveKey="0">
                <SingleFarmerLog eventKey={0}></SingleFarmerLog>
                <SingleFarmerLog eventKey={1}></SingleFarmerLog>
                <SingleFarmerLog eventKey={2}></SingleFarmerLog>
              </Accordion>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default ViewPostLogComp
