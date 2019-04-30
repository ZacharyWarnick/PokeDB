<template>
  <div class="search-results">
    <Navbar />
    <img class="bg" src="../assets/home-background.jpg" />
    <b-container id="main-content">
      <div v-if="poke_first" class="text-scroll-bg fade-container">
        <SearchResultPokemon
          :v-show="pokemon.length > 0"
          :pokemon="pokemon"
          :related="related_pokemon"
        />
        <SearchResultTypes :types="types" />
      </div>
      <div v-else class="text-scroll-bg fade-container">
        <SearchResultTypes :types="types" />
        <SearchResultPokemon
          :v-show="pokemon.length > 0"
          :pokemon="pokemon"
          :related="related_pokemon"
        />
      </div>
    </b-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SearchResultPokemon from "@/components/SearchResultPokemon.vue";
import SearchResultTypes from "@/components/SearchResultTypes.vue";
import { getSearchResults } from "@/api";

export default {
  name: "SearchResults",
  components: {
    Navbar,
    SearchResultPokemon,
    SearchResultTypes
  },
  data() {
    return {
      poke_first: true,
      pokemon: [],
      related_pokemon: [],
      types: []
    };
  },
  methods: {
    handleResponse: function(response) {
      const data = response.data;
      this.poke_first = data.pokemon.relavance >= data.types.relevance;
      this.pokemon = data.pokemon.data;
      this.related_pokemon = data.pokemon.related_pokemon;
      this.types = data.types.data;
    }
  },
  mounted() {
    if (this.$route.query.q) {
      getSearchResults(this.$route.query.q).then(this.handleResponse);
    }
  },
  watch: {
    "$route.query.q"() {
      getSearchResults(this.$route.query.q).then(this.handleResponse);
    }
  }
};
</script>
