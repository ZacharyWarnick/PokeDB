<template>
  <div class="overflow-auto">
    <!-- Use text in props -->
    <b-pagination
      v-model="currentPage"
      v-bind:total-rows="rows"
      v-bind:per-page="perPage"
      @input="toPage(currentPage)"
      first-text="First"
      prev-text="Prev"
      next-text="Next"
      last-text="Last"
      align="center"
    ></b-pagination>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name:"Pagination",
        rows: Number,
        perPage: Number,
        currentPage: Number,
        toPage: Function
      }
    }
  }
</script>