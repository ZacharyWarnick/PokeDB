<template>
  <div class="search-results">
    <Navbar />
    <img class="bg" src="../assets/home-background.jpg" />

    <b-container id="main-content">
      <div>
        <div
          v-if="this.pokemon.length > 0 || this.types.length > 0"
          class="text-scroll-bg fade-container"
        >
          <b-jumbotron class="search-header">
            <strong
              ><h1>
                Showing Results For:<br />
                "{{ this.$route.query.q }}"
              </h1></strong
            >
          </b-jumbotron>
          <div v-if="poke_first" class="pokemon-results">
            <SearchResultPokemon
              :v-show="pokemon.length > 0"
              :pokemon="pokemon"
              :related="related_pokemon"
            />

            <SearchResultTypes :types="types" />
            <hr />
          </div>
          <div v-else class="type-results">
            <strong><SearchResultTypes :types="types"/></strong>
            <SearchResultPokemon
              :v-show="pokemon.length > 0"
              :pokemon="pokemon"
              :related="related_pokemon"
            />
          </div>
        </div>
      </div>
      <div v-show="this.pokemon.length == 0 && this.types.length == 0">
        <div class="text-scroll-bg fade-container">
          <b-jumbotron class="search-header">
            <strong>
              <h1>We're sorry</h1>
              <br />
              <h2>We couldn't find anything matching that query</h2></strong
            >
          </b-jumbotron>
        </div>
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

<style scoped>
.search-header {
  padding: 25px;
}
.fade-container {
  margin: 2vh;
  padding-top: 2vh;
}

.pokemon-results {
  padding: 2vh;
}

.type-results {
  padding: 2vh;
}
</style>
