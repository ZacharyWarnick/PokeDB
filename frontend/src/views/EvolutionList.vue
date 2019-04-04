<template>
  <div class="evolution">
    <Navbar />
    <div class="fade-container">
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
          types: [this.$types["poison"]]
        },
        {
          name: "sandshrew",
          display_name: "Sandshrew",
          id: 27,
          types: [this.$types["ground"]]
        },
        {
          name: "magikarp",
          display_name: "Magikarp",
          id: 129,
          types: [this.$types["water"]]
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
.fade-container {
  padding-top: 0px;
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
