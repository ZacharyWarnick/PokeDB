<template>
  <div id="home">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg">
        <div class="row">
          <div class="col-lg-12">
            <div class="jumbotron">
              <p class="hero-text">
                PokéDB
                <transition onload name="RollRtoL">
                  <img class="pokeball" src="../assets/pokeball.png" />
                </transition>
              </p>
              <p class="subhead-text">
                An indexed database for Pokémon, their evolutions, and types.
                <br />Click below to start exploring.
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
                <router-link to="/types" class="btn btn-primary btn-dark"
                  >Go!</router-link
                >
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
                <router-link to="/pokemon" class="btn btn-primary btn-dark"
                  >Go!</router-link
                >
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
                  Answer the question: what came first, the Togepi or the egg?
                </p>
                <router-link to="/evolutions" class="btn btn-primary btn-dark"
                  >Go!</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
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

<style scoped>
#home {
  min-height: 100vh !important;
  background-color: rgba(65, 65, 65, 0.2);
}

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

.container-text {
  padding: 25px;
}

.pokeball {
  display: inline-block;
  vertical-align: middle;
  position: relative;
  max-height: 100px;
  max-width: 300%;
  opacity: 0;
  animation: RollRtoL 3s 1s forwards;
}

.card {
  box-shadow: 2px 2px 2px;
}

.btn {
  background-color: darkgray;
  border-style: solid;
  border-color: black;
  border-width: 1.5px;
}

@keyframes RollRtoL {
  0% {
    transform: translateX(300%) rotate(540deg);
    opacity: 0;
  }

  80% {
    transform: translateX(-1%) rotate(-2deg);
    opacity: 1;
  }
<<<<<<< HEAD
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
  width: 100%;
  position: fixed;
  animation: navFill 1.5s 1 forwards;
}

@keyframes navFill {
  0% {
    width: 25%;
  }
=======
>>>>>>> develop

  100% {
    transform: translateX(0%) rotate(0deg);
    opacity: 1;
  }
}
</style>
