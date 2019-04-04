<template>
  <div class="fade-container">
    <Navbar />
    <b-container class="section-padding">
      <b-jumbotron header="Pokémon" lead="Gotta Catch 'Em All" />
    </b-container>
    <section>
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
                v-bind:types="p.types"
              />
              <router-link
                v-bind:to="'/pokemon/' + p.name"
                class="btn btn-outline-dark"
                >Info</router-link
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
  name: "PokemonList",
  components: {
    Navbar,
    SpriteBasic
  },
  data() {
    return {
      pokemon: [
        {
          name: "ekans",
          id: 23,
          types: [this.$types["poison"]]
        },
        {
          name: "arbok",
          id: 24,
          types: [this.$types["poison"]]
        },
        {
          name: "sandshrew",
          id: 27,
          types: [this.$types["ground"]]
        },
        {
          name: "sandslash",
          id: 28,
          types: [this.$types["ground"]]
        },
        {
          name: "magikarp",
          id: 129,
          types: [this.$types["water"]]
        },
        {
          name: "gyarados",
          id: 130,
          types: [this.$types["water"], this.$types["flying"]]
        }
      ]
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px;
}

.row-card {
  margin-bottom: 15px;
}
.fade-container {
    animation: FadeIn 1.5s 1 forwards;
}
@keyframes FadeIn {
  0%{
    opacity: 0
  }
  
  100% {
    opacity: 1;
  }
}
</style>
