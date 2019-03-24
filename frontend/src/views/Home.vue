<template>
  <div class="home">
    <Navbar />
    <div class="container">
      <div class="jumbotron">
        <h1 class="display-4">This is the first thing you see.</h1>
        <p class="lead">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
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
          title="Card 1"
          msg="Message for card 1."
          link="/about"
          link_text="About"
        />
        <CardItem
          title="Card 2"
          msg="Message for card 2."
          link="/about"
          link_text="About"
        />
        <CardItem
          title="Card 3"
          msg="Message for card 3."
          link="/about"
          link_text="About"
        />
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
</style>

