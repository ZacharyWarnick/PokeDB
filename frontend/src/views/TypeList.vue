<template>
  <div id="type-list">
    <Navbar />
    <b-container id="main-content">
      <img class="bg" src="../assets/home-background.jpg" />
      <div class="container text-scroll-bg fade-container">
        <b-container class="section-padding">
          <b-jumbotron class="text-center" header="Types">
            <p class="lead text-muted">
              There are 18 types across all Pokémon games.
            </p>
          </b-jumbotron>
        </b-container>

        <section class="album">
          <Pagination
            :current_page="current_page"
            :total_items="total_items"
            :per_page="per_page"
            :toPage="fetchData"
            :sorts="sorts"
          />
          <div class="container">
            <div class="row">
              <div class="col-md-4" v-for="(t, idx) in types" :key="idx">
                <div class="card mb-4 shadow-sm">
                  <img
                    class="align-self-center"
                    style="max-width: 64px; padding-top: 15px;"
                    :src="require(`../assets/types/${t.identifier}.png`)"
                  />
                  <div class="card-body">
                    <div
                      class="d-flex justify-content-between align-items-center"
                    >
                      <router-link
                        tag="button"
                        class="btn btn-lg btn-block btn-outline-secondary"
                        :to="'/types/' + t.identifier"
                        >{{ capitalize(t.identifier) }}</router-link
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import Pagination from "@/components/Pagination.vue";
import { getTypeListing } from "@/api";

export default {
  name: "Types",
  components: {
    Navbar,
    Pagination
  },
  methods: {
    updateListing(response) {
      this.current_page = response.current_page;
      this.total_items = response.total_items;
      this.per_page = response.per_page;
      this.types = response.data;
    },
    fetchData(current, sort, order) {
      console.log(sort);
      getTypeListing({ sort: sort, order: order, page: current }).then(
        response => this.updateListing(response.data)
      );
    }
  },
  data() {
    return {
      types: null,
      current_page: 1,
      total_items: 1,
      per_page: 16,
      sorts: {
        id: "Type ID",
        name: "Name",
        count: "Pokemon having Type",
        stats: "Average Stats",
        adv: "Relative Advantage"
      }
    };
  },
  mounted() {
    this.fetchData(this.current_page, "chain", "asc");
  }
};
</script>
