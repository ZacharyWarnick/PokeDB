<template>
  <div class = "evolution">
    <Navbar />
    <b-jumbotron header="Evolution Chain" lead="First Pokémon in evolution chain is displayed." />
    <section class="section-padding">
      <b-container class="justify-content-center">
        <b-row>
          <b-col
            cols="12"
            sm="6"
            md="4"
            lg="3"
            v-bind:key="basepokemon[$route.params.name].first.name.id"
          >
            <b-card style="margin-top: 10px;">
              <SpriteBasic
                v-bind:name="basepokemon[$route.params.name].first.name"
                v-bind:id="basepokemon[$route.params.name].first.name.id"
                v-bind:types="basepokemon[$route.params.name].first.name.types"
              />
              <router-link
                v-bind:to="'/pokemon/' + [$route.params.name]"
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
            second: {
              name: "arbok",
              id: 24,
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
            second:{
              name: "sandslash",
              id: 28,
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
            second: {
              name: "gyarados",
              id: 130,
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
