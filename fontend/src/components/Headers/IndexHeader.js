/*eslint-disable*/
import React from "react";

// reactstrap components
import { Container } from "reactstrap";
// core components

function IndexHeader() {
  let pageHeader = React.createRef();

  React.useEffect(() => {
    if (window.innerWidth > 991) {
      const updateScroll = () => {
        let windowScrollTop = window.pageYOffset / 3;
        pageHeader.current.style.transform =
          "translate3d(0," + windowScrollTop + "px,0)";
      };
      window.addEventListener("scroll", updateScroll);
      return function cleanup() {
        window.removeEventListener("scroll", updateScroll);
      };
    }
  });

  return (
    <>
      <div className="page-header clear-filter" filter-color="blue">
        <div
          className="page-header-image"
          style={{
            backgroundImage: "url(" + require("assets/img/header.jpg") + ")"
          }}
          ref={pageHeader}
        ></div>
        <Container>
        <div className="content-center brand">
            <img
              alt="..."
              className="n-logo"
              src={require("assets/img/northroppyimg.png")}
              style={{ width: "100px", height: "100px" }}  // Adjust the width as needed
            />
            <h1 className="h1-seo">Northrop Grumman Volleyball</h1>
          </div>

          <h6 className="category category-absolute">
            Designed by CSUSM {" "}
            . Coded by Blake Fullerton{" "}
            .
          </h6>
        </Container>
      </div>
    </>
  );
}

export default IndexHeader;
