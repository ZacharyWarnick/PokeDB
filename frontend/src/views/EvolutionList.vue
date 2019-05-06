<template>
  <div class="evolution">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container fade-container">
        <div class="container text-scroll-bg">
          <b-jumbotron
            header="Evolutions"
            lead="First Pokémon in evolution chain is displayed."
          />
          <Pagination
            :current_page="current_page"
            :total_items="total_items"
            :per_page="per_page"
            :toPage="fetchData"
            :sorts="sorts"
          />
          <section class="section-padding">
            <b-container class="justify-content-center">
              <b-row>
                <b-col
                  cols="12"
                  sm="6"
                  md="4"
                  lg="3"
                  v-for="(chain, idx) in evolutions"
                  v-bind:key="idx"
                >
                  <b-card style="margin-top: 10px;">
                    <SpriteBasic
                      v-bind:name="chain.stages[0].evolves_from.name"
                      v-bind:id="chain.stages[0].evolves_from.id"
                      v-bind:types="[
                        chain.stages[0].evolves_from.first_type,
                        chain.stages[0].evolves_from.second_type
                      ]"
                    />
                    <SpriteBasic
                      v-for="stage in chain.stages"
                      :key="stage.pokemon.id"
                      v-bind:name="stage.pokemon.name"
                      v-bind:id="stage.pokemon.id"
                      v-bind:types="[
                        stage.pokemon.first_type,
                        stage.pokemon.second_type
                      ]"
                    />
                    <router-link
                      v-bind:to="'/evolutions/' + chain.base_pokemon.identifier"
                      class="btn btn-outline-dark"
                      >Evolution Chain</router-link
                    >
                  </b-card>
                </b-col>
              </b-row>
            </b-container>
          </section>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SpriteBasic from "@/components/SpriteBasic.vue";
import Pagination from "@/components/Pagination.vue";
import { getEvolutionListing } from "@/api";

export default {
  name: "EvolutionList",
  components: {
    Navbar,
    SpriteBasic,
    Pagination
  },
  methods: {
    updateListing(response) {
      this.current_page = response.current_page;
      this.total_items = response.total_items;
      this.per_page = response.per_page;
      this.evolutions = response.data;
      console.log(this.evolutions);
    },
    fetchData(current, sort, order) {
      console.log(sort);
      getEvolutionListing({ sort: sort, order: order, page: current }).then(
        response => this.updateListing(response.data)
      );
    }
  },
  data() {
    return {
      evolutions: null,
      current_page: 1,
      total_items: 1,
      per_page: 16,
      sorts: {
        chain: "Chain ID",
        diff: "Complexity",
        base: "Base Pokemon ID",
        count: "Evolution Count",
        level: "Max Level"
      }
    };
  },
  mounted() {
    this.fetchData(this.current_page, "chain", "asc");
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
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
</style>
