<template>

  <div class="home">
    <div class="fade-container">
    <Navbar/>
    <div @click="clicked=!clicked">
      <div class="bg">
        <div class="container text-scroll-bg">
        <transition onload name ="PokeIn">
          <img src="../assets/PokeBallUpright.png" class="upright"/>
        </transition>
          <div class="container container-text">

            <div class="row">
              <div class="col-lg">
                <p class=hero-text>PokéDB <img src="../assets/pokeball.png" style="max-width: 110px"></p>
                <p class="subhead-text">An indexed database for Pokémon, their evolutions and types. <br/>Click below to start exploring. </p>


              </div>
            </div>


            <div class="row" id="parallel-fill">
              <div class="col-sm parallel-slices" id="parallelogram1">
                <h1 class="parallel-text">Types</h1>
              </div>
              <div class="col-sm" id="parallelogram2">
                <h1 class="parallel-text">Pokémon</h1>
              </div>
              <div class="col-sm" id="parallelogram3">
                <h1 class="parallel-text">Evolutions</h1>
              </div>
            </div>

          </div>

      </div>
      </div>
    </div>
    </div>
  </div>
</template>


<style scoped>

  .hero-text {
    -webkit-text-fill-color: black;
    font-size: 72pt;
    align-content: center;
    margin-bottom: 20px;
  }

  .subhead-text {
    font-size: 24pt;
    align-content: center;
    margin-bottom: 25px;
    -webkit-text-fill-color: rgb(88, 88, 88);

  }

  .row {
    margin-bottom: 50px;
  }
  .bg {
    padding-top: 0;

    margin-bottom: 0px;

    /* The image used */
    /*background-image: url('../assets/home-background.jpg');
  
    /* Full height */
    height: 100%;
  
    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;

    align-content: center;

    position: sticky;
      }
  
  .container-text {
    opacity: 0;
    transform: translateY(-900px);
    padding: 25px;
    animation: fadeInAfterPoke 1s 1 forwards;
    animation-delay: 1.4s;
  }
  
  #parallelogram1 {
  position: absolute;
  transform: translateX(50px); 
  height: 300px;
  width: 350px;
  clip-path: polygon(0 0%, 100% 0%, 75% 100%, 0% 100%);
  clip-path: fill-box;
  background-image: url(https://assets.vg247.com/current//2017/02/eevee_evolutions.png);
  background-size: 400px;
  background-position-x: -35px;
  padding: 10px;

  border-style: solid;
  border-color: rgb(36, 36, 36);
  border-width: 3px;
  }
   
  #parallelogram2 {
  transform: translateX(320px);   
  position: absolute;    
  height: 300px;
  width: 400px;
  clip-path: polygon(22% 0, 100% 0%, 78% 100%, 0% 100%);
  
  background-image: url(https://www.playatgamegrid.com/wp-content/uploads/Pokemon-group.jpg);
  background-size: 600px;
  background-position-y: -10px;

  border-style: solid;
  border-color: rgb(36, 36, 36);
  border-width: 3px;
  }
    
  #parallelogram3 {
  position: absolute; 
  transform: translateX(640px);   
  height: 300px;
  width: 350px;
  clip-path: polygon(25% 0, 100% 0%, 100% 100%, 0% 100%);
  background: blue;
  
  border-style: solid;
  border-color: rgb(36, 36, 36);
  border-width: 3px;
  }

  .parallel-text {
    font-size: 36pt;
    -webkit-text-fill-color: white;
    text-align: center;
    -webkit-text-stroke-width: 2px;
    -webkit-text-stroke-color: black;
  }

  @keyframes fadeInAfterPoke {
    0% {
      opacity: 0;
      scale: 0.1;
    }
    100% {
      opacity: 1;
      scale: 1;
    }
  }

  .text-scroll-bg {
    background-color: rgba(250, 250, 250, 0.9);
    width: 1920px;
    height: 1500px;

    padding-top: 30px;
    padding-bottom: 30px;
    align-content: center;
    box-shadow: 4px 4px 4px;

    animation: textUP 1.5s 1 forwards;
  
  }

  @keyframes textUP {
    0% {
      transform: translateY(100%);
      opacity: 0;
    }
    100% {
      transform: translateY(0%);
      opacity: 1;
    }
  }

  .vertical {
    max-width: 900px;
    max-height: 900px;
    opacity: 0;
  }
  
  .fade-container {
      animation: FadeIn 1.5s 1 forwards;
  }

  .home {

    margin-bottom: 0%;
    overflow: hidden;
    background-color: rgba(65, 65, 65, 0.9)
  }

  @keyframes FadeIn {
    0%{
      opacity: 0
    }
    
    100% {
      opacity: 1;
    }
  }

  .upright {
    max-width: 1100px;
    animation: PokeIn 2s 1 forwards;
    position: relative;
    z-index: 0;
  }


  @keyframes PokeIn {
    0% {
      transform: translateY(100%);

    }
    
    33% {
      transform: translateY(-20%);     
      transform: rotate(-180deg); 
       }

    66% {
      transform: translateY(0%);
    }
    100% {
      transform: translateY(-120%)
    }

  }

 #navbar {
  z-index: 1;
  width: 20%;
  position: fixed;
  animation: navFill 1.5s 1 forwards;
}

@keyframes navFill {
  0% {
    width: 25%;
  }


  100% {
    width: 100%;
  }
}   
</style>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar, 
  },
  el:'#home',
  data () {
    return {
      clicked: true
    }
  }
};
</script>