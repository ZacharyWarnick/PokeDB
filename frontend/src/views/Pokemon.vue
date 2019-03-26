<template>
  <div class="pokemon">
    <Navbar />

    <section id="about" class="container section-padding">
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
          <div class="profile-wrapper wow">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h2><strong>22</strong> {{ $route.params.name }}</h2>
              </div>
              <div>
                <img
                  class="type-badge"
                  src="https://nintendowire.com/wp-content/uploads/2016/07/Grass.png"
                />
                <img
                  class="type-badge"
                  src="https://nintendowire.com/wp-content/uploads/2016/07/Grass.png"
                />
              </div>
            </div>
            <p class="poke-desc">
              This is some text. This is some text. This is some text. This is
              some text. This is some text. This is some text. This is some
              text. This is some text. This is some text. This is some text.
              This is some text.
            </p>
            <hr />
            <p class="poke-info">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat.
            </p>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
          <div class="img-thumb wow">
            <img
              src="https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527784709esduz.png"
              alt="Pokemon Pic"
              class="img-fluid poke-img"
            />
          </div>
        </div>
      </div>
    </section>

    <section id="evolution" class="container section-padding">
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
