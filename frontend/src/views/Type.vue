<template>
  <div class="Type" style="padding-left">
    <Navbar />
      <div class="bg">
      <div class="container text-scroll-bg">
      <b-container>
        <b-jumbotron
          class="section-padding"
          :header="capitalize($route.params.name)"
          header-tag="h2"
        />
      </b-container>
      <section class="section-padding">
        <b-container>
          <b-row>
            <b-col md="6" class="my-auto">
              <p class="lead text-justify">{{ all[$route.params.name].info }}</p>
            </b-col>
            <b-col md="6">
              <img :src="all[$route.params.name].image" width="320px" />
            </b-col>
          </b-row>
          <hr />
          <b-row>
            <b-col md="6" class="my-auto">
              <p class="text-justify">
                {{ all[$route.params.name].info2 }}
              </p>
            </b-col>

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
                    <tr
                      v-for="i in Math.max(
                        all[$route.params.name].advantages.length,
                        all[$route.params.name].weaknesses.length
                      )"
                      :key="i"
                    >
                      <td class="table-strong">
                        {{
                          capitalize(all[$route.params.name].advantages[i - 1])
                        }}
                      </td>
                      <td class="table-weak">
                        {{
                          capitalize(all[$route.params.name].weaknesses[i - 1])
                        }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </b-container>
            </b-col>
          </b-row>
        </b-container>
      </section>
      <section class="section-padding">
        <h2>Pokemon of this type:</h2>
        <b-container class="d-flex justify-content-center">
          <b-row class="align-items-center">
            <b-col v-for="p in all[$route.params.name].related" :key="p.id">
              <b-card>
                <SpriteBasic
                  v-bind:name="p.name"
                  v-bind:id="p.id"
                  v-bind:types="p.types"
                />
              </b-card>
            </b-col>
          </b-row>
        </b-container>
      </section>
      </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import SpriteBasic from "@/components/SpriteBasic.vue";

export default {
  name: "Type",
  components: {
    Navbar,
    SpriteBasic
  },
  methods: {
    capitalize(s) {
      if (typeof s !== "string") return "";
      return s.charAt(0).toUpperCase() + s.slice(1);
    }
  },
  data() {
    return {
      all: {
        water: {
          info: [
            "Water is one of the three basic elemental types along with Fire and Grass,",
            "which constitute the three starter Pokémon. This creates a simple triangle",
            "to explain the type concept easily to new players. Water is the most common",
            "type with over 100 Pokémon, which are based on a wide variety of fish and",
            "other sea-dwelling creatures."
          ].join(" "),
          info2: [
            "Notable Trainers who specialize in Water-type Pokémon include Misty of Cerulean City,",
            "Juan and Wallace of Sootopolis City, Crasher Wake of Pastoria City, Cress of Striaton City,",
            "Marlon of Humilau City, Siebold of the Kalos Elite Four, and Trial Captain Lana of Konikoni City.",
            "Prior to changes in Generation IV, all damaging Water-type moves were special,",
            "but they may now also be physical depending on the attack."
          ].join(" "),
          image: "https://pokeweakness.com/images/1891870-131lapras.png",
          advantages: ["ground"],
          weaknesses: [""],
          related: [
            {
              name: "Magikarp",
              id: 129,
              types: [
                {
                  name: "water",
                  badge_image: require("../assets/badge-water.png")
                }
              ]
            },
            {
              name: "Gyarados",
              id: 130,
              types: [
                {
                  name: "water",
                  badge_image: require("../assets/badge-water.png")
                },
                {
                  name: "flying",
                  badge_image: require("../assets/badge-flying.png")
                }
              ]
            }
          ]
        },
        poison: {
          info: [
            "The Poison type is regarded as one of the weakest offensively.",
            "Prior to Pokémon X/Y it was super-effective only against Grass",
            "(many of which are dual Poison so neutralizes the effect).",
            "It now has an extra advantage against the new Fairy type.",
            "In the first generation it was also super-effective against Bug but this was changed.",
            "It fares a little better defensively but its best advantage is through status moves like Toxic."
          ].join(" "),
          info2: [
            "Notable Trainers who specialize in Poison-type Pokémon include Janine of Fuchsia City,",
            "her father Koga of the Indigo Plateau Elite Four, Roxie of Virbank City, and Team Skull Admin Plumeria.",
            "Some villainous teams, such as Team Rocket, also frequently use Poison-type Pokémon.",
            "Prior to changes in Generation IV, all damaging Poison-type moves were physical,",
            "but they may now also be special depending on the attack."
          ].join(" "),
          image: "http://bogleech.com/pokemon/koffing.png",
          advantages: [""],
          weaknesses: [""],
          related: [
            {
              name: "Ekans",
              id: 23,
              types: [
                {
                  name: "poison",
                  badge_image: require("../assets/badge-poison.png")
                }
              ]
            },
            {
              name: "Arbok",
              id: 24,
              types: [
                {
                  name: "poison",
                  badge_image: require("../assets/badge-poison.png")
                }
              ]
            }
          ]
        },
        ground: {
          info: [
            "Ground is one of the strongest types offensively:",
            "it is super-effective against five other types (as is Fighting)",
            "and Earthquake is one of the strongest moves in the game with power and accuracy both 100.",
            "Unfortunately, many Ground type Pokémon are dual Rock types, lumbering them with 4x Grass and Water disadvantages."
          ].join(" "),
          info2: [
            "Notable Trainers who specialize in Ground-type Pokémon are Giovanni of Viridian City,",
            "Bertha of the Sinnoh Elite Four, Clay of Driftveil City, and Island Kahuna Hapu of Poni Island.",
            "Prior to changes in Generation IV, all damaging Ground-type moves were physical,",
            "but they may now also be special depending on the attack."
          ].join(" "),
          image: "https://cdn.bulbagarden.net/upload/3/31/050Diglett.png",
          advantages: ["", ""],
          weaknesses: ["water", "flying"],
          related: [
            {
              name: "Sandshrew",
              id: 27,
              types: [
                {
                  name: "ground",
                  badge_image: require("../assets/badge-ground.png")
                }
              ]
            },
            {
              name: "Sandslash",
              id: 28,
              types: [
                {
                  name: "ground",
                  badge_image: require("../assets/badge-ground.png")
                }
              ]
            }
          ]
        },
        flying: {
          info: [
            "Most Flying type Pokémon are based on birds or insects, along with some mythical creatures like dragons.",
            "On average they are faster than any other type. Nearly every Flying type has Flying as the secondary type,",
            "usually with Normal.",
            "There is only one pure Flying Pokémon (Tornadus), and one line with Flying as a primary type (Noibat/Noivern)."
          ].join(" "),
          info2: [
            "Notable Trainers who specialize in Flying-type Pokémon are the Gym Leaders Falkner of Violet City,",
            "Winona of Fortree City, Skyla of Mistralton City, and Kahili of Alola Elite Four.",
            "Prior to changes in Generation IV, all damaging Flying-type moves were physical,",
            "but they may now also be special depending on the attack."
          ].join(" "),
          image:
            "https://assets.pokemon.com/assets/cms2/img/pokedex/full/018.png",
          advantages: [""],
          weaknesses: [""],
          related: [
            {
              name: "Gyarados",
              id: 130,
              types: [
                {
                  name: "water",
                  badge_image: require("../assets/badge-water.png")
                },
                {
                  name: "flying",
                  badge_image: require("../assets/badge-flying.png")
                }
              ]
            }
          ]
        }
      }
    };
  }
};
</script>

<!--
Color of tables or fromatting subject to change
-->
<style scoped>
.section-padding {
  padding: 15px 0;
}
.container {
  margin-top: 20px;
  margin-bottom: 10px;
  align-items: center;
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

  padding-top: 30px;
  padding-bottom: 30px;
  align-content: center;
  box-shadow: 4px 4px 4px;

  animation: textUP 1.5s 1 forwards;

}
.bg {
padding-top: 0;

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
</style>