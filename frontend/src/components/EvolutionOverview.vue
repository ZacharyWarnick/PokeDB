<template>
  <div class="d-flex justify-content-center">
    <b-card class="text-left">
      <b-card-body title="Evolution Chain">
        <b-row class="align-items-center">
          <b-col>
            <SpriteBasic
              name="Bulbasaur"
              sprite="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
              v-bind:types="types1"
            />
          </b-col>

          <b-col>
            <SpriteBasic
              name="Ivysaur"
              sprite="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png"
              v-bind:types="types2"
            />
          </b-col>

          <!-- Unnecessary at this stage. -->
          <b-col v-if="false">
            <SpriteBasic
              id="sprite"
              name="Venusaur"
              sprite="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"
              v-bind:types="types3"
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
    species: String
  },
  data() {
    return {
      types1: [
        {
          name: "grass",
          badge_img:
            "https://nintendowire.com/wp-content/uploads/2016/07/Grass.png"
        }
      ],
      types2: [
        {
          name: "grass",
          badge_img:
            "https://nintendowire.com/wp-content/uploads/2016/07/Grass.png"
        }
      ],
      types3: [
        {
          name: "grass",
          badge_img:
            "https://nintendowire.com/wp-content/uploads/2016/07/Grass.png"
        },
        {
          name: "poison",
          badge_img:
            "https://nintendowire.com/wp-content/uploads/2016/07/Grass.png"
        }
      ]
    };
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

