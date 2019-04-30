<template>
  <div id="poke-search">
    <section class="section-padding" v-show="showPokemon">
      <h2>Pokémon</h2>
      <pre class="json" v-for="(poke, idx) in pokemon" :key="idx">{{
        poke
      }}</pre>
    </section>
    <section v-show="showRelated">
      <h2>Related</h2>
      <pre class="json" v-for="(poke, idx) in related" :key="idx">{{
        poke
      }}</pre>
    </section>
  </div>
</template>

<script>
export default {
  name: "SearchResultPokemon",
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
</style>
