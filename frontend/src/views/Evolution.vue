<template>
  <div class="evolution">
    <Navbar />
    <div class="bg">
      <div class="container text-scroll-bg">
        <b-jumbotron
            :header="'Chain: ' + chain.base_pokemon.name"
            lead="The first Pokémon in an evolution chain defines the species."
        />
        <div class="overview-container">
          <h1>Here are all the pokemon in the chain</h1>
          <h3>Scroll down to find out indformation about individual steps</h3>
        </div>
      <hr>
        <div class="d-flex justify-content-center">
              <b-row class="align-items-center">
                <b-col >
                  <a :href="'/pokemon/' + chain.base_pokemon.id" style="text-decoration:none"> <SpriteBasic class="base"
                  
                    v-bind:name="chain.base_pokemon.name"
                    v-bind:id="chain.base_pokemon.id"
                    v-bind:types="chain.base_pokemon.first_type.identifier"
                  /> </a>           
                </b-col>

                <b-col v-for="stage in chain.stages" v-bind:key="stage">       
                  <a :href="'/pokemon/' + stage.pokemon.id" style="text-decoration:none"><SpriteBasic class="looped"
                  
                    v-bind:name="stage.pokemon.name"
                    v-bind:id="stage.pokemon.id"
                    v-bind:types="stage.pokemon.first_type.identifier"
                  /> </a>
                </b-col>
              </b-row>
          </div>
      <hr>
      <div class="indv-step-container">
        <h2>Individual Steps</h2>
        <div class="steps">
          <b-row v-for="stage in chain.stages" v-bind:key="stage">
            <b-col md="4">
              <a :href="'/pokemon/' + stage.pokemon.name" style="text-decoration:none"> 
              <SpriteBasic class="looped"
                v-bind:name="stage.evolves_from.name"
                v-bind:id="stage.evolves_from.id"
                v-bind:types="stage.evolves_from.first_type.identifier"
              /> 
              </a>           
            </b-col>
            <b-col sm="1">
              <img src="@/assets/arrow-png-icon-1.jpg" width="75px" class="arrow">
            </b-col>
            <b-col md="4">
              <a :href="'/pokemon/' + stage.pokemon.name" style="text-decoration:none"> 
              <SpriteBasic class="looped"
                v-bind:name="stage.pokemon.name"
                v-bind:id="stage.pokemon.id"
                v-bind:types="stage.pokemon.first_type.identifier"
              /> 
              </a>           
            </b-col>
            <b-col sm="3">
              <ul class="list-unstyled requirements-list">
                <li>Trigger: {{capitalize(stage.trigger)}}</li>
                <li v-if="stage.trigger_item != null">Trigger Item: {{capitalize(stage.trigger_item)}}</li>
                <li v-if="stage.time_of_day != null"> Time of Day: {{stage.time_of_day}} </li>
                <li v-if="stage.affection != null">Required Affection: {{stage.affection}} </li>
                <li v-if="stage.beauty != null">Required Beauty: {{stage.beauty}} </li>
                <li v-if="stage.happiness != null">Required Happiness: {{stage.happiness}} </li>
                <li>Difficulty: {{stage.difficulty}} </li>
              </ul>
            </b-col>
            <hr>
          </b-row>
        </div>
       </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SpriteBasic from "@/components/SpriteBasic.vue";
import { getPokemon }from "@/api";
import { getEvolution } from "@/api";

function getID() {

  var pathArray = window.location.pathname.split('/');

  var lastLocation = pathArray.slice(-1).pop()

  return String(lastLocation);
}

export default {
  name: "Evolution",
  components: {
    Navbar,
    SpriteBasic
  },
  methods: {
  capitalize(s) {
    if (typeof s !== "string") return "";
    return s.charAt(0).toUpperCase() + s.slice(1);
  }
  },
  data() {
    return {
      chain :null
    }
  },
  mounted() {
    getEvolution(getID()).then(
      response => (this.chain = response.data)
    )
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
}

.text-scroll-bg {
  background-color: white;
  width: 1920px;
  height: 1500px;

  padding-top: 30px;
  padding-bottom: 30px;
  align-content: center;
  box-shadow: 4px 4px 4px;
}
.bg {
  padding-top: 0;

  margin-bottom: 0px;

  /* The image used */
  background-image: url("../assets/home-background.jpg");

  /* Full height */
  height: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;

  align-content: center;

  position: sticky;
}
.arrow {
  width: 75px;
  transform: translateX(-25px) translateY(40px);
}

.overview-container{
  background-color: rgb(228, 228, 228);
  padding: 25px;
  margin-bottom: 50px;
}
.indv-step-container {
  padding: 20px 0px;
  align-content: center;
}

.steps{
  padding: 50px;
}

.requirements-list {
  padding: 20px 10px;
}
.base:hover {
  box-shadow: 1px 1px 3px 5px gray;
}
.looped:hover {
  box-shadow: 1px 1px 3px 5px gray;
}
</style>
