import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;

Vue.use(BootstrapVue);

Vue.prototype.$types = {
  poison: {
    name: "poison",
    badge_image: require("./assets/badge-poison.png")
  },
  ground: {
    name: "ground",
    badge_image: require("./assets/badge-ground.png")
  },
  water: {
    name: "water",
    badge_image: require("./assets/badge-water.png")
  },
  flying: {
    name: "flying",
    badge_image: require("./assets/badge-flying.png")
  }
};

new Vue({
  el: "#app",
  router,
  render: h => h(App)
});
