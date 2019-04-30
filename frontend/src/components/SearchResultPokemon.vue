<template>
  <div id="poke-search">
    <section class="section-padding" v-show="showPokemon">
      <h2>Pokémon</h2>
      <pre class="json" v-for="(poke, idx) in pokemon" :key="idx"></pre>
        <b-container>
            <b-row>
              <b-col
                cols="12"
                sm="6"
                md="4"
                lg="3"
                v-for="p in pokemon"
                v-bind:key="p"
              >
                <b-card class="row-card shadow-sm">
                  <SpriteBasic
                    v-bind:name="p.name"
                    v-bind:id="p.id"
                    v-bind:types="p.types"
                  />
                  <router-link
                    v-bind:to="'/pokemon/' + p.identifier"
                    class="btn btn-outline-dark"
                    >Info</router-link
                  >
                </b-card>
              </b-col>
            </b-row>
          </b-container>
    </section>
    <section v-show="showRelated">
      <h2>Related</h2>
      <pre class="json" v-for="(poke, idx) in related" :key="idx"></pre>
         <b-container>
            <b-row>
              <b-col
                cols="12"
                sm="6"
                md="4"
                lg="3"
                v-for="p in pokemon"
                v-bind:key="p"
              >
                <b-card class="row-card shadow-sm">
                  <SpriteBasic
                    v-bind:name="p.name"
                    v-bind:id="p.id"
                    v-bind:types="p.types"
                  />
                  <router-link
                    v-bind:to="'/pokemon/' + p.identifier"
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
import SpriteBasic from "@/components/SpriteBasic.vue";

export default {
  name: "SearchResultPokemon",
  components: {
    SpriteBasic
  },
  props: {
    pokemon: Array,
    related: Array
  },
  computed: {
    showPokemon: function() {
      return this.pokemon && this.pokemon.length > 0;
    },
    showRelated: function() {
      return this.related && this.related.length > 0;
    }
  }
};
</script>

<style scoped>
.json {
  text-align: left;
  word-wrap: normal;
  max-width: 100%;
  max-lines: 2;
  overflow-x: auto;
  white-space: pre-wrap;
  white-space: -moz-pre-wrap;
  white-space: -pre-wrap;
  white-space: -o-pre-wrap;
}
.row-card {
  margin: 15px 10px;
}
</style>
