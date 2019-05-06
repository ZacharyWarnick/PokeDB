<template>
  <b-row>
    <b-col cols="3">
      <b-dropdown class="mx-auto" ref="dropdown" :text="sorts[active_sort]">
        <b-dropdown-item
          v-for="(sort, key) in sorts"
          :key="key"
          @click="handleClick(key)"
          >{{ sorts[key] }}</b-dropdown-item
        >
      </b-dropdown>
    </b-col>
    <b-col cols="1">
      <b-dropdown :text="order">
        <b-dropdown-item
          v-for="(o, idx) in ['Ascending', 'Descending']"
          :key="idx"
          @click="reorder(idx)"
          >{{ o }}</b-dropdown-item
        >
      </b-dropdown>
    </b-col>
    <b-col>
      <b-pagination
        v-model="current_page"
        v-bind:total-rows="total_items"
        v-bind:per-page="per_page"
        @input="toPage(current_page, active_sort, order)"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
        align="center"
      />
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    total_items: Number,
    per_page: Number,
    toPage: Function,
    sorts: Object
  },
  data() {
    return {
      current_page: 1,
      active_sort: "id",
      order: "ASC"
    };
  },
  methods: {
    handleClick(key) {
      this.active_sort = key;
      this.toPage(this.current_page, this.active_sort, this.order);
    },
    reorder(idx) {
      const orders = ["ASC", "DESC"];
      this.order = orders[idx];
      this.toPage(this.current_page, this.active_sort, this.order);
    }
  }
};
</script>
