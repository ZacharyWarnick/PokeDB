<template>
  <div class="types">

    <Navbar />
    <div class="bg">
    <div class="fade-container">
    <div class="container text-scroll-bg">
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
                  <div class="d-flex justify-content-between align-items-center">
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
                  <div class="d-flex justify-content-between align-items-center">
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
                  <div class="d-flex justify-content-between align-items-center">
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
                  <div class="d-flex justify-content-between align-items-center">
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
    </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import CardItem from "@/components/CardItem.vue";

export default {
  name: "Types",
  components: {
    Navbar,
    CardItem
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px;
}
.fade-container {
  padding-top: 0px;
	animation: FadeIn 1.5s 1 forwards;
}
@keyframes FadeIn {
  0%{
    opacity: 0
  }
  
  100% {
    opacity: 1;
  }
}
.text-scroll-bg {
  background-color: white;
  width: 1920px;
  height: 1500px;

  padding-top: 30px;
  padding-bottom: 30px;
  align-content: center;
  box-shadow: 4px 4px 4px;

  animation: textUP 1.5s 1 forwards;

}
.bg {
  padding-top: 0;

  margin-bottom: 0px;

  /* The image used */
  background-image: url('../assets/home-background.jpg');

  /* Full height */
  height: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;

  align-content: center;

  position: sticky;
}
</style>
