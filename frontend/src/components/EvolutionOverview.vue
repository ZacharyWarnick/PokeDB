<template>
  <b-card>
    <div class="container-fluid">
      <div class="row align-items-center">
        <div class="col-sm">
          <div class="img-thumb wow">
            <img
              src="https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527784709esduz.png"
              alt="Pokemon Pic"
              class="img-fluid poke-img"
            />
          </div>
        </div>
        <div class="col-sm">
          <div class="row">
            <div class="col-sm justify-center align-center">
              <span class="infocard infocard-arrow"
                ><i class="icon-arrow icon-arrow-e"></i
              ></span>
            </div>

            <div class="col-sm">
              <div class="img-thumb wow">
                <img
                  src="https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527784709esduz.png"
                  alt="Pokemon Pic"
                  class="img-fluid poke-img"
                />
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-sm justify-center">
              <span class="infocard infocard-arrow"
                ><i class="icon-arrow icon-arrow-e"></i
              ></span>
            </div>

            <div class="col-sm">
              <div class="img-thumb wow">
                <img
                  src="https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527784709esduz.png"
                  alt="Pokemon Pic"
                  class="img-fluid poke-img"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm justify-center">
          <span class="infocard infocard-arrow"
            ><i class="icon-arrow icon-arrow-e"></i
          ></span>
        </div>

        <div class="col-sm">
          <div class="img-thumb wow">
            <img
              src="https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527784709esduz.png"
              alt="Pokemon Pic"
              class="img-fluid poke-img"
            />
          </div>
        </div>
      </div>
    </div>
  </b-card>
</template>

<script>
export default {
  name: "EvolutionOverview",
  props: {
    species: String
  }
};
</script>


<style scoped>
.icon-arrow-e::before {
  content: "\2192\FE0E";
}

.infocard-list-evo > .infocard-arrow {
  width: 165px;
}

.icon-arrow {
  display: block;
  font: normal 2.5rem/1 "Arial Unicode MS", "Trebuchet MS", "Arial", "Helvetica",
    sans-serif;
}
</style>

