<template>
  <div class="d-flex justify-content-center">
    <b-card class="text-left">
      <router-link
        :to="'/evolutions/' + this.id"
        tag="b-card-title"
        class="btn btn-outline-dark"
        >Evolution Chain</router-link
      >
      <b-card-body>
        <b-row class="align-items-center">

          <b-col >
            <SpriteBasic class="base"
              v-bind:name="chain.base_pokemon.name"
              v-bind:id="chain.base_pokemon.id"
              v-bind:types="chain.base_pokemon.first_type.identifier"
            />            
          </b-col>

          <b-col v-for="stage in chain.stages" v-bind:key="stage">       
            <SpriteBasic
              v-bind:name="stage.pokemon.name"
              v-bind:id="stage.pokemon.id"
              v-bind:types="stage.pokemon.first_type.identifier"
            /> 
          </b-col>
           

        </b-row>
      </b-card-body>
    </b-card>

  </div>
</template>


<script>
import SpriteBasic from "@/components/SpriteBasic.vue";
import { getEvolution } from "@/api";

export default {
  name: "EvolutionOverview",
  components: {
    SpriteBasic
  },
  data() {
    return {
    chain: null
    }
  },

  methods: {
    capitalize(s) {
      if (typeof s !== "string") return "";
      return s.charAt(0).toUpperCase() + s.slice(1);
    }
  },
  props: {
    id: String
  },

  mounted() {
    console.log(this.id);
    getEvolution(this.id).then(
      response => (this.chain = response.data)
    )
  }
}
</script>

<style scoped>
.icon-arrow-e::before {
  content: "\2192\FE0E";
}

.infocard-list-evo > .infocard-arrow {
  width: 165px;
}

.icon-arrow {
  display: block;
  font: normal 2.5rem/1 "Arial Unicode MS", "Trebuchet MS", "Arial", "Helvetica",
    sans-serif;
}

</style>