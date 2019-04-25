<template>
  <div id="type-list">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg fade-container">
        <b-container class="section-padding">
          <b-jumbotron class="text-center" header="Types">
            <p class="lead text-muted">
              There are 18 types across all Pokémon games.
            </p>
          </b-jumbotron>
        </b-container>

        <section class="album">
          <div class="container">
            <div class="row">
              <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                  <img
                    class="card-img-top"
                    src="https://i.pinimg.com/originals/b0/bc/69/b0bc69eacf147a54ec4e5c4cacdf81db.jpg"
                  />
                  <div class="card-body">
                    <div
                      class="d-flex justify-content-between align-items-center"
                    >
                      <router-link
                        tag="button"
                        class="btn btn-lg btn-block btn-outline-secondary"
                        to="/types/water"
                        >View</router-link
                      >
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                  <img
                    class="card-img-top"
                    src="https://i.ytimg.com/vi/inE_NHjK3fE/maxresdefault.jpg"
                  />
                  <div class="card-body">
                    <div
                      class="d-flex justify-content-between align-items-center"
                    >
                      <router-link
                        tag="button"
                        class="btn btn-lg btn-block btn-outline-secondary"
                        to="/types/flying"
                        >View</router-link
                      >
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                  <img
                    class="card-img-top"
                    src="https://i.ytimg.com/vi/NU_Z-qkSCYs/maxresdefault.jpg"
                  />
                  <div class="card-body">
                    <div
                      class="d-flex justify-content-between align-items-center"
                    >
                      <router-link
                        tag="button"
                        class="btn btn-lg btn-block btn-outline-secondary"
                        to="/types/poison"
                        >View</router-link
                      >
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                  <img
                    class="card-img-top"
                    src="https://d2juyu303oh9b6.cloudfront.net/image/152367997cae9bab386e4c45237f347b.jpg?&icq=80&sig=def4fe4660a040f5b8e270c031a0dd94"
                  />
                  <div class="card-body">
                    <div
                      class="d-flex justify-content-between align-items-center"
                    >
                      <router-link
                        to="/types/ground"
                        tag="button"
                        class="btn btn-lg btn-block btn-outline-secondary"
                        >View</router-link
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Types",
  components: {
    Navbar
  }
};
</script>
