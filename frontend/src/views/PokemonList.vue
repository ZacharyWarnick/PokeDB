<template>
  <div id="pokemon-list">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg fade-container">
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
                    v-bind:types="[p.first_type, p.second_Type]"
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
    </b-container>
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
.row-card {
  margin-bottom: 15px;
}
</style>
