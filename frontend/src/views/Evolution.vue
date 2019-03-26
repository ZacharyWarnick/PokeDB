<template>
  <div class="Evolutions" style="padding-left">
    <Navbar />
    <div class="jumbotron">
      <h1>{{ $route.params.name }}</h1>
    </div>
        <div class="album py-5 bg-light">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
              <div class="card-body">
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. 
                Put information on the evolution chain.</p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <a href="/evolutions/magikarp"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <p><font size="24">&rarr;</font></p>
          <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
              <div class="card-body">
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. Put information on the evolution chain.</p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <a href="/evolutions/sandshrew"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
  </div>
  </div>
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import CardItem from "@/components/CardItem.vue";
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    CardItem
  }
};
</script>

<style scoped>
  .container {
    margin-top: 10px;
  }

  .jumbotron {
    text-align: center;
  }

</style>



