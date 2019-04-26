<template>
  <div class="pokemon">
<<<<<<< HEAD
     <Navbar />
    <div class="bg">
      <div class="container text-scroll-bg">
      <section id="about" class="container section-padding">
      <b-row>
        <b-col  md="6">
          <div class="profile-wrapper wow">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h2>
                  <strong>{{ pokemon.name }}</strong>
                  {{pokemon.id}}
                </h2>
                <h2 v-if="pokemon.second_type != null">
                  {{capitalize(pokemon.first_type.identifier)}}
                  {{capitalize(pokemon.second_type.identifier)}}
                </h2>
                <h2 v-else>
                  {{capitalize(pokemon.first_type.identifier)}}
                  {{chainID.base_pokemon}}
                </h2>
              </div>
            </div>
            <p class="poke-desc">
              {{ pokemon.flavor_text }}
            </p>
        </b-col>
        <b-col md="6" >
          <img v-bind:src="pokemon.image" /> 
        </b-col>
        </b-row>
        <hr />
        <b-row>
          <b-col md="6">
            <h2>Base Stats</h2>
            <ul class="stats-list">
              <li>
                Attack: {{pokemon.base_stats.attack}}
              </li>
              <li>
                Defense: {{pokemon.base_stats.defense}}
              </li>
              <li>
                HP: {{pokemon.base_stats.hp}}
              </li>
              <li>
                Special Attack: {{pokemon.base_stats.special_attack}}
              </li>
              <li>
                Special Defense: {{pokemon.base_stats.special_defense}}
              </li>
              <li>
                Speed: {{pokemon.base_stats.speed}}
              </li>
            </ul>
          </b-col>
          <b-col md="6">
            <h2>Identifying Features</h2>
            <ul class="stats-list">
              <li>
                Color: {{capitalize(pokemon.color)}}
              </li>
              <li class="genus">
                Genus: {{pokemon.genus}}
              </li>

              <li v-if="pokemon.has_alt_form == true">
                Alternate Form: Yes
              </li>
              <li v-else>
                Alternate Form: None
              </li>

              <li>
                Generation: {{pokemon.since_gen}}
              </li>
            </ul>
          </b-col>
        </b-row>
        <hr>
        <h2 class="evo-header">{{pokemon.name}} is a part of this chain:</h2>
        <EvolutionOverview v-if="pokemon.evolution_chain_id != null"
          :id="chainID"
          :page_name="pokemon.name"
        />
      </section>
      </div>
    </div>
=======
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg fade-container">
        <section id="about" class="container section-padding">
          <b-row>
            <b-col lg="6" md="6" sm="12" cols="12">
              <div class="profile-wrapper wow">
                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <h2>
                      <strong>{{ all[$route.params.name].id }}</strong>
                      {{ all[$route.params.name].display_name }}
                    </h2>
                  </div>
                  <div>
                    <router-link
                      tag="img"
                      v-for="the_type in all[$route.params.name].types"
                      v-bind:to="'/types/' + the_type.name"
                      v-bind:key="the_type.id"
                      class="type-badge"
                      v-bind:src="the_type.badge_image"
                    />
                  </div>
                </div>
                <p class="poke-desc">
                  {{ all[$route.params.name].flavor_text }}
                </p>
                <hr />
                <div class="poke-info">
                  <ul>
                    <li>
                      <strong>Health</strong>
                      {{ all[$route.params.name].stats.hp }}
                    </li>
                    <li>
                      <strong>Attack</strong>
                      {{ all[$route.params.name].stats.atk }}
                    </li>
                    <li>
                      <strong>Defense</strong>
                      {{ all[$route.params.name].stats.def }}
                    </li>
                    <li>
                      <strong>Sp. Atk</strong>
                      {{ all[$route.params.name].stats.sp_atk }}
                    </li>
                    <li>
                      <strong>Sp. Def</strong>
                      {{ all[$route.params.name].stats.sp_def }}
                    </li>
                    <li>
                      <strong>Speed</strong>
                      {{ all[$route.params.name].stats.spd }}
                    </li>
                  </ul>
                </div>
              </div>
            </b-col>

            <b-col lg="6" md="6" sm="12" cols="12" class="my-auto">
              <div class="img-thumb wow">
                <img
                  v-bind:src="all[$route.params.name].sprite"
                  class="img-fluid poke-img"
                />
              </div>
            </b-col>
          </b-row>
        </section>

        <section id="evolution" class="container section-padding">
          <EvolutionOverview
            v-bind:name="all[$route.params.name].ev.name"
            v-bind:first="all[$route.params.name].ev.first"
            v-bind:second="all[$route.params.name].ev.second"
          />
        </section>
      </div>
    </b-container>
>>>>>>> develop
  </div>
    
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import EvolutionOverview from "@/components/EvolutionOverview.vue";
import { getPokemon }from "@/api";
import { getEvolution } from "@/api";

//Take last element of the url path and request it from the api
function getID() {

  var pathArray = window.location.pathname.split('/');

  var lastLocation = pathArray.slice(-1).pop()

  return String(lastLocation);
}

export default {
  name: "Pokemon",
  components: {
    Navbar,
    EvolutionOverview
  },
    data () {
    return {
      pokemon: null,
      chainID: null
    }
  },

  methods: {
    capitalize(s) {
      if (typeof s !== "string") return "";
      return s.charAt(0).toUpperCase() + s.slice(1);
    }
  },
  mounted() {
    getPokemon(getID()).then(
      response => (this.pokemon = response.data) && 
      (this.chainID = response.data.evolution_chain_id)
    )
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
}

.profile-wrapper {
  padding: 45px 0;
  text-align: left;
}

.genus {
  text-decoration: line-through;
}
.type-badge {
  max-height: 32px;
  height: 100%;
  width: auto;
  padding: 0 4px;
}

.stats-list {
  list-style-type: disc;
  float:left;
  margin-left: 2px;
  padding-left: 50px;
  font-size: 19px;
  font-weight: lighter;
  text-align: justify;
  word-wrap:break-word;
}
.poke-desc {
  padding: 20px 0;
}

.poke-info {
  padding: 10px 0;
}

.poke-img {
  max-height: 400px;
}

.poke-img-box:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
<<<<<<< HEAD

.evo-header {
  padding: 20px 0px;
}
.text-scroll-bg {
  background-color: white;
  width: 1920px;
  height: 1500px;

  padding-top: 30px;
  padding-bottom: 30px;
  align-content: center;
  box-shadow: 4px 4px 4px;

  animation: textUP 1.5s 1 forwards;
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
=======
>>>>>>> develop
</style>
