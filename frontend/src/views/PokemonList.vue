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
        	 <b-pagination
              v-model="pokemon.current_page"
              v-bind:total-rows="pokemon.total_items"
              v-bind:per-page="pokemon.per_page"
              @input="updateListing(pokemon.current_page)"
              first-text="First"
              prev-text="Prev"
              next-text="Next"
              last-text="Last"
              align="center"
            />
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
import Pagination from "@/components/Pagination.vue";

import { getPokemonListing } from "@/api";

export default {
  name: "PokemonList",
  components: {
    Navbar,
    SpriteBasic,
    Pagination
  },
  methods: {
    updateListing(current) {
      getPokemonListing({ sort: "id", order: "ASC", page: current }).then(
        response => (this.pokemon = response.data)
      );
    }
  },
  data() {
    return {
      pokemon: null
    };
  },
  mounted() {
    this.updateListing(1)
  }
};
</script>

<style scoped>
.row-card {
  margin-bottom: 15px;
}
</style>
