<template>
  <div id="evolution">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg fade-container">
        <b-container class="section-padding">
          <b-jumbotron
            header="Evolution Chain"
            lead="The first Pokémon in an evolution chain defines the species."
          />
        </b-container>
        <section class="section-padding">
          <b-container class="justify-content-center">
            <b-row>
              <b-col
                cols="12"
                sm="6"
                md="4"
                lg="3"
                v-for="p in basepokemon[$route.params.name]"
                v-bind:key="p.id"
              >
                <b-card class="row-card shadow-sm">
                  <SpriteBasic
                    v-bind:name="p.display_name"
                    v-bind:id="p.id"
                    v-bind:types="p.types"
                  />
                  <router-link
                    v-bind:to="'/pokemon/' + p.name"
                    class="btn btn-outline-dark"
                    >{{ p.order }} Pokémon</router-link
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
            types: [this.$types["poison"]]
          },
          second: {
            name: "arbok",
            display_name: "Arbok",
            id: 24,
            order: "Second",
            types: [this.$types["poison"]]
          }
        },
        sandshrew: {
          first: {
            name: "sandshrew",
            display_name: "Sandshrew",
            id: 27,
            order: "First",
            types: [this.$types["ground"]]
          },
          second: {
            name: "sandslash",
            display_name: "Sandslash",
            id: 28,
            order: "Second",
            types: [this.$types["ground"]]
          }
        },
        magikarp: {
          first: {
            name: "magikarp",
            display_name: "Magikarp",
            id: 129,
            order: "First",
            types: [this.$types["water"]]
          },
          second: {
            name: "gyarados",
            display_name: "Gyarados",
            id: 130,
            order: "Second",
            types: [this.$types["water"], this.$types["flying"]]
          }
        }
      }
    };
  }
};
</script>
