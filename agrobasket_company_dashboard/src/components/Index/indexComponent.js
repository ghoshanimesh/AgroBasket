import React from "react"
import "./indexComponent.css"

const IndexComponent = () => {
  return (
    <div>
      <section class="smart-scroll">
        <div class="container-fluid">
          <nav class="navbar navbar-expand-md navbar-light">
            <a class="navbar-brand heading-black" href="/">
              <img src="/images/logo.png" height="50" />
            </a>
            <button
              class="navbar-toggler navbar-toggler-right border-0"
              type="button"
              data-toggle="collapse"
              data-target="#navbarCollapse"
              aria-controls="navbarCollapse"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span data-feather="grid"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
              <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                  <a class="nav-link page-scroll" href="#about">
                    About Us
                  </a>
                </li>
              </ul>
              <a class="btn btn-primary" href="/loginPage">
                Login / Register
              </a>
            </div>
          </nav>
        </div>
      </section>

      <section class="pb-md-4" id="home">
        <div class="container">
          <div class="row">
            <div class="col-md-8 col-sm-10 col-12 mx-auto text-center">
              <img
                src="images/banner.jpg"
                class="img-fluid mx-auto img-banner"
                alt="Mockup"
              />
              <h1 class="heading-black mt-3 mb-0 font-weight-bold">Agro Basket</h1>
              <p class="lead">Manage all your farmers and produce at one place with your sales. </p>
            </div>
          </div>
        </div>
      </section>
      <section class="py-6 bg-light" id="about">
        <div class="container">
          <div class="row">
            <div class="col-md-7 mx-auto text-center">
              <h2 class="text-capitalize header text-primary font-weight-bold">
                Who we are?
              </h2>
              <div class="divider mx-auto bg-primary"></div>
            </div>
          </div>
          <div class="row mt-2 px-4">
            <p class="about-us-para text-primary text-center">
              Agrobasket is a precision agriculture platform that leverages data
              to pick the finest produce from the best farmers and deliver it to
              companies based on a contract. We monitor every stage of the
              Farm-to-Company cycle to derive synergies for our customers and
              partner ecosystem.
            </p>
          </div>
        </div>
      </section>
      <section class="py-6">
        <div class="container">
          <div class="row mt-5">
            <div class="col-md-10 mx-auto">
              <div class="card bg-dark p-4">
                <div class="card-body d-md-flex flex-row align-items-center text-center text-md-left">
                  <div class="mb-4 mb-md-0">
                    <h4 class="text-white">Try AgroBasket Now!</h4>
                    <span class="text-light">
                      Sign up now and connect with farmers.
                    </span>
                  </div>
                  <a href="/loginPage" class="btn btn-primary ml-md-auto d-inline-flex flex-row align-items-center">
                    Get Started
                    <em
                      data-feather="chevrons-right"
                      width="20"
                      height="20"
                      class="ml-2"
                    ></em>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <footer class="pt-3 pb-5">
        <div class="container">
          <div class="row mt-5">
            <div class="col-12 text-center">
              &copy; 2021 AgroBasket - All Rights Reserved
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default IndexComponent
