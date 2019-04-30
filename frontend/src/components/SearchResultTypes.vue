<template>
  <div id="type-search">
    <section class="section-padding" v-show="showTypes">
      <h1>Types</h1>
      <b-container class="content font-correct">
          <b-row >
            <b-col class="lg-6" v-for="(t, idx) in types" :key="idx">
              <div class="type-desc">
                <b-card :title="capitalize(t.identifier)">
                  <b-card-text>
                    {{t.desc_info}}
                  </b-card-text>

                  <router-link
                    v-bind:to="'/types/' + t.identifier"
                    class="btn btn-outline-dark"
                    >Info</router-link
                  >
                </b-card>
              <div>
            </b-col>
          </b-row>
      </b-container>
    </section>
    <hr/>
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

.content {
  padding: 1vh;
  margin: 1vh;
}

.font-correct {
  font-family: "Montserrat", sans-serif;
}

.type-desc title {
  padding: 1vh;
  justify-content: center
}

.description {
  justify-content: center;
  margin: 1vh;
  padding: 1vh; 
}
</style>
