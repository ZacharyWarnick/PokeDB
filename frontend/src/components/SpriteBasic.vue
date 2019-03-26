<template>
  <div style="padding: 10px">
    <div class="d-flex justify-content-center">
      <div class="my-auto">
        <img
          v-bind:src="
            'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' +
              id +
              '.png'
          "
          alt="Pokemon Pic"
          class="poke-image img-fluid"
        />
      </div>
      <b-container class="my-auto">
        <span>{{ name }}</span>
        <b-row class="justify-content-center align-items-center">
          <div v-for="item in types" :key="item.badge_image">
            <router-link
              tag="img"
              v-bind:to="'/types/' + item.name"
              v-bind:src="item.badge_image"
              alt="Type Badge"
              class="img-fluid badge-image"
            />
          </div>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpriteBasic",
  props: {
    name: String,
    id: Number,
    types: Array
  }
};
</script>

<style scoped>
.poke-image {
  padding: 0;
  margin: 0;
  min-width: 96px;
  min-height: 96px;
}

.content-area {
  max-height: 96px;
  text-align: center;
  display: inline-block;
}

.badge-image {
  max-width: 44px;
  margin: 0 2px;
}
</style>