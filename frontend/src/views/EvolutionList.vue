<template>
  <div>
    <Navbar />
    <b-jumbotron header="Evolutions" lead="First Pokémon in evolution chain is displayed." />
    <section class="section-padding">
      <b-container class="justify-content-center">
        <b-row>
          <b-col
            cols="12"
            sm="6"
            md="4"
            lg="3"
            v-for="p in pokemon"
            v-bind:key="p.id"
          >
            <b-card style="margin-top: 10px;">
              <SpriteBasic
                v-bind:name="p.display_name"
                v-bind:id="p.id"
                v-bind:types="p.types"
              />
              <router-link
                v-bind:to="'/evolutions/' + p.name"
                class="btn btn-outline-dark"
                >Evolution Chain</router-link
              >
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>
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
  data() {
    return {
      pokemon: [
        {
          name: "ekans",
          display_name:"Ekans",
          id: 23,
          sprite:
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
          types: [
            {
              name: "poison",
              badge_image: require("../assets/badge-poison.png")
            }
          ]
        },
        {
          name: "sandshrew",
          display_name: "Sandshrew",
          id: 27,
          sprite:
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png",
          types: [
            {
              name: "ground",
              badge_image: require("../assets/badge-ground.png")
            }
          ]
        },
        {
          name: "magikarp",
          display_name: "Magikarp",
          id: 129,
          sprite:
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png",
          types: [
            {
              name: "water",
              badge_image: require("../assets/badge-water.png")
            }
          ]
        },
      ]
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
}
</style>
