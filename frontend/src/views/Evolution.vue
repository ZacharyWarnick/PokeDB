<template>
  <div id="evolution">
    <Navbar />
    <div class="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg">
        <b-jumbotron
          :header="chain.base_pokemon.name"
          lead="Scroll down to find out indformation about individual steps"
        />
        <hr />
        <div class="d-flex justify-content-center">
          <b-row class="align-items-center">
            <b-col>
              <router-link
                :to="'/pokemon/' + chain.base_pokemon.id"
                style="text-decoration:none"
              >
                <SpriteBasic
                  class="base"
                  v-bind:name="chain.base_pokemon.name"
                  v-bind:id="chain.base_pokemon.id"
                  v-bind:types="chain.base_pokemon.first_type.identifier"
                />
              </router-link>
            </b-col>

            <b-col v-for="stage in chain.stages" v-bind:key="stage">
              <router-link
                :to="'/pokemon/' + stage.pokemon.id"
                style="text-decoration:none"
                ><SpriteBasic
                  class="looped"
                  v-bind:name="stage.pokemon.name"
                  v-bind:id="stage.pokemon.id"
                  v-bind:types="stage.pokemon.first_type.identifier"
                />
              </router-link>
            </b-col>
          </b-row>
        </div>

        <hr />
        <div class="indv-step-container">
          <h2>Individual Steps</h2>
          <div class="steps">
            <b-row v-for="stage in chain.stages" v-bind:key="stage">
              <b-col md="4">
                <router-link
                  :to="'/pokemon/' + stage.pokemon.name"
                  style="text-decoration:none"
                >
                  <SpriteBasic
                    class="looped"
                    v-bind:name="stage.evolves_from.name"
                    v-bind:id="stage.evolves_from.id"
                    v-bind:types="stage.evolves_from.first_type.identifier"
                  />
                </router-link>
              </b-col>
              <b-col sm="1">
                <img
                  src="@/assets/arrow-png-icon-1.jpg"
                  width="75px"
                  class="arrow"
                />
              </b-col>
              <b-col md="4">
                <router-link
                  :to="'/pokemon/' + stage.pokemon.identifier"
                  style="text-decoration:none"
                >
                  <SpriteBasic
                    class="looped"
                    v-bind:name="stage.pokemon.name"
                    v-bind:id="stage.pokemon.id"
                    v-bind:types="stage.pokemon.first_type.identifier"
                  />
                </router-link>
              </b-col>
              <b-col sm="3" class="test-left">
                <ul class="list-unstyled requirements-list text-left">
                  <li>
                    <strong>Trigger:</strong> {{ capitalize(stage.trigger) }}
                  </li>
                  <li v-if="stage.trigger_item != null">
                    <strong>Trigger Item:</strong>
                    {{ capitalize(stage.trigger_item) }}
                  </li>
                  <li v-if="stage.time_of_day != null">
                    <strong>Time of Day:</strong> {{ stage.time_of_day }}
                  </li>
                  <li v-if="stage.affection != null">
                    <strong>Required Affection:</strong> {{ stage.affection }}
                  </li>
                  <li v-if="stage.beauty != null">
                    <strong>Required Beauty:</strong> {{ stage.beauty }}
                  </li>
                  <li v-if="stage.happiness != null">
                    <strong>Required Happiness:</strong> {{ stage.happiness }}
                  </li>
                  <li v-if="stage.location != null">
                    <strong>Location:</strong> {{ stage.location }}
                  </li>
                  <li><strong>Difficulty:</strong> {{ stage.difficulty }}</li>
                </ul>
              </b-col>
              <hr />
            </b-row>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SpriteBasic from "@/components/SpriteBasic.vue";
import { getEvolution } from "@/api";

function getID() {
  var pathArray = window.location.pathname.split("/");

  var lastLocation = pathArray.slice(-1).pop();

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
      chain: null
    };
  },
  mounted() {
    getEvolution(getID()).then(response => (this.chain = response.data));
  }
};
</script>

<style scoped>
.arrow {
  width: 75px;
  transform: translateX(-25px) translateY(40px);
}

.overview-container {
  background-color: rgb(228, 228, 228);
  padding: 25px;
  margin-bottom: 50px;
}

.indv-step-container {
  padding: 20px 0px;
  align-content: center;
}

.steps {
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
