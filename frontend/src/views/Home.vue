<template>
  <div class="home">
    <div class="fade-container">
      <Navbar />
      <div class="bg">
        <div class="container text-scroll-bg">
          <transition onload name="PokeIn">
            <img src="../assets/PokeBallUpright.png" class="upright" />
          </transition>
          <div class="container container-text">
            <div class="row">
              <div class="col-lg-12">
                <div class="jumbotron">
                  <p class="hero-text">
                    PokéDB
                    <img
                      src="../assets/pokeball.png"
                      style="max-width: 110px"
                    />
                  </p>
                  <p class="subhead-text">
                    An indexed database for Pokémon, their evolutions, and
                    types. <br />Click below to start exploring.
                  </p>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-sm-4">
                <div class="card" id="types-card">
                  <div class="card-header">
                    Types
                  </div>
                  <div class="card-body">
                    <p class="card-text">
                      Explore the 18 types across all the pokémon games.
                    </p>
                    <a href="/types" class="btn btn-primary btn-dark">Go!</a>
                  </div>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="card" id="poke-card">
                  <div class="card-header">
                    Pokémon
                  </div>
                  <div class="card-body">
                    <p class="card-text">
                      There are hundreds of pokémon. Which one is your favorite?
                    </p>
                    <a href="/pokemon/" class="btn btn-primary btn-dark">Go!</a>
                  </div>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="card" id="evol-card">
                  <div class="card-header">
                    Evolutions
                  </div>
                  <div class="card-body">
                    <p class="card-text">
                      Answer the question: what came first, the Togepi or the
                      egg?
                    </p>
                    <a href="/evolutions" class="btn btn-primary btn-dark"
                      >Go!</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.jumbrotron {
  align-content: center;
  align-self: center;
  box-shadow: 2px 2px 2px;
}
.hero-text {
  -webkit-text-fill-color: black;
  font-size: 72pt;
  align-content: center;
  margin-bottom: 20px;
}

.subhead-text {
  font-size: 24pt;
  align-content: center;
  margin-bottom: 25px;
  -webkit-text-fill-color: rgb(51, 51, 51);
}
.row {
  margin-bottom: 50px;
}
.bg {
  padding-top: 0;

  margin-bottom: 0px;

  /* The image used */
  background-image: url("../assets/home-background.jpg");

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

.container-text {
  opacity: 0;
  margin-top: 0%;
  transform: translateY(-100%);
  padding: 25px;
  animation: fadeInAfterPoke 1s 1 forwards;
  animation-delay: 1.4s;
}
@media (max-width: 991px) {
  .container-text {
    opacity: 0;
    margin-top: 55%;
    transform: translateY(-100%);
    padding: 25px;
    animation: fadeInAfterPoke 1s 1 forwards;
    animation-delay: 1.4s;
  }
}

.card {
  box-shadow: 4px 4px 4px;
}

.btn {
  background-color: darkgray;
  border-style: solid;
  border-color: black;
  border-width: 1.5px;
}
@keyframes fadeInAfterPoke {
  0% {
    opacity: 0;
    scale: 0.1;
  }
  100% {
    opacity: 1;
    scale: 1;
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

@keyframes textUP {
  0% {
    transform: translateY(100%);
    opacity: 0;
  }
  100% {
    transform: translateY(0%);
    opacity: 1;
  }
}

.fade-container {
  animation: FadeIn 1.5s 1 forwards;
}
.home {
  margin-bottom: 0%;
  overflow: hidden;
  background-color: rgba(65, 65, 65, 0.9);
}

@keyframes FadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

.upright {
  width: 85%;
  max-width: 1100px;
  animation: PokeIn 2s 1 forwards;
  position: relative;
  z-index: 0;
}

@keyframes PokeIn {
  0% {
    transform: translateY(100%);
  }

  33% {
    transform: translateY(-20%);
    transform: rotate(-180deg);
  }

  66% {
    transform: translateY(0%);
  }
  100% {
    transform: translateY(-120%);
  }
}

#navbar {
  z-index: 1;
  width: 20%;
  position: fixed;
  animation: navFill 1.5s 1 forwards;
}

@keyframes navFill {
  0% {
    width: 25%;
  }

  100% {
    width: 100%;
  }
}
</style>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar
  },
  el: "#home",
  data() {
    return {
      clicked: true
    };
  }
};
</script>