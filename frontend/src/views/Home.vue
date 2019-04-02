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

        <div class="container-text">
          
          <div class="hero-text">POKEDB</div>
          <div class="row">

            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur, saepe? Dignissimos laudantium,
              a accusamus explicabo illo distinctio, ipsam soluta quo qui minus voluptatum at labore ab ullam magni ea expedita.</p>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur, saepe? Dignissimos laudantium,
              a accusamus explicabo illo distinctio, ipsam soluta quo qui minus voluptatum at labore ab ullam magni ea expedita.</p>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur, saepe? Dignissimos laudantium,</p>
          </div>
        </div>
      </div>
      </div>
    </div>
    </div>
  </div>
</template>


<style scoped>

  .hero-te {
    z-index: 1;
    position: absolute;
  }
  .bg {
    padding-top: 0;
    padding-bottom: 0%;
    margin-bottom: 0px;
    /* The image used */
    background-image: url('../assets/home-background.jpg');
  
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
    transform: translateY(-250%);
    padding: 25px;
    animation: fadeInAfterPoke 1s 1 forwards;
    animation-delay: 1.4s
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
    height: 100%;

    padding-top: 30px;
    padding-bottom: 30px;
    margin-bottom: 0%;
    align-content: center;

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