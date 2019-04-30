<template>
  <div id="type-search">
    <section class="section-padding" v-show="showTypes">
      <h2>Types</h2>
      <pre class="json" v-for="(t, idx) in types" :key="idx">{{ t }}</pre>
    </section>
  </div>
</template>

<script>
export default {
  props: {
    types: Array
  },
  computed: {
    showTypes: function() {
      return this.types && this.types.length > 0;
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
