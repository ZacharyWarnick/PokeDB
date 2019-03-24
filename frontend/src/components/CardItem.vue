<template>
  <div class="col-sm-4">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ title }}</h5>
        <p class="card-text">{{ msg }}</p>
        <router-link tag="button" v-bind:to="link" class="btn btn-primary">{{ link_text }}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardItem",
  props: {
    title: String,
    msg: String,
    link: String,
    link_text: String
  }
};
</script>
