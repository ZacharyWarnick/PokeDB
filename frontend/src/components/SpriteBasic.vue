<template>
  <div style="padding: 10px">
    <div class="d-flex justify-content-center">
      <div class="my-auto">
        <router-link
          tag="img"
          v-bind:to="'/pokemon/' + name.toLowerCase()"
          v-bind:src="
            'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' +
              id +
              '.png'
          "
          class="poke-image img-fluid"
        />
      </div>
      <b-container class="my-auto">
        <span>{{ name }}</span>
        <b-row class="justify-content-center align-items-center">
          <div v-for="(item, idx) in getTypes()" :key="idx">
            <router-link
              tag="img"
              v-bind:to="'/types/' + item.name"
              v-bind:src="item.image"
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
  },
  methods: {
    getTypes: function() {
      var out = [];

      for (let t of this.types) {
        if (t != null) {
          const newItem = {
            name: t.identifier,
            image: require(`../assets/types/${t.identifier}.png`)
          };
          out.push(newItem);
        }
      }

      return out;
    }
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
  max-width: 22px;
  margin: 0 2px;
}
</style>
