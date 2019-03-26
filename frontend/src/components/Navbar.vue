<template>
  <b-navbar toggleable="lg" class="navbar-expand-lg navbar-light bg-light">
    <router-link to="/" class="navbar-brand">PokéDB</router-link>
    <b-navbar-toggle target="nav_collapse" />

    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <router-link to="/" tag="b-nav-item">
          Home
          <span class="sr-only">(current)</span>
        </router-link>
        <router-link to="/types" tag="b-nav-item">Types</router-link>
        <router-link to="/" tag="b-nav-item">Evolution</router-link>
        <router-link to="/" tag="b-nav-item">Pokémon</router-link>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input class="mr-sm-2" type="text" placeholder="Search" />
          <b-button variant="outline-success" class="my-2 my-sm-0" type="submit"
            >Search</b-button
          >
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
