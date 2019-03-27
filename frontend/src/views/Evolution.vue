<template>
  <div class = "evolution">
    <Navbar />
    <b-jumbotron header="Evolution Chain" lead="First Pokémon in evolution chain is displayed." />
    <section class="section-padding">
      <b-container class="justify-content-center">
        <b-row>
          <b-col
            v-for="p in basepokemon[$route.params.name]"
            v-bind:key="p.name.id"
          >
            <b-card class="row-card shadow-sm">
              <SpriteBasic
                v-bind:name="p.display_name"
                v-bind:id="p.name.id"
                v-bind:types="p.types"
              />
              <router-link
                v-bind:to="'/pokemon/' + [$route.params.name]"
                class="btn btn-outline-dark"
                >{{p.order}} Pokémon</router-link
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
  name: "Evolution",
  components: {
    Navbar,
    SpriteBasic
  },
  data() {
    return {
      basepokemon: {
        ekans: {
            first: {
              name: "ekans",
              display_name: "Ekans",
              id: 23,
              order: "First",
              sprite:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
              types: [
                {
                  name: "poison",
                  badge_image: require("../assets/badge-poison.png")
                }
              ]
            },
            second: {
              name: "arbok",
              display_name: "Arbok",
              id: 24,
              order: "Second",
              sprite:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png",
              types: [
                {
                  name: "poison",
                  badge_image: require("../assets/badge-poison.png")
                }
              ]
            }

        },
        sandshrew: {
            first:{
              name: "sandshrew",
              display_name: "Sandshrew",
              id: 27,
              order: "First",
              sprite:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png",
              types: [
                {
                  name: "ground",
                  badge_image: require("../assets/badge-ground.png")
                }
              ]
            },
            second:{
              name: "sandslash",
              display_name: "Sandslash",
              id: 28,
              order: "Second",
              sprite:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png",
              types: [
                {
                  name: "ground",
                  badge_image: require("../assets/badge-ground.png")
                }
              ]
            }

        },
        magikarp: {
            first: {
              name: "magikarp",
              display_name: "Magikarp",
              id: 129,
              order: "First",
              sprite:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png",
              types: [
                {
                  name: "water",
                  badge_image: require("../assets/badge-water.png")
                }
              ]
            },
            second: {
              name: "gyarados",
              display_name: "Gyarados",
              id: 130,
              order: "Second",
              sprite:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png",
              types: [
                {
                  name: "water",
                  badge_image: require("../assets/badge-water.png")
                },
                {
                  name: "flying",
                  badge_image: require("../assets/badge-flying.png")
                }
              ]
            }
        }
      }
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
}
</style>
