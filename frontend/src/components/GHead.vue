<template>
  <div class="home">
    <Navbar />
    <div class="bg">
    <div class="jumbotron-fluid">
        <h1 class="display-4">{{title}}</h1>
        <p class="lead">
          {{msg}}
        </p>
      </div>
    </div>
  </div>

</template>

<style scoped>
  .container {
    margin-top: 10px;

  }
  .bg {
    padding-top: 4%;
    padding-bottom: 4%;
    
    /* The image used */
    background-image: url('../assets/home-background.jpg');

    /* Full height */
    height: 90%; 

    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    align-content: center;
  }
  .jumbotron-fluid {
    height: 120px;
    width: 50%;
    margin-left: 25%;
    align-content: center;
    background-color: rgba(255, 255, 255, 0.7);
  }
</style>


<script>
export default {
  name: "GHead",
  props: {
    title: String,
    msg: String,
  }
};
</script>