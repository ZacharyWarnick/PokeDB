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
          <Pagination
            :current_page="current_page"
            :total_items="total_items"
            :per_page="per_page"
            :toPage="fetchData"
            :sorts="sorts"
          />
          <b-container>
            <b-row>
              <b-col
                cols="12"
                sm="6"
                md="4"
                lg="3"
                v-for="p in pokemon"
                v-bind:key="p.id"
              >
                <b-card class="row-card shadow-sm">
                  <SpriteBasic
                    v-bind:name="p.name"
                    v-bind:id="p.id"
                    v-bind:types="[p.first_type, p.second_type]"
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
    updateListing(response) {
      this.current_page = response.data.current_page;
      this.total_items = response.data.total_items;
      this.per_page = response.data.per_page;
      this.pokemon = response.data.data;
    },
    fetchData(current, sort, order) {
      getPokemonListing({ sort: sort, order: order, page: current }).then(
        response => this.updateListing(response)
      );
    }
  },
  data() {
    return {
      current_page: 1,
      total_items: 1,
      per_page: 16,
      pokemon: null,
      sorts: {
        id: "ID",
        name: "Name",
        gen: "Generation",
        color: "Color",
        type: "Primary Type"
      }
    };
  },
  mounted() {
    this.fetchData(this.current_page, "id", "asc");
  }
};
</script>

<style scoped>
.row-card {
  margin-bottom: 15px;
}
</style>
