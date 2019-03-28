import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Pokemon from "./views/Pokemon.vue";
import PokemonList from "./views/PokemonList.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/types",
      name: "Types",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/TypeList.vue")
    },
    {
      path: "/types/:name",
      name: "Type",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Type.vue")
    },
    {
      path: "/about",
      name: "About",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/evolutions",
      name: "Evolutions",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/EvolutionList.vue")
    },
    {
      path: "/evolutions/:name",
      name: "Evolution",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Evolution.vue")
    },
    {
      path: "/pokemon",
      name: "Pokémon",
      component: PokemonList
    },
    {
      path: "/pokemon/:name",
      name: "Pokémon",
      component: Pokemon
    }
  ]
});
