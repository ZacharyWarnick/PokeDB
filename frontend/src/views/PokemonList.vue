<template>
  <div>
    <Navbar />
    <div class="bg">
      <div class="fade-container">
        <div class="container text-scroll-bg">
          <b-container class="section-padding">
            <b-jumbotron header="Pokémon" lead="Gotta Catch 'Em All" />
          </b-container>
          <section>
            <b-container>
              <b-row>
                <b-col
                  cols="12"
                  sm="6"
                  md="4"
                  lg="3"
                  v-for="p in pokemon.data"
                  v-bind:key="p.id"
                >
                  <b-card class="row-card shadow-sm">
                    <SpriteBasic
                      v-bind:name="p.name"
                      v-bind:id="p.id"
                      v-bind:types="p.types"
                    />
                    <router-link
                      v-bind:to="'/pokemon/' + p.identifier"
                      class="btn btn-outline-dark"
                      >Info</router-link
                    >
                  </b-card>
                </b-col>
              </b-row>
            </b-container>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SpriteBasic from "@/components/SpriteBasic.vue";

import { getPokemonListing } from "@/api";

export default {
  name: "PokemonList",
  components: {
    Navbar,
    SpriteBasic
  },
  data() {
    return {
      pokemon: null
    };
  },
  mounted() {
    getPokemonListing({ sort: "id", order: "ASC", page: 1 }).then(
      response => (this.pokemon = response.data)
    );
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px;
}

.row-card {
  margin-bottom: 15px;
}

.fade-container {
  padding-top: 0px;
  animation: FadeIn 1.5s 1 forwards;
}
@keyframes FadeIn {
  0% {
    opacity: 0;
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
</style>
