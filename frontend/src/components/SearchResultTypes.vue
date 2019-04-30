<template>
  <div id="type-search">
    <section class="section-padding" v-show="showTypes">
      <h2>Types</h2>
      <pre class="json" v-for="(t, idx) in types" :key="idx">
      <b-container>
        <div>
          <b-card
            :title="capitalize(t.identifier)"
            :img-src="'@/assets/badge-' + t.identifier + '.png'"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              {{t.desc_info}}
            </b-card-text>

            <b-button :href="'/types' + t.identifier" variant="primary">More Info</b-button>
          </b-card>
        </div>
      </b-container>
      </pre>
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
  },
  methods: {
    capitalize(s) {
      if (typeof s !== "string") return "";
      return s.charAt(0).toUpperCase() + s.slice(1);
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
