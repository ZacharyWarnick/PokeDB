<template>
  <div>
    <Navbar />
    <section class="section-padding">
      <b-container class="justify-content-center">
        <b-row>
          <b-col cols="12" sm="6" md="4" lg="3" v-for="p in sample_pokemon" v-bind:key="p.id">
            <b-card style="margin-top: 10px;">
              <SpriteBasic
                v-bind:name="p.name"
                v-bind:sprite="p.sprite"
                v-bind:types="p.types"
              />
              <router-link v-bind:to="'/pokemon/' + p.name" class="btn btn-outline-dark">Info</router-link>
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
  name: "PokemonList",
  components: {
    Navbar,
    SpriteBasic
  },
  data() {
    return {
      sample_pokemon: [
        {
          name: "ekans",
          id: 23,
          sprite:
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
          types: [
            {
              name: "poison",
              badge_img: require("../assets/badge-poison.png")
            }
          ]
        },
        {
          name: "arbok",
          id: 24,
          sprite:
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png",
          types: [
            {
              name: "poison",
              badge_img:require("../assets/badge-poison.png")
            }
          ]
        }
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
