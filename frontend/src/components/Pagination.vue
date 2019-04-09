<template>
  <div class="overflow-auto">
    <!-- Use text in props -->
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
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
        currentPage: Number
      }
    }
  }
</script>