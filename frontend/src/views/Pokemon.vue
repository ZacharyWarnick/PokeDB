<template>
  <div class="pokemon">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg">
        <b-container>
          <b-row class="justify-content-between">
            <b-col cols="12" md="6">
              <div class="profile-wrapper wow">
                <div class="d-flex align-items-center">
                  <div>
                    <h2>
                      <strong>{{ pokemon.name }}</strong>
                      {{ pokemon.id }}
                    </h2>
                    <h2 v-if="pokemon.second_type != null">
                      {{ capitalize(pokemon.first_type.identifier) }}
                      {{ capitalize(pokemon.second_type.identifier) }}
                    </h2>
                    <h2 v-else>
                      {{ capitalize(pokemon.first_type.identifier) }}
                      {{ chainID.base_pokemon }}
                    </h2>
                  </div>
                </div>
                <p class="poke-desc">
                  {{ pokemon.flavor_text }}
                </p>
              </div>
            </b-col>
            <b-col cols="12" md="4">
              <img
                style="max-width: 100%; height: auto;"
                v-bind:src="pokemon.image"
              />
            </b-col>
          </b-row>
        </b-container>
        <hr />
        <b-row>
          <b-col md="6">
            <h2>Base Stats</h2>
            <ul class="stats-list">
              <li>Attack: {{ pokemon.base_stats.attack }}</li>
              <li>Defense: {{ pokemon.base_stats.defense }}</li>
              <li>HP: {{ pokemon.base_stats.hp }}</li>
              <li>Special Attack: {{ pokemon.base_stats.special_attack }}</li>
              <li>Special Defense: {{ pokemon.base_stats.special_defense }}</li>
              <li>Speed: {{ pokemon.base_stats.speed }}</li>
            </ul>
          </b-col>
          <b-col md="6">
            <h2>Identifying Features</h2>
            <ul class="stats-list">
              <li>Color: {{ capitalize(pokemon.color) }}</li>
              <li>Genus: {{ pokemon.genus }}</li>

              <li v-if="pokemon.has_alt_form == true">
                Alternate Form: Yes
              </li>
              <li v-else>
                Alternate Form: None
              </li>

              <li>Generation: {{ pokemon.since_gen }}</li>
            </ul>
          </b-col>
        </b-row>
        <hr />
        <h2 v-if="pokemon.evolution_chain_id != null" class="evo-header">
          {{ pokemon.name }} is a part of this chain:
        </h2>
        <EvolutionOverview
          v-if="pokemon.evolution_chain_id != null"
          :id="chainID"
          :page_name="pokemon.identifier"
        />
        <h2 v-else>This pokémon is not part of an evolution chain.</h2>
      </div>
    </b-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import EvolutionOverview from "@/components/EvolutionOverview.vue";
import { getPokemon } from "@/api";

export default {
  name: "Pokemon",
  components: {
    Navbar,
    EvolutionOverview
  },
  data() {
    return {
      pokemon: null,
      chainID: null
    };
  },
  mounted() {
    getPokemon(this.$route.params.name).then(
      response =>
        (this.pokemon = response.data) &&
        (this.chainID = response.data.evolution_chain_id)
    );
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
}

.type-badge {
  max-height: 32px;
  height: 100%;
  width: auto;
  padding: 0 4px;
}

.stats-list {
  list-style-type: disc;
  float: left;
  margin-left: 2px;
  padding-left: 50px;
  font-size: 19px;
  font-weight: lighter;
  text-align: justify;
  word-wrap: break-word;
}
.poke-desc {
  text-align: left;
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

.evo-header {
  padding: 20px 0px;
}
</style>
