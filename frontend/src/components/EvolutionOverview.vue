<template>
  <div class="d-flex justify-content-center">
    <b-card class="text-left">
      <router-link
        :to="'/evolutions/' + first.name.toLowerCase()"
        tag="b-card-title"
        class="btn btn-outline-dark"
        >Evolution Chain</router-link
      >
      <b-card-body>
        <b-row class="align-items-center">
          <b-col>
            <SpriteBasic
              v-bind:name="first.name"
              v-bind:id="first.id"
              v-bind:types="first.types"
            />
          </b-col>

          <b-col>
            <SpriteBasic
              v-bind:name="second.name"
              v-bind:id="second.id"
              v-bind:types="second.types"
            />
          </b-col>
        </b-row>
      </b-card-body>
    </b-card>
  </div>
</template>


<script>
import SpriteBasic from "@/components/SpriteBasic.vue";

export default {
  name: "EvolutionOverview",
  components: {
    SpriteBasic
  },
  props: {
    species: String,
    first: Object,
    second: Object
  }
};
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