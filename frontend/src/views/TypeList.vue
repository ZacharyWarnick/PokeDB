<template>
  <div class="Types">
    <Navbar/>
    <section class="jumbotron text-center">
    <div class="container">
      <h1 class="jumbotron-heading">All Types</h1>
      <p class="lead text-muted">There are 18 common types across all pokémon games.<br/> Click on a card to find out more.</p>
    </div>
    </section>

    <div class="album py-5 bg-light">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <!--<svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>-->
              <img class="card-img-top" src="https://i.pinimg.com/originals/b0/bc/69/b0bc69eacf147a54ec4e5c4cacdf81db.jpg">
              <div class="card-body">
                <p class="card-text"><b>Water</b></p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <a href="/types/Water"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <!--<svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>-->
              <img class="card-img-top" src="https://i.ytimg.com/vi/NU_Z-qkSCYs/maxresdefault.jpg">
              <div class="card-body">
                <p class="card-text"><b>Poison</b></p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <a href="/types/Poison"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
                  </div>
                </div>
              </div>
            </div>
          </div>


          <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <!--<svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>-->
              <img class="card-img-top" src="https://d2juyu303oh9b6.cloudfront.net/image/152367997cae9bab386e4c45237f347b.jpg?&icq=80&sig=def4fe4660a040f5b8e270c031a0dd94">
              <div class="card-body">
                <p class="card-text"><b>Ground</b></p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <a href="/types/Ground"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
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
import Navbar from "@/components/Navbar.vue";
import CardItem from "@/components/CardItem.vue";

export default {
  name: "Types",
  components: {
    Navbar,
    CardItem
  }
};
</script>

<style scoped>
  .container {
    margin-top: 10px;
  };
  .jumbotron {
    height: 100px;
  }
</style>
