<template>
<div class="Type">
  <Navbar />
    <div class="bg">
      <div class="container text-scroll-bg">

      <b-jumbotron
        :header="capitalize(type.identifier)"
        header-tag="h2"
      />

    <section class="section-padding">
      <b-container>
        <b-row>
          <b-col md="6" class="my-auto">
            <p class="lead text-justify">{{ type.desc_info }}</p>
          </b-col>
          <b-col md="6">
            <img src="../assets/team/ian.jpg" width="320px" />
          </b-col>
        </b-row>
        <hr />
        <b-row>
          <b-col md="6">
            <b-container>
              <table class="table">
                <thead>
                  <tr>
                    <th class="table-strong" scope="col">Strong Against</th>
                    <th class="table-weak" scope="col">Weak Against</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="table-strong">
                      {{
                        capitalize("Words")
                      }}
                    </td>
                    <td class="table-weak">
                      {{
                        capitalize("Words")
                      }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </b-container>
          </b-col>
          <b-col md="6" class="my-auto">
            <h2>Offense</h2>
            <p class="text-justify">
              {{ type.desc_atk }}
            </p>
          </b-col>
        </b-row>
        <b-row>
          <b-col md="6">
            <h2>Info</h2>
            <ul class="list-unstyled info">
                <li><b>Damgage Class:</b>        {{capitalize(type.damage_class)}}</li>
                <li><b>Number of Pokémon:</b>    {{type.pokemon_count}}</li>
                <li><b>Stat Average:</b>         {{type.stat_average}}</li>
                <li><b>Relative Advantage:</b>   {{type.relative_advantage}}</li>
            </ul>            
          </b-col>
          <b-col md="6">            
            <h2>Defense</h2>
            <p>{{type.desc_def}}</p>
          </b-col>
        </b-row>
      </b-container>
    <hr /> 
    </section>
    <section class="section-padding">
      <h2>Pokémon of This Type</h2>
      <h3>There are {{type.pokemon_count}} {{type.identifier}} pokémon </h3>
    </section>
  </div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

import { getType }from "@/api";

function getID() {

  var pathArray = window.location.pathname.split('/');

  var lastLocation = pathArray.slice(-1).pop()

  return String(lastLocation);
}

export default {
  name: "Type",
  components: {
    Navbar,
  },

  data () {
    return {
      type: null
    }
  },

  methods: {
    capitalize(s) {
      if (typeof s !== "string") return "";
      return s.charAt(0).toUpperCase() + s.slice(1);
    },
  },

  mounted() {
    getType(getID()).then(
      response => (this.type = response.data)
    )   
  }
}  
</script>

<!--
Color of tables or fromatting subject to change
-->
<style scoped>

#navbar {
  z-index: 1;
  width: 100%;
  position: fixed;

}

.jumbotron {
  padding: 30px 0px;
}

.table-strong {
  background-color: rgba(0, 128, 0, 0.7);
}

.table-weak {
  background-color: rgba(255, 0, 0, 0.7);
}

.text-scroll-bg {
  background-color: white;
  width: 1920px;
  height: 1500px;

  padding-top: 70px;
  padding-bottom: 30px;
  align-content: center;
  box-shadow: 4px 4px 4px;

}
.bg {
  padding-top: 0;

  margin-bottom: 0px;

  /* The image used */
  background-image: url("../assets/home-background.jpg");

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
.info {
  text-align: left;
  align-content: center;
  padding-left: 120px;
}
</style>
