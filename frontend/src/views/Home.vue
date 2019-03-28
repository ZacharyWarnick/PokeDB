<template>
  <div class="home">
    <Navbar />
    <div class="spacer">
    <div class="bg">
   
    <div class="container">
      <div class="jumbotron">
        <h1 class="display-4">Welcome to PokéDB</h1>
        <p class="lead">
          This is an indexed database of all things Pokémon. 
          Click below to find out imformation on the Pokeémon, types, evolution patterns, and so much more!
        </p>

        <p class="lead">
          <a class="btn btn-primary btn-lg" href="#" role="button"
            >Learn more</a
          >
        </p>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <CardItem
          title="Pokémon"
          msg="Learn about the various Pokémon across all the games."
          link="/pokemon"
          link_text="Go"
        />
        <CardItem
          title="Types"
          msg="Learn about the 18 standard types, or the 3 hidden and special types."
          link="/types"
          link_text="Go"
        />
        <CardItem
          title="Evolutions"
          msg="Learn about the paths each Pokémon takes to evolve."
          link="/evolutions/"
          link_text="Go"
        />
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
  .bg {

    padding-top: 8%;
    padding-bottom: 8%;
    /* The image used */
    background-image: url('../assets/home-background.jpg');

    /* Full height */
    height: 100%; 

    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    align-content: center;
  }

  .spacer {
    padding-top: 5%;
    padding-bottom: 5%;


    background-color: rgba(10, 10, 10, .5);
  }
</style>

