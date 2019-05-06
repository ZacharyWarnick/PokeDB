<template>
  <div class="Type">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg">
        <section class="section-padding">
          <b-container>
            <b-row>
              <b-col md="6" class="my-auto">
                <h2 class="align-left">
                  <strong>{{ capitalize(type.identifier) }}</strong>
                </h2>
                <p class="lead text-justify">{{ type.desc_info }}</p>
              </b-col>
              <b-col md="6" class="type-img-col">
                <img  :src="require('../assets/types/' + (type.identifier + '.png'))" class="type-img"/>
              </b-col>
            </b-row>
            <hr />
            <b-row>
              <b-col md="6">
                <b-container>
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col">Versus Type</th>
                        <th scope="col">Modifier</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        class="bug"
                        :class="{
                          weak: type.vs_bug < 1,
                          strong: type.vs_bug > 1
                        }"
                      >
                        <td>
                          Bug
                        </td>
                        <td>
                          {{ type.vs_bug }}
                        </td>
                      </tr>
                      <tr
                        class="dark"
                        :class="{
                          weak: type.vs_dark < 1,
                          strong: type.vs_dark > 1
                        }"
                      >
                        <td>
                          Dark
                        </td>
                        <td>
                          {{ type.vs_dark }}
                        </td>
                      </tr>

                      <tr
                        class="dragon"
                        :class="{
                          weak: type.vs_dragon < 1,
                          strong: type.vs_dragon > 1
                        }"
                      >
                        <td>
                          Dragon
                        </td>
                        <td>
                          {{ type.vs_dragon }}
                        </td>
                      </tr>

                      <tr
                        class="electric"
                        :class="{
                          weak: type.vs_electric < 1,
                          strong: type.vs_electric > 1
                        }"
                      >
                        <td>
                          Electric
                        </td>
                        <td>
                          {{ type.vs_electric }}
                        </td>
                      </tr>

                      <tr
                        class="fairy"
                        :class="{
                          weak: type.vs_fairy < 1,
                          strong: type.vs_fairy > 1
                        }"
                      >
                        <td>
                          Fairy
                        </td>
                        <td>
                          {{ type.vs_fairy }}
                        </td>
                      </tr>

                      <tr
                        class="fighting"
                        :class="{
                          weak: type.vs_fighting < 1,
                          strong: type.vs_fighting > 1
                        }"
                      >
                        <td>
                          Fighting
                        </td>
                        <td>
                          {{ type.vs_fighting }}
                        </td>
                      </tr>
                      <tr
                        class="fire"
                        :class="{
                          weak: type.vs_fire < 1,
                          strong: type.vs_fire > 1
                        }"
                      >
                        <td>
                          Fire
                        </td>
                        <td>
                          {{ type.vs_fire }}
                        </td>
                      </tr>
                      <tr
                        class="flying"
                        :class="{
                          weak: type.vs_flying < 1,
                          strong: type.vs_flying > 1
                        }"
                      >
                        <td>
                          Flying
                        </td>
                        <td>
                          {{ type.vs_flying }}
                        </td>
                      </tr>

                      <tr
                        class="ghost"
                        :class="{
                          weak: type.vs_ghost < 1,
                          strong: type.vs_ghost > 1
                        }"
                      >
                        <td>
                          Ghost
                        </td>
                        <td>
                          {{ type.vs_ghost }}
                        </td>
                      </tr>
                      <tr
                        class="grass"
                        :class="{
                          weak: type.vs_grass < 1,
                          strong: type.vs_grass > 1
                        }"
                      >
                        <td>
                          Grass
                        </td>
                        <td>
                          {{ type.vs_grass }}
                        </td>
                      </tr>
                      <tr
                        class="ground"
                        :class="{
                          weak: type.vs_ground < 1,
                          strong: type.vs_ground > 1
                        }"
                      >
                        <td>
                          Ground
                        </td>
                        <td>
                          {{ type.vs_ground }}
                        </td>
                      </tr>
                      <tr
                        class="ice"
                        :class="{
                          weak: type.vs_ice < 1,
                          strong: type.vs_ice > 1
                        }"
                      >
                        <td>
                          Ice
                        </td>
                        <td>
                          {{ type.vs_ice }}
                        </td>
                      </tr>
                      <tr
                        class="normal"
                        :class="{
                          weak: type.vs_normal < 1,
                          strong: type.vs_normal > 1
                        }"
                      >
                        <td>
                          Normal
                        </td>
                        <td>
                          {{ type.vs_normal }}
                        </td>
                      </tr>
                      <tr
                        class="poison"
                        :class="{
                          weak: type.vs_poison < 1,
                          strong: type.vs_poison > 1
                        }"
                      >
                        <td>
                          Poison
                        </td>
                        <td>
                          {{ type.vs_poison }}
                        </td>
                      </tr>

                      <tr
                        class="psychic"
                        :class="{
                          weak: type.vs_psychic < 1,
                          strong: type.vs_psychic > 1
                        }"
                      >
                        <td>
                          Psychic
                        </td>
                        <td>
                          {{ type.vs_psychic }}
                        </td>
                      </tr>
                      <tr
                        class="rock"
                        :class="{
                          weak: type.vs_rock < 1,
                          strong: type.vs_rock > 1
                        }"
                      >
                        <td>
                          Rock
                        </td>
                        <td>
                          {{ type.vs_rock }}
                        </td>
                      </tr>
                      <tr
                        class="steel"
                        :class="{
                          weak: type.vs_steel < 1,
                          strong: type.vs_steel > 1
                        }"
                      >
                        <td>
                          Steel
                        </td>
                        <td>
                          {{ type.vs_steel }}
                        </td>
                      </tr>
                      <tr
                        class="water"
                        :class="{
                          weak: type.vs_water < 1,
                          strong: type.vs_water > 1
                        }"
                      >
                        <td>
                          Water
                        </td>
                        <td>
                          {{ type.vs_water }}
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </b-container>
              </b-col>
              <b-col md="6">
                <h2>Info</h2>
                <ul class="list-unstyled info">
                  <li>
                    <b>Damgage Class:</b> {{ capitalize(type.damage_class) }}
                  </li>
                  <li><b>Number of Pokémon:</b> {{ type.pokemon_count }}</li>
                  <li><b>Stat Average:</b> {{ type.stat_average }}</li>
                  <li>
                    <b>Relative Advantage:</b> {{ type.relative_advantage }}
                  </li>
                </ul>
                <h2>Offense</h2>
                <p class="text-justify attack">
                  {{ type.desc_atk }}
                </p>

                <h2>Defense</h2>
                <p class="text-justify defense">{{ type.desc_def }}</p>
              </b-col>
            </b-row>
          </b-container>
        </section>
        <hr />
        <section class="section-padding">
          <h2>Pokémon of This Type</h2>
          <h3>
            There are {{ type.pokemon_count }} {{ type.identifier }} pokémon
          </h3>
        </section>
      </div>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

import { getType } from "@/api";

export default {
  name: "Type",
  components: {
    Navbar
  },
  data() {
    return {
      type: null
    };
  },
  methods: {
    capitalize(s) {
      if (typeof s !== "string") return "";
      return s.charAt(0).toUpperCase() + s.slice(1);
    },
  },
  mounted() {
    getType(this.$route.params.name).then(
      response => (this.type = response.data)
    );
  },

  computed: {
    image() {
      return require('../assets/types/' + this.type.identifier + '.png')
    } 
  }
};
</script>

<style scoped>
.jumbotron {
  padding: 30px 0px;
}

.info {
  text-align: left;
  align-content: center;
  padding-left: 120px;
  padding-bottom: 50px;
}

.attack {
  padding-bottom: 50px;
}

.strong {
  background-color: rgb(15, 177, 0);
}
.weak {
  background-color: rgb(173, 12, 0);
}
.type-img-col{
  vertical-align: middle;
}
.type-img {
  align-self: center;
  margin: 1vh;
  padding-top: 3vh;
}
</style>
