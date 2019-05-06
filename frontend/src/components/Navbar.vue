<template>
  <b-navbar
    toggleable="lg"
    class="navbar-expand-lg navbar-dark navbar-default"
    variant="dark"
    fixed="top"
    id="navbar"
  >
    <router-link to="/" class="navbar-brand">PokéDB</router-link>
    <b-navbar-toggle target="nav_collapse" />

    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <router-link to="/pokemon" tag="b-nav-item">Pokémon</router-link>
        <router-link to="/evolutions" tag="b-nav-item">Evolutions</router-link>
        <router-link to="/types" tag="b-nav-item">Types</router-link>
        <router-link to="/about" tag="b-nav-item">About</router-link>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form @submit.stop.prevent>
            <b-form-input
              v-model="text"
              trim
              class="mr-sm-2"
              type="text"
              placeholder="Search"
              @keydown.enter="runSearch"
            />
          </b-form>
          <b-button
            variant="outline-success"
            class="my-2 my-sm-0"
            type="submit"
            @click="runSearch"
            >Search</b-button
          >
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  data() {
    return {
      text: ""
    };
  },
  methods: {
    runSearch: function() {
      this.$router.push({ name: "Search", query: { q: this.text } });
      console.log(this.$router);
    },
    validateInput: function() {
      return this.text.length > 0;
    }
  }
};
</script>
