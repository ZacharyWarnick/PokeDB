<template>
  <div class="pokemon">
    <Navbar />

    <section id="about" class="container section-padding">
      <b-row>
        <b-col lg="6" md="6" sm="12" cols="12">
          <div class="profile-wrapper wow">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h2>
                  <strong>{{ all[$route.params.name].id }}</strong>
                  {{ all[$route.params.name].display_name }}
                </h2>
              </div>
              <div>
                <router-link
                  tag="img"
                  v-for="type in all[$route.params.name].types"
                  v-bind:to="'/types/' + type.name"
                  v-bind:key="type.id"
                  class="type-badge"
                  v-bind:src="type.badge_image"
                />
              </div>
            </div>
            <p class="poke-desc">
              {{ all[$route.params.name].flavor_text }}
            </p>
            <hr />
            <div class="poke-info">
              <ul>
                <li>
                  <strong>Health</strong> {{ all[$route.params.name].stats.hp }}
                </li>
                <li>
                  <strong>Attack</strong>
                  {{ all[$route.params.name].stats.atk }}
                </li>
                <li>
                  <strong>Defense</strong>
                  {{ all[$route.params.name].stats.def }}
                </li>
                <li>
                  <strong>Sp. Atk</strong>
                  {{ all[$route.params.name].stats.sp_atk }}
                </li>
                <li>
                  <strong>Sp. Def</strong>
                  {{ all[$route.params.name].stats.sp_def }}
                </li>
                <li>
                  <strong>Speed</strong>
                  {{ all[$route.params.name].stats.spd }}
                </li>
              </ul>
            </div>
          </div>
        </b-col>

        <b-col lg="6" md="6" sm="12" cols="12" class="my-auto">
          <div class="img-thumb wow">
            <img
              v-bind:src="all[$route.params.name].sprite"
              alt="Pokemon Pic"
              class="img-fluid poke-img"
            />
          </div>
        </b-col>
      </b-row>
    </section>

    <section id="evolution" class="container section-padding">
      <EvolutionOverview
        v-bind:name="all[$route.params.name].ev.name"
        v-bind:first="all[$route.params.name].ev.first"
        v-bind:second="all[$route.params.name].ev.second"
      />
    </section>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import EvolutionOverview from "@/components/EvolutionOverview.vue";

export default {
  name: "Pokemon",
  components: {
    Navbar,
    EvolutionOverview
  },
  data() {
    var all_types = {
      poison: {
        id: 4,
        name: "poison",
        badge_image: require("../assets/badge-poison.png")
      },
      ground: {
        id: 4,
        name: "ground",
        badge_image: require("../assets/badge-ground.png")
      },
      water: {
        id: 4,
        name: "water",
        badge_image: require("../assets/badge-water.png")
      },
      flying: {
        id: 4,
        name: "flying",
        badge_image: require("../assets/badge-flying.png")
      }
    };
    var evolution_info = {
      ekans: {
        species: "ekans",
        first: {
          name: "Ekans",
          id: 23,
          types: [all_types["poison"]]
        },
        second: {
          name: "Arbok",
          id: 24,
          types: [all_types["poison"]]
        }
      },
      sandshrew: {
        species: "sandshrew",
        first: {
          name: "Sandshrew",
          id: 27,
          types: [all_types["ground"]]
        },
        second: {
          name: "Sandslash",
          id: 28,
          types: [all_types["ground"]]
        }
      },
      magikarp: {
        species: "magikarp",
        first: {
          name: "Magikarp",
          id: 129,
          types: [all_types["water"]]
        },
        second: {
          name: "Gyarados",
          id: 130,
          types: [all_types["water"], all_types["flying"]]
        }
      }
    };

    return {
      all: {
        ekans: {
          display_name: "Ekans",
          id: 23,
          sprite:
            "https://cdn.bulbagarden.net/upload/thumb/f/fa/023Ekans.png/250px-023Ekans.png",
          types: [all_types["poison"]],
          flavor_text:
            "Ekans curls itself up in a spiral while it rests. Assuming this position allows it to quickly respond to a threat from any direction with a glare from its upraised head.",
          stats: {
            hp: 35,
            atk: 60,
            def: 44,
            sp_atk: 40,
            sp_def: 54,
            spd: 55
          },
          ev: evolution_info["ekans"]
        },
        arbok: {
          display_name: "Arbok",
          id: 24,
          sprite:
            "https://cdn.bulbagarden.net/upload/thumb/c/cd/024Arbok.png/250px-024Arbok.png",
          types: [all_types["poison"]],
          flavor_text:
            "The latest research has determined that there are over 20 possible arrangements of the patterns on its stomach.",
          stats: {
            hp: 60,
            atk: 95,
            def: 69,
            sp_atk: 65,
            sp_def: 79,
            spd: 80
          },
          ev: evolution_info["ekans"]
        },
        sandshrew: {
          display_name: "Sandshrew",
          id: 27,
          sprite: "https://cdn.bulbagarden.net/upload/9/9e/027Sandshrew.png",
          types: [all_types["ground"]],
          flavor_text:
            "Sandshrew has a very dry hide that is extremely tough. The Pokémon can roll into a ball that repels any attack. At night, it burrows into the desert sand to sleep.",
          stats: {
            hp: 50,
            atk: 75,
            def: 85,
            sp_atk: 20,
            sp_def: 30,
            spd: 40
          },
          ev: evolution_info["sandshrew"]
        },
        sandslash: {
          display_name: "Sandslash",
          id: 28,
          sprite:
            "https://assets.pokemon.com/assets/cms2/img/pokedex/full/028.png",
          types: [all_types["ground"]],
          flavor_text:
            "Sandslash can roll up its body as if it were a ball covered with large spikes. In battle, this Pokémon will try to make the foe flinch by jabbing it with its spines. It then leaps at the stunned foe to tear wildly with its sharp claws.",
          stats: {
            hp: 75,
            atk: 100,
            def: 110,
            sp_atk: 45,
            sp_def: 55,
            spd: 65
          },
          ev: evolution_info["sandshrew"]
        },
        magikarp: {
          display_name: "Magikarp",
          id: 129,
          sprite:
            "https://cdn.bulbagarden.net/upload/thumb/0/02/129Magikarp.png/250px-129Magikarp.png",
          types: [all_types["water"]],
          flavor_text:
            "Magikarp is virtually useless in battle as it can only splash around. As a result, it is considered to be weak. However, it is actually a very hardy Pokémon that can survive in any body of water no matter how polluted it is.",
          stats: {
            hp: 20,
            atk: 10,
            def: 55,
            sp_atk: 15,
            sp_def: 20,
            spd: 80
          },
          ev: evolution_info["magikarp"]
        },
        gyarados: {
          display_name: "Gyarados",
          id: 130,
          sprite:
            "https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png",
          types: [all_types["water"], all_types["flying"]],
          flavor_text:
            "Once Gyarados goes on a rampage, its ferociously violent blood doesn’t calm until it has burned everything down. There are records of this Pokémon’s rampages lasting a whole month.",
          stats: {
            hp: 95,
            atk: 125,
            def: 79,
            sp_atk: 60,
            sp_def: 100,
            spd: 81
          },
          ev: evolution_info["magikarp"]
        }
      }
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 15px 0;
}

.profile-wrapper {
  padding: 45px 0;
  text-align: left;
}

.type-badge {
  max-height: 32px;
  height: 100%;
  width: auto;
  padding: 0 4px;
}

.poke-desc {
  padding: 20px 0;
}

.poke-info {
  padding: 10px 0;
}

.poke-img {
  max-height: 400px;
}

.poke-img-box:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
</style>
