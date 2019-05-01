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
          <section class="section-padding">
            <b-pagination
              v-model="evolutions.current_page"
              v-bind:total-rows="evolutions.total_items"
              v-bind:per-page="evolutions.per_page"
              @input="updateListing(evolutions.current_page)"
              first-text="First"
              prev-text="Prev"
              next-text="Next"
              last-text="Last"
              align="center"
            />
            <b-container class="justify-content-center">
              <b-row>
                <b-col
                  cols="12"
                  sm="6"
                  md="4"
                  lg="3"
                  v-for="chain in evolutions.data"
                  v-bind:key="chain.id"
                >
                  <b-card style="margin-top: 10px;">
                    <SpriteBasic
                      v-for:key="poke in chain.stages"
                      v-bind:name="poke.pokemon.name"
                      v-bind:id="poke.id"
                      v-bind:types="poke.pokemon.first_type"
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

export default {
  name: "EvolutionList",
  components: {
    Navbar,
    SpriteBasic
  },
  methods: {
  updateListing(current) {
    getEvolutionListing({ sort: "id", order: "ASC", page: current }).then(
      response => (this.evolutions = response.data)
    );
  }
  },
  data() {
    return {
      evolutions: null
    };
  },
  mounted() {
    this.updateListing(1)
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
