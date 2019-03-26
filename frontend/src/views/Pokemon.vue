<template>
  <div class="pokemon">
    <Navbar />

    <section id="about" class="container section-padding">
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
          <div class="profile-wrapper wow">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h2>
                  <strong>{{ all[$route.params.name].id }}</strong>
                  {{ all[$route.params.name].display_name }}
                </h2>
              </div>
              <div>
                <img
                  v-for="type in all[$route.params.name].types"
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
                  <strong>Health</strong>
                  {{ all[$route.params.name].stats.spd }}
                </li>
              </ul>
            </div>
          </div>
        </div>

        <b-col lg="6" md="6" sm="12" cols="12" class="my-auto">
          <div class="img-thumb wow">
            <img
              v-bind:src="all[$route.params.name].sprite"
              alt="Pokemon Pic"
              class="img-fluid poke-img"
            />
          </div>
        </b-col>
      </div>
    </section>

    <section id="evolution" class="container">
      <EvolutionOverview />
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
    return {
      all: {
        ekans: {
          display_name: "Ekans",
          id: 23,
          sprite:
            "https://cdn.bulbagarden.net/upload/thumb/f/fa/023Ekans.png/250px-023Ekans.png",
          types: [
            {
              id: 4,
              name: "poison",
              badge_image: require("../assets/badge-poison.png")
            }
          ],
          flavor_text:
            "Ekans curls itself up in a spiral while it rests. Assuming this position allows it to quickly respond to a threat from any direction with a glare from its upraised head.",
          stats: {
            hp: 35,
            atk: 60,
            def: 44,
            sp_atk: 40,
            sp_def: 54,
            spd: 55
          }
        },
        arbok: {
          display_name: "Arbok",
          id: 24,
          sprite:
            "https://cdn.bulbagarden.net/upload/thumb/c/cd/024Arbok.png/250px-024Arbok.png",
          types: [
            {
              id: 4,
              name: "poison",
              badge_image: require("../assets/badge-poison.png")
            }
          ],
          flavor_text:
            "The latest research has determined that there are over 20 possible arrangements of the patterns on its stomach.",
          stats: {
            hp: 60,
            atk: 95,
            def: 69,
            sp_atk: 65,
            sp_def: 79,
            spd: 80
          }
        }
      }
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 60px 0;
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
