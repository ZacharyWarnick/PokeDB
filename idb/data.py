POKEMON_OG6 = {
    'ekans': {
        'id': 23,
        'description': 'Snake that is 3 meters long and weighs around 6.9 kilograms.',
        'category': 'Snake',
        'type': ['poison'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png'

    },
    'arbok': {
        'id': 24,
        'description': 'Cobra that is 3.5 meters long and weighs around 65 kilograms.',
        'category': 'Cobra',
        'type': ['poison'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png'
    },
    'sandshrew': {
        'id': 27,
        'description': 'Mouse that is 0.6 meters tall and weighs around 12 kilograms.',
        'category': 'Mouse',
        'type': ['ground'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png'
    },
    'sandslash': {
        'id': 28,
        'description': 'Mouse that is 1 meters tall and weighs around 29.5 kilograms.',
        'category': 'Mouse',
        'type': ['ground'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png'
    },
    'magikarp': {
        'id': 129,
        'description': 'Fish that is 0.9 meters long and weighs around 10.0 kilograms.',
        'category': 'Fish',
        'type': ['water'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png'
    },
    'gyarados': {
        'id': 130,
        'description': 'Atrocious Pokémon that is 3.5 meters long and weighs around 65 kilograms.',
        'category': 'Atrocious Pokémon',
        'type': ['water', 'flying'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png'
    }
}

POKEMON = [
    {
        "name": "Bulbasaur",
        "genus": "Seed Pokémon",
        "identifier": "bulbasaur",
        "evolution_chain": 1,
        "color": "green",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun’s rays,\nthe seed grows progressively larger.",
        "has_alt_form": False,
        "id": 1
    },
    {
        "name": "Ivysaur",
        "genus": "Seed Pokémon",
        "identifier": "ivysaur",
        "evolution_chain": 1,
        "color": "green",
        "since_gen": 1,
        "evolves_from": 1,
        "type1": 12,
        "type2": 4,
        "flavor_text": "There is a bud on this Pokémon’s back. To support its weight,\nIvysaur’s legs and trunk grow thick and strong.\nIf it starts spending more time lying in the sunlight,\nit’s a sign that the bud will bloom into a large flower soon.",
        "has_alt_form": False,
        "id": 2
    },
    {
        "name": "Venusaur",
        "genus": "Seed Pokémon",
        "identifier": "venusaur",
        "evolution_chain": 1,
        "color": "green",
        "since_gen": 1,
        "evolves_from": 2,
        "type1": 12,
        "type2": 4,
        "flavor_text": "There is a large flower on Venusaur’s back. The flower is said\nto take on vivid colors if it gets plenty of nutrition and sunlight.\nThe flower’s aroma soothes the emotions of people.",
        "has_alt_form": False,
        "id": 3
    },
    {
        "name": "Charmander",
        "genus": "Lizard Pokémon",
        "identifier": "charmander",
        "evolution_chain": 2,
        "color": "red",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 10,
        "type2": None,
        "flavor_text": "The flame that burns at the tip of its tail is an indication\nof its emotions. The flame wavers when Charmander\nis enjoying itself. If the Pokémon becomes enraged,\nthe flame burns fiercely.",
        "has_alt_form": False,
        "id": 4
    },
    {
        "name": "Charmeleon",
        "genus": "Flame Pokémon",
        "identifier": "charmeleon",
        "evolution_chain": 2,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 4,
        "type1": 10,
        "type2": None,
        "flavor_text": "Charmeleon mercilessly destroys its foes using its sharp\nclaws. If it encounters a strong foe, it turns aggressive.\nIn this excited state, the flame at the tip of its tail flares with\na bluish white color.",
        "has_alt_form": False,
        "id": 5
    },
    {
        "name": "Charizard",
        "genus": "Flame Pokémon",
        "identifier": "charizard",
        "evolution_chain": 2,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 5,
        "type1": 10,
        "type2": 3,
        "flavor_text": "Charizard flies around the sky in search of powerful opponents.\nIt breathes fire of such great heat that it melts anything.\nHowever, it never turns its fiery breath on any opponent\nweaker than itself.",
        "has_alt_form": False,
        "id": 6
    },
    {
        "name": "Squirtle",
        "genus": "Tiny Turtle Pokémon",
        "identifier": "squirtle",
        "evolution_chain": 3,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "Squirtle’s shell is not merely used for protection.\nThe shell’s rounded shape and the grooves on its\nsurface help minimize resistance in water,\nenabling this Pokémon to swim at high speeds.",
        "has_alt_form": False,
        "id": 7
    },
    {
        "name": "Wartortle",
        "genus": "Turtle Pokémon",
        "identifier": "wartortle",
        "evolution_chain": 3,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 7,
        "type1": 11,
        "type2": None,
        "flavor_text": "Its tail is large and covered with a rich, thick fur. The tail\nbecomes increasingly deeper in color as Wartortle ages.\nThe scratches on its shell are evidence of this Pokémon’s\ntoughness as a battler.",
        "has_alt_form": False,
        "id": 8
    },
    {
        "name": "Blastoise",
        "genus": "Shellfish Pokémon",
        "identifier": "blastoise",
        "evolution_chain": 3,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 8,
        "type1": 11,
        "type2": None,
        "flavor_text": "Blastoise has water spouts that protrude from its shell.\nThe water spouts are very accurate.\nThey can shoot bullets of water with enough accuracy\nto strike empty cans from a distance of over 160 feet.",
        "has_alt_form": False,
        "id": 9
    },
    {
        "name": "Caterpie",
        "genus": "Worm Pokémon",
        "identifier": "caterpie",
        "evolution_chain": 4,
        "color": "green",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 7,
        "type2": None,
        "flavor_text": "Perhaps because it would like to grow up\nquickly, it has a voracious appetite, eating\na hundred leaves a day.",
        "has_alt_form": False,
        "id": 10
    },
    {
        "name": "Metapod",
        "genus": "Cocoon Pokémon",
        "identifier": "metapod",
        "evolution_chain": 4,
        "color": "green",
        "since_gen": 1,
        "evolves_from": 10,
        "type1": 7,
        "type2": None,
        "flavor_text": "Its shell is filled with a thick liquid. All of the\ncells throughout its body are being rebuilt in\npreparation for evolution.",
        "has_alt_form": False,
        "id": 11
    },
    {
        "name": "Butterfree",
        "genus": "Butterfly Pokémon",
        "identifier": "butterfree",
        "evolution_chain": 4,
        "color": "white",
        "since_gen": 1,
        "evolves_from": 11,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Its wings are covered in toxic scales. If it finds\nbird Pokémon going after Caterpie, Butterfree\nsprinkles its scales on them to drive them off.",
        "has_alt_form": False,
        "id": 12
    },
    {
        "name": "Weedle",
        "genus": "Hairy Bug Pokémon",
        "identifier": "weedle",
        "evolution_chain": 5,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Weedle has an extremely acute sense of smell. It is capable\nof distinguishing its favorite kinds of leaves from those it\ndislikes just by sniffing with its big red proboscis (nose).",
        "has_alt_form": False,
        "id": 13
    },
    {
        "name": "Kakuna",
        "genus": "Cocoon Pokémon",
        "identifier": "kakuna",
        "evolution_chain": 5,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 13,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Kakuna remains virtually immobile as it clings to a tree.\nHowever, on the inside, it is extremely busy as it prepares\nfor its coming evolution.\nThis is evident from how hot the shell becomes to the touch.",
        "has_alt_form": False,
        "id": 14
    },
    {
        "name": "Beedrill",
        "genus": "Poison Bee Pokémon",
        "identifier": "beedrill",
        "evolution_chain": 5,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 14,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Beedrill is extremely territorial. No one should ever approach\nits nest—this is for their own safety. If angered, they will attack\nin a furious swarm.",
        "has_alt_form": False,
        "id": 15
    },
    {
        "name": "Pidgey",
        "genus": "Tiny Bird Pokémon",
        "identifier": "pidgey",
        "evolution_chain": 6,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Pidgey has an extremely sharp sense of direction.\nIt is capable of unerringly returning home to its nest,\nhowever far it may be removed from its familiar surroundings.",
        "has_alt_form": False,
        "id": 16
    },
    {
        "name": "Pidgeotto",
        "genus": "Bird Pokémon",
        "identifier": "pidgeotto",
        "evolution_chain": 6,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 16,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Pidgeotto claims a large area as its own territory. This\nPokémon flies around, patrolling its living space. If its territory\nis violated, it shows no mercy in thoroughly punishing the foe\nwith its sharp claws.",
        "has_alt_form": False,
        "id": 17
    },
    {
        "name": "Pidgeot",
        "genus": "Bird Pokémon",
        "identifier": "pidgeot",
        "evolution_chain": 6,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 17,
        "type1": 1,
        "type2": 3,
        "flavor_text": "This Pokémon has a dazzling plumage of beautifully\nglossy feathers. Many Trainers are captivated by the\nstriking beauty of the feathers on its head, compelling\nthem to choose Pidgeot as their Pokémon.",
        "has_alt_form": False,
        "id": 18
    },
    {
        "name": "Rattata",
        "genus": "Mouse Pokémon",
        "identifier": "rattata",
        "evolution_chain": 7,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "Its incisors grow continuously throughout its life.\nIf its incisors get too long, this Pokémon\nbecomes unable to eat, and it starves to death.",
        "has_alt_form": False,
        "id": 19
    },
    {
        "name": "Raticate",
        "genus": "Mouse Pokémon",
        "identifier": "raticate",
        "evolution_chain": 7,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 19,
        "type1": 1,
        "type2": None,
        "flavor_text": "People say that it fled from its enemies by\nusing its small webbed hind feet to swim\nfrom island to island in Alola.",
        "has_alt_form": False,
        "id": 20
    },
    {
        "name": "Spearow",
        "genus": "Tiny Bird Pokémon",
        "identifier": "spearow",
        "evolution_chain": 8,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Its reckless nature leads it to stand up to\nothers—even large Pokémon—if it has to protect\nits territory.",
        "has_alt_form": False,
        "id": 21
    },
    {
        "name": "Fearow",
        "genus": "Beak Pokémon",
        "identifier": "fearow",
        "evolution_chain": 8,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 21,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Carrying food through Fearow’s territory is\ndangerous. It will snatch the food away from\nyou in a flash!",
        "has_alt_form": False,
        "id": 22
    },
    {
        "name": "Ekans",
        "genus": "Snake Pokémon",
        "identifier": "ekans",
        "evolution_chain": 9,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 4,
        "type2": None,
        "flavor_text": "By dislocating its jaw, it can swallow prey larger\nthan itself. After a meal, it curls up and rests.",
        "has_alt_form": False,
        "id": 23
    },
    {
        "name": "Arbok",
        "genus": "Cobra Pokémon",
        "identifier": "arbok",
        "evolution_chain": 9,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 23,
        "type1": 4,
        "type2": None,
        "flavor_text": "The latest research has determined that there\nare over 20 possible arrangements of the\npatterns on its stomach.",
        "has_alt_form": False,
        "id": 24
    },
    {
        "name": "Pikachu",
        "genus": "Mouse Pokémon",
        "identifier": "pikachu",
        "evolution_chain": 10,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 172,
        "type1": 13,
        "type2": None,
        "flavor_text": "Its nature is to store up electricity. Forests\nwhere nests of Pikachu live are dangerous,\nsince the trees are so often struck by lightning.",
        "has_alt_form": False,
        "id": 25
    },
    {
        "name": "Raichu",
        "genus": "Mouse Pokémon",
        "identifier": "raichu",
        "evolution_chain": 10,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 25,
        "type1": 13,
        "type2": None,
        "flavor_text": "As electricity builds up inside its body, it\nbecomes more aggressive. One theory is that\nthe electricity buildup is actually causing stress.",
        "has_alt_form": False,
        "id": 26
    },
    {
        "name": "Sandshrew",
        "genus": "Mouse Pokémon",
        "identifier": "sandshrew",
        "evolution_chain": 11,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 5,
        "type2": None,
        "flavor_text": "It lives in areas of limited rainfall. When danger\napproaches, it curls up into a ball to protect its\nsoft stomach.",
        "has_alt_form": False,
        "id": 27
    },
    {
        "name": "Sandslash",
        "genus": "Mouse Pokémon",
        "identifier": "sandslash",
        "evolution_chain": 11,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 27,
        "type1": 5,
        "type2": None,
        "flavor_text": "Its claws and horns often break off. The broken\nclaws and horns can be used to carve plows for\ntilling farm fields.",
        "has_alt_form": False,
        "id": 28
    },
    {
        "name": "Nidoran♀",
        "genus": "Poison Pin Pokémon",
        "identifier": "nidoran-f",
        "evolution_chain": 12,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 4,
        "type2": None,
        "flavor_text": "Nidoran♀ has barbs that secrete a powerful poison.\nThey are thought to have developed as protection for\nthis small-bodied Pokémon. When enraged, it releases\na horrible toxin from its horn.",
        "has_alt_form": False,
        "id": 29
    },
    {
        "name": "Nidorina",
        "genus": "Poison Pin Pokémon",
        "identifier": "nidorina",
        "evolution_chain": 12,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 29,
        "type1": 4,
        "type2": None,
        "flavor_text": "When Nidorina are with their friends or family, they keep\ntheir barbs tucked away to prevent hurting each other.\nThis Pokémon appears to become nervous if separated\nfrom the others.",
        "has_alt_form": False,
        "id": 30
    },
    {
        "name": "Nidoqueen",
        "genus": "Drill Pokémon",
        "identifier": "nidoqueen",
        "evolution_chain": 12,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 30,
        "type1": 4,
        "type2": 5,
        "flavor_text": "Nidoqueen’s body is encased in extremely hard scales.\nIt is adept at sending foes flying with harsh tackles. This\nPokémon is at its strongest when it is defending its young.",
        "has_alt_form": False,
        "id": 31
    },
    {
        "name": "Nidoran♂",
        "genus": "Poison Pin Pokémon",
        "identifier": "nidoran-m",
        "evolution_chain": 13,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 4,
        "type2": None,
        "flavor_text": "Nidoran♂ has developed muscles for moving its ears. Thanks\nto them, the ears can be freely moved in any direction. Even\nthe slightest sound does not escape this Pokémon’s notice.",
        "has_alt_form": False,
        "id": 32
    },
    {
        "name": "Nidorino",
        "genus": "Poison Pin Pokémon",
        "identifier": "nidorino",
        "evolution_chain": 13,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 32,
        "type1": 4,
        "type2": None,
        "flavor_text": "Nidorino has a horn that is harder than a diamond. If it senses\na hostile presence, all the barbs on its back bristle up at once,\nand it challenges the foe with all its might.",
        "has_alt_form": False,
        "id": 33
    },
    {
        "name": "Nidoking",
        "genus": "Drill Pokémon",
        "identifier": "nidoking",
        "evolution_chain": 13,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 33,
        "type1": 4,
        "type2": 5,
        "flavor_text": "Nidoking’s thick tail packs enormously destructive power.\nWith one swing, it can topple a metal transmission tower. Once\nthis Pokémon goes on a rampage, there is no stopping it.",
        "has_alt_form": False,
        "id": 34
    },
    {
        "name": "Clefairy",
        "genus": "Fairy Pokémon",
        "identifier": "clefairy",
        "evolution_chain": 14,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 173,
        "type1": 18,
        "type2": None,
        "flavor_text": "They’re popular, but they’re rare. Trainers who\nshow them off recklessly may be targeted\nby thieves.",
        "has_alt_form": False,
        "id": 35
    },
    {
        "name": "Clefable",
        "genus": "Fairy Pokémon",
        "identifier": "clefable",
        "evolution_chain": 14,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 35,
        "type1": 18,
        "type2": None,
        "flavor_text": "It can’t help but hear a pin drop from over half\na mile away, so it lives deep in the mountains\nwhere there aren’t many people or Pokémon.",
        "has_alt_form": False,
        "id": 36
    },
    {
        "name": "Vulpix",
        "genus": "Fox Pokémon",
        "identifier": "vulpix",
        "evolution_chain": 15,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 10,
        "type2": None,
        "flavor_text": "Its beautiful tails have made it very popular.\nHowever, if it’s not brushed diligently, it will\nbe a mass of tangles before you know it.",
        "has_alt_form": False,
        "id": 37
    },
    {
        "name": "Ninetales",
        "genus": "Fox Pokémon",
        "identifier": "ninetales",
        "evolution_chain": 15,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 37,
        "type1": 10,
        "type2": None,
        "flavor_text": "It is vindictive and relentless by nature.\nThose who cross it even once will be cursed for\na thousand years, along with their descendants.",
        "has_alt_form": False,
        "id": 38
    },
    {
        "name": "Jigglypuff",
        "genus": "Balloon Pokémon",
        "identifier": "jigglypuff",
        "evolution_chain": 16,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 174,
        "type1": 1,
        "type2": 18,
        "flavor_text": "Recordings of Jigglypuff’s strange lullabies can\nbe purchased from department stores. These\nCDs can be found near the bedding area.",
        "has_alt_form": False,
        "id": 39
    },
    {
        "name": "Wigglytuff",
        "genus": "Balloon Pokémon",
        "identifier": "wigglytuff",
        "evolution_chain": 16,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 39,
        "type1": 1,
        "type2": 18,
        "flavor_text": "Thanks to its bouncy body and fine fur,\nthis Pokémon is sought after. Holding one\nin your arms while you sleep feels great.",
        "has_alt_form": False,
        "id": 40
    },
    {
        "name": "Zubat",
        "genus": "Bat Pokémon",
        "identifier": "zubat",
        "evolution_chain": 17,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 4,
        "type2": 3,
        "flavor_text": "It has no eyeballs, so it can’t see. It checks its\nsurroundings via the ultrasonic waves it emits\nfrom its mouth.",
        "has_alt_form": False,
        "id": 41
    },
    {
        "name": "Golbat",
        "genus": "Bat Pokémon",
        "identifier": "golbat",
        "evolution_chain": 17,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 41,
        "type1": 4,
        "type2": 3,
        "flavor_text": "Every once in a while, you’ll see a Golbat that’s\nmissing some fangs. This happens when hunger\ndrives it to try biting a Steel-type Pokémon.",
        "has_alt_form": False,
        "id": 42
    },
    {
        "name": "Oddish",
        "genus": "Weed Pokémon",
        "identifier": "oddish",
        "evolution_chain": 18,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Oddish searches for fertile, nutrient-rich soil, then plants itself.\nDuring the daytime, while it is planted, this Pokémon’s feet\nare thought to change shape and become similar to the roots\nof trees.",
        "has_alt_form": False,
        "id": 43
    },
    {
        "name": "Gloom",
        "genus": "Weed Pokémon",
        "identifier": "gloom",
        "evolution_chain": 18,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 43,
        "type1": 12,
        "type2": 4,
        "flavor_text": "From its mouth Gloom drips honey that smells absolutely\nhorrible. Apparently, it loves the horrid stench. It sniffs the\nnoxious fumes and then drools even more of its honey.",
        "has_alt_form": False,
        "id": 44
    },
    {
        "name": "Vileplume",
        "genus": "Flower Pokémon",
        "identifier": "vileplume",
        "evolution_chain": 18,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 44,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Vileplume has the world’s largest petals. They are used to\nattract prey that are then doused with toxic spores. Once the\nprey are immobilized, this Pokémon catches and devours them.",
        "has_alt_form": False,
        "id": 45
    },
    {
        "name": "Paras",
        "genus": "Mushroom Pokémon",
        "identifier": "paras",
        "evolution_chain": 19,
        "color": "red",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 7,
        "type2": 12,
        "flavor_text": "Whether it’s due to a lack of moisture or a lack\nof nutrients, in Alola the mushrooms on Paras\ndon’t grow up quite right.",
        "has_alt_form": False,
        "id": 46
    },
    {
        "name": "Parasect",
        "genus": "Mushroom Pokémon",
        "identifier": "parasect",
        "evolution_chain": 19,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 46,
        "type1": 7,
        "type2": 12,
        "flavor_text": "The bug is mostly dead, with the mushroom on\nits back having become the main body. If the\nmushroom comes off, the bug stops moving.",
        "has_alt_form": False,
        "id": 47
    },
    {
        "name": "Venonat",
        "genus": "Insect Pokémon",
        "identifier": "venonat",
        "evolution_chain": 20,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Venonat is said to have evolved with a coat of thin, stiff hair\nthat covers its entire body for protection. It possesses large\neyes that never fail to spot even minuscule prey.",
        "has_alt_form": False,
        "id": 48
    },
    {
        "name": "Venomoth",
        "genus": "Poison Moth Pokémon",
        "identifier": "venomoth",
        "evolution_chain": 20,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 48,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Venomoth is nocturnal—it is a Pokémon that only becomes\nactive at night. Its favorite prey are small insects that gather\naround streetlights, attracted by the light in the darkness.",
        "has_alt_form": False,
        "id": 49
    },
    {
        "name": "Diglett",
        "genus": "Mole Pokémon",
        "identifier": "diglett",
        "evolution_chain": 21,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 5,
        "type2": None,
        "flavor_text": "It travels through tunnels that it digs\nunderground. It hates sunlight, so it comes\nout only after the sun goes down.",
        "has_alt_form": False,
        "id": 50
    },
    {
        "name": "Dugtrio",
        "genus": "Mole Pokémon",
        "identifier": "dugtrio",
        "evolution_chain": 21,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 50,
        "type1": 5,
        "type2": None,
        "flavor_text": "While the three of them normally get along\nsplendidly, on rare occasions a huge fight will\nbreak out over which head gets to eat first.",
        "has_alt_form": False,
        "id": 51
    },
    {
        "name": "Meowth",
        "genus": "Scratch Cat Pokémon",
        "identifier": "meowth",
        "evolution_chain": 22,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "When visiting a junkyard, you may catch sight\nof it having an intense fight with Murkrow over\nshiny objects.",
        "has_alt_form": False,
        "id": 52
    },
    {
        "name": "Persian",
        "genus": "Classy Cat Pokémon",
        "identifier": "persian",
        "evolution_chain": 22,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 52,
        "type1": 1,
        "type2": None,
        "flavor_text": "Although the jewel on its forehead appears to\nbe a different color than those of Alolan\nPersian, it’s mostly made of the same material.",
        "has_alt_form": False,
        "id": 53
    },
    {
        "name": "Psyduck",
        "genus": "Duck Pokémon",
        "identifier": "psyduck",
        "evolution_chain": 23,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "Using psychokinesis gives it a headache, so it\nnormally passes the time spacing out and doing\nas little as possible.",
        "has_alt_form": False,
        "id": 54
    },
    {
        "name": "Golduck",
        "genus": "Duck Pokémon",
        "identifier": "golduck",
        "evolution_chain": 23,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 54,
        "type1": 11,
        "type2": None,
        "flavor_text": "Even fast-swimming fish Pokémon can be\ndisabled by Golduck. It brings them to a\nstandstill and seizes them.",
        "has_alt_form": False,
        "id": 55
    },
    {
        "name": "Mankey",
        "genus": "Pig Monkey Pokémon",
        "identifier": "mankey",
        "evolution_chain": 24,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 2,
        "type2": None,
        "flavor_text": "The smallest of things could cause it to lose its\ntemper. Because it doesn’t hold in its stress,\nthis Pokémon can live a long time.",
        "has_alt_form": False,
        "id": 56
    },
    {
        "name": "Primeape",
        "genus": "Pig Monkey Pokémon",
        "identifier": "primeape",
        "evolution_chain": 24,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 56,
        "type1": 2,
        "type2": None,
        "flavor_text": "It will never forgive opponents who have\nangered it. Even after it has beaten them down\nuntil they can’t move, it never ever forgives.",
        "has_alt_form": False,
        "id": 57
    },
    {
        "name": "Growlithe",
        "genus": "Puppy Pokémon",
        "identifier": "growlithe",
        "evolution_chain": 25,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 10,
        "type2": None,
        "flavor_text": "While it’s quite friendly toward humans once it’s\ngrown used to them, in the wild it must be quite\nfierce to defend its territory from Rockruff.",
        "has_alt_form": False,
        "id": 58
    },
    {
        "name": "Arcanine",
        "genus": "Legendary Pokémon",
        "identifier": "arcanine",
        "evolution_chain": 25,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 58,
        "type1": 10,
        "type2": None,
        "flavor_text": "Legends tell of its fighting alongside a general\nand conquering a whole country.",
        "has_alt_form": False,
        "id": 59
    },
    {
        "name": "Poliwag",
        "genus": "Tadpole Pokémon",
        "identifier": "poliwag",
        "evolution_chain": 26,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "Despite the danger, it wants to come up on land.\nSo it does its best to waddle along, but when\nan enemy finds it, it rushes back to the water.",
        "has_alt_form": False,
        "id": 60
    },
    {
        "name": "Poliwhirl",
        "genus": "Tadpole Pokémon",
        "identifier": "poliwhirl",
        "evolution_chain": 26,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 60,
        "type1": 11,
        "type2": None,
        "flavor_text": "Although it has become capable of living on\nland, it spends its time in the water, where\nits prey, fish Pokémon, are plentiful.",
        "has_alt_form": False,
        "id": 61
    },
    {
        "name": "Poliwrath",
        "genus": "Tadpole Pokémon",
        "identifier": "poliwrath",
        "evolution_chain": 26,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 61,
        "type1": 11,
        "type2": 2,
        "flavor_text": "It’s quite a gifted swimmer, even among\nWater-type Pokémon, but it normally spends its\ntime on land.",
        "has_alt_form": False,
        "id": 62
    },
    {
        "name": "Abra",
        "genus": "Psi Pokémon",
        "identifier": "abra",
        "evolution_chain": 27,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 14,
        "type2": None,
        "flavor_text": "It uses various psychic powers even while it’s\nsleeping, so you can’t tell whether or not\nit’s awake.",
        "has_alt_form": False,
        "id": 63
    },
    {
        "name": "Kadabra",
        "genus": "Psi Pokémon",
        "identifier": "kadabra",
        "evolution_chain": 27,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 63,
        "type1": 14,
        "type2": None,
        "flavor_text": "It stares at a silver spoon to amplify its psychic\npowers before it lets loose. Apparently, gold\nspoons are no good.",
        "has_alt_form": False,
        "id": 64
    },
    {
        "name": "Alakazam",
        "genus": "Psi Pokémon",
        "identifier": "alakazam",
        "evolution_chain": 27,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 64,
        "type1": 14,
        "type2": None,
        "flavor_text": "Alakazam uses its psychic powers to make the\nspoons it carries. Each spoon is an original that\nthere’s only one of in the whole world.",
        "has_alt_form": False,
        "id": 65
    },
    {
        "name": "Machop",
        "genus": "Superpower Pokémon",
        "identifier": "machop",
        "evolution_chain": 28,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 2,
        "type2": None,
        "flavor_text": "Once this Pokémon has gained enough\nconfidence and muscle from training with its\nfriends, it challenges Makuhita to a battle.",
        "has_alt_form": False,
        "id": 66
    },
    {
        "name": "Machoke",
        "genus": "Superpower Pokémon",
        "identifier": "machoke",
        "evolution_chain": 28,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": 66,
        "type1": 2,
        "type2": None,
        "flavor_text": "When it encounters an enemy that’s truly\nmighty, this Pokémon removes the power-save\nbelt from its waist and unleashes its full power.",
        "has_alt_form": False,
        "id": 67
    },
    {
        "name": "Machamp",
        "genus": "Superpower Pokémon",
        "identifier": "machamp",
        "evolution_chain": 28,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": 67,
        "type1": 2,
        "type2": None,
        "flavor_text": "It grasps its opponents with its four arms and\ntwists them up in an intricate hold. People call\nit “the Machamp special.”",
        "has_alt_form": False,
        "id": 68
    },
    {
        "name": "Bellsprout",
        "genus": "Flower Pokémon",
        "identifier": "bellsprout",
        "evolution_chain": 29,
        "color": "green",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Bellsprout’s thin and flexible body lets it bend and sway\nto avoid any attack, however strong it may be. From its mouth,\nthis Pokémon spits a corrosive fluid that melts even iron.",
        "has_alt_form": False,
        "id": 69
    },
    {
        "name": "Weepinbell",
        "genus": "Flycatcher Pokémon",
        "identifier": "weepinbell",
        "evolution_chain": 29,
        "color": "green",
        "since_gen": 1,
        "evolves_from": 69,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Weepinbell has a large hook on its rear end. At night, the\nPokémon hooks on to a tree branch and goes to sleep.\nIf it moves around in its sleep, it may wake up to find itself\non the ground.",
        "has_alt_form": False,
        "id": 70
    },
    {
        "name": "Victreebel",
        "genus": "Flycatcher Pokémon",
        "identifier": "victreebel",
        "evolution_chain": 29,
        "color": "green",
        "since_gen": 1,
        "evolves_from": 70,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Victreebel has a long vine that extends from its head.\nThis vine is waved and flicked about as if it were an animal\nto attract prey. When an unsuspecting prey draws near,\nthis Pokémon swallows it whole.",
        "has_alt_form": False,
        "id": 71
    },
    {
        "name": "Tentacool",
        "genus": "Jellyfish Pokémon",
        "identifier": "tentacool",
        "evolution_chain": 30,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": 4,
        "flavor_text": "It drifts through the sea searching for prey.\nIts poisonous tentacles break off sometimes,\nbut after a while, they grow back.",
        "has_alt_form": False,
        "id": 72
    },
    {
        "name": "Tentacruel",
        "genus": "Jellyfish Pokémon",
        "identifier": "tentacruel",
        "evolution_chain": 30,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 72,
        "type1": 11,
        "type2": 4,
        "flavor_text": "It fires off ultrasonic waves from its red orbs\nto weaken its prey, and then it wraps them up\nin its 80 tentacles.",
        "has_alt_form": False,
        "id": 73
    },
    {
        "name": "Geodude",
        "genus": "Rock Pokémon",
        "identifier": "geodude",
        "evolution_chain": 31,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 6,
        "type2": 5,
        "flavor_text": "Geodude that have lived a long life have had all\ntheir edges smoothed out until they’re totally\nround. They also have a calm, quiet disposition.",
        "has_alt_form": False,
        "id": 74
    },
    {
        "name": "Graveler",
        "genus": "Rock Pokémon",
        "identifier": "graveler",
        "evolution_chain": 31,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 74,
        "type1": 6,
        "type2": 5,
        "flavor_text": "It climbs up cliffs as it heads toward the peak\nof a mountain. As soon as it reaches the summit,\nit rolls back down the way it came.",
        "has_alt_form": False,
        "id": 75
    },
    {
        "name": "Golem",
        "genus": "Megaton Pokémon",
        "identifier": "golem",
        "evolution_chain": 31,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 75,
        "type1": 6,
        "type2": 5,
        "flavor_text": "When Golem grow old, they stop shedding their\nshells. Those that have lived a long, long time\nhave shells green with moss.",
        "has_alt_form": False,
        "id": 76
    },
    {
        "name": "Ponyta",
        "genus": "Fire Horse Pokémon",
        "identifier": "ponyta",
        "evolution_chain": 32,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 10,
        "type2": None,
        "flavor_text": "Ponyta is very weak at birth. It can barely stand up.\nThis Pokémon becomes stronger by stumbling and\nfalling to keep up with its parent.",
        "has_alt_form": False,
        "id": 77
    },
    {
        "name": "Rapidash",
        "genus": "Fire Horse Pokémon",
        "identifier": "rapidash",
        "evolution_chain": 32,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 77,
        "type1": 10,
        "type2": None,
        "flavor_text": "Rapidash usually can be seen casually cantering in the fields\nand plains. However, when this Pokémon turns serious, its\nfiery manes flare and blaze as it gallops its way up to 150 mph.",
        "has_alt_form": False,
        "id": 78
    },
    {
        "name": "Slowpoke",
        "genus": "Dopey Pokémon",
        "identifier": "slowpoke",
        "evolution_chain": 33,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": 14,
        "flavor_text": "There are some places where Slowpoke is\nworshiped because of a long-standing belief\nthat whenever Slowpoke yawns, it rains.",
        "has_alt_form": False,
        "id": 79
    },
    {
        "name": "Slowbro",
        "genus": "Hermit Crab Pokémon",
        "identifier": "slowbro",
        "evolution_chain": 33,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 79,
        "type1": 11,
        "type2": 14,
        "flavor_text": "Spacing out is basically all it does. It turns back\ninto Slowpoke if its tail, along with Shellder,\nbreaks off.",
        "has_alt_form": False,
        "id": 80
    },
    {
        "name": "Magnemite",
        "genus": "Magnet Pokémon",
        "identifier": "magnemite",
        "evolution_chain": 34,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 13,
        "type2": 9,
        "flavor_text": "It’s frequently the cause of power outages,\nwhich is why some power plants send out\nelectrical signals that it can’t stand.",
        "has_alt_form": False,
        "id": 81
    },
    {
        "name": "Magneton",
        "genus": "Magnet Pokémon",
        "identifier": "magneton",
        "evolution_chain": 34,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": 81,
        "type1": 13,
        "type2": 9,
        "flavor_text": "Delicate equipment can malfunction in areas\ninhabited by Magneton, which send out\nmysterious electrical signals.",
        "has_alt_form": False,
        "id": 82
    },
    {
        "name": "Farfetch’d",
        "genus": "Wild Duck Pokémon",
        "identifier": "farfetchd",
        "evolution_chain": 35,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Farfetch’d is always seen with a stalk from a plant of some\nsort. Apparently, there are good stalks and bad stalks. This\nPokémon has been known to fight with others over stalks.",
        "has_alt_form": False,
        "id": 83
    },
    {
        "name": "Doduo",
        "genus": "Twin Bird Pokémon",
        "identifier": "doduo",
        "evolution_chain": 36,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Doduo’s two heads contain completely identical brains. A\nscientific study reported that on rare occasions, there will be\nexamples of this Pokémon possessing different sets of brains.",
        "has_alt_form": False,
        "id": 84
    },
    {
        "name": "Dodrio",
        "genus": "Triple Bird Pokémon",
        "identifier": "dodrio",
        "evolution_chain": 36,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 84,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Apparently, the heads aren’t the only parts of the body that\nDodrio has three of. It has three sets of hearts and lungs as\nwell, so it is capable of running long distances without rest.",
        "has_alt_form": False,
        "id": 85
    },
    {
        "name": "Seel",
        "genus": "Sea Lion Pokémon",
        "identifier": "seel",
        "evolution_chain": 37,
        "color": "white",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "It has always been supposed that Seel live only\nin cold seas. Their having shown up in Alola is\na mystery.",
        "has_alt_form": False,
        "id": 86
    },
    {
        "name": "Dewgong",
        "genus": "Sea Lion Pokémon",
        "identifier": "dewgong",
        "evolution_chain": 37,
        "color": "white",
        "since_gen": 1,
        "evolves_from": 86,
        "type1": 11,
        "type2": 15,
        "flavor_text": "It swims through the ocean at a speed of eight\nknots, searching for Pokémon that will become\nits prey. It’s especially fond of Wishiwashi.",
        "has_alt_form": False,
        "id": 87
    },
    {
        "name": "Grimer",
        "genus": "Sludge Pokémon",
        "identifier": "grimer",
        "evolution_chain": 38,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 4,
        "type2": None,
        "flavor_text": "It was born from sludge on the ocean floor. In a\nsterile environment, the germs within its body\ncan’t multiply, and it dies.",
        "has_alt_form": False,
        "id": 88
    },
    {
        "name": "Muk",
        "genus": "Sludge Pokémon",
        "identifier": "muk",
        "evolution_chain": 38,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 88,
        "type1": 4,
        "type2": None,
        "flavor_text": "Their food sources have decreased, and their\nnumbers have declined sharply. Sludge ponds\nare being built to prevent their extinction.",
        "has_alt_form": False,
        "id": 89
    },
    {
        "name": "Shellder",
        "genus": "Bivalve Pokémon",
        "identifier": "shellder",
        "evolution_chain": 39,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "The sand that accumulates inside its shell\neventually becomes a pearl. But the pearl gets\nin the way, so it spits it out and discards it.",
        "has_alt_form": False,
        "id": 90
    },
    {
        "name": "Cloyster",
        "genus": "Bivalve Pokémon",
        "identifier": "cloyster",
        "evolution_chain": 39,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 90,
        "type1": 11,
        "type2": 15,
        "flavor_text": "If areas of Cloyster’s very hard shell get\ndamaged, those areas swell, gradually growing\ninto large sharp spikes.",
        "has_alt_form": False,
        "id": 91
    },
    {
        "name": "Gastly",
        "genus": "Gas Pokémon",
        "identifier": "gastly",
        "evolution_chain": 40,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 8,
        "type2": 4,
        "flavor_text": "It’s said that gas emanating from a graveyard\nwas possessed by the grievances of the\ndeceased and thus became a Pokémon.",
        "has_alt_form": False,
        "id": 92
    },
    {
        "name": "Haunter",
        "genus": "Gas Pokémon",
        "identifier": "haunter",
        "evolution_chain": 40,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 92,
        "type1": 8,
        "type2": 4,
        "flavor_text": "On moonless nights, Haunter searches for\nsomeone to curse, so it’s best not to go out\nwalking around.",
        "has_alt_form": False,
        "id": 93
    },
    {
        "name": "Gengar",
        "genus": "Shadow Pokémon",
        "identifier": "gengar",
        "evolution_chain": 40,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 93,
        "type1": 8,
        "type2": 4,
        "flavor_text": "You can hear tales told all over the world about\nhow Gengar will pay a visit to children who\nare naughty.",
        "has_alt_form": False,
        "id": 94
    },
    {
        "name": "Onix",
        "genus": "Rock Snake Pokémon",
        "identifier": "onix",
        "evolution_chain": 41,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 6,
        "type2": 5,
        "flavor_text": "Onix has a magnet in its brain. It acts as a compass so that\nthis Pokémon does not lose direction while it is tunneling.\nAs it grows older, its body becomes increasingly rounder\nand smoother.",
        "has_alt_form": False,
        "id": 95
    },
    {
        "name": "Drowzee",
        "genus": "Hypnosis Pokémon",
        "identifier": "drowzee",
        "evolution_chain": 42,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 14,
        "type2": None,
        "flavor_text": "It can be spotted near recreational facilities,\nintending to eat the pleasant dreams of children\nwho enjoyed themselves there that day.",
        "has_alt_form": False,
        "id": 96
    },
    {
        "name": "Hypno",
        "genus": "Hypnosis Pokémon",
        "identifier": "hypno",
        "evolution_chain": 42,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 96,
        "type1": 14,
        "type2": None,
        "flavor_text": "In Alola, Komala is Hypno’s main target. It rarely\nharms people.",
        "has_alt_form": False,
        "id": 97
    },
    {
        "name": "Krabby",
        "genus": "River Crab Pokémon",
        "identifier": "krabby",
        "evolution_chain": 43,
        "color": "red",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "Krabby live on beaches, burrowed inside holes dug into\nthe sand. On sandy beaches with little in the way of food,\nthese Pokémon can be seen squabbling with each other\nover territory.",
        "has_alt_form": False,
        "id": 98
    },
    {
        "name": "Kingler",
        "genus": "Pincer Pokémon",
        "identifier": "kingler",
        "evolution_chain": 43,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 98,
        "type1": 11,
        "type2": None,
        "flavor_text": "Kingler has an enormous, oversized claw. It waves this huge\nclaw in the air to communicate with others. However, because\nthe claw is so heavy, the Pokémon quickly tires.",
        "has_alt_form": False,
        "id": 99
    },
    {
        "name": "Voltorb",
        "genus": "Ball Pokémon",
        "identifier": "voltorb",
        "evolution_chain": 44,
        "color": "red",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 13,
        "type2": None,
        "flavor_text": "Voltorb is extremely sensitive—it explodes at the slightest\nof shocks. It is rumored that it was first created when a\nPoké Ball was exposed to a powerful pulse of energy.",
        "has_alt_form": False,
        "id": 100
    },
    {
        "name": "Electrode",
        "genus": "Ball Pokémon",
        "identifier": "electrode",
        "evolution_chain": 44,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 100,
        "type1": 13,
        "type2": None,
        "flavor_text": "One of Electrode’s characteristics is its attraction to electricity.\nIt is a problematical Pokémon that congregates mostly at\nelectrical power plants to feed on electricity that has just\nbeen generated.",
        "has_alt_form": False,
        "id": 101
    },
    {
        "name": "Exeggcute",
        "genus": "Egg Pokémon",
        "identifier": "exeggcute",
        "evolution_chain": 45,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 12,
        "type2": 14,
        "flavor_text": "Six of them form a single Pokémon. Should one\nof the six be lost, the next morning there will\nonce more be six.",
        "has_alt_form": False,
        "id": 102
    },
    {
        "name": "Exeggutor",
        "genus": "Coconut Pokémon",
        "identifier": "exeggutor",
        "evolution_chain": 45,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 102,
        "type1": 12,
        "type2": 14,
        "flavor_text": "It engages its enemies using psychic powers.\nEach of its three heads fires off psychokinetic\nenergy, tripling its power.",
        "has_alt_form": False,
        "id": 103
    },
    {
        "name": "Cubone",
        "genus": "Lonely Pokémon",
        "identifier": "cubone",
        "evolution_chain": 46,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 5,
        "type2": None,
        "flavor_text": "At night, it weeps loudly for its dead mother,\nbut those cries only attract its natural\nenemy—Mandibuzz.",
        "has_alt_form": False,
        "id": 104
    },
    {
        "name": "Marowak",
        "genus": "Bone Keeper Pokémon",
        "identifier": "marowak",
        "evolution_chain": 46,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 104,
        "type1": 5,
        "type2": None,
        "flavor_text": "It throws bones at Mandibuzz to knock it down.\nIt’s thought that Marowak is trying to avenge\nits parent.",
        "has_alt_form": False,
        "id": 105
    },
    {
        "name": "Hitmonlee",
        "genus": "Kicking Pokémon",
        "identifier": "hitmonlee",
        "evolution_chain": 47,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 236,
        "type1": 2,
        "type2": None,
        "flavor_text": "Hitmonlee’s legs freely contract and stretch. Using these\nspringlike legs, it bowls over foes with devastating kicks.\nAfter battle, it rubs down its legs and loosens the muscles\nto overcome fatigue.",
        "has_alt_form": False,
        "id": 106
    },
    {
        "name": "Hitmonchan",
        "genus": "Punching Pokémon",
        "identifier": "hitmonchan",
        "evolution_chain": 47,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 236,
        "type1": 2,
        "type2": None,
        "flavor_text": "Hitmonchan is said to possess the spirit of a boxer who had\nbeen working toward a world championship. This Pokémon\nhas an indomitable spirit and will never give up in the face\nof adversity.",
        "has_alt_form": False,
        "id": 107
    },
    {
        "name": "Lickitung",
        "genus": "Licking Pokémon",
        "identifier": "lickitung",
        "evolution_chain": 48,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "It checks out whatever’s around it by licking\neverything. If you don’t clean off a spot where\nit’s licked you, you’ll break out in a rash!",
        "has_alt_form": False,
        "id": 108
    },
    {
        "name": "Koffing",
        "genus": "Poison Gas Pokémon",
        "identifier": "koffing",
        "evolution_chain": 49,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 4,
        "type2": None,
        "flavor_text": "Koffing embodies toxic substances. It mixes the toxins with raw\ngarbage to set off a chemical reaction that results in a terribly\npowerful poison gas. The higher the temperature, the more gas\nis concocted by this Pokémon.",
        "has_alt_form": False,
        "id": 109
    },
    {
        "name": "Weezing",
        "genus": "Poison Gas Pokémon",
        "identifier": "weezing",
        "evolution_chain": 49,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 109,
        "type1": 4,
        "type2": None,
        "flavor_text": "Weezing alternately shrinks and inflates its twin bodies to mix\ntogether toxic gases inside. The more the gases are mixed,\nthe more powerful the toxins become. The Pokémon also\nbecomes more putrid.",
        "has_alt_form": False,
        "id": 110
    },
    {
        "name": "Rhyhorn",
        "genus": "Spikes Pokémon",
        "identifier": "rhyhorn",
        "evolution_chain": 50,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 5,
        "type2": 6,
        "flavor_text": "Rhyhorn’s brain is very small. It is so dense, while on a run\nit forgets why it started running in the first place. It apparently\nremembers sometimes if it demolishes something.",
        "has_alt_form": False,
        "id": 111
    },
    {
        "name": "Rhydon",
        "genus": "Drill Pokémon",
        "identifier": "rhydon",
        "evolution_chain": 50,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": 111,
        "type1": 5,
        "type2": 6,
        "flavor_text": "Rhydon has a horn that serves as a drill. It is used for\ndestroying rocks and boulders. This Pokémon occasionally\nrams into streams of magma, but the armor-like hide prevents\nit from feeling the heat.",
        "has_alt_form": False,
        "id": 112
    },
    {
        "name": "Chansey",
        "genus": "Egg Pokémon",
        "identifier": "chansey",
        "evolution_chain": 51,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 440,
        "type1": 1,
        "type2": None,
        "flavor_text": "It seems that other Pokémon’s efforts to take\nits delicious, nutritious egg away from it caused\nChansey to get faster at fleeing.",
        "has_alt_form": False,
        "id": 113
    },
    {
        "name": "Tangela",
        "genus": "Vine Pokémon",
        "identifier": "tangela",
        "evolution_chain": 52,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 12,
        "type2": None,
        "flavor_text": "Tangela’s vines snap off easily if they are grabbed. This\nhappens without pain, allowing it to make a quick getaway.\nThe lost vines are replaced by newly grown vines the very\nnext day.",
        "has_alt_form": False,
        "id": 114
    },
    {
        "name": "Kangaskhan",
        "genus": "Parent Pokémon",
        "identifier": "kangaskhan",
        "evolution_chain": 53,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "Kangaskhan protects its child by keeping it in\nits pouch. It has zero forgiveness for those\nwho harm its child and will beat them down.",
        "has_alt_form": False,
        "id": 115
    },
    {
        "name": "Horsea",
        "genus": "Dragon Pokémon",
        "identifier": "horsea",
        "evolution_chain": 54,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "If Horsea senses danger, it will reflexively spray a dense\nblack ink from its mouth and try to escape. This Pokémon\nswims by cleverly flapping the fin on its back.",
        "has_alt_form": False,
        "id": 116
    },
    {
        "name": "Seadra",
        "genus": "Dragon Pokémon",
        "identifier": "seadra",
        "evolution_chain": 54,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 116,
        "type1": 11,
        "type2": None,
        "flavor_text": "Seadra generates whirlpools by spinning its body.\nThe whirlpools are strong enough to swallow even\nfishing boats. This Pokémon weakens prey with\nthese currents, then swallows it whole.",
        "has_alt_form": False,
        "id": 117
    },
    {
        "name": "Goldeen",
        "genus": "Goldfish Pokémon",
        "identifier": "goldeen",
        "evolution_chain": 55,
        "color": "red",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "Although known for their splendid tail fins,\nGoldeen apparently compete among themselves\nto see whose horn is thickest and sharpest.",
        "has_alt_form": False,
        "id": 118
    },
    {
        "name": "Seaking",
        "genus": "Goldfish Pokémon",
        "identifier": "seaking",
        "evolution_chain": 55,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 118,
        "type1": 11,
        "type2": None,
        "flavor_text": "Its horn spins like a drill to steadily hollow out\nrocks—even harder ones. The coloration of the\nmale is more vivid.",
        "has_alt_form": False,
        "id": 119
    },
    {
        "name": "Staryu",
        "genus": "Star Shape Pokémon",
        "identifier": "staryu",
        "evolution_chain": 56,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "In many places, there are folktales of stardust\nfalling into the ocean and becoming Staryu.",
        "has_alt_form": False,
        "id": 120
    },
    {
        "name": "Starmie",
        "genus": "Mysterious Pokémon",
        "identifier": "starmie",
        "evolution_chain": 56,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": 120,
        "type1": 11,
        "type2": 14,
        "flavor_text": "Its sparkling core is called “the gem of the sea.”\nThis core can be made into high-priced\naccessories that are traded in secret.",
        "has_alt_form": False,
        "id": 121
    },
    {
        "name": "Mr. Mime",
        "genus": "Barrier Pokémon",
        "identifier": "mr-mime",
        "evolution_chain": 57,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": 439,
        "type1": 14,
        "type2": 18,
        "flavor_text": "Its pantomime skills are wonderful. You may\nbecome enraptured while watching it, but next\nthing you know, Mr. Mime has made a real wall.",
        "has_alt_form": False,
        "id": 122
    },
    {
        "name": "Scyther",
        "genus": "Mantis Pokémon",
        "identifier": "scyther",
        "evolution_chain": 58,
        "color": "green",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Its two sharp scythes are more than just\nweapons. It uses them with dexterity to dress\nits prey before eating.",
        "has_alt_form": False,
        "id": 123
    },
    {
        "name": "Jynx",
        "genus": "Human Shape Pokémon",
        "identifier": "jynx",
        "evolution_chain": 59,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 238,
        "type1": 15,
        "type2": 14,
        "flavor_text": "It sways its hips to a rhythm all its own. The\nprecise movements of Jynx living in Alola are\ntruly wonderful.",
        "has_alt_form": False,
        "id": 124
    },
    {
        "name": "Electabuzz",
        "genus": "Electric Pokémon",
        "identifier": "electabuzz",
        "evolution_chain": 60,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 239,
        "type1": 13,
        "type2": None,
        "flavor_text": "Electricity permeates its body. It swings\nits arms round and round to charge up\nelectricity before unleashing a punch.",
        "has_alt_form": False,
        "id": 125
    },
    {
        "name": "Magmar",
        "genus": "Spitfire Pokémon",
        "identifier": "magmar",
        "evolution_chain": 61,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 240,
        "type1": 10,
        "type2": None,
        "flavor_text": "Its entire body is burning. When it breathes,\nthe temperature rises. When it sneezes, flames\nshoot out!",
        "has_alt_form": False,
        "id": 126
    },
    {
        "name": "Pinsir",
        "genus": "Stag Beetle Pokémon",
        "identifier": "pinsir",
        "evolution_chain": 62,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 7,
        "type2": None,
        "flavor_text": "It gets into territorial disputes with Vikavolt.\nFor some reason, it apparently gets along well\nwith Heracross in Alola.",
        "has_alt_form": False,
        "id": 127
    },
    {
        "name": "Tauros",
        "genus": "Wild Bull Pokémon",
        "identifier": "tauros",
        "evolution_chain": 63,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "They live in groups. The one with the longest,\nthickest, and most-scarred horns is the boss\nof the herd.",
        "has_alt_form": False,
        "id": 128
    },
    {
        "name": "Magikarp",
        "genus": "Fish Pokémon",
        "identifier": "magikarp",
        "evolution_chain": 64,
        "color": "red",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": None,
        "flavor_text": "In the distant past, they were fairly strong, but\nthey have become gradually weaker over time.",
        "has_alt_form": False,
        "id": 129
    },
    {
        "name": "Gyarados",
        "genus": "Atrocious Pokémon",
        "identifier": "gyarados",
        "evolution_chain": 64,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 129,
        "type1": 11,
        "type2": 3,
        "flavor_text": "It fires hyper beams in all directions, burning the\nsurrounding area to ash. There are some regions\nwhere it’s called “the deity of destruction.”",
        "has_alt_form": False,
        "id": 130
    },
    {
        "name": "Lapras",
        "genus": "Transport Pokémon",
        "identifier": "lapras",
        "evolution_chain": 65,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 11,
        "type2": 15,
        "flavor_text": "It likes swimming around with people on its\nback. In the Alola region, it’s an important means\nof transportation over water.",
        "has_alt_form": False,
        "id": 131
    },
    {
        "name": "Ditto",
        "genus": "Transform Pokémon",
        "identifier": "ditto",
        "evolution_chain": 66,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "While it can transform into anything, each Ditto\napparently has its own strengths and\nweaknesses when it comes to transformations.",
        "has_alt_form": False,
        "id": 132
    },
    {
        "name": "Eevee",
        "genus": "Evolution Pokémon",
        "identifier": "eevee",
        "evolution_chain": 67,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "The question of why only Eevee has such\nunstable genes has still not been solved.",
        "has_alt_form": False,
        "id": 133
    },
    {
        "name": "Vaporeon",
        "genus": "Bubble Jet Pokémon",
        "identifier": "vaporeon",
        "evolution_chain": 67,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 133,
        "type1": 11,
        "type2": None,
        "flavor_text": "Clean, clear waters are its usual habitat. When\nit’s about to be attacked by an invading enemy,\nit dives into the water to hide.",
        "has_alt_form": False,
        "id": 134
    },
    {
        "name": "Jolteon",
        "genus": "Lightning Pokémon",
        "identifier": "jolteon",
        "evolution_chain": 67,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": 133,
        "type1": 13,
        "type2": None,
        "flavor_text": "Its lungs contain an organ that creates\nelectricity. The crackling sound of electricity\ncan be heard when it exhales.",
        "has_alt_form": False,
        "id": 135
    },
    {
        "name": "Flareon",
        "genus": "Flame Pokémon",
        "identifier": "flareon",
        "evolution_chain": 67,
        "color": "red",
        "since_gen": 1,
        "evolves_from": 133,
        "type1": 10,
        "type2": None,
        "flavor_text": "If it inhales deeply, that’s a sign it’s about to\nattack. Prepare to be hit by flames of over\n3,000 degrees Fahrenheit!",
        "has_alt_form": False,
        "id": 136
    },
    {
        "name": "Porygon",
        "genus": "Virtual Pokémon",
        "identifier": "porygon",
        "evolution_chain": 68,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 1,
        "type2": None,
        "flavor_text": "This Pokémon was created using the\ncutting-edge science of 20 years ago, so\nmany parts of it have since become obsolete.",
        "has_alt_form": False,
        "id": 137
    },
    {
        "name": "Omanyte",
        "genus": "Spiral Pokémon",
        "identifier": "omanyte",
        "evolution_chain": 69,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 6,
        "type2": 11,
        "flavor_text": "Omanyte lived in the seas of antiquity. Its\nfossils have been found bearing bite marks from\nArcheops, so apparently Archeops preyed on it.",
        "has_alt_form": False,
        "id": 138
    },
    {
        "name": "Omastar",
        "genus": "Spiral Pokémon",
        "identifier": "omastar",
        "evolution_chain": 69,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 138,
        "type1": 6,
        "type2": 11,
        "flavor_text": "Its heavy shell is thought to be the reason this\nancient Pokémon died out. It’s apparently a\ndistant ancestor of Octillery.",
        "has_alt_form": False,
        "id": 139
    },
    {
        "name": "Kabuto",
        "genus": "Shellfish Pokémon",
        "identifier": "kabuto",
        "evolution_chain": 70,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 6,
        "type2": 11,
        "flavor_text": "This Pokémon thrived 300 million years ago. It’s\nsaid that living specimens can still be seen\nin a certain region—a rare sight.",
        "has_alt_form": False,
        "id": 140
    },
    {
        "name": "Kabutops",
        "genus": "Shellfish Pokémon",
        "identifier": "kabutops",
        "evolution_chain": 70,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 140,
        "type1": 6,
        "type2": 11,
        "flavor_text": "Its body had begun to change so it could\nfunction on land. But it didn’t adapt in time and\nwent extinct.",
        "has_alt_form": False,
        "id": 141
    },
    {
        "name": "Aerodactyl",
        "genus": "Fossil Pokémon",
        "identifier": "aerodactyl",
        "evolution_chain": 71,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 6,
        "type2": 3,
        "flavor_text": "Restored from DNA found in amber, this\nPokémon exhibited ferocity that was greater\nthan expected. Some casualties resulted.",
        "has_alt_form": False,
        "id": 142
    },
    {
        "name": "Snorlax",
        "genus": "Sleeping Pokémon",
        "identifier": "snorlax",
        "evolution_chain": 72,
        "color": "black",
        "since_gen": 1,
        "evolves_from": 446,
        "type1": 1,
        "type2": None,
        "flavor_text": "It doesn’t do anything other than eat and sleep.\nWhen prompted to make a serious effort,\nthough, it apparently displays awesome power.",
        "has_alt_form": False,
        "id": 143
    },
    {
        "name": "Articuno",
        "genus": "Freeze Pokémon",
        "identifier": "articuno",
        "evolution_chain": 73,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 15,
        "type2": 3,
        "flavor_text": "Articuno is a legendary bird Pokémon that can control ice.\nThe flapping of its wings chills the air. As a result, it is said\nthat when this Pokémon flies, snow will fall.",
        "has_alt_form": False,
        "id": 144
    },
    {
        "name": "Zapdos",
        "genus": "Electric Pokémon",
        "identifier": "zapdos",
        "evolution_chain": 74,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 13,
        "type2": 3,
        "flavor_text": "Zapdos is a legendary bird Pokémon that has the ability\nto control electricity. It usually lives in thunderclouds.\nThe Pokémon gains power if it is stricken by lightning bolts.",
        "has_alt_form": False,
        "id": 145
    },
    {
        "name": "Moltres",
        "genus": "Flame Pokémon",
        "identifier": "moltres",
        "evolution_chain": 75,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 10,
        "type2": 3,
        "flavor_text": "Moltres is a legendary bird Pokémon that has the ability\nto control fire. If this Pokémon is injured, it is said to dip its\nbody in the molten magma of a volcano to burn and heal itself.",
        "has_alt_form": False,
        "id": 146
    },
    {
        "name": "Dratini",
        "genus": "Dragon Pokémon",
        "identifier": "dratini",
        "evolution_chain": 76,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 16,
        "type2": None,
        "flavor_text": "It’s still weak, so it lurks on the floor of bodies\nof water, eating whatever food sinks down and\nliving a quiet life.",
        "has_alt_form": False,
        "id": 147
    },
    {
        "name": "Dragonair",
        "genus": "Dragon Pokémon",
        "identifier": "dragonair",
        "evolution_chain": 76,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": 147,
        "type1": 16,
        "type2": None,
        "flavor_text": "Lakes where Dragonair live are filled with\nofferings from people, because they believe this\nPokémon is able to control the weather.",
        "has_alt_form": False,
        "id": 148
    },
    {
        "name": "Dragonite",
        "genus": "Dragon Pokémon",
        "identifier": "dragonite",
        "evolution_chain": 76,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": 148,
        "type1": 16,
        "type2": 3,
        "flavor_text": "It flies over raging seas as if they were nothing.\nObserving this, a ship’s captain dubbed this\nPokémon “the sea incarnate.”",
        "has_alt_form": False,
        "id": 149
    },
    {
        "name": "Mewtwo",
        "genus": "Genetic Pokémon",
        "identifier": "mewtwo",
        "evolution_chain": 77,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 14,
        "type2": None,
        "flavor_text": "Mewtwo is a Pokémon that was created by genetic\nmanipulation. However, even though the scientific power\nof humans created this Pokémon’s body, they failed to\nendow Mewtwo with a compassionate heart.",
        "has_alt_form": False,
        "id": 150
    },
    {
        "name": "Mew",
        "genus": "New Species Pokémon",
        "identifier": "mew",
        "evolution_chain": 78,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": None,
        "type1": 14,
        "type2": None,
        "flavor_text": "Mew is said to possess the genetic composition of all\nPokémon. It is capable of making itself invisible at will,\nso it entirely avoids notice even if it approaches people.",
        "has_alt_form": False,
        "id": 151
    }
]

EVOLUTION = [
    {
        "evolves_from": 1,
        "chain": 1,
        "trigger": "level-up",
        "level": 16,
        "id": 1
    },
    {
        "evolves_from": 2,
        "chain": 1,
        "trigger": "level-up",
        "level": 32,
        "id": 2
    },
    {
        "evolves_from": 4,
        "chain": 2,
        "trigger": "level-up",
        "level": 16,
        "id": 3
    },
    {
        "evolves_from": 5,
        "chain": 2,
        "trigger": "level-up",
        "level": 36,
        "id": 4
    },
    {
        "evolves_from": 7,
        "chain": 3,
        "trigger": "level-up",
        "level": 16,
        "id": 5
    },
    {
        "evolves_from": 8,
        "chain": 3,
        "trigger": "level-up",
        "level": 36,
        "id": 6
    },
    {
        "evolves_from": 10,
        "chain": 4,
        "trigger": "level-up",
        "level": 7,
        "id": 7
    },
    {
        "evolves_from": 11,
        "chain": 4,
        "trigger": "level-up",
        "level": 10,
        "id": 8
    },
    {
        "evolves_from": 13,
        "chain": 5,
        "trigger": "level-up",
        "level": 7,
        "id": 9
    },
    {
        "evolves_from": 14,
        "chain": 5,
        "trigger": "level-up",
        "level": 10,
        "id": 10
    },
    {
        "evolves_from": 16,
        "chain": 6,
        "trigger": "level-up",
        "level": 18,
        "id": 11
    },
    {
        "evolves_from": 17,
        "chain": 6,
        "trigger": "level-up",
        "level": 36,
        "id": 12
    },
    {
        "evolves_from": 19,
        "chain": 7,
        "trigger": "level-up",
        "level": 20,
        "id": 13
    },
    {
        "evolves_from": 21,
        "chain": 8,
        "trigger": "level-up",
        "level": 20,
        "id": 14
    },
    {
        "evolves_from": 23,
        "chain": 9,
        "trigger": "level-up",
        "level": 22,
        "id": 15
    },
    {
        "evolves_from": 172,
        "chain": 10,
        "trigger": "level-up",
        "happiness": 220,
        "id": 16
    },
    {
        "evolves_from": 25,
        "chain": 10,
        "trigger": "use-item",
        "trigger_item": "thunder-stone",
        "id": 17
    },
    {
        "evolves_from": 27,
        "chain": 11,
        "trigger": "level-up",
        "level": 22,
        "id": 18
    },
    {
        "evolves_from": 29,
        "chain": 12,
        "trigger": "level-up",
        "level": 16,
        "id": 19
    },
    {
        "evolves_from": 30,
        "chain": 12,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 20
    },
    {
        "evolves_from": 32,
        "chain": 13,
        "trigger": "level-up",
        "level": 16,
        "id": 21
    },
    {
        "evolves_from": 33,
        "chain": 13,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 22
    },
    {
        "evolves_from": 173,
        "chain": 14,
        "trigger": "level-up",
        "happiness": 220,
        "id": 23
    },
    {
        "evolves_from": 35,
        "chain": 14,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 24
    },
    {
        "evolves_from": 37,
        "chain": 15,
        "trigger": "use-item",
        "trigger_item": "fire-stone",
        "id": 25
    },
    {
        "evolves_from": 174,
        "chain": 16,
        "trigger": "level-up",
        "happiness": 220,
        "id": 26
    },
    {
        "evolves_from": 39,
        "chain": 16,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 27
    },
    {
        "evolves_from": 41,
        "chain": 17,
        "trigger": "level-up",
        "level": 22,
        "id": 28
    },
    {
        "evolves_from": 43,
        "chain": 18,
        "trigger": "level-up",
        "level": 21,
        "id": 29
    },
    {
        "evolves_from": 44,
        "chain": 18,
        "trigger": "use-item",
        "trigger_item": "leaf-stone",
        "id": 30
    },
    {
        "evolves_from": 46,
        "chain": 19,
        "trigger": "level-up",
        "level": 24,
        "id": 31
    },
    {
        "evolves_from": 48,
        "chain": 20,
        "trigger": "level-up",
        "level": 31,
        "id": 32
    },
    {
        "evolves_from": 50,
        "chain": 21,
        "trigger": "level-up",
        "level": 26,
        "id": 33
    },
    {
        "evolves_from": 52,
        "chain": 22,
        "trigger": "level-up",
        "level": 28,
        "id": 34
    },
    {
        "evolves_from": 54,
        "chain": 23,
        "trigger": "level-up",
        "level": 33,
        "id": 35
    },
    {
        "evolves_from": 56,
        "chain": 24,
        "trigger": "level-up",
        "level": 28,
        "id": 36
    },
    {
        "evolves_from": 58,
        "chain": 25,
        "trigger": "use-item",
        "trigger_item": "fire-stone",
        "id": 37
    },
    {
        "evolves_from": 60,
        "chain": 26,
        "trigger": "level-up",
        "level": 25,
        "id": 38
    },
    {
        "evolves_from": 61,
        "chain": 26,
        "trigger": "use-item",
        "trigger_item": "water-stone",
        "id": 39
    },
    {
        "evolves_from": 63,
        "chain": 27,
        "trigger": "level-up",
        "level": 16,
        "id": 40
    },
    {
        "evolves_from": 64,
        "chain": 27,
        "trigger": "trade",
        "id": 41
    },
    {
        "evolves_from": 66,
        "chain": 28,
        "trigger": "level-up",
        "level": 28,
        "id": 42
    },
    {
        "evolves_from": 67,
        "chain": 28,
        "trigger": "trade",
        "id": 43
    },
    {
        "evolves_from": 69,
        "chain": 29,
        "trigger": "level-up",
        "level": 21,
        "id": 44
    },
    {
        "evolves_from": 70,
        "chain": 29,
        "trigger": "use-item",
        "trigger_item": "leaf-stone",
        "id": 45
    },
    {
        "evolves_from": 72,
        "chain": 30,
        "trigger": "level-up",
        "level": 30,
        "id": 46
    },
    {
        "evolves_from": 74,
        "chain": 31,
        "trigger": "level-up",
        "level": 25,
        "id": 47
    },
    {
        "evolves_from": 75,
        "chain": 31,
        "trigger": "trade",
        "id": 48
    },
    {
        "evolves_from": 77,
        "chain": 32,
        "trigger": "level-up",
        "level": 40,
        "id": 49
    },
    {
        "evolves_from": 79,
        "chain": 33,
        "trigger": "level-up",
        "level": 37,
        "id": 50
    },
    {
        "evolves_from": 81,
        "chain": 34,
        "trigger": "level-up",
        "level": 30,
        "id": 51
    },
    {
        "evolves_from": 84,
        "chain": 36,
        "trigger": "level-up",
        "level": 31,
        "id": 52
    },
    {
        "evolves_from": 86,
        "chain": 37,
        "trigger": "level-up",
        "level": 34,
        "id": 53
    },
    {
        "evolves_from": 88,
        "chain": 38,
        "trigger": "level-up",
        "level": 38,
        "id": 54
    },
    {
        "evolves_from": 90,
        "chain": 39,
        "trigger": "use-item",
        "trigger_item": "water-stone",
        "id": 55
    },
    {
        "evolves_from": 92,
        "chain": 40,
        "trigger": "level-up",
        "level": 25,
        "id": 56
    },
    {
        "evolves_from": 93,
        "chain": 40,
        "trigger": "trade",
        "id": 57
    },
    {
        "evolves_from": 96,
        "chain": 42,
        "trigger": "level-up",
        "level": 26,
        "id": 58
    },
    {
        "evolves_from": 98,
        "chain": 43,
        "trigger": "level-up",
        "level": 28,
        "id": 59
    },
    {
        "evolves_from": 100,
        "chain": 44,
        "trigger": "level-up",
        "level": 30,
        "id": 60
    },
    {
        "evolves_from": 102,
        "chain": 45,
        "trigger": "use-item",
        "trigger_item": "leaf-stone",
        "id": 61
    },
    {
        "evolves_from": 104,
        "chain": 46,
        "trigger": "level-up",
        "level": 28,
        "id": 62
    },
    {
        "evolves_from": 236,
        "chain": 47,
        "trigger": "level-up",
        "level": 20,
        "relative_stats": 1,
        "id": 63
    },
    {
        "evolves_from": 236,
        "chain": 47,
        "trigger": "level-up",
        "level": 20,
        "relative_stats": -1,
        "id": 64
    },
    {
        "evolves_from": 109,
        "chain": 49,
        "trigger": "level-up",
        "level": 35,
        "id": 65
    },
    {
        "evolves_from": 111,
        "chain": 50,
        "trigger": "level-up",
        "level": 42,
        "id": 66
    },
    {
        "evolves_from": 440,
        "chain": 51,
        "trigger": "level-up",
        "held_item": "oval-stone",
        "time_of_day": "day",
        "id": 67
    },
    {
        "evolves_from": 116,
        "chain": 54,
        "trigger": "level-up",
        "level": 32,
        "id": 68
    },
    {
        "evolves_from": 118,
        "chain": 55,
        "trigger": "level-up",
        "level": 33,
        "id": 69
    },
    {
        "evolves_from": 120,
        "chain": 56,
        "trigger": "use-item",
        "trigger_item": "water-stone",
        "id": 70
    },
    {
        "evolves_from": 439,
        "chain": 57,
        "trigger": "level-up",
        "known_move": "mimic",
        "id": 71
    },
    {
        "evolves_from": 238,
        "chain": 59,
        "trigger": "level-up",
        "level": 30,
        "id": 72
    },
    {
        "evolves_from": 239,
        "chain": 60,
        "trigger": "level-up",
        "level": 30,
        "id": 73
    },
    {
        "evolves_from": 240,
        "chain": 61,
        "trigger": "level-up",
        "level": 30,
        "id": 74
    },
    {
        "evolves_from": 129,
        "chain": 64,
        "trigger": "level-up",
        "level": 20,
        "id": 75
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "use-item",
        "trigger_item": "water-stone",
        "id": 76
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "use-item",
        "trigger_item": "thunder-stone",
        "id": 77
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "use-item",
        "trigger_item": "fire-stone",
        "id": 78
    },
    {
        "evolves_from": 138,
        "chain": 69,
        "trigger": "level-up",
        "level": 40,
        "id": 79
    },
    {
        "evolves_from": 140,
        "chain": 70,
        "trigger": "level-up",
        "level": 40,
        "id": 80
    },
    {
        "evolves_from": 446,
        "chain": 72,
        "trigger": "level-up",
        "happiness": 220,
        "id": 81
    },
    {
        "evolves_from": 147,
        "chain": 76,
        "trigger": "level-up",
        "level": 30,
        "id": 82
    },
    {
        "evolves_from": 148,
        "chain": 76,
        "trigger": "level-up",
        "level": 55,
        "id": 83
    },
    {
        "evolves_from": 152,
        "chain": 79,
        "trigger": "level-up",
        "level": 16,
        "id": 84
    },
    {
        "evolves_from": 153,
        "chain": 79,
        "trigger": "level-up",
        "level": 32,
        "id": 85
    },
    {
        "evolves_from": 155,
        "chain": 80,
        "trigger": "level-up",
        "level": 14,
        "id": 86
    },
    {
        "evolves_from": 156,
        "chain": 80,
        "trigger": "level-up",
        "level": 36,
        "id": 87
    },
    {
        "evolves_from": 158,
        "chain": 81,
        "trigger": "level-up",
        "level": 18,
        "id": 88
    },
    {
        "evolves_from": 159,
        "chain": 81,
        "trigger": "level-up",
        "level": 30,
        "id": 89
    },
    {
        "evolves_from": 161,
        "chain": 82,
        "trigger": "level-up",
        "level": 15,
        "id": 90
    },
    {
        "evolves_from": 163,
        "chain": 83,
        "trigger": "level-up",
        "level": 20,
        "id": 91
    },
    {
        "evolves_from": 165,
        "chain": 84,
        "trigger": "level-up",
        "level": 18,
        "id": 92
    },
    {
        "evolves_from": 167,
        "chain": 85,
        "trigger": "level-up",
        "level": 22,
        "id": 93
    },
    {
        "evolves_from": 42,
        "chain": 17,
        "trigger": "level-up",
        "happiness": 220,
        "id": 94
    },
    {
        "evolves_from": 170,
        "chain": 86,
        "trigger": "level-up",
        "level": 27,
        "id": 95
    },
    {
        "evolves_from": 175,
        "chain": 87,
        "trigger": "level-up",
        "happiness": 220,
        "id": 96
    },
    {
        "evolves_from": 177,
        "chain": 88,
        "trigger": "level-up",
        "level": 25,
        "id": 97
    },
    {
        "evolves_from": 179,
        "chain": 89,
        "trigger": "level-up",
        "level": 15,
        "id": 98
    },
    {
        "evolves_from": 180,
        "chain": 89,
        "trigger": "level-up",
        "level": 30,
        "id": 99
    },
    {
        "evolves_from": 44,
        "chain": 18,
        "trigger": "use-item",
        "trigger_item": "sun-stone",
        "id": 100
    },
    {
        "evolves_from": 298,
        "chain": 90,
        "trigger": "level-up",
        "happiness": 220,
        "id": 101
    },
    {
        "evolves_from": 183,
        "chain": 90,
        "trigger": "level-up",
        "level": 18,
        "id": 102
    },
    {
        "evolves_from": 438,
        "chain": 91,
        "trigger": "level-up",
        "known_move": "mimic",
        "id": 103
    },
    {
        "evolves_from": 61,
        "chain": 26,
        "trigger": "trade",
        "held_item": "kings-rock",
        "id": 104
    },
    {
        "evolves_from": 187,
        "chain": 92,
        "trigger": "level-up",
        "level": 18,
        "id": 105
    },
    {
        "evolves_from": 188,
        "chain": 92,
        "trigger": "level-up",
        "level": 27,
        "id": 106
    },
    {
        "evolves_from": 191,
        "chain": 94,
        "trigger": "use-item",
        "trigger_item": "sun-stone",
        "id": 107
    },
    {
        "evolves_from": 194,
        "chain": 96,
        "trigger": "level-up",
        "level": 20,
        "id": 108
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "time_of_day": "day",
        "happiness": 220,
        "id": 109
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "time_of_day": "night",
        "happiness": 220,
        "id": 110
    },
    {
        "evolves_from": 79,
        "chain": 33,
        "trigger": "trade",
        "held_item": "kings-rock",
        "id": 111
    },
    {
        "evolves_from": 360,
        "chain": 100,
        "trigger": "level-up",
        "level": 15,
        "id": 112
    },
    {
        "evolves_from": 204,
        "chain": 102,
        "trigger": "level-up",
        "level": 31,
        "id": 113
    },
    {
        "evolves_from": 95,
        "chain": 41,
        "trigger": "trade",
        "held_item": "metal-coat",
        "id": 114
    },
    {
        "evolves_from": 209,
        "chain": 105,
        "trigger": "level-up",
        "level": 23,
        "id": 115
    },
    {
        "evolves_from": 123,
        "chain": 58,
        "trigger": "trade",
        "held_item": "metal-coat",
        "id": 116
    },
    {
        "evolves_from": 216,
        "chain": 110,
        "trigger": "level-up",
        "level": 30,
        "id": 117
    },
    {
        "evolves_from": 218,
        "chain": 111,
        "trigger": "level-up",
        "level": 38,
        "id": 118
    },
    {
        "evolves_from": 220,
        "chain": 112,
        "trigger": "level-up",
        "level": 33,
        "id": 119
    },
    {
        "evolves_from": 223,
        "chain": 114,
        "trigger": "level-up",
        "level": 25,
        "id": 120
    },
    {
        "evolves_from": 458,
        "chain": 116,
        "trigger": "level-up",
        "party_species": "remoraid",
        "id": 121
    },
    {
        "evolves_from": 228,
        "chain": 118,
        "trigger": "level-up",
        "level": 24,
        "id": 122
    },
    {
        "evolves_from": 117,
        "chain": 54,
        "trigger": "trade",
        "held_item": "dragon-scale",
        "id": 123
    },
    {
        "evolves_from": 231,
        "chain": 119,
        "trigger": "level-up",
        "level": 25,
        "id": 124
    },
    {
        "evolves_from": 137,
        "chain": 68,
        "trigger": "trade",
        "held_item": "up-grade",
        "id": 125
    },
    {
        "evolves_from": 236,
        "chain": 47,
        "trigger": "level-up",
        "level": 20,
        "id": 126
    },
    {
        "evolves_from": 113,
        "chain": 51,
        "trigger": "level-up",
        "happiness": 220,
        "id": 127
    },
    {
        "evolves_from": 246,
        "chain": 126,
        "trigger": "level-up",
        "level": 30,
        "id": 128
    },
    {
        "evolves_from": 247,
        "chain": 126,
        "trigger": "level-up",
        "level": 55,
        "id": 129
    },
    {
        "evolves_from": 252,
        "chain": 130,
        "trigger": "level-up",
        "level": 16,
        "id": 130
    },
    {
        "evolves_from": 253,
        "chain": 130,
        "trigger": "level-up",
        "level": 36,
        "id": 131
    },
    {
        "evolves_from": 255,
        "chain": 131,
        "trigger": "level-up",
        "level": 16,
        "id": 132
    },
    {
        "evolves_from": 256,
        "chain": 131,
        "trigger": "level-up",
        "level": 36,
        "id": 133
    },
    {
        "evolves_from": 258,
        "chain": 132,
        "trigger": "level-up",
        "level": 16,
        "id": 134
    },
    {
        "evolves_from": 259,
        "chain": 132,
        "trigger": "level-up",
        "level": 36,
        "id": 135
    },
    {
        "evolves_from": 261,
        "chain": 133,
        "trigger": "level-up",
        "level": 18,
        "id": 136
    },
    {
        "evolves_from": 263,
        "chain": 134,
        "trigger": "level-up",
        "level": 20,
        "id": 137
    },
    {
        "evolves_from": 265,
        "chain": 135,
        "trigger": "level-up",
        "level": 7,
        "id": 138
    },
    {
        "evolves_from": 266,
        "chain": 135,
        "trigger": "level-up",
        "level": 10,
        "id": 139
    },
    {
        "evolves_from": 265,
        "chain": 135,
        "trigger": "level-up",
        "level": 7,
        "id": 140
    },
    {
        "evolves_from": 268,
        "chain": 135,
        "trigger": "level-up",
        "level": 10,
        "id": 141
    },
    {
        "evolves_from": 270,
        "chain": 136,
        "trigger": "level-up",
        "level": 14,
        "id": 142
    },
    {
        "evolves_from": 271,
        "chain": 136,
        "trigger": "use-item",
        "trigger_item": "water-stone",
        "id": 143
    },
    {
        "evolves_from": 273,
        "chain": 137,
        "trigger": "level-up",
        "level": 14,
        "id": 144
    },
    {
        "evolves_from": 274,
        "chain": 137,
        "trigger": "use-item",
        "trigger_item": "leaf-stone",
        "id": 145
    },
    {
        "evolves_from": 276,
        "chain": 138,
        "trigger": "level-up",
        "level": 22,
        "id": 146
    },
    {
        "evolves_from": 278,
        "chain": 139,
        "trigger": "level-up",
        "level": 25,
        "id": 147
    },
    {
        "evolves_from": 280,
        "chain": 140,
        "trigger": "level-up",
        "level": 20,
        "id": 148
    },
    {
        "evolves_from": 281,
        "chain": 140,
        "trigger": "level-up",
        "level": 30,
        "id": 149
    },
    {
        "evolves_from": 283,
        "chain": 141,
        "trigger": "level-up",
        "level": 22,
        "id": 150
    },
    {
        "evolves_from": 285,
        "chain": 142,
        "trigger": "level-up",
        "level": 23,
        "id": 151
    },
    {
        "evolves_from": 287,
        "chain": 143,
        "trigger": "level-up",
        "level": 18,
        "id": 152
    },
    {
        "evolves_from": 288,
        "chain": 143,
        "trigger": "level-up",
        "level": 36,
        "id": 153
    },
    {
        "evolves_from": 290,
        "chain": 144,
        "trigger": "level-up",
        "level": 20,
        "id": 154
    },
    {
        "evolves_from": 290,
        "chain": 144,
        "trigger": "shed",
        "id": 155
    },
    {
        "evolves_from": 293,
        "chain": 145,
        "trigger": "level-up",
        "level": 20,
        "id": 156
    },
    {
        "evolves_from": 294,
        "chain": 145,
        "trigger": "level-up",
        "level": 40,
        "id": 157
    },
    {
        "evolves_from": 296,
        "chain": 146,
        "trigger": "level-up",
        "level": 24,
        "id": 158
    },
    {
        "evolves_from": 300,
        "chain": 148,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 159
    },
    {
        "evolves_from": 304,
        "chain": 151,
        "trigger": "level-up",
        "level": 32,
        "id": 160
    },
    {
        "evolves_from": 305,
        "chain": 151,
        "trigger": "level-up",
        "level": 42,
        "id": 161
    },
    {
        "evolves_from": 307,
        "chain": 152,
        "trigger": "level-up",
        "level": 37,
        "id": 162
    },
    {
        "evolves_from": 309,
        "chain": 153,
        "trigger": "level-up",
        "level": 26,
        "id": 163
    },
    {
        "evolves_from": 406,
        "chain": 158,
        "trigger": "level-up",
        "time_of_day": "day",
        "happiness": 220,
        "id": 164
    },
    {
        "evolves_from": 316,
        "chain": 159,
        "trigger": "level-up",
        "level": 26,
        "id": 165
    },
    {
        "evolves_from": 318,
        "chain": 160,
        "trigger": "level-up",
        "level": 30,
        "id": 166
    },
    {
        "evolves_from": 320,
        "chain": 161,
        "trigger": "level-up",
        "level": 40,
        "id": 167
    },
    {
        "evolves_from": 322,
        "chain": 162,
        "trigger": "level-up",
        "level": 33,
        "id": 168
    },
    {
        "evolves_from": 325,
        "chain": 164,
        "trigger": "level-up",
        "level": 32,
        "id": 169
    },
    {
        "evolves_from": 328,
        "chain": 166,
        "trigger": "level-up",
        "level": 35,
        "id": 170
    },
    {
        "evolves_from": 329,
        "chain": 166,
        "trigger": "level-up",
        "level": 45,
        "id": 171
    },
    {
        "evolves_from": 331,
        "chain": 167,
        "trigger": "level-up",
        "level": 32,
        "id": 172
    },
    {
        "evolves_from": 333,
        "chain": 168,
        "trigger": "level-up",
        "level": 35,
        "id": 173
    },
    {
        "evolves_from": 339,
        "chain": 173,
        "trigger": "level-up",
        "level": 30,
        "id": 174
    },
    {
        "evolves_from": 341,
        "chain": 174,
        "trigger": "level-up",
        "level": 30,
        "id": 175
    },
    {
        "evolves_from": 343,
        "chain": 175,
        "trigger": "level-up",
        "level": 36,
        "id": 176
    },
    {
        "evolves_from": 345,
        "chain": 176,
        "trigger": "level-up",
        "level": 40,
        "id": 177
    },
    {
        "evolves_from": 347,
        "chain": 177,
        "trigger": "level-up",
        "level": 40,
        "id": 178
    },
    {
        "evolves_from": 349,
        "chain": 178,
        "trigger": "level-up",
        "beauty": 171,
        "id": 179
    },
    {
        "evolves_from": 353,
        "chain": 181,
        "trigger": "level-up",
        "level": 37,
        "id": 180
    },
    {
        "evolves_from": 355,
        "chain": 182,
        "trigger": "level-up",
        "level": 37,
        "id": 181
    },
    {
        "evolves_from": 433,
        "chain": 184,
        "trigger": "level-up",
        "time_of_day": "night",
        "happiness": 220,
        "id": 182
    },
    {
        "evolves_from": 361,
        "chain": 186,
        "trigger": "level-up",
        "level": 42,
        "id": 183
    },
    {
        "evolves_from": 363,
        "chain": 187,
        "trigger": "level-up",
        "level": 32,
        "id": 184
    },
    {
        "evolves_from": 364,
        "chain": 187,
        "trigger": "level-up",
        "level": 44,
        "id": 185
    },
    {
        "evolves_from": 366,
        "chain": 188,
        "trigger": "trade",
        "held_item": "deep-sea-tooth",
        "id": 186
    },
    {
        "evolves_from": 366,
        "chain": 188,
        "trigger": "trade",
        "held_item": "deep-sea-scale",
        "id": 187
    },
    {
        "evolves_from": 371,
        "chain": 191,
        "trigger": "level-up",
        "level": 30,
        "id": 188
    },
    {
        "evolves_from": 372,
        "chain": 191,
        "trigger": "level-up",
        "level": 50,
        "id": 189
    },
    {
        "evolves_from": 374,
        "chain": 192,
        "trigger": "level-up",
        "level": 20,
        "id": 190
    },
    {
        "evolves_from": 375,
        "chain": 192,
        "trigger": "level-up",
        "level": 45,
        "id": 191
    },
    {
        "evolves_from": 387,
        "chain": 203,
        "trigger": "level-up",
        "level": 18,
        "id": 192
    },
    {
        "evolves_from": 388,
        "chain": 203,
        "trigger": "level-up",
        "level": 32,
        "id": 193
    },
    {
        "evolves_from": 390,
        "chain": 204,
        "trigger": "level-up",
        "level": 14,
        "id": 194
    },
    {
        "evolves_from": 391,
        "chain": 204,
        "trigger": "level-up",
        "level": 36,
        "id": 195
    },
    {
        "evolves_from": 393,
        "chain": 205,
        "trigger": "level-up",
        "level": 16,
        "id": 196
    },
    {
        "evolves_from": 394,
        "chain": 205,
        "trigger": "level-up",
        "level": 36,
        "id": 197
    },
    {
        "evolves_from": 396,
        "chain": 206,
        "trigger": "level-up",
        "level": 14,
        "id": 198
    },
    {
        "evolves_from": 397,
        "chain": 206,
        "trigger": "level-up",
        "level": 34,
        "id": 199
    },
    {
        "evolves_from": 399,
        "chain": 207,
        "trigger": "level-up",
        "level": 15,
        "id": 200
    },
    {
        "evolves_from": 401,
        "chain": 208,
        "trigger": "level-up",
        "level": 10,
        "id": 201
    },
    {
        "evolves_from": 403,
        "chain": 209,
        "trigger": "level-up",
        "level": 15,
        "id": 202
    },
    {
        "evolves_from": 404,
        "chain": 209,
        "trigger": "level-up",
        "level": 30,
        "id": 203
    },
    {
        "evolves_from": 315,
        "chain": 158,
        "trigger": "use-item",
        "trigger_item": "shiny-stone",
        "id": 204
    },
    {
        "evolves_from": 408,
        "chain": 211,
        "trigger": "level-up",
        "level": 30,
        "id": 205
    },
    {
        "evolves_from": 410,
        "chain": 212,
        "trigger": "level-up",
        "level": 30,
        "id": 206
    },
    {
        "evolves_from": 412,
        "chain": 213,
        "trigger": "level-up",
        "level": 20,
        "gender": "female",
        "id": 207
    },
    {
        "evolves_from": 412,
        "chain": 213,
        "trigger": "level-up",
        "level": 20,
        "gender": "male",
        "id": 208
    },
    {
        "evolves_from": 415,
        "chain": 214,
        "trigger": "level-up",
        "level": 21,
        "gender": "female",
        "id": 209
    },
    {
        "evolves_from": 418,
        "chain": 216,
        "trigger": "level-up",
        "level": 26,
        "id": 210
    },
    {
        "evolves_from": 420,
        "chain": 217,
        "trigger": "level-up",
        "level": 25,
        "id": 211
    },
    {
        "evolves_from": 422,
        "chain": 218,
        "trigger": "level-up",
        "level": 30,
        "id": 212
    },
    {
        "evolves_from": 190,
        "chain": 93,
        "trigger": "level-up",
        "known_move": "double-hit",
        "id": 213
    },
    {
        "evolves_from": 425,
        "chain": 219,
        "trigger": "level-up",
        "level": 28,
        "id": 214
    },
    {
        "evolves_from": 427,
        "chain": 220,
        "trigger": "level-up",
        "happiness": 220,
        "id": 215
    },
    {
        "evolves_from": 200,
        "chain": 98,
        "trigger": "use-item",
        "trigger_item": "dusk-stone",
        "id": 216
    },
    {
        "evolves_from": 198,
        "chain": 97,
        "trigger": "use-item",
        "trigger_item": "dusk-stone",
        "id": 217
    },
    {
        "evolves_from": 431,
        "chain": 221,
        "trigger": "level-up",
        "level": 38,
        "id": 218
    },
    {
        "evolves_from": 434,
        "chain": 223,
        "trigger": "level-up",
        "level": 34,
        "id": 219
    },
    {
        "evolves_from": 436,
        "chain": 224,
        "trigger": "level-up",
        "level": 33,
        "id": 220
    },
    {
        "evolves_from": 443,
        "chain": 230,
        "trigger": "level-up",
        "level": 24,
        "id": 221
    },
    {
        "evolves_from": 444,
        "chain": 230,
        "trigger": "level-up",
        "level": 48,
        "id": 222
    },
    {
        "evolves_from": 447,
        "chain": 232,
        "trigger": "level-up",
        "time_of_day": "day",
        "happiness": 220,
        "id": 223
    },
    {
        "evolves_from": 449,
        "chain": 233,
        "trigger": "level-up",
        "level": 34,
        "id": 224
    },
    {
        "evolves_from": 451,
        "chain": 234,
        "trigger": "level-up",
        "level": 40,
        "id": 225
    },
    {
        "evolves_from": 453,
        "chain": 235,
        "trigger": "level-up",
        "level": 37,
        "id": 226
    },
    {
        "evolves_from": 456,
        "chain": 237,
        "trigger": "level-up",
        "level": 31,
        "id": 227
    },
    {
        "evolves_from": 459,
        "chain": 239,
        "trigger": "level-up",
        "level": 40,
        "id": 228
    },
    {
        "evolves_from": 215,
        "chain": 109,
        "trigger": "level-up",
        "held_item": "razor-claw",
        "time_of_day": "night",
        "id": 229
    },
    {
        "evolves_from": 82,
        "chain": 34,
        "trigger": "level-up",
        "location": 10,
        "id": 230
    },
    {
        "evolves_from": 108,
        "chain": 48,
        "trigger": "level-up",
        "known_move": "rollout",
        "id": 231
    },
    {
        "evolves_from": 112,
        "chain": 50,
        "trigger": "trade",
        "held_item": "protector",
        "id": 232
    },
    {
        "evolves_from": 114,
        "chain": 52,
        "trigger": "level-up",
        "known_move": "ancient-power",
        "id": 233
    },
    {
        "evolves_from": 125,
        "chain": 60,
        "trigger": "trade",
        "held_item": "electirizer",
        "id": 234
    },
    {
        "evolves_from": 126,
        "chain": 61,
        "trigger": "trade",
        "held_item": "magmarizer",
        "id": 235
    },
    {
        "evolves_from": 176,
        "chain": 87,
        "trigger": "use-item",
        "trigger_item": "shiny-stone",
        "id": 236
    },
    {
        "evolves_from": 193,
        "chain": 95,
        "trigger": "level-up",
        "known_move": "ancient-power",
        "id": 237
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "location": 8,
        "id": 238
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "location": 48,
        "id": 239
    },
    {
        "evolves_from": 207,
        "chain": 104,
        "trigger": "level-up",
        "held_item": "razor-fang",
        "time_of_day": "night",
        "id": 240
    },
    {
        "evolves_from": 221,
        "chain": 112,
        "trigger": "level-up",
        "known_move": "ancient-power",
        "id": 241
    },
    {
        "evolves_from": 233,
        "chain": 68,
        "trigger": "trade",
        "held_item": "dubious-disc",
        "id": 242
    },
    {
        "evolves_from": 281,
        "chain": 140,
        "trigger": "use-item",
        "trigger_item": "dawn-stone",
        "gender": "male",
        "id": 243
    },
    {
        "evolves_from": 299,
        "chain": 147,
        "trigger": "level-up",
        "location": 10,
        "id": 244
    },
    {
        "evolves_from": 356,
        "chain": 182,
        "trigger": "trade",
        "held_item": "reaper-cloth",
        "id": 245
    },
    {
        "evolves_from": 361,
        "chain": 186,
        "trigger": "use-item",
        "trigger_item": "dawn-stone",
        "gender": "female",
        "id": 246
    },
    {
        "evolves_from": 495,
        "chain": 256,
        "trigger": "level-up",
        "level": 17,
        "id": 247
    },
    {
        "evolves_from": 496,
        "chain": 256,
        "trigger": "level-up",
        "level": 36,
        "id": 248
    },
    {
        "evolves_from": 498,
        "chain": 257,
        "trigger": "level-up",
        "level": 17,
        "id": 249
    },
    {
        "evolves_from": 499,
        "chain": 257,
        "trigger": "level-up",
        "level": 36,
        "id": 250
    },
    {
        "evolves_from": 501,
        "chain": 258,
        "trigger": "level-up",
        "level": 17,
        "id": 251
    },
    {
        "evolves_from": 502,
        "chain": 258,
        "trigger": "level-up",
        "level": 36,
        "id": 252
    },
    {
        "evolves_from": 504,
        "chain": 259,
        "trigger": "level-up",
        "level": 20,
        "id": 253
    },
    {
        "evolves_from": 506,
        "chain": 260,
        "trigger": "level-up",
        "level": 16,
        "id": 254
    },
    {
        "evolves_from": 507,
        "chain": 260,
        "trigger": "level-up",
        "level": 32,
        "id": 255
    },
    {
        "evolves_from": 509,
        "chain": 261,
        "trigger": "level-up",
        "level": 20,
        "id": 256
    },
    {
        "evolves_from": 511,
        "chain": 262,
        "trigger": "use-item",
        "trigger_item": "leaf-stone",
        "id": 257
    },
    {
        "evolves_from": 513,
        "chain": 263,
        "trigger": "use-item",
        "trigger_item": "fire-stone",
        "id": 258
    },
    {
        "evolves_from": 515,
        "chain": 264,
        "trigger": "use-item",
        "trigger_item": "water-stone",
        "id": 259
    },
    {
        "evolves_from": 517,
        "chain": 265,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 260
    },
    {
        "evolves_from": 519,
        "chain": 266,
        "trigger": "level-up",
        "level": 21,
        "id": 261
    },
    {
        "evolves_from": 520,
        "chain": 266,
        "trigger": "level-up",
        "level": 32,
        "id": 262
    },
    {
        "evolves_from": 522,
        "chain": 267,
        "trigger": "level-up",
        "level": 27,
        "id": 263
    },
    {
        "evolves_from": 524,
        "chain": 268,
        "trigger": "level-up",
        "level": 25,
        "id": 264
    },
    {
        "evolves_from": 525,
        "chain": 268,
        "trigger": "trade",
        "id": 265
    },
    {
        "evolves_from": 527,
        "chain": 269,
        "trigger": "level-up",
        "happiness": 220,
        "id": 266
    },
    {
        "evolves_from": 529,
        "chain": 270,
        "trigger": "level-up",
        "level": 31,
        "id": 267
    },
    {
        "evolves_from": 532,
        "chain": 272,
        "trigger": "level-up",
        "level": 25,
        "id": 268
    },
    {
        "evolves_from": 533,
        "chain": 272,
        "trigger": "trade",
        "id": 269
    },
    {
        "evolves_from": 535,
        "chain": 273,
        "trigger": "level-up",
        "level": 25,
        "id": 270
    },
    {
        "evolves_from": 536,
        "chain": 273,
        "trigger": "level-up",
        "level": 36,
        "id": 271
    },
    {
        "evolves_from": 540,
        "chain": 276,
        "trigger": "level-up",
        "level": 20,
        "id": 272
    },
    {
        "evolves_from": 541,
        "chain": 276,
        "trigger": "level-up",
        "happiness": 220,
        "id": 273
    },
    {
        "evolves_from": 543,
        "chain": 277,
        "trigger": "level-up",
        "level": 22,
        "id": 274
    },
    {
        "evolves_from": 544,
        "chain": 277,
        "trigger": "level-up",
        "level": 30,
        "id": 275
    },
    {
        "evolves_from": 546,
        "chain": 278,
        "trigger": "use-item",
        "trigger_item": "sun-stone",
        "id": 276
    },
    {
        "evolves_from": 548,
        "chain": 279,
        "trigger": "use-item",
        "trigger_item": "sun-stone",
        "id": 277
    },
    {
        "evolves_from": 551,
        "chain": 281,
        "trigger": "level-up",
        "level": 29,
        "id": 278
    },
    {
        "evolves_from": 552,
        "chain": 281,
        "trigger": "level-up",
        "level": 40,
        "id": 279
    },
    {
        "evolves_from": 554,
        "chain": 282,
        "trigger": "level-up",
        "level": 35,
        "id": 280
    },
    {
        "evolves_from": 557,
        "chain": 284,
        "trigger": "level-up",
        "level": 34,
        "id": 281
    },
    {
        "evolves_from": 559,
        "chain": 285,
        "trigger": "level-up",
        "level": 39,
        "id": 282
    },
    {
        "evolves_from": 562,
        "chain": 287,
        "trigger": "level-up",
        "level": 34,
        "id": 283
    },
    {
        "evolves_from": 564,
        "chain": 288,
        "trigger": "level-up",
        "level": 37,
        "id": 284
    },
    {
        "evolves_from": 566,
        "chain": 289,
        "trigger": "level-up",
        "level": 37,
        "id": 285
    },
    {
        "evolves_from": 568,
        "chain": 290,
        "trigger": "level-up",
        "level": 36,
        "id": 286
    },
    {
        "evolves_from": 570,
        "chain": 291,
        "trigger": "level-up",
        "level": 30,
        "id": 287
    },
    {
        "evolves_from": 572,
        "chain": 292,
        "trigger": "use-item",
        "trigger_item": "shiny-stone",
        "id": 288
    },
    {
        "evolves_from": 574,
        "chain": 293,
        "trigger": "level-up",
        "level": 32,
        "id": 289
    },
    {
        "evolves_from": 575,
        "chain": 293,
        "trigger": "level-up",
        "level": 41,
        "id": 290
    },
    {
        "evolves_from": 577,
        "chain": 294,
        "trigger": "level-up",
        "level": 32,
        "id": 291
    },
    {
        "evolves_from": 578,
        "chain": 294,
        "trigger": "level-up",
        "level": 41,
        "id": 292
    },
    {
        "evolves_from": 580,
        "chain": 295,
        "trigger": "level-up",
        "level": 35,
        "id": 293
    },
    {
        "evolves_from": 582,
        "chain": 296,
        "trigger": "level-up",
        "level": 35,
        "id": 294
    },
    {
        "evolves_from": 583,
        "chain": 296,
        "trigger": "level-up",
        "level": 47,
        "id": 295
    },
    {
        "evolves_from": 585,
        "chain": 297,
        "trigger": "level-up",
        "level": 34,
        "id": 296
    },
    {
        "evolves_from": 588,
        "chain": 299,
        "trigger": "trade",
        "trade_species": "shelmet",
        "id": 297
    },
    {
        "evolves_from": 590,
        "chain": 300,
        "trigger": "level-up",
        "level": 39,
        "id": 298
    },
    {
        "evolves_from": 592,
        "chain": 301,
        "trigger": "level-up",
        "level": 40,
        "id": 299
    },
    {
        "evolves_from": 595,
        "chain": 303,
        "trigger": "level-up",
        "level": 36,
        "id": 300
    },
    {
        "evolves_from": 597,
        "chain": 304,
        "trigger": "level-up",
        "level": 40,
        "id": 301
    },
    {
        "evolves_from": 599,
        "chain": 305,
        "trigger": "level-up",
        "level": 38,
        "id": 302
    },
    {
        "evolves_from": 600,
        "chain": 305,
        "trigger": "level-up",
        "level": 49,
        "id": 303
    },
    {
        "evolves_from": 602,
        "chain": 306,
        "trigger": "level-up",
        "level": 39,
        "id": 304
    },
    {
        "evolves_from": 603,
        "chain": 306,
        "trigger": "use-item",
        "trigger_item": "thunder-stone",
        "id": 305
    },
    {
        "evolves_from": 605,
        "chain": 307,
        "trigger": "level-up",
        "level": 42,
        "id": 306
    },
    {
        "evolves_from": 607,
        "chain": 308,
        "trigger": "level-up",
        "level": 41,
        "id": 307
    },
    {
        "evolves_from": 608,
        "chain": 308,
        "trigger": "use-item",
        "trigger_item": "dusk-stone",
        "id": 308
    },
    {
        "evolves_from": 610,
        "chain": 309,
        "trigger": "level-up",
        "level": 38,
        "id": 309
    },
    {
        "evolves_from": 611,
        "chain": 309,
        "trigger": "level-up",
        "level": 48,
        "id": 310
    },
    {
        "evolves_from": 613,
        "chain": 310,
        "trigger": "level-up",
        "level": 37,
        "id": 311
    },
    {
        "evolves_from": 616,
        "chain": 312,
        "trigger": "trade",
        "trade_species": "karrablast",
        "id": 312
    },
    {
        "evolves_from": 619,
        "chain": 314,
        "trigger": "level-up",
        "level": 50,
        "id": 313
    },
    {
        "evolves_from": 622,
        "chain": 316,
        "trigger": "level-up",
        "level": 43,
        "id": 314
    },
    {
        "evolves_from": 624,
        "chain": 317,
        "trigger": "level-up",
        "level": 52,
        "id": 315
    },
    {
        "evolves_from": 627,
        "chain": 319,
        "trigger": "level-up",
        "level": 54,
        "id": 316
    },
    {
        "evolves_from": 629,
        "chain": 320,
        "trigger": "level-up",
        "level": 54,
        "id": 317
    },
    {
        "evolves_from": 633,
        "chain": 323,
        "trigger": "level-up",
        "level": 50,
        "id": 318
    },
    {
        "evolves_from": 634,
        "chain": 323,
        "trigger": "level-up",
        "level": 64,
        "id": 319
    },
    {
        "evolves_from": 636,
        "chain": 324,
        "trigger": "level-up",
        "level": 59,
        "id": 320
    },
    {
        "evolves_from": 349,
        "chain": 178,
        "trigger": "trade",
        "held_item": "prism-scale",
        "id": 321
    },
    {
        "evolves_from": 82,
        "chain": 34,
        "trigger": "level-up",
        "location": 379,
        "id": 322
    },
    {
        "evolves_from": 299,
        "chain": 147,
        "trigger": "level-up",
        "location": 379,
        "id": 323
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "location": 375,
        "id": 324
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "location": 380,
        "id": 325
    },
    {
        "evolves_from": 682,
        "chain": 350,
        "trigger": "trade",
        "held_item": "sachet",
        "id": 327
    },
    {
        "evolves_from": 661,
        "chain": 341,
        "trigger": "level-up",
        "level": 17,
        "id": 328
    },
    {
        "evolves_from": 708,
        "chain": 364,
        "trigger": "trade",
        "id": 329
    },
    {
        "evolves_from": 662,
        "chain": 341,
        "trigger": "level-up",
        "level": 35,
        "id": 330
    },
    {
        "evolves_from": 653,
        "chain": 338,
        "trigger": "level-up",
        "level": 16,
        "id": 331
    },
    {
        "evolves_from": 686,
        "chain": 352,
        "trigger": "level-up",
        "level": 30,
        "needs_inversion": true,
        "id": 332
    },
    {
        "evolves_from": 654,
        "chain": 338,
        "trigger": "level-up",
        "level": 36,
        "id": 333
    },
    {
        "evolves_from": 650,
        "chain": 337,
        "trigger": "level-up",
        "level": 16,
        "id": 334
    },
    {
        "evolves_from": 692,
        "chain": 355,
        "trigger": "level-up",
        "level": 37,
        "id": 335
    },
    {
        "evolves_from": 651,
        "chain": 337,
        "trigger": "level-up",
        "level": 36,
        "id": 336
    },
    {
        "evolves_from": 656,
        "chain": 339,
        "trigger": "level-up",
        "level": 16,
        "id": 337
    },
    {
        "evolves_from": 657,
        "chain": 339,
        "trigger": "level-up",
        "level": 36,
        "id": 338
    },
    {
        "evolves_from": 679,
        "chain": 349,
        "trigger": "level-up",
        "level": 35,
        "id": 339
    },
    {
        "evolves_from": 704,
        "chain": 362,
        "trigger": "level-up",
        "level": 40,
        "id": 340
    },
    {
        "evolves_from": 665,
        "chain": 342,
        "trigger": "level-up",
        "level": 12,
        "id": 341
    },
    {
        "evolves_from": 664,
        "chain": 342,
        "trigger": "level-up",
        "level": 9,
        "id": 342
    },
    {
        "evolves_from": 688,
        "chain": 353,
        "trigger": "level-up",
        "level": 39,
        "id": 343
    },
    {
        "evolves_from": 710,
        "chain": 365,
        "trigger": "trade",
        "id": 344
    },
    {
        "evolves_from": 659,
        "chain": 340,
        "trigger": "level-up",
        "level": 20,
        "id": 345
    },
    {
        "evolves_from": 669,
        "chain": 344,
        "trigger": "level-up",
        "level": 19,
        "id": 346
    },
    {
        "evolves_from": 670,
        "chain": 344,
        "trigger": "use-item",
        "trigger_item": "shiny-stone",
        "id": 347
    },
    {
        "evolves_from": 680,
        "chain": 349,
        "trigger": "use-item",
        "trigger_item": "dusk-stone",
        "id": 348
    },
    {
        "evolves_from": 674,
        "chain": 346,
        "trigger": "level-up",
        "level": 32,
        "party_type": "dark",
        "id": 349
    },
    {
        "evolves_from": 684,
        "chain": 351,
        "trigger": "trade",
        "held_item": "whipped-dream",
        "id": 350
    },
    {
        "evolves_from": 690,
        "chain": 354,
        "trigger": "level-up",
        "level": 48,
        "id": 351
    },
    {
        "evolves_from": 696,
        "chain": 357,
        "trigger": "level-up",
        "level": 39,
        "time_of_day": "day",
        "id": 352
    },
    {
        "evolves_from": 698,
        "chain": 358,
        "trigger": "level-up",
        "level": 39,
        "time_of_day": "night",
        "id": 353
    },
    {
        "evolves_from": 712,
        "chain": 366,
        "trigger": "level-up",
        "level": 37,
        "id": 354
    },
    {
        "evolves_from": 694,
        "chain": 356,
        "trigger": "use-item",
        "trigger_item": "sun-stone",
        "id": 355
    },
    {
        "evolves_from": 667,
        "chain": 343,
        "trigger": "level-up",
        "level": 35,
        "id": 356
    },
    {
        "evolves_from": 672,
        "chain": 345,
        "trigger": "level-up",
        "level": 32,
        "id": 357
    },
    {
        "evolves_from": 705,
        "chain": 362,
        "trigger": "level-up",
        "level": 50,
        "needs_rain": true,
        "id": 358
    },
    {
        "evolves_from": 714,
        "chain": 367,
        "trigger": "level-up",
        "level": 48,
        "id": 359
    },
    {
        "evolves_from": 677,
        "chain": 348,
        "trigger": "level-up",
        "level": 25,
        "id": 360
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "known_move_type": "fairy",
        "affection": 2,
        "id": 361
    },
    {
        "evolves_from": 82,
        "chain": 34,
        "trigger": "level-up",
        "location": 629,
        "id": 362
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "location": 650,
        "id": 363
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "location": 640,
        "id": 364
    },
    {
        "evolves_from": 299,
        "chain": 147,
        "trigger": "level-up",
        "location": 629,
        "id": 365
    },
    {
        "evolves_from": 82,
        "chain": 34,
        "trigger": "level-up",
        "id": 366
    },
    {
        "evolves_from": 104,
        "chain": 46,
        "trigger": "level-up",
        "level": 28,
        "time_of_day": "night",
        "id": 367
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "id": 368
    },
    {
        "evolves_from": 133,
        "chain": 67,
        "trigger": "level-up",
        "id": 369
    },
    {
        "evolves_from": 299,
        "chain": 147,
        "trigger": "level-up",
        "id": 370
    },
    {
        "evolves_from": 349,
        "chain": 178,
        "trigger": "level-up",
        "beauty": 170,
        "id": 371
    },
    {
        "evolves_from": 677,
        "chain": 348,
        "trigger": "level-up",
        "level": 25,
        "gender": "male",
        "id": 372
    },
    {
        "evolves_from": 722,
        "chain": 374,
        "trigger": "level-up",
        "level": 17,
        "id": 373
    },
    {
        "evolves_from": 723,
        "chain": 374,
        "trigger": "level-up",
        "level": 34,
        "id": 374
    },
    {
        "evolves_from": 725,
        "chain": 375,
        "trigger": "level-up",
        "level": 17,
        "id": 375
    },
    {
        "evolves_from": 726,
        "chain": 375,
        "trigger": "level-up",
        "level": 34,
        "id": 376
    },
    {
        "evolves_from": 728,
        "chain": 376,
        "trigger": "level-up",
        "level": 17,
        "id": 377
    },
    {
        "evolves_from": 729,
        "chain": 376,
        "trigger": "level-up",
        "level": 34,
        "id": 378
    },
    {
        "evolves_from": 731,
        "chain": 377,
        "trigger": "level-up",
        "level": 14,
        "id": 379
    },
    {
        "evolves_from": 732,
        "chain": 377,
        "trigger": "level-up",
        "level": 28,
        "id": 380
    },
    {
        "evolves_from": 734,
        "chain": 378,
        "trigger": "level-up",
        "level": 20,
        "time_of_day": "day",
        "id": 381
    },
    {
        "evolves_from": 736,
        "chain": 379,
        "trigger": "level-up",
        "level": 20,
        "id": 382
    },
    {
        "evolves_from": 737,
        "chain": 379,
        "trigger": "level-up",
        "id": 383
    },
    {
        "evolves_from": 739,
        "chain": 380,
        "trigger": "level-up",
        "id": 384
    },
    {
        "evolves_from": 742,
        "chain": 382,
        "trigger": "level-up",
        "level": 25,
        "id": 385
    },
    {
        "evolves_from": 744,
        "chain": 383,
        "trigger": "level-up",
        "level": 25,
        "time_of_day": "day",
        "id": 386
    },
    {
        "evolves_from": 744,
        "chain": 383,
        "trigger": "level-up",
        "level": 25,
        "time_of_day": "night",
        "id": 387
    },
    {
        "evolves_from": 747,
        "chain": 385,
        "trigger": "level-up",
        "level": 38,
        "id": 388
    },
    {
        "evolves_from": 749,
        "chain": 386,
        "trigger": "level-up",
        "level": 30,
        "id": 389
    },
    {
        "evolves_from": 751,
        "chain": 387,
        "trigger": "level-up",
        "level": 22,
        "id": 390
    },
    {
        "evolves_from": 753,
        "chain": 388,
        "trigger": "level-up",
        "level": 34,
        "time_of_day": "day",
        "id": 391
    },
    {
        "evolves_from": 755,
        "chain": 389,
        "trigger": "level-up",
        "level": 24,
        "id": 392
    },
    {
        "evolves_from": 757,
        "chain": 390,
        "trigger": "level-up",
        "level": 33,
        "gender": "female",
        "id": 393
    },
    {
        "evolves_from": 759,
        "chain": 391,
        "trigger": "level-up",
        "level": 27,
        "id": 394
    },
    {
        "evolves_from": 761,
        "chain": 392,
        "trigger": "level-up",
        "level": 18,
        "id": 395
    },
    {
        "evolves_from": 762,
        "chain": 392,
        "trigger": "level-up",
        "known_move": "stomp",
        "id": 396
    },
    {
        "evolves_from": 767,
        "chain": 396,
        "trigger": "level-up",
        "level": 30,
        "id": 397
    },
    {
        "evolves_from": 769,
        "chain": 397,
        "trigger": "level-up",
        "level": 42,
        "id": 398
    },
    {
        "evolves_from": 772,
        "chain": 399,
        "trigger": "level-up",
        "happiness": 220,
        "id": 399
    },
    {
        "evolves_from": 782,
        "chain": 408,
        "trigger": "level-up",
        "level": 35,
        "id": 400
    },
    {
        "evolves_from": 783,
        "chain": 408,
        "trigger": "level-up",
        "level": 45,
        "id": 401
    },
    {
        "evolves_from": 789,
        "chain": 413,
        "trigger": "level-up",
        "level": 43,
        "id": 402
    },
    {
        "evolves_from": 790,
        "chain": 413,
        "trigger": "level-up",
        "level": 53,
        "id": 403
    },
    {
        "evolves_from": 790,
        "chain": 413,
        "trigger": "level-up",
        "level": 53,
        "id": 404
    },
    {
        "evolves_from": 803,
        "chain": 424,
        "trigger": "level-up",
        "known_move": "dragon-pulse",
        "id": 405
    }
]

TYPE = {
    'water': {
        'info' : 'Water is one of the three basic elemental types along with Fire and Grass,'\
                'which constitute the three starter Pokémon. This creates a simple triangle'\
                'to explain the type concept easily to new players. Water is the most common'\
                'type with over 100 Pokémon, which are based on a wide variety of fish and'\
                'other sea-dwelling creatures.',
        'info2' : 'Notable Trainers who specialize in Water-type Pokémon include Misty of Cerulean City,'\
                  'Juan and Wallace of Sootopolis City, Crasher Wake of Pastoria City, Cress of Striaton City,'\
                  'Marlon of Humilau City, Siebold of the Kalos Elite Four, and Trial Captain Lana of Konikoni City.'\
                  'Prior to changes in Generation IV, all damaging Water-type moves were special,'\
                  'but they may now also be physical depending on the attack.',
        'image' : 'https://pokeweakness.com/images/1891870-131lapras.png',
        'advantages': ['ground', 'rock', 'fire'],
        'weaknesses': ['grass', 'electric'],
        'pokemon': [ALL['magikarp']['id'], ALL['gyarados']['id']]
        "damage_class" : 'special',
        'identifier' : 'water',
        'vs_normal' : 1.0,
        'vs_fighting' : 1.0,
        'vs_flying' : 1.0,
        'vs_poison' : 1.0,
        'vs_ground' : 2.0,
        'vs_rock' :  2.0,
        'vs_bug' : 1.0,
        'vs_ghost' : 1.0,
        'vs_steel' : 1.0,
        'vs_fire' : 2.0,
        'vs_water' : 0.5,
        'vs_grass' : 0.5,
        'vs_electric' : 1.0,
        'vs_psychic' : 1.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 0.5,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 11
    },
    'flying': {
        'info' : 'Most Flying type Pokémon are based on birds or insects, along with some mythical creatures like dragons.'\
        'On average they are faster than any other type. Nearly every Flying type has Flying as the secondary type,'\
        'usually with Normal.'\
        'There is only one pure Flying Pokémon (Tornadus), and one line with Flying as a primary type (Noibat/Noivern).',
        'info2' : 'Notable Trainers who specialize in Flying-type Pokémon are the Gym Leaders Falkner of Violet City,'\
        'Winona of Fortree City, Skyla of Mistralton City, and Kahili of Alola Elite Four.'\
        'Prior to changes in Generation IV, all damaging Flying-type moves were physical,'\
        'but they may now also be special depending on the attack.',
        'image' : 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/018.png',
        'advantages': ['fighting', 'bug', 'grass'],
        'weaknesses': ['rock', 'electric', 'ice'],
        'pokemon': [ALL['gyarados']['id']]
        'damage_class' : 'physical',
        'identifier' : 'flying',
        'vs_normal' : 1.0,
        'vs_fighting' : 2.0,
        'vs_flying' : 1.0,
        'vs_poison' : 1.0,
        'vs_ground' : 1.0,
        'vs_rock' : 0.5,
        'vs_bug' : 2.0,
        'vs_ghost' : 1.0,
        'vs_steel' : 0.5,
        'vs_fire' : 1.0,
        'vs_water' : 1.0,
        'vs_grass' : 2.0,
        'vs_electric' : 0.5,
        'vs_psychic' : 1.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 3
    },
    'ground': {
        'info' : 'Ground is one of the strongest types offensively:'\
        'it is super-effective against five other types (as is Fighting)'\
        'and Earthquake is one of the strongest moves in the game with power and accuracy both 100.'\
        'Unfortunately, many Ground type Pokémon are dual Rock types, lumbering them with 4x Grass and Water disadvantages.',
        'info2' : 'Notable Trainers who specialize in Ground-type Pokémon are Giovanni of Viridian City,'\
        'Bertha of the Sinnoh Elite Four, Clay of Driftveil City, and Island Kahuna Hapu of Poni Island.'\
        'Prior to changes in Generation IV, all damaging Ground-type moves were physical,'\
        'but they may now also be special depending on the attack.',
        'image' : 'https://cdn.bulbagarden.net/upload/3/31/050Diglett.png',
        'advantages': ['poison', 'rock', 'fire', 'steel', 'electric'],
        'weaknesses': ['water', 'grass', 'ice'],
        'pokemon': [ALL['sandslash']['id'], ALL['sandshrew']['id']]
        'damage_class' : 'physical',
        'identifier': 'ground',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 0.0,
        'vs_poison': 2.0,
        'vs_ground': 1.0,
        'vs_rock': 2.0,
        'vs_bug': 0.5,
        'vs_ghost': 1.0,
        'vs_steel': 2.0,
        'vs_fire': 2.0,
        'vs_water': 1.0,
        'vs_grass': 0.5,
        'vs_electric': 2.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 5
    },
    'poison': {
        'info' : 'The Poison type is regarded as one of the weakest offensively.'\
        'Prior to Pokémon X/Y it was super-effective only against Grass'\
        '(many of which are dual Poison so neutralizes the effect).'\
        'It now has an extra advantage against the new Fairy type.'\
        'In the first generation it was also super-effective against Bug but this was changed.'\
        'It fares a little better defensively but its best advantage is through status moves like Toxic.',
        'info2' : 'Notable Trainers who specialize in Poison-type Pokémon include Janine of Fuchsia City,'\
        'her father Koga of the Indigo Plateau Elite Four, Roxie of Virbank City, and Team Skull Admin Plumeria.'\
        'Some villainous teams, such as Team Rocket, also frequently use Poison-type Pokémon.'\
        'Prior to changes in Generation IV, all damaging Poison-type moves were physical,'\
        'but they may now also be special depending on the attack.',
        'image' : 'http://bogleech.com/pokemon/koffing.png',
        'advantages': ['grass', 'fairy'],
        'weaknesses': ['ground', 'psychic'],
        'pokemon': [ALL['ekans']['id'], ALL['arbok']['id']]
        'damage_class': 'physical',
        'identifier': 'poison',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 0.5,
        'vs_ground': 0.5,
        'vs_rock': 0.5,
        'vs_bug': 1.0,
        'vs_ghost': 0.5,
        'vs_steel': 0.0,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 2.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 2.0,
        'id': 4
    },
    'normal' : {
        'info' : '',
        'info2' : '',
        'image' : '',
        'advantages' : '',
        'weaknesses' : '',
        'pokemon' : '',
        'damage_class': 'physical',
        'identifier': 'normal',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 0.5,
        'vs_bug': 1.0,
        'vs_ghost': 0.0,
        'vs_steel': 0.5,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 1


    },
    'fighting': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': '',
        'identifier': '',
        'damage_class': 'physical',
        'identifier': 'fighting',
        'vs_normal': 2.0,
        'vs_fighting': 1.0,
        'vs_flying': 0.5,
        'vs_poison': 0.5,
        'vs_ground': 1.0,
        'vs_rock': 2.0,
        'vs_bug': 0.5,
        'vs_ghost': 0.0,
        'vs_steel': 2.0,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 0.5,
        'vs_ice': 2.0,
        'vs_dragon': 1.0,
        'vs_dark': 2.0,
        'vs_fairy': 0.5,
        'id': 2
    },
    'rock': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'physical',
        'identifier' : 'rock',
        'vs_normal' : 1.0,
        'vs_fighting' : 0.5,
        'vs_flying' : 2.0,
        'vs_poison' : 1.0,
        'vs_ground' : 0.5,
        'vs_rock' : 1.0,
        'vs_bug' : 2.0,
        'vs_ghost' : 1.0,
        'vs_steel' : 0.5,
        'vs_fire' : 2.0,
        'vs_water' : 1.0,
        'vs_grass' : 1.0,
        'vs_electric' : 1.0,
        'vs_psychic' : 1.0,
        'vs_ice' : 2.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 6

    },
    'bug': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'physical',
        'identifier' : 'bug',
        'vs_normal' : 1.0,
        'vs_fighting' : 0.5,
        'vs_flying' : 0.5,
        'vs_poison' : 0.5,
        'vs_ground' : 1.0,
        'vs_rock' : 1.0,
        'vs_bug' : 1.0,
        'vs_ghost' : 0.5,
        'vs_steel' : 0.5,
        'vs_fire' : 0.5,
        'vs_water' : 1.0,
        'vs_grass' : 2.0,
        'vs_electric' : 1.0,
        'vs_psychic' : 2.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 2.0,
        'vs_fairy' : 0.5,
        'id' : 7
    },
    'ghost': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'physical',
        'identifier' : 'ghost',
        'vs_normal' : 0.0,
        'vs_fighting' : 1.0,
        'vs_flying' : 1.0,
        'vs_poison' : 1.0,
        'vs_ground' : 1.0,
        'vs_rock' : 1.0,
        'vs_bug' : 1.0,
        'vs_ghost' : 2.0,
        'vs_steel' : 1.0,
        'vs_fire' : 1.0,
        'vs_water' : 1.0,
        'vs_grass' : 1.0,
        'vs_electric' : 1.0,
        'vs_psychic' : 2.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 0.5,
        'vs_fairy' : 1.0,
        'id' : 8

    },
    'steel': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'physical',
        'identifier': 'steel',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 2.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 0.5,
        'vs_water': 0.5,
        'vs_grass': 1.0,
        'vs_electric': 0.5,
        'vs_psychic': 1.0,
        'vs_ice': 2.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 2.0,
        'id': 9
    },
    'fire': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'fire',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 0.5,
        'vs_bug': 2.0,
        'vs_ghost': 1.0,
        'vs_steel': 2.0,
        'vs_fire': 0.5,
        'vs_water': 0.5,
        'vs_grass': 2.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 2.0,
        'vs_dragon': 0.5,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 10
    },
    'grass': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'special',
        'identifier' : 'grass',
        'vs_normal' : 1.0,
        'vs_fighting' : 1.0,
        'vs_flying' : 0.5,
        'vs_poison' : 0.5,
        'vs_ground' : 2.0,
        'vs_rock' : 2.0,
        'vs_bug' : 0.5,
        'vs_ghost' : 1.0,
        'vs_steel' : 0.5,
        'vs_fire' : 0.5,
        'vs_water' : 2.0,
        'vs_grass' : 0.5,
        'vs_electric' : 1.0,
        'vs_psychic' : 1.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 0.5,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 12
    },
    'electric': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'electric',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 2.0,
        'vs_poison': 1.0,
        'vs_ground': 0.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 1.0,
        'vs_fire': 1.0,
        'vs_water': 2.0,
        'vs_grass': 0.5,
        'vs_electric': 0.5,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 0.5,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 13
    },
    'psychic': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'psychic',
        'vs_normal': 1.0,
        'vs_fighting': 2.0,
        'vs_flying': 1.0,
        'vs_poison': 2.0,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 0.5,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 0.0,
        'vs_fairy': 1.0,
        'id': 14
    },
    'ice': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'ice',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 2.0,
        'vs_poison': 1.0,
        'vs_ground': 2.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 0.5,
        'vs_water': 0.5,
        'vs_grass': 2.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 0.5,
        'vs_dragon': 2.0,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 15
    },
    'dragon': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'dragon',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 2.0,
        'vs_dark': 1.0,
        'vs_fairy': 0.0,
        'id': 16
    },
    'dark': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'dark',
        'vs_normal': 1.0,
        'vs_fighting': 0.5,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 2.0,
        'vs_steel': 1.0,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 2.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 0.5,
        'vs_fairy': 0.5,
        'id': 17

    },
    'fairy': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': '',
        'identifier': 'fairy',
        'vs_normal': 1.0,
        'vs_fighting': 2.0,
        'vs_flying': 1.0,
        'vs_poison': 0.5,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 0.5,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 2.0,
        'vs_dark': 2.0,
        'vs_fairy': 1.0,
        'id': 18

    }


}

LOCATIONS = {}

FORMS = [
    {
        "pokemon_name": "Unown A",
        "form_label": "A",
        "identifier": "a",
        "pokemon_id": 201,
        "id": 201
    },
    {
        "pokemon_name": "Normal Deoxys",
        "form_label": "Normal Forme",
        "identifier": "normal",
        "pokemon_id": 386,
        "id": 386
    },
    {
        "pokemon_name": "Plant Burmy",
        "form_label": "Plant Cloak",
        "identifier": "plant",
        "pokemon_id": 412,
        "id": 412
    },
    {
        "pokemon_name": "Plant Wormadam",
        "form_label": "Plant Cloak",
        "identifier": "plant",
        "pokemon_id": 413,
        "id": 413
    },
    {
        "pokemon_name": "Overcast Cherrim",
        "form_label": "Overcast Form",
        "identifier": "overcast",
        "pokemon_id": 421,
        "id": 421
    },
    {
        "pokemon_name": "West Shellos",
        "form_label": "West Sea",
        "identifier": "west",
        "pokemon_id": 422,
        "id": 422
    },
    {
        "pokemon_name": "West Gastrodon",
        "form_label": "West Sea",
        "identifier": "west",
        "pokemon_id": 423,
        "id": 423
    },
    {
        "pokemon_name": "Altered Giratina",
        "form_label": "Altered Forme",
        "identifier": "altered",
        "pokemon_id": 487,
        "id": 487
    },
    {
        "pokemon_name": "Land Shaymin",
        "form_label": "Land Forme",
        "identifier": "land",
        "pokemon_id": 492,
        "id": 492
    },
    {
        "pokemon_name": "Normal Arceus",
        "form_label": "Normal Type",
        "identifier": "normal",
        "pokemon_id": 493,
        "id": 493
    },
    {
        "pokemon_name": "Red-Striped Basculin",
        "form_label": "Red-Striped Form",
        "identifier": "red-striped",
        "pokemon_id": 550,
        "id": 550
    },
    {
        "pokemon_name": "Standard Darmanitan",
        "form_label": "Standard Mode",
        "identifier": "standard",
        "pokemon_id": 555,
        "id": 555
    },
    {
        "pokemon_name": "Spring Deerling",
        "form_label": "Spring Form",
        "identifier": "spring",
        "pokemon_id": 585,
        "id": 585
    },
    {
        "pokemon_name": "Spring Sawsbuck",
        "form_label": "Spring Form",
        "identifier": "spring",
        "pokemon_id": 586,
        "id": 586
    },
    {
        "pokemon_name": "Incarnate Tornadus",
        "form_label": "Incarnate Forme",
        "identifier": "incarnate",
        "pokemon_id": 641,
        "id": 641
    },
    {
        "pokemon_name": "Incarnate Thundurus",
        "form_label": "Incarnate Forme",
        "identifier": "incarnate",
        "pokemon_id": 642,
        "id": 642
    },
    {
        "pokemon_name": "Incarnate Landorus",
        "form_label": "Incarnate Forme",
        "identifier": "incarnate",
        "pokemon_id": 645,
        "id": 645
    },
    {
        "pokemon_name": "Ordinary Keldeo",
        "form_label": "Ordinary Form",
        "identifier": "ordinary",
        "pokemon_id": 647,
        "id": 647
    },
    {
        "pokemon_name": "Aria Meloetta",
        "form_label": "Aria Forme",
        "identifier": "aria",
        "pokemon_id": 648,
        "id": 648
    },
    {
        "pokemon_name": "Meadow Vivillon",
        "form_label": "Meadow Pattern",
        "identifier": "meadow",
        "pokemon_id": 666,
        "id": 666
    },
    {
        "pokemon_name": "Red Flabébé",
        "form_label": "Red Flower",
        "identifier": "red",
        "pokemon_id": 669,
        "id": 669
    },
    {
        "pokemon_name": "Red Floette",
        "form_label": "Red Flower",
        "identifier": "red",
        "pokemon_id": 670,
        "id": 670
    },
    {
        "pokemon_name": "Red Florges",
        "form_label": "Red Flower",
        "identifier": "red",
        "pokemon_id": 671,
        "id": 671
    },
    {
        "pokemon_name": "Natural Furfrou",
        "form_label": "Natural Form",
        "identifier": "natural",
        "pokemon_id": 676,
        "id": 676
    },
    {
        "pokemon_name": "Male Meowstic",
        "form_label": "Male",
        "identifier": "male",
        "pokemon_id": 678,
        "id": 678
    },
    {
        "pokemon_name": "Shield Aegislash",
        "form_label": "Shield Forme",
        "identifier": "shield",
        "pokemon_id": 681,
        "id": 681
    },
    {
        "pokemon_name": "Average Pumpkaboo",
        "form_label": "Average Size",
        "identifier": "average",
        "pokemon_id": 710,
        "id": 710
    },
    {
        "pokemon_name": "Average Gourgeist",
        "form_label": "Average Size",
        "identifier": "average",
        "pokemon_id": 711,
        "id": 711
    },
    {
        "pokemon_name": "Active Xerneas",
        "form_label": "Active Mode",
        "identifier": "active",
        "pokemon_id": 716,
        "id": 716
    },
    {
        "pokemon_name": "Confined Hoopa",
        "form_label": "Hoopa Confined",
        "identifier": "confined",
        "pokemon_id": 720,
        "id": 720
    },
    {
        "pokemon_name": "Baile Oricorio",
        "form_label": "Baile Style",
        "identifier": "baile",
        "pokemon_id": 741,
        "id": 741
    },
    {
        "pokemon_name": "Midday Lycanroc",
        "form_label": "Midday Form",
        "identifier": "midday",
        "pokemon_id": 745,
        "id": 745
    },
    {
        "pokemon_name": "Solo Wishiwashi",
        "form_label": "Solo Form",
        "identifier": "solo",
        "pokemon_id": 746,
        "id": 746
    },
    {
        "pokemon_name": "Red Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "red-meteor",
        "pokemon_id": 774,
        "id": 774
    },
    {
        "pokemon_name": "Disguised Mimikyu",
        "form_label": "Disguised Form",
        "identifier": "disguised",
        "pokemon_id": 778,
        "id": 778
    },
    {
        "pokemon_name": "Unown B",
        "form_label": "B",
        "identifier": "b",
        "pokemon_id": 201,
        "id": 10001
    },
    {
        "pokemon_name": "Unown C",
        "form_label": "C",
        "identifier": "c",
        "pokemon_id": 201,
        "id": 10002
    },
    {
        "pokemon_name": "Unown D",
        "form_label": "D",
        "identifier": "d",
        "pokemon_id": 201,
        "id": 10003
    },
    {
        "pokemon_name": "Unown E",
        "form_label": "E",
        "identifier": "e",
        "pokemon_id": 201,
        "id": 10004
    },
    {
        "pokemon_name": "Unown F",
        "form_label": "F",
        "identifier": "f",
        "pokemon_id": 201,
        "id": 10005
    },
    {
        "pokemon_name": "Unown G",
        "form_label": "G",
        "identifier": "g",
        "pokemon_id": 201,
        "id": 10006
    },
    {
        "pokemon_name": "Unown H",
        "form_label": "H",
        "identifier": "h",
        "pokemon_id": 201,
        "id": 10007
    },
    {
        "pokemon_name": "Unown I",
        "form_label": "I",
        "identifier": "i",
        "pokemon_id": 201,
        "id": 10008
    },
    {
        "pokemon_name": "Unown J",
        "form_label": "J",
        "identifier": "j",
        "pokemon_id": 201,
        "id": 10009
    },
    {
        "pokemon_name": "Unown K",
        "form_label": "K",
        "identifier": "k",
        "pokemon_id": 201,
        "id": 10010
    },
    {
        "pokemon_name": "Unown L",
        "form_label": "L",
        "identifier": "l",
        "pokemon_id": 201,
        "id": 10011
    },
    {
        "pokemon_name": "Unown M",
        "form_label": "M",
        "identifier": "m",
        "pokemon_id": 201,
        "id": 10012
    },
    {
        "pokemon_name": "Unown N",
        "form_label": "N",
        "identifier": "n",
        "pokemon_id": 201,
        "id": 10013
    },
    {
        "pokemon_name": "Unown O",
        "form_label": "O",
        "identifier": "o",
        "pokemon_id": 201,
        "id": 10014
    },
    {
        "pokemon_name": "Unown P",
        "form_label": "P",
        "identifier": "p",
        "pokemon_id": 201,
        "id": 10015
    },
    {
        "pokemon_name": "Unown Q",
        "form_label": "Q",
        "identifier": "q",
        "pokemon_id": 201,
        "id": 10016
    },
    {
        "pokemon_name": "Unown R",
        "form_label": "R",
        "identifier": "r",
        "pokemon_id": 201,
        "id": 10017
    },
    {
        "pokemon_name": "Unown S",
        "form_label": "S",
        "identifier": "s",
        "pokemon_id": 201,
        "id": 10018
    },
    {
        "pokemon_name": "Unown T",
        "form_label": "T",
        "identifier": "t",
        "pokemon_id": 201,
        "id": 10019
    },
    {
        "pokemon_name": "Unown U",
        "form_label": "U",
        "identifier": "u",
        "pokemon_id": 201,
        "id": 10020
    },
    {
        "pokemon_name": "Unown V",
        "form_label": "V",
        "identifier": "v",
        "pokemon_id": 201,
        "id": 10021
    },
    {
        "pokemon_name": "Unown W",
        "form_label": "W",
        "identifier": "w",
        "pokemon_id": 201,
        "id": 10022
    },
    {
        "pokemon_name": "Unown X",
        "form_label": "X",
        "identifier": "x",
        "pokemon_id": 201,
        "id": 10023
    },
    {
        "pokemon_name": "Unown Y",
        "form_label": "Y",
        "identifier": "y",
        "pokemon_id": 201,
        "id": 10024
    },
    {
        "pokemon_name": "Unown Z",
        "form_label": "Z",
        "identifier": "z",
        "pokemon_id": 201,
        "id": 10025
    },
    {
        "pokemon_name": "Unown !",
        "form_label": "!",
        "identifier": "exclamation",
        "pokemon_id": 201,
        "id": 10026
    },
    {
        "pokemon_name": "Unown ?",
        "form_label": "?",
        "identifier": "question",
        "pokemon_id": 201,
        "id": 10027
    },
    {
        "pokemon_name": "Sunny Castform",
        "form_label": "Sunny Form",
        "identifier": "sunny",
        "pokemon_id": 351,
        "id": 10028
    },
    {
        "pokemon_name": "Rainy Castform",
        "form_label": "Rainy Form",
        "identifier": "rainy",
        "pokemon_id": 351,
        "id": 10029
    },
    {
        "pokemon_name": "Snowy Castform",
        "form_label": "Snowy Form",
        "identifier": "snowy",
        "pokemon_id": 351,
        "id": 10030
    },
    {
        "pokemon_name": "Attack Deoxys",
        "form_label": "Attack Forme",
        "identifier": "attack",
        "pokemon_id": 386,
        "id": 10031
    },
    {
        "pokemon_name": "Defense Deoxys",
        "form_label": "Defense Forme",
        "identifier": "defense",
        "pokemon_id": 386,
        "id": 10032
    },
    {
        "pokemon_name": "Speed Deoxys",
        "form_label": "Speed Forme",
        "identifier": "speed",
        "pokemon_id": 386,
        "id": 10033
    },
    {
        "pokemon_name": "Sandy Burmy",
        "form_label": "Sandy Cloak",
        "identifier": "sandy",
        "pokemon_id": 412,
        "id": 10034
    },
    {
        "pokemon_name": "Trash Burmy",
        "form_label": "Trash Cloak",
        "identifier": "trash",
        "pokemon_id": 412,
        "id": 10035
    },
    {
        "pokemon_name": "Sandy Wormadam",
        "form_label": "Sandy Cloak",
        "identifier": "sandy",
        "pokemon_id": 413,
        "id": 10036
    },
    {
        "pokemon_name": "Trash Wormadam",
        "form_label": "Trash Cloak",
        "identifier": "trash",
        "pokemon_id": 413,
        "id": 10037
    },
    {
        "pokemon_name": "Sunshine Cherrim",
        "form_label": "Sunshine Form",
        "identifier": "sunshine",
        "pokemon_id": 421,
        "id": 10038
    },
    {
        "pokemon_name": "East Shellos",
        "form_label": "East Sea",
        "identifier": "east",
        "pokemon_id": 422,
        "id": 10039
    },
    {
        "pokemon_name": "East Gastrodon",
        "form_label": "East Sea",
        "identifier": "east",
        "pokemon_id": 423,
        "id": 10040
    },
    {
        "pokemon_name": "Bug Arceus",
        "form_label": "Bug Type",
        "identifier": "bug",
        "pokemon_id": 493,
        "id": 10041
    },
    {
        "pokemon_name": "Dark Arceus",
        "form_label": "Dark Type",
        "identifier": "dark",
        "pokemon_id": 493,
        "id": 10042
    },
    {
        "pokemon_name": "Dragon Arceus",
        "form_label": "Dragon Type",
        "identifier": "dragon",
        "pokemon_id": 493,
        "id": 10043
    },
    {
        "pokemon_name": "Electric Arceus",
        "form_label": "Electric Type",
        "identifier": "electric",
        "pokemon_id": 493,
        "id": 10044
    },
    {
        "pokemon_name": "Fighting Arceus",
        "form_label": "Fighting Type",
        "identifier": "fighting",
        "pokemon_id": 493,
        "id": 10045
    },
    {
        "pokemon_name": "Fire Arceus",
        "form_label": "Fire Type",
        "identifier": "fire",
        "pokemon_id": 493,
        "id": 10046
    },
    {
        "pokemon_name": "Flying Arceus",
        "form_label": "Flying Type",
        "identifier": "flying",
        "pokemon_id": 493,
        "id": 10047
    },
    {
        "pokemon_name": "Ghost Arceus",
        "form_label": "Ghost Type",
        "identifier": "ghost",
        "pokemon_id": 493,
        "id": 10048
    },
    {
        "pokemon_name": "Grass Arceus",
        "form_label": "Grass Type",
        "identifier": "grass",
        "pokemon_id": 493,
        "id": 10049
    },
    {
        "pokemon_name": "Ground Arceus",
        "form_label": "Ground Type",
        "identifier": "ground",
        "pokemon_id": 493,
        "id": 10050
    },
    {
        "pokemon_name": "Ice Arceus",
        "form_label": "Ice Type",
        "identifier": "ice",
        "pokemon_id": 493,
        "id": 10051
    },
    {
        "pokemon_name": "Poison Arceus",
        "form_label": "Poison Type",
        "identifier": "poison",
        "pokemon_id": 493,
        "id": 10052
    },
    {
        "pokemon_name": "Psychic Arceus",
        "form_label": "Psychic Type",
        "identifier": "psychic",
        "pokemon_id": 493,
        "id": 10053
    },
    {
        "pokemon_name": "Rock Arceus",
        "form_label": "Rock Type",
        "identifier": "rock",
        "pokemon_id": 493,
        "id": 10054
    },
    {
        "pokemon_name": "Steel Arceus",
        "form_label": "Steel Type",
        "identifier": "steel",
        "pokemon_id": 493,
        "id": 10055
    },
    {
        "pokemon_name": "Water Arceus",
        "form_label": "Water Type",
        "identifier": "water",
        "pokemon_id": 493,
        "id": 10056
    },
    {
        "pokemon_name": "??? Arceus",
        "form_label": "??? Type",
        "identifier": "unknown",
        "pokemon_id": 493,
        "id": 10057
    },
    {
        "pokemon_name": "Heat Rotom",
        "form_label": "Heat Rotom",
        "identifier": "heat",
        "pokemon_id": 479,
        "id": 10058
    },
    {
        "pokemon_name": "Wash Rotom",
        "form_label": "Wash Rotom",
        "identifier": "wash",
        "pokemon_id": 479,
        "id": 10059
    },
    {
        "pokemon_name": "Frost Rotom",
        "form_label": "Frost Rotom",
        "identifier": "frost",
        "pokemon_id": 479,
        "id": 10060
    },
    {
        "pokemon_name": "Fan Rotom",
        "form_label": "Fan Rotom",
        "identifier": "fan",
        "pokemon_id": 479,
        "id": 10061
    },
    {
        "pokemon_name": "Mow Rotom",
        "form_label": "Mow Rotom",
        "identifier": "mow",
        "pokemon_id": 479,
        "id": 10062
    },
    {
        "pokemon_name": "Origin Giratina",
        "form_label": "Origin Forme",
        "identifier": "origin",
        "pokemon_id": 487,
        "id": 10063
    },
    {
        "pokemon_name": "Sky Shaymin",
        "form_label": "Sky Forme",
        "identifier": "sky",
        "pokemon_id": 492,
        "id": 10064
    },
    {
        "pokemon_name": "Spiky-eared Pichu",
        "form_label": "Spiky-eared",
        "identifier": "spiky-eared",
        "pokemon_id": 172,
        "id": 10065
    },
    {
        "pokemon_name": "Blue-Striped Basculin",
        "form_label": "Blue-Striped Form",
        "identifier": "blue-striped",
        "pokemon_id": 550,
        "id": 10066
    },
    {
        "pokemon_name": "Zen Darmanitan",
        "form_label": "Zen Mode",
        "identifier": "zen",
        "pokemon_id": 555,
        "id": 10067
    },
    {
        "pokemon_name": "Summer Deerling",
        "form_label": "Summer Form",
        "identifier": "summer",
        "pokemon_id": 585,
        "id": 10068
    },
    {
        "pokemon_name": "Autumn Deerling",
        "form_label": "Autumn Form",
        "identifier": "autumn",
        "pokemon_id": 585,
        "id": 10069
    },
    {
        "pokemon_name": "Winter Deerling",
        "form_label": "Winter Form",
        "identifier": "winter",
        "pokemon_id": 585,
        "id": 10070
    },
    {
        "pokemon_name": "Summer Sawsbuck",
        "form_label": "Summer Form",
        "identifier": "summer",
        "pokemon_id": 586,
        "id": 10071
    },
    {
        "pokemon_name": "Autumn Sawsbuck",
        "form_label": "Autumn Form",
        "identifier": "autumn",
        "pokemon_id": 586,
        "id": 10072
    },
    {
        "pokemon_name": "Winter Sawsbuck",
        "form_label": "Winter Form",
        "identifier": "winter",
        "pokemon_id": 586,
        "id": 10073
    },
    {
        "pokemon_name": "Pirouette Meloetta",
        "form_label": "Pirouette Forme",
        "identifier": "pirouette",
        "pokemon_id": 648,
        "id": 10074
    },
    {
        "pokemon_name": "Douse Genesect",
        "form_label": "Douse Drive",
        "identifier": "douse",
        "pokemon_id": 649,
        "id": 10075
    },
    {
        "pokemon_name": "Shock Genesect",
        "form_label": "Shock Drive",
        "identifier": "shock",
        "pokemon_id": 649,
        "id": 10076
    },
    {
        "pokemon_name": "Burn Genesect",
        "form_label": "Burn Drive",
        "identifier": "burn",
        "pokemon_id": 649,
        "id": 10077
    },
    {
        "pokemon_name": "Chill Genesect",
        "form_label": "Chill Drive",
        "identifier": "chill",
        "pokemon_id": 649,
        "id": 10078
    },
    {
        "pokemon_name": "Therian Tornadus",
        "form_label": "Therian Forme",
        "identifier": "therian",
        "pokemon_id": 641,
        "id": 10079
    },
    {
        "pokemon_name": "Therian Thundurus",
        "form_label": "Therian Forme",
        "identifier": "therian",
        "pokemon_id": 642,
        "id": 10080
    },
    {
        "pokemon_name": "Therian Landorus",
        "form_label": "Therian Forme",
        "identifier": "therian",
        "pokemon_id": 645,
        "id": 10081
    },
    {
        "pokemon_name": "Black Kyurem",
        "form_label": "Black Kyurem",
        "identifier": "black",
        "pokemon_id": 646,
        "id": 10082
    },
    {
        "pokemon_name": "White Kyurem",
        "form_label": "White Kyurem",
        "identifier": "white",
        "pokemon_id": 646,
        "id": 10083
    },
    {
        "pokemon_name": "Resolute Keldeo",
        "form_label": "Resolute Form",
        "identifier": "resolute",
        "pokemon_id": 647,
        "id": 10084
    },
    {
        "pokemon_name": "Fairy Arceus",
        "form_label": "Fairy Type",
        "identifier": "fairy",
        "pokemon_id": 493,
        "id": 10085
    },
    {
        "pokemon_name": "Icy Snow Vivillon",
        "form_label": "Icy Snow Pattern",
        "identifier": "icy-snow",
        "pokemon_id": 666,
        "id": 10086
    },
    {
        "pokemon_name": "Polar Vivillon",
        "form_label": "Polar Pattern",
        "identifier": "polar",
        "pokemon_id": 666,
        "id": 10087
    },
    {
        "pokemon_name": "Tundra Vivillon",
        "form_label": "Tundra Pattern",
        "identifier": "tundra",
        "pokemon_id": 666,
        "id": 10088
    },
    {
        "pokemon_name": "Continental Vivillon",
        "form_label": "Continental Pattern",
        "identifier": "continental",
        "pokemon_id": 666,
        "id": 10089
    },
    {
        "pokemon_name": "Garden Vivillon",
        "form_label": "Garden Pattern",
        "identifier": "garden",
        "pokemon_id": 666,
        "id": 10090
    },
    {
        "pokemon_name": "Elegant Vivillon",
        "form_label": "Elegant Pattern",
        "identifier": "elegant",
        "pokemon_id": 666,
        "id": 10091
    },
    {
        "pokemon_name": "Modern Vivillon",
        "form_label": "Modern Pattern",
        "identifier": "modern",
        "pokemon_id": 666,
        "id": 10092
    },
    {
        "pokemon_name": "Marine Vivillon",
        "form_label": "Marine Pattern",
        "identifier": "marine",
        "pokemon_id": 666,
        "id": 10093
    },
    {
        "pokemon_name": "Archipelago Vivillon",
        "form_label": "Archipelago Pattern",
        "identifier": "archipelago",
        "pokemon_id": 666,
        "id": 10094
    },
    {
        "pokemon_name": "High Plains Vivillon",
        "form_label": "High Plains Pattern",
        "identifier": "high-plains",
        "pokemon_id": 666,
        "id": 10095
    },
    {
        "pokemon_name": "Sandstorm Vivillon",
        "form_label": "Sandstorm Pattern",
        "identifier": "sandstorm",
        "pokemon_id": 666,
        "id": 10096
    },
    {
        "pokemon_name": "River Vivillon",
        "form_label": "River Pattern",
        "identifier": "river",
        "pokemon_id": 666,
        "id": 10097
    },
    {
        "pokemon_name": "Monsoon Vivillon",
        "form_label": "Monsoon Pattern",
        "identifier": "monsoon",
        "pokemon_id": 666,
        "id": 10098
    },
    {
        "pokemon_name": "Savanna Vivillon",
        "form_label": "Savanna Pattern",
        "identifier": "savanna",
        "pokemon_id": 666,
        "id": 10099
    },
    {
        "pokemon_name": "Sun Vivillon",
        "form_label": "Sun Pattern",
        "identifier": "sun",
        "pokemon_id": 666,
        "id": 10100
    },
    {
        "pokemon_name": "Ocean Vivillon",
        "form_label": "Ocean Pattern",
        "identifier": "ocean",
        "pokemon_id": 666,
        "id": 10101
    },
    {
        "pokemon_name": "Jungle Vivillon",
        "form_label": "Jungle Pattern",
        "identifier": "jungle",
        "pokemon_id": 666,
        "id": 10102
    },
    {
        "pokemon_name": "Yellow Flabébé",
        "form_label": "Yellow Flower",
        "identifier": "yellow",
        "pokemon_id": 669,
        "id": 10103
    },
    {
        "pokemon_name": "Orange Flabébé",
        "form_label": "Orange Flower",
        "identifier": "orange",
        "pokemon_id": 669,
        "id": 10104
    },
    {
        "pokemon_name": "Blue Flabébé",
        "form_label": "Blue Flower",
        "identifier": "blue",
        "pokemon_id": 669,
        "id": 10105
    },
    {
        "pokemon_name": "White Flabébé",
        "form_label": "White Flower",
        "identifier": "white",
        "pokemon_id": 669,
        "id": 10106
    },
    {
        "pokemon_name": "Yellow Floette",
        "form_label": "Yellow Flower",
        "identifier": "yellow",
        "pokemon_id": 670,
        "id": 10107
    },
    {
        "pokemon_name": "Orange Floette",
        "form_label": "Orange Flower",
        "identifier": "orange",
        "pokemon_id": 670,
        "id": 10108
    },
    {
        "pokemon_name": "Blue Floette",
        "form_label": "Blue Flower",
        "identifier": "blue",
        "pokemon_id": 670,
        "id": 10109
    },
    {
        "pokemon_name": "White Floette",
        "form_label": "White Flower",
        "identifier": "white",
        "pokemon_id": 670,
        "id": 10110
    },
    {
        "pokemon_name": "Yellow Florges",
        "form_label": "Yellow Flower",
        "identifier": "yellow",
        "pokemon_id": 671,
        "id": 10111
    },
    {
        "pokemon_name": "Orange Florges",
        "form_label": "Orange Flower",
        "identifier": "orange",
        "pokemon_id": 671,
        "id": 10112
    },
    {
        "pokemon_name": "Blue Florges",
        "form_label": "Blue Flower",
        "identifier": "blue",
        "pokemon_id": 671,
        "id": 10113
    },
    {
        "pokemon_name": "White Florges",
        "form_label": "White Flower",
        "identifier": "white",
        "pokemon_id": 671,
        "id": 10114
    },
    {
        "pokemon_name": "Heart Furfrou",
        "form_label": "Heart Trim",
        "identifier": "heart",
        "pokemon_id": 676,
        "id": 10115
    },
    {
        "pokemon_name": "Star Furfrou",
        "form_label": "Star Trim",
        "identifier": "star",
        "pokemon_id": 676,
        "id": 10116
    },
    {
        "pokemon_name": "Diamond Furfrou",
        "form_label": "Diamond Trim",
        "identifier": "diamond",
        "pokemon_id": 676,
        "id": 10117
    },
    {
        "pokemon_name": "Debutante Furfrou",
        "form_label": "Debutante Trim",
        "identifier": "debutante",
        "pokemon_id": 676,
        "id": 10118
    },
    {
        "pokemon_name": "Matron Furfrou",
        "form_label": "Matron Trim",
        "identifier": "matron",
        "pokemon_id": 676,
        "id": 10119
    },
    {
        "pokemon_name": "Dandy Furfrou",
        "form_label": "Dandy Trim",
        "identifier": "dandy",
        "pokemon_id": 676,
        "id": 10120
    },
    {
        "pokemon_name": "La Reine Furfrou",
        "form_label": "La Reine Trim",
        "identifier": "la-reine",
        "pokemon_id": 676,
        "id": 10121
    },
    {
        "pokemon_name": "Kabuki Furfrou",
        "form_label": "Kabuki Trim",
        "identifier": "kabuki",
        "pokemon_id": 676,
        "id": 10122
    },
    {
        "pokemon_name": "Pharaoh Furfrou",
        "form_label": "Pharaoh Trim",
        "identifier": "pharaoh",
        "pokemon_id": 676,
        "id": 10123
    },
    {
        "pokemon_name": "Female Meowstic",
        "form_label": "Female",
        "identifier": "female",
        "pokemon_id": 678,
        "id": 10124
    },
    {
        "pokemon_name": "Blade Aegislash",
        "form_label": "Blade Forme",
        "identifier": "blade",
        "pokemon_id": 681,
        "id": 10125
    },
    {
        "pokemon_name": "Small Pumpkaboo",
        "form_label": "Small Size",
        "identifier": "small",
        "pokemon_id": 710,
        "id": 10126
    },
    {
        "pokemon_name": "Large Pumpkaboo",
        "form_label": "Large Size",
        "identifier": "large",
        "pokemon_id": 710,
        "id": 10127
    },
    {
        "pokemon_name": "Super Pumpkaboo",
        "form_label": "Super Size",
        "identifier": "super",
        "pokemon_id": 710,
        "id": 10128
    },
    {
        "pokemon_name": "Small Gourgeist",
        "form_label": "Small Size",
        "identifier": "small",
        "pokemon_id": 711,
        "id": 10129
    },
    {
        "pokemon_name": "Large Gourgeist",
        "form_label": "Large Size",
        "identifier": "large",
        "pokemon_id": 711,
        "id": 10130
    },
    {
        "pokemon_name": "Super Gourgeist",
        "form_label": "Super Size",
        "identifier": "super",
        "pokemon_id": 711,
        "id": 10131
    },
    {
        "pokemon_name": "Neutral Xerneas",
        "form_label": "Neutral Mode",
        "identifier": "neutral",
        "pokemon_id": 716,
        "id": 10132
    },
    {
        "pokemon_name": "Mega Venusaur",
        "form_label": "Mega Venusaur",
        "identifier": "mega",
        "pokemon_id": 3,
        "id": 10133
    },
    {
        "pokemon_name": "Mega Charizard X",
        "form_label": "Mega Charizard X",
        "identifier": "mega-x",
        "pokemon_id": 6,
        "id": 10134
    },
    {
        "pokemon_name": "Mega Charizard Y",
        "form_label": "Mega Charizard Y",
        "identifier": "mega-y",
        "pokemon_id": 6,
        "id": 10135
    },
    {
        "pokemon_name": "Mega Blastoise",
        "form_label": "Mega Blastoise",
        "identifier": "mega",
        "pokemon_id": 9,
        "id": 10136
    },
    {
        "pokemon_name": "Mega Alakazam",
        "form_label": "Mega Alakazam",
        "identifier": "mega",
        "pokemon_id": 65,
        "id": 10137
    },
    {
        "pokemon_name": "Mega Gengar",
        "form_label": "Mega Gengar",
        "identifier": "mega",
        "pokemon_id": 94,
        "id": 10138
    },
    {
        "pokemon_name": "Mega Kangaskhan",
        "form_label": "Mega Kangaskhan",
        "identifier": "mega",
        "pokemon_id": 115,
        "id": 10139
    },
    {
        "pokemon_name": "Mega Pinsir",
        "form_label": "Mega Pinsir",
        "identifier": "mega",
        "pokemon_id": 127,
        "id": 10140
    },
    {
        "pokemon_name": "Mega Gyarados",
        "form_label": "Mega Gyarados",
        "identifier": "mega",
        "pokemon_id": 130,
        "id": 10141
    },
    {
        "pokemon_name": "Mega Aerodactyl",
        "form_label": "Mega Aerodactyl",
        "identifier": "mega",
        "pokemon_id": 142,
        "id": 10142
    },
    {
        "pokemon_name": "Mega Mewtwo X",
        "form_label": "Mega Mewtwo X",
        "identifier": "mega-x",
        "pokemon_id": 150,
        "id": 10143
    },
    {
        "pokemon_name": "Mega Mewtwo Y",
        "form_label": "Mega Mewtwo Y",
        "identifier": "mega-y",
        "pokemon_id": 150,
        "id": 10144
    },
    {
        "pokemon_name": "Mega Ampharos",
        "form_label": "Mega Ampharos",
        "identifier": "mega",
        "pokemon_id": 181,
        "id": 10145
    },
    {
        "pokemon_name": "Mega Scizor",
        "form_label": "Mega Scizor",
        "identifier": "mega",
        "pokemon_id": 212,
        "id": 10146
    },
    {
        "pokemon_name": "Mega Heracross",
        "form_label": "Mega Heracross",
        "identifier": "mega",
        "pokemon_id": 214,
        "id": 10147
    },
    {
        "pokemon_name": "Mega Houndoom",
        "form_label": "Mega Houndoom",
        "identifier": "mega",
        "pokemon_id": 229,
        "id": 10148
    },
    {
        "pokemon_name": "Mega Tyranitar",
        "form_label": "Mega Tyranitar",
        "identifier": "mega",
        "pokemon_id": 248,
        "id": 10149
    },
    {
        "pokemon_name": "Mega Blaziken",
        "form_label": "Mega Blaziken",
        "identifier": "mega",
        "pokemon_id": 257,
        "id": 10150
    },
    {
        "pokemon_name": "Mega Gardevoir",
        "form_label": "Mega Gardevoir",
        "identifier": "mega",
        "pokemon_id": 282,
        "id": 10151
    },
    {
        "pokemon_name": "Mega Mawile",
        "form_label": "Mega Mawile",
        "identifier": "mega",
        "pokemon_id": 303,
        "id": 10152
    },
    {
        "pokemon_name": "Mega Aggron",
        "form_label": "Mega Aggron",
        "identifier": "mega",
        "pokemon_id": 306,
        "id": 10153
    },
    {
        "pokemon_name": "Mega Medicham",
        "form_label": "Mega Medicham",
        "identifier": "mega",
        "pokemon_id": 308,
        "id": 10154
    },
    {
        "pokemon_name": "Mega Manectric",
        "form_label": "Mega Manectric",
        "identifier": "mega",
        "pokemon_id": 310,
        "id": 10155
    },
    {
        "pokemon_name": "Mega Banette",
        "form_label": "Mega Banette",
        "identifier": "mega",
        "pokemon_id": 354,
        "id": 10156
    },
    {
        "pokemon_name": "Mega Absol",
        "form_label": "Mega Absol",
        "identifier": "mega",
        "pokemon_id": 359,
        "id": 10157
    },
    {
        "pokemon_name": "Mega Garchomp",
        "form_label": "Mega Garchomp",
        "identifier": "mega",
        "pokemon_id": 445,
        "id": 10158
    },
    {
        "pokemon_name": "Mega Lucario",
        "form_label": "Mega Lucario",
        "identifier": "mega",
        "pokemon_id": 448,
        "id": 10159
    },
    {
        "pokemon_name": "Mega Abomasnow",
        "form_label": "Mega Abomasnow",
        "identifier": "mega",
        "pokemon_id": 460,
        "id": 10160
    },
    {
        "pokemon_name": "Fancy Vivillon",
        "form_label": "Fancy Pattern",
        "identifier": "fancy",
        "pokemon_id": 666,
        "id": 10161
    },
    {
        "pokemon_name": "Poké Ball Vivillon",
        "form_label": "Poké Ball Pattern",
        "identifier": "poke-ball",
        "pokemon_id": 666,
        "id": 10162
    },
    {
        "pokemon_name": "Eternal Floette",
        "form_label": "Eternal Flower",
        "identifier": "eternal",
        "pokemon_id": 670,
        "id": 10163
    },
    {
        "pokemon_name": "Mega Latias",
        "form_label": "Mega Latias",
        "identifier": "mega",
        "pokemon_id": 380,
        "id": 10164
    },
    {
        "pokemon_name": "Mega Latios",
        "form_label": "Mega Latios",
        "identifier": "mega",
        "pokemon_id": 381,
        "id": 10165
    },
    {
        "pokemon_name": "Mega Swampert",
        "form_label": "Mega Swampert",
        "identifier": "mega",
        "pokemon_id": 260,
        "id": 10166
    },
    {
        "pokemon_name": "Mega Sceptile",
        "form_label": "Mega Sceptile",
        "identifier": "mega",
        "pokemon_id": 254,
        "id": 10167
    },
    {
        "pokemon_name": "Mega Sableye",
        "form_label": "Mega Sableye",
        "identifier": "mega",
        "pokemon_id": 302,
        "id": 10168
    },
    {
        "pokemon_name": "Mega Altaria",
        "form_label": "Mega Altaria",
        "identifier": "mega",
        "pokemon_id": 334,
        "id": 10169
    },
    {
        "pokemon_name": "Mega Gallade",
        "form_label": "Mega Gallade",
        "identifier": "mega",
        "pokemon_id": 475,
        "id": 10170
    },
    {
        "pokemon_name": "Mega Audino",
        "form_label": "Mega Audino",
        "identifier": "mega",
        "pokemon_id": 531,
        "id": 10171
    },
    {
        "pokemon_name": "Mega Sharpedo",
        "form_label": "Mega Sharpedo",
        "identifier": "mega",
        "pokemon_id": 319,
        "id": 10172
    },
    {
        "pokemon_name": "Mega Slowbro",
        "form_label": "Mega Slowbro",
        "identifier": "mega",
        "pokemon_id": 80,
        "id": 10173
    },
    {
        "pokemon_name": "Mega Steelix",
        "form_label": "Mega Steelix",
        "identifier": "mega",
        "pokemon_id": 208,
        "id": 10174
    },
    {
        "pokemon_name": "Mega Pidgeot",
        "form_label": "Mega Pidgeot",
        "identifier": "mega",
        "pokemon_id": 18,
        "id": 10175
    },
    {
        "pokemon_name": "Mega Glalie",
        "form_label": "Mega Glalie",
        "identifier": "mega",
        "pokemon_id": 362,
        "id": 10176
    },
    {
        "pokemon_name": "Mega Diancie",
        "form_label": "Mega Diancie",
        "identifier": "mega",
        "pokemon_id": 719,
        "id": 10177
    },
    {
        "pokemon_name": "Mega Metagross",
        "form_label": "Mega Metagross",
        "identifier": "mega",
        "pokemon_id": 376,
        "id": 10178
    },
    {
        "pokemon_name": "Primal Kyogre",
        "form_label": "Primal Reversion",
        "identifier": "primal",
        "pokemon_id": 382,
        "id": 10179
    },
    {
        "pokemon_name": "Primal Groudon",
        "form_label": "Primal Reversion",
        "identifier": "primal",
        "pokemon_id": 383,
        "id": 10180
    },
    {
        "pokemon_name": "Mega Rayquaza",
        "form_label": "Mega Rayquaza",
        "identifier": "mega",
        "pokemon_id": 384,
        "id": 10181
    },
    {
        "pokemon_name": "Pikachu Rock Star",
        "form_label": "Pikachu Rock Star",
        "identifier": "rock-star",
        "pokemon_id": 25,
        "id": 10182
    },
    {
        "pokemon_name": "Pikachu Belle",
        "form_label": "Pikachu Belle",
        "identifier": "belle",
        "pokemon_id": 25,
        "id": 10183
    },
    {
        "pokemon_name": "Pikachu Pop Star",
        "form_label": "Pikachu Pop Star",
        "identifier": "pop-star",
        "pokemon_id": 25,
        "id": 10184
    },
    {
        "pokemon_name": "Pikachu Ph.D.",
        "form_label": "Pikachu Ph.D.",
        "identifier": "phd",
        "pokemon_id": 25,
        "id": 10185
    },
    {
        "pokemon_name": "Pikachu Libre",
        "form_label": "Pikachu Libre",
        "identifier": "libre",
        "pokemon_id": 25,
        "id": 10186
    },
    {
        "pokemon_name": "Cosplay Pikachu",
        "form_label": "Cosplay Pikachu",
        "identifier": "cosplay",
        "pokemon_id": 25,
        "id": 10187
    },
    {
        "pokemon_name": "Hoopa Unbound",
        "form_label": "Hoopa Unbound",
        "identifier": "unbound",
        "pokemon_id": 720,
        "id": 10188
    },
    {
        "pokemon_name": "Mega Camerupt",
        "form_label": "Mega Camerupt",
        "identifier": "mega",
        "pokemon_id": 323,
        "id": 10189
    },
    {
        "pokemon_name": "Mega Lopunny",
        "form_label": "Mega Lopunny",
        "identifier": "mega",
        "pokemon_id": 428,
        "id": 10190
    },
    {
        "pokemon_name": "Mega Salamence",
        "form_label": "Mega Salamence",
        "identifier": "mega",
        "pokemon_id": 373,
        "id": 10191
    },
    {
        "pokemon_name": "Mega Beedrill",
        "form_label": "Mega Beedrill",
        "identifier": "mega",
        "pokemon_id": 15,
        "id": 10192
    },
    {
        "pokemon_name": "Alolan Rattata",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 19,
        "id": 10193
    },
    {
        "pokemon_name": "Alolan Raticate",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 20,
        "id": 10194
    },
    {
        "pokemon_name": "Totem Alolan Raticate",
        "form_label": "",
        "identifier": "totem-alola",
        "pokemon_id": 20,
        "id": 10195
    },
    {
        "pokemon_name": "Original Cap Pikachu",
        "form_label": "Original Cap",
        "identifier": "original-cap",
        "pokemon_id": 25,
        "id": 10196
    },
    {
        "pokemon_name": "Hoenn Cap Pikachu",
        "form_label": "Hoenn Cap",
        "identifier": "hoenn-cap",
        "pokemon_id": 25,
        "id": 10197
    },
    {
        "pokemon_name": "Sinnoh Cap Pikachu",
        "form_label": "Sinnoh Cap",
        "identifier": "sinnoh-cap",
        "pokemon_id": 25,
        "id": 10198
    },
    {
        "pokemon_name": "Unova Cap Pikachu",
        "form_label": "Unova Cap",
        "identifier": "unova-cap",
        "pokemon_id": 25,
        "id": 10199
    },
    {
        "pokemon_name": "Kalos Cap Pikachu",
        "form_label": "Kalos Cap",
        "identifier": "kalos-cap",
        "pokemon_id": 25,
        "id": 10200
    },
    {
        "pokemon_name": "Alola Cap Pikachu",
        "form_label": "Alola Cap",
        "identifier": "alola-cap",
        "pokemon_id": 25,
        "id": 10201
    },
    {
        "pokemon_name": "Alolan Raichu",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 26,
        "id": 10202
    },
    {
        "pokemon_name": "Alolan Sandshrew",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 27,
        "id": 10203
    },
    {
        "pokemon_name": "Alolan Sandslash",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 28,
        "id": 10204
    },
    {
        "pokemon_name": "Alolan Vulpix",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 37,
        "id": 10205
    },
    {
        "pokemon_name": "Alolan Ninetales",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 38,
        "id": 10206
    },
    {
        "pokemon_name": "Alolan Diglett",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 50,
        "id": 10207
    },
    {
        "pokemon_name": "Alolan Dugtrio",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 51,
        "id": 10208
    },
    {
        "pokemon_name": "Alolan Meowth",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 52,
        "id": 10209
    },
    {
        "pokemon_name": "Alolan Persian",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 53,
        "id": 10210
    },
    {
        "pokemon_name": "Alolan Geodude",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 74,
        "id": 10211
    },
    {
        "pokemon_name": "Alolan Graveler",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 75,
        "id": 10212
    },
    {
        "pokemon_name": "Alolan Golem",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 76,
        "id": 10213
    },
    {
        "pokemon_name": "Alolan Grimer",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 88,
        "id": 10214
    },
    {
        "pokemon_name": "Alolan Muk",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 89,
        "id": 10215
    },
    {
        "pokemon_name": "Alolan Exeggutor",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 103,
        "id": 10216
    },
    {
        "pokemon_name": "Alolan Marowak",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 105,
        "id": 10217
    },
    {
        "pokemon_name": "Battle Bond Greninja",
        "form_label": "",
        "identifier": "battle-bond",
        "pokemon_id": 658,
        "id": 10218
    },
    {
        "pokemon_name": "Ash's Greninja",
        "form_label": "Ash-Greninja",
        "identifier": "ash",
        "pokemon_id": 658,
        "id": 10219
    },
    {
        "pokemon_name": "10% Zygarde",
        "form_label": "10% Forme",
        "identifier": "10",
        "pokemon_id": 718,
        "id": 10220
    },
    {
        "pokemon_name": "50% Zygarde",
        "form_label": "50% Forme",
        "identifier": "50",
        "pokemon_id": 718,
        "id": 10221
    },
    {
        "pokemon_name": "Complete Zygarde",
        "form_label": "Complete Forme",
        "identifier": "complete",
        "pokemon_id": 718,
        "id": 10222
    },
    {
        "pokemon_name": "Totem Gumshoos",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 735,
        "id": 10223
    },
    {
        "pokemon_name": "Totem Vikavolt",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 738,
        "id": 10224
    },
    {
        "pokemon_name": "Pom-pom Oricorio",
        "form_label": "Pom-Pom Style",
        "identifier": "pom-pom",
        "pokemon_id": 741,
        "id": 10225
    },
    {
        "pokemon_name": "Pa’u Oricorio",
        "form_label": "Pa’u Style",
        "identifier": "pau",
        "pokemon_id": 741,
        "id": 10226
    },
    {
        "pokemon_name": "Sensu Oricorio",
        "form_label": "Sensu Style",
        "identifier": "sensu",
        "pokemon_id": 741,
        "id": 10227
    },
    {
        "pokemon_name": "Midnight Lycanroc",
        "form_label": "Midnight Form",
        "identifier": "midnight",
        "pokemon_id": 745,
        "id": 10228
    },
    {
        "pokemon_name": "School Wishiwashi",
        "form_label": "School Form",
        "identifier": "school",
        "pokemon_id": 746,
        "id": 10229
    },
    {
        "pokemon_name": "Totem Lurantis",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 754,
        "id": 10230
    },
    {
        "pokemon_name": "Totem Salazzle",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 758,
        "id": 10231
    },
    {
        "pokemon_name": "Orange Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "orange-meteor",
        "pokemon_id": 774,
        "id": 10249
    },
    {
        "pokemon_name": "Yellow Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "yellow-meteor",
        "pokemon_id": 774,
        "id": 10250
    },
    {
        "pokemon_name": "Green Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "green-meteor",
        "pokemon_id": 774,
        "id": 10251
    },
    {
        "pokemon_name": "Blue Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "blue-meteor",
        "pokemon_id": 774,
        "id": 10252
    },
    {
        "pokemon_name": "Indigo Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "indigo-meteor",
        "pokemon_id": 774,
        "id": 10253
    },
    {
        "pokemon_name": "Violent Meteor Minior",
        "form_label": "Meteor Form",
        "identifier": "violet-meteor",
        "pokemon_id": 774,
        "id": 10254
    },
    {
        "pokemon_name": "Red Core Minior",
        "form_label": "Red Core",
        "identifier": "red",
        "pokemon_id": 774,
        "id": 10255
    },
    {
        "pokemon_name": "Orange Core Minior",
        "form_label": "Orange Core",
        "identifier": "orange",
        "pokemon_id": 774,
        "id": 10256
    },
    {
        "pokemon_name": "Yellow Core Minior",
        "form_label": "Yellow Core",
        "identifier": "yellow",
        "pokemon_id": 774,
        "id": 10257
    },
    {
        "pokemon_name": "Green Core Minior",
        "form_label": "Green Core",
        "identifier": "green",
        "pokemon_id": 774,
        "id": 10258
    },
    {
        "pokemon_name": "Blue Core Minior",
        "form_label": "Blue Core",
        "identifier": "blue",
        "pokemon_id": 774,
        "id": 10259
    },
    {
        "pokemon_name": "Indigo Core Minior",
        "form_label": "Indigo Core",
        "identifier": "indigo",
        "pokemon_id": 774,
        "id": 10260
    },
    {
        "pokemon_name": "Violet Core Minior",
        "form_label": "Violet Core",
        "identifier": "violet",
        "pokemon_id": 774,
        "id": 10261
    },
    {
        "pokemon_name": "Busted Mimikyu",
        "form_label": "Busted Form",
        "identifier": "busted",
        "pokemon_id": 778,
        "id": 10262
    },
    {
        "pokemon_name": "Totem Disguised Mimikyu",
        "form_label": "",
        "identifier": "totem-disguised",
        "pokemon_id": 778,
        "id": 10263
    },
    {
        "pokemon_name": "Totem Busted Mimikyu",
        "form_label": "",
        "identifier": "totem-busted",
        "pokemon_id": 778,
        "id": 10264
    },
    {
        "pokemon_name": "Totem Kommo’o",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 784,
        "id": 10265
    },
    {
        "pokemon_name": "Original Magearna",
        "form_label": "Original Color",
        "identifier": "original",
        "pokemon_id": 801,
        "id": 10266
    },
    {
        "pokemon_name": "",
        "form_label": "Partner Cap",
        "identifier": "partner-cap",
        "pokemon_id": 25,
        "id": 10267
    },
    {
        "pokemon_name": "Totem Ribombee",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 743,
        "id": 10309
    },
    {
        "pokemon_name": "Own Tempo Rockruff",
        "form_label": "",
        "identifier": "own-tempo",
        "pokemon_id": 744,
        "id": 10310
    },
    {
        "pokemon_name": "Dusk Lycanroc",
        "form_label": "Dusk Form",
        "identifier": "dusk",
        "pokemon_id": 745,
        "id": 10311
    },
    {
        "pokemon_name": "Totem Araquanid",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 752,
        "id": 10312
    },
    {
        "pokemon_name": "Totem Togedemaru",
        "form_label": "",
        "identifier": "totem",
        "pokemon_id": 777,
        "id": 10313
    },
    {
        "pokemon_name": "Dusk Necrozma",
        "form_label": "Dusk Mane",
        "identifier": "dusk",
        "pokemon_id": 800,
        "id": 10314
    },
    {
        "pokemon_name": "Dawn Necrozma",
        "form_label": "Dawn Wings",
        "identifier": "dawn",
        "pokemon_id": 800,
        "id": 10315
    },
    {
        "pokemon_name": "Ultra Necrozma",
        "form_label": "Ultra Necrozma",
        "identifier": "ultra",
        "pokemon_id": 800,
        "id": 10316
    }
]

BASE_STATS = [
    {
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "special-attack": 65,
        "special-defense": 65,
        "speed": 45,
        "id": 1
    },
    {
        "hp": 60,
        "attack": 62,
        "defense": 63,
        "special-attack": 80,
        "special-defense": 80,
        "speed": 60,
        "id": 2
    },
    {
        "hp": 80,
        "attack": 82,
        "defense": 83,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 80,
        "id": 3
    },
    {
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "special-attack": 60,
        "special-defense": 50,
        "speed": 65,
        "id": 4
    },
    {
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "special-attack": 80,
        "special-defense": 65,
        "speed": 80,
        "id": 5
    },
    {
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "special-attack": 109,
        "special-defense": 85,
        "speed": 100,
        "id": 6
    },
    {
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "special-attack": 50,
        "special-defense": 64,
        "speed": 43,
        "id": 7
    },
    {
        "hp": 59,
        "attack": 63,
        "defense": 80,
        "special-attack": 65,
        "special-defense": 80,
        "speed": 58,
        "id": 8
    },
    {
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "special-attack": 85,
        "special-defense": 105,
        "speed": 78,
        "id": 9
    },
    {
        "hp": 45,
        "attack": 30,
        "defense": 35,
        "special-attack": 20,
        "special-defense": 20,
        "speed": 45,
        "id": 10
    },
    {
        "hp": 50,
        "attack": 20,
        "defense": 55,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 30,
        "id": 11
    },
    {
        "hp": 60,
        "attack": 45,
        "defense": 50,
        "special-attack": 90,
        "special-defense": 80,
        "speed": 70,
        "id": 12
    },
    {
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "special-attack": 20,
        "special-defense": 20,
        "speed": 50,
        "id": 13
    },
    {
        "hp": 45,
        "attack": 25,
        "defense": 50,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 35,
        "id": 14
    },
    {
        "hp": 65,
        "attack": 90,
        "defense": 40,
        "special-attack": 45,
        "special-defense": 80,
        "speed": 75,
        "id": 15
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 56,
        "id": 16
    },
    {
        "hp": 63,
        "attack": 60,
        "defense": 55,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 71,
        "id": 17
    },
    {
        "hp": 83,
        "attack": 80,
        "defense": 75,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 101,
        "id": 18
    },
    {
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "special-attack": 25,
        "special-defense": 35,
        "speed": 72,
        "id": 19
    },
    {
        "hp": 55,
        "attack": 81,
        "defense": 60,
        "special-attack": 50,
        "special-defense": 70,
        "speed": 97,
        "id": 20
    },
    {
        "hp": 40,
        "attack": 60,
        "defense": 30,
        "special-attack": 31,
        "special-defense": 31,
        "speed": 70,
        "id": 21
    },
    {
        "hp": 65,
        "attack": 90,
        "defense": 65,
        "special-attack": 61,
        "special-defense": 61,
        "speed": 100,
        "id": 22
    },
    {
        "hp": 35,
        "attack": 60,
        "defense": 44,
        "special-attack": 40,
        "special-defense": 54,
        "speed": 55,
        "id": 23
    },
    {
        "hp": 60,
        "attack": 95,
        "defense": 69,
        "special-attack": 65,
        "special-defense": 79,
        "speed": 80,
        "id": 24
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 25
    },
    {
        "hp": 60,
        "attack": 90,
        "defense": 55,
        "special-attack": 90,
        "special-defense": 80,
        "speed": 110,
        "id": 26
    },
    {
        "hp": 50,
        "attack": 75,
        "defense": 85,
        "special-attack": 20,
        "special-defense": 30,
        "speed": 40,
        "id": 27
    },
    {
        "hp": 75,
        "attack": 100,
        "defense": 110,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 65,
        "id": 28
    },
    {
        "hp": 55,
        "attack": 47,
        "defense": 52,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 41,
        "id": 29
    },
    {
        "hp": 70,
        "attack": 62,
        "defense": 67,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 56,
        "id": 30
    },
    {
        "hp": 90,
        "attack": 92,
        "defense": 87,
        "special-attack": 75,
        "special-defense": 85,
        "speed": 76,
        "id": 31
    },
    {
        "hp": 46,
        "attack": 57,
        "defense": 40,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 50,
        "id": 32
    },
    {
        "hp": 61,
        "attack": 72,
        "defense": 57,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 65,
        "id": 33
    },
    {
        "hp": 81,
        "attack": 102,
        "defense": 77,
        "special-attack": 85,
        "special-defense": 75,
        "speed": 85,
        "id": 34
    },
    {
        "hp": 70,
        "attack": 45,
        "defense": 48,
        "special-attack": 60,
        "special-defense": 65,
        "speed": 35,
        "id": 35
    },
    {
        "hp": 95,
        "attack": 70,
        "defense": 73,
        "special-attack": 95,
        "special-defense": 90,
        "speed": 60,
        "id": 36
    },
    {
        "hp": 38,
        "attack": 41,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 65,
        "speed": 65,
        "id": 37
    },
    {
        "hp": 73,
        "attack": 76,
        "defense": 75,
        "special-attack": 81,
        "special-defense": 100,
        "speed": 100,
        "id": 38
    },
    {
        "hp": 115,
        "attack": 45,
        "defense": 20,
        "special-attack": 45,
        "special-defense": 25,
        "speed": 20,
        "id": 39
    },
    {
        "hp": 140,
        "attack": 70,
        "defense": 45,
        "special-attack": 85,
        "special-defense": 50,
        "speed": 45,
        "id": 40
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "special-attack": 30,
        "special-defense": 40,
        "speed": 55,
        "id": 41
    },
    {
        "hp": 75,
        "attack": 80,
        "defense": 70,
        "special-attack": 65,
        "special-defense": 75,
        "speed": 90,
        "id": 42
    },
    {
        "hp": 45,
        "attack": 50,
        "defense": 55,
        "special-attack": 75,
        "special-defense": 65,
        "speed": 30,
        "id": 43
    },
    {
        "hp": 60,
        "attack": 65,
        "defense": 70,
        "special-attack": 85,
        "special-defense": 75,
        "speed": 40,
        "id": 44
    },
    {
        "hp": 75,
        "attack": 80,
        "defense": 85,
        "special-attack": 110,
        "special-defense": 90,
        "speed": 50,
        "id": 45
    },
    {
        "hp": 35,
        "attack": 70,
        "defense": 55,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 25,
        "id": 46
    },
    {
        "hp": 60,
        "attack": 95,
        "defense": 80,
        "special-attack": 60,
        "special-defense": 80,
        "speed": 30,
        "id": 47
    },
    {
        "hp": 60,
        "attack": 55,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 55,
        "speed": 45,
        "id": 48
    },
    {
        "hp": 70,
        "attack": 65,
        "defense": 60,
        "special-attack": 90,
        "special-defense": 75,
        "speed": 90,
        "id": 49
    },
    {
        "hp": 10,
        "attack": 55,
        "defense": 25,
        "special-attack": 35,
        "special-defense": 45,
        "speed": 95,
        "id": 50
    },
    {
        "hp": 35,
        "attack": 100,
        "defense": 50,
        "special-attack": 50,
        "special-defense": 70,
        "speed": 120,
        "id": 51
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 90,
        "id": 52
    },
    {
        "hp": 65,
        "attack": 70,
        "defense": 60,
        "special-attack": 65,
        "special-defense": 65,
        "speed": 115,
        "id": 53
    },
    {
        "hp": 50,
        "attack": 52,
        "defense": 48,
        "special-attack": 65,
        "special-defense": 50,
        "speed": 55,
        "id": 54
    },
    {
        "hp": 80,
        "attack": 82,
        "defense": 78,
        "special-attack": 95,
        "special-defense": 80,
        "speed": 85,
        "id": 55
    },
    {
        "hp": 40,
        "attack": 80,
        "defense": 35,
        "special-attack": 35,
        "special-defense": 45,
        "speed": 70,
        "id": 56
    },
    {
        "hp": 65,
        "attack": 105,
        "defense": 60,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 95,
        "id": 57
    },
    {
        "hp": 55,
        "attack": 70,
        "defense": 45,
        "special-attack": 70,
        "special-defense": 50,
        "speed": 60,
        "id": 58
    },
    {
        "hp": 90,
        "attack": 110,
        "defense": 80,
        "special-attack": 100,
        "special-defense": 80,
        "speed": 95,
        "id": 59
    },
    {
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 90,
        "id": 60
    },
    {
        "hp": 65,
        "attack": 65,
        "defense": 65,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 61
    },
    {
        "hp": 90,
        "attack": 95,
        "defense": 95,
        "special-attack": 70,
        "special-defense": 90,
        "speed": 70,
        "id": 62
    },
    {
        "hp": 25,
        "attack": 20,
        "defense": 15,
        "special-attack": 105,
        "special-defense": 55,
        "speed": 90,
        "id": 63
    },
    {
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "special-attack": 120,
        "special-defense": 70,
        "speed": 105,
        "id": 64
    },
    {
        "hp": 55,
        "attack": 50,
        "defense": 45,
        "special-attack": 135,
        "special-defense": 95,
        "speed": 120,
        "id": 65
    },
    {
        "hp": 70,
        "attack": 80,
        "defense": 50,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 35,
        "id": 66
    },
    {
        "hp": 80,
        "attack": 100,
        "defense": 70,
        "special-attack": 50,
        "special-defense": 60,
        "speed": 45,
        "id": 67
    },
    {
        "hp": 90,
        "attack": 130,
        "defense": 80,
        "special-attack": 65,
        "special-defense": 85,
        "speed": 55,
        "id": 68
    },
    {
        "hp": 50,
        "attack": 75,
        "defense": 35,
        "special-attack": 70,
        "special-defense": 30,
        "speed": 40,
        "id": 69
    },
    {
        "hp": 65,
        "attack": 90,
        "defense": 50,
        "special-attack": 85,
        "special-defense": 45,
        "speed": 55,
        "id": 70
    },
    {
        "hp": 80,
        "attack": 105,
        "defense": 65,
        "special-attack": 100,
        "special-defense": 70,
        "speed": 70,
        "id": 71
    },
    {
        "hp": 40,
        "attack": 40,
        "defense": 35,
        "special-attack": 50,
        "special-defense": 100,
        "speed": 70,
        "id": 72
    },
    {
        "hp": 80,
        "attack": 70,
        "defense": 65,
        "special-attack": 80,
        "special-defense": 120,
        "speed": 100,
        "id": 73
    },
    {
        "hp": 40,
        "attack": 80,
        "defense": 100,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 20,
        "id": 74
    },
    {
        "hp": 55,
        "attack": 95,
        "defense": 115,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 35,
        "id": 75
    },
    {
        "hp": 80,
        "attack": 120,
        "defense": 130,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 45,
        "id": 76
    },
    {
        "hp": 50,
        "attack": 85,
        "defense": 55,
        "special-attack": 65,
        "special-defense": 65,
        "speed": 90,
        "id": 77
    },
    {
        "hp": 65,
        "attack": 100,
        "defense": 70,
        "special-attack": 80,
        "special-defense": 80,
        "speed": 105,
        "id": 78
    },
    {
        "hp": 90,
        "attack": 65,
        "defense": 65,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 15,
        "id": 79
    },
    {
        "hp": 95,
        "attack": 75,
        "defense": 110,
        "special-attack": 100,
        "special-defense": 80,
        "speed": 30,
        "id": 80
    },
    {
        "hp": 25,
        "attack": 35,
        "defense": 70,
        "special-attack": 95,
        "special-defense": 55,
        "speed": 45,
        "id": 81
    },
    {
        "hp": 50,
        "attack": 60,
        "defense": 95,
        "special-attack": 120,
        "special-defense": 70,
        "speed": 70,
        "id": 82
    },
    {
        "hp": 52,
        "attack": 90,
        "defense": 55,
        "special-attack": 58,
        "special-defense": 62,
        "speed": 60,
        "id": 83
    },
    {
        "hp": 35,
        "attack": 85,
        "defense": 45,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 75,
        "id": 84
    },
    {
        "hp": 60,
        "attack": 110,
        "defense": 70,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 110,
        "id": 85
    },
    {
        "hp": 65,
        "attack": 45,
        "defense": 55,
        "special-attack": 45,
        "special-defense": 70,
        "speed": 45,
        "id": 86
    },
    {
        "hp": 90,
        "attack": 70,
        "defense": 80,
        "special-attack": 70,
        "special-defense": 95,
        "speed": 70,
        "id": 87
    },
    {
        "hp": 80,
        "attack": 80,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 25,
        "id": 88
    },
    {
        "hp": 105,
        "attack": 105,
        "defense": 75,
        "special-attack": 65,
        "special-defense": 100,
        "speed": 50,
        "id": 89
    },
    {
        "hp": 30,
        "attack": 65,
        "defense": 100,
        "special-attack": 45,
        "special-defense": 25,
        "speed": 40,
        "id": 90
    },
    {
        "hp": 50,
        "attack": 95,
        "defense": 180,
        "special-attack": 85,
        "special-defense": 45,
        "speed": 70,
        "id": 91
    },
    {
        "hp": 30,
        "attack": 35,
        "defense": 30,
        "special-attack": 100,
        "special-defense": 35,
        "speed": 80,
        "id": 92
    },
    {
        "hp": 45,
        "attack": 50,
        "defense": 45,
        "special-attack": 115,
        "special-defense": 55,
        "speed": 95,
        "id": 93
    },
    {
        "hp": 60,
        "attack": 65,
        "defense": 60,
        "special-attack": 130,
        "special-defense": 75,
        "speed": 110,
        "id": 94
    },
    {
        "hp": 35,
        "attack": 45,
        "defense": 160,
        "special-attack": 30,
        "special-defense": 45,
        "speed": 70,
        "id": 95
    },
    {
        "hp": 60,
        "attack": 48,
        "defense": 45,
        "special-attack": 43,
        "special-defense": 90,
        "speed": 42,
        "id": 96
    },
    {
        "hp": 85,
        "attack": 73,
        "defense": 70,
        "special-attack": 73,
        "special-defense": 115,
        "speed": 67,
        "id": 97
    },
    {
        "hp": 30,
        "attack": 105,
        "defense": 90,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 50,
        "id": 98
    },
    {
        "hp": 55,
        "attack": 130,
        "defense": 115,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 75,
        "id": 99
    },
    {
        "hp": 40,
        "attack": 30,
        "defense": 50,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 100,
        "id": 100
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 70,
        "special-attack": 80,
        "special-defense": 80,
        "speed": 150,
        "id": 101
    },
    {
        "hp": 60,
        "attack": 40,
        "defense": 80,
        "special-attack": 60,
        "special-defense": 45,
        "speed": 40,
        "id": 102
    },
    {
        "hp": 95,
        "attack": 95,
        "defense": 85,
        "special-attack": 125,
        "special-defense": 75,
        "speed": 55,
        "id": 103
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 95,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 35,
        "id": 104
    },
    {
        "hp": 60,
        "attack": 80,
        "defense": 110,
        "special-attack": 50,
        "special-defense": 80,
        "speed": 45,
        "id": 105
    },
    {
        "hp": 50,
        "attack": 120,
        "defense": 53,
        "special-attack": 35,
        "special-defense": 110,
        "speed": 87,
        "id": 106
    },
    {
        "hp": 50,
        "attack": 105,
        "defense": 79,
        "special-attack": 35,
        "special-defense": 110,
        "speed": 76,
        "id": 107
    },
    {
        "hp": 90,
        "attack": 55,
        "defense": 75,
        "special-attack": 60,
        "special-defense": 75,
        "speed": 30,
        "id": 108
    },
    {
        "hp": 40,
        "attack": 65,
        "defense": 95,
        "special-attack": 60,
        "special-defense": 45,
        "speed": 35,
        "id": 109
    },
    {
        "hp": 65,
        "attack": 90,
        "defense": 120,
        "special-attack": 85,
        "special-defense": 70,
        "speed": 60,
        "id": 110
    },
    {
        "hp": 80,
        "attack": 85,
        "defense": 95,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 25,
        "id": 111
    },
    {
        "hp": 105,
        "attack": 130,
        "defense": 120,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 40,
        "id": 112
    },
    {
        "hp": 250,
        "attack": 5,
        "defense": 5,
        "special-attack": 35,
        "special-defense": 105,
        "speed": 50,
        "id": 113
    },
    {
        "hp": 65,
        "attack": 55,
        "defense": 115,
        "special-attack": 100,
        "special-defense": 40,
        "speed": 60,
        "id": 114
    },
    {
        "hp": 105,
        "attack": 95,
        "defense": 80,
        "special-attack": 40,
        "special-defense": 80,
        "speed": 90,
        "id": 115
    },
    {
        "hp": 30,
        "attack": 40,
        "defense": 70,
        "special-attack": 70,
        "special-defense": 25,
        "speed": 60,
        "id": 116
    },
    {
        "hp": 55,
        "attack": 65,
        "defense": 95,
        "special-attack": 95,
        "special-defense": 45,
        "speed": 85,
        "id": 117
    },
    {
        "hp": 45,
        "attack": 67,
        "defense": 60,
        "special-attack": 35,
        "special-defense": 50,
        "speed": 63,
        "id": 118
    },
    {
        "hp": 80,
        "attack": 92,
        "defense": 65,
        "special-attack": 65,
        "special-defense": 80,
        "speed": 68,
        "id": 119
    },
    {
        "hp": 30,
        "attack": 45,
        "defense": 55,
        "special-attack": 70,
        "special-defense": 55,
        "speed": 85,
        "id": 120
    },
    {
        "hp": 60,
        "attack": 75,
        "defense": 85,
        "special-attack": 100,
        "special-defense": 85,
        "speed": 115,
        "id": 121
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 65,
        "special-attack": 100,
        "special-defense": 120,
        "speed": 90,
        "id": 122
    },
    {
        "hp": 70,
        "attack": 110,
        "defense": 80,
        "special-attack": 55,
        "special-defense": 80,
        "speed": 105,
        "id": 123
    },
    {
        "hp": 65,
        "attack": 50,
        "defense": 35,
        "special-attack": 115,
        "special-defense": 95,
        "speed": 95,
        "id": 124
    },
    {
        "hp": 65,
        "attack": 83,
        "defense": 57,
        "special-attack": 95,
        "special-defense": 85,
        "speed": 105,
        "id": 125
    },
    {
        "hp": 65,
        "attack": 95,
        "defense": 57,
        "special-attack": 100,
        "special-defense": 85,
        "speed": 93,
        "id": 126
    },
    {
        "hp": 65,
        "attack": 125,
        "defense": 100,
        "special-attack": 55,
        "special-defense": 70,
        "speed": 85,
        "id": 127
    },
    {
        "hp": 75,
        "attack": 100,
        "defense": 95,
        "special-attack": 40,
        "special-defense": 70,
        "speed": 110,
        "id": 128
    },
    {
        "hp": 20,
        "attack": 10,
        "defense": 55,
        "special-attack": 15,
        "special-defense": 20,
        "speed": 80,
        "id": 129
    },
    {
        "hp": 95,
        "attack": 125,
        "defense": 79,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 81,
        "id": 130
    },
    {
        "hp": 130,
        "attack": 85,
        "defense": 80,
        "special-attack": 85,
        "special-defense": 95,
        "speed": 60,
        "id": 131
    },
    {
        "hp": 48,
        "attack": 48,
        "defense": 48,
        "special-attack": 48,
        "special-defense": 48,
        "speed": 48,
        "id": 132
    },
    {
        "hp": 55,
        "attack": 55,
        "defense": 50,
        "special-attack": 45,
        "special-defense": 65,
        "speed": 55,
        "id": 133
    },
    {
        "hp": 130,
        "attack": 65,
        "defense": 60,
        "special-attack": 110,
        "special-defense": 95,
        "speed": 65,
        "id": 134
    },
    {
        "hp": 65,
        "attack": 65,
        "defense": 60,
        "special-attack": 110,
        "special-defense": 95,
        "speed": 130,
        "id": 135
    },
    {
        "hp": 65,
        "attack": 130,
        "defense": 60,
        "special-attack": 95,
        "special-defense": 110,
        "speed": 65,
        "id": 136
    },
    {
        "hp": 65,
        "attack": 60,
        "defense": 70,
        "special-attack": 85,
        "special-defense": 75,
        "speed": 40,
        "id": 137
    },
    {
        "hp": 35,
        "attack": 40,
        "defense": 100,
        "special-attack": 90,
        "special-defense": 55,
        "speed": 35,
        "id": 138
    },
    {
        "hp": 70,
        "attack": 60,
        "defense": 125,
        "special-attack": 115,
        "special-defense": 70,
        "speed": 55,
        "id": 139
    },
    {
        "hp": 30,
        "attack": 80,
        "defense": 90,
        "special-attack": 55,
        "special-defense": 45,
        "speed": 55,
        "id": 140
    },
    {
        "hp": 60,
        "attack": 115,
        "defense": 105,
        "special-attack": 65,
        "special-defense": 70,
        "speed": 80,
        "id": 141
    },
    {
        "hp": 80,
        "attack": 105,
        "defense": 65,
        "special-attack": 60,
        "special-defense": 75,
        "speed": 130,
        "id": 142
    },
    {
        "hp": 160,
        "attack": 110,
        "defense": 65,
        "special-attack": 65,
        "special-defense": 110,
        "speed": 30,
        "id": 143
    },
    {
        "hp": 90,
        "attack": 85,
        "defense": 100,
        "special-attack": 95,
        "special-defense": 125,
        "speed": 85,
        "id": 144
    },
    {
        "hp": 90,
        "attack": 90,
        "defense": 85,
        "special-attack": 125,
        "special-defense": 90,
        "speed": 100,
        "id": 145
    },
    {
        "hp": 90,
        "attack": 100,
        "defense": 90,
        "special-attack": 125,
        "special-defense": 85,
        "speed": 90,
        "id": 146
    },
    {
        "hp": 41,
        "attack": 64,
        "defense": 45,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 50,
        "id": 147
    },
    {
        "hp": 61,
        "attack": 84,
        "defense": 65,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 70,
        "id": 148
    },
    {
        "hp": 91,
        "attack": 134,
        "defense": 95,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 80,
        "id": 149
    },
    {
        "hp": 106,
        "attack": 110,
        "defense": 90,
        "special-attack": 154,
        "special-defense": 90,
        "speed": 130,
        "id": 150
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 100,
        "id": 151
    },
    {
        "hp": 45,
        "attack": 49,
        "defense": 65,
        "special-attack": 49,
        "special-defense": 65,
        "speed": 45,
        "id": 152
    },
    {
        "hp": 60,
        "attack": 62,
        "defense": 80,
        "special-attack": 63,
        "special-defense": 80,
        "speed": 60,
        "id": 153
    },
    {
        "hp": 80,
        "attack": 82,
        "defense": 100,
        "special-attack": 83,
        "special-defense": 100,
        "speed": 80,
        "id": 154
    },
    {
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "special-attack": 60,
        "special-defense": 50,
        "speed": 65,
        "id": 155
    },
    {
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "special-attack": 80,
        "special-defense": 65,
        "speed": 80,
        "id": 156
    },
    {
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "special-attack": 109,
        "special-defense": 85,
        "speed": 100,
        "id": 157
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 64,
        "special-attack": 44,
        "special-defense": 48,
        "speed": 43,
        "id": 158
    },
    {
        "hp": 65,
        "attack": 80,
        "defense": 80,
        "special-attack": 59,
        "special-defense": 63,
        "speed": 58,
        "id": 159
    },
    {
        "hp": 85,
        "attack": 105,
        "defense": 100,
        "special-attack": 79,
        "special-defense": 83,
        "speed": 78,
        "id": 160
    },
    {
        "hp": 35,
        "attack": 46,
        "defense": 34,
        "special-attack": 35,
        "special-defense": 45,
        "speed": 20,
        "id": 161
    },
    {
        "hp": 85,
        "attack": 76,
        "defense": 64,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 90,
        "id": 162
    },
    {
        "hp": 60,
        "attack": 30,
        "defense": 30,
        "special-attack": 36,
        "special-defense": 56,
        "speed": 50,
        "id": 163
    },
    {
        "hp": 100,
        "attack": 50,
        "defense": 50,
        "special-attack": 86,
        "special-defense": 96,
        "speed": 70,
        "id": 164
    },
    {
        "hp": 40,
        "attack": 20,
        "defense": 30,
        "special-attack": 40,
        "special-defense": 80,
        "speed": 55,
        "id": 165
    },
    {
        "hp": 55,
        "attack": 35,
        "defense": 50,
        "special-attack": 55,
        "special-defense": 110,
        "speed": 85,
        "id": 166
    },
    {
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 30,
        "id": 167
    },
    {
        "hp": 70,
        "attack": 90,
        "defense": 70,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 40,
        "id": 168
    },
    {
        "hp": 85,
        "attack": 90,
        "defense": 80,
        "special-attack": 70,
        "special-defense": 80,
        "speed": 130,
        "id": 169
    },
    {
        "hp": 75,
        "attack": 38,
        "defense": 38,
        "special-attack": 56,
        "special-defense": 56,
        "speed": 67,
        "id": 170
    },
    {
        "hp": 125,
        "attack": 58,
        "defense": 58,
        "special-attack": 76,
        "special-defense": 76,
        "speed": 67,
        "id": 171
    },
    {
        "hp": 20,
        "attack": 40,
        "defense": 15,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 60,
        "id": 172
    },
    {
        "hp": 50,
        "attack": 25,
        "defense": 28,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 15,
        "id": 173
    },
    {
        "hp": 90,
        "attack": 30,
        "defense": 15,
        "special-attack": 40,
        "special-defense": 20,
        "speed": 15,
        "id": 174
    },
    {
        "hp": 35,
        "attack": 20,
        "defense": 65,
        "special-attack": 40,
        "special-defense": 65,
        "speed": 20,
        "id": 175
    },
    {
        "hp": 55,
        "attack": 40,
        "defense": 85,
        "special-attack": 80,
        "special-defense": 105,
        "speed": 40,
        "id": 176
    },
    {
        "hp": 40,
        "attack": 50,
        "defense": 45,
        "special-attack": 70,
        "special-defense": 45,
        "speed": 70,
        "id": 177
    },
    {
        "hp": 65,
        "attack": 75,
        "defense": 70,
        "special-attack": 95,
        "special-defense": 70,
        "speed": 95,
        "id": 178
    },
    {
        "hp": 55,
        "attack": 40,
        "defense": 40,
        "special-attack": 65,
        "special-defense": 45,
        "speed": 35,
        "id": 179
    },
    {
        "hp": 70,
        "attack": 55,
        "defense": 55,
        "special-attack": 80,
        "special-defense": 60,
        "speed": 45,
        "id": 180
    },
    {
        "hp": 90,
        "attack": 75,
        "defense": 85,
        "special-attack": 115,
        "special-defense": 90,
        "speed": 55,
        "id": 181
    },
    {
        "hp": 75,
        "attack": 80,
        "defense": 95,
        "special-attack": 90,
        "special-defense": 100,
        "speed": 50,
        "id": 182
    },
    {
        "hp": 70,
        "attack": 20,
        "defense": 50,
        "special-attack": 20,
        "special-defense": 50,
        "speed": 40,
        "id": 183
    },
    {
        "hp": 100,
        "attack": 50,
        "defense": 80,
        "special-attack": 60,
        "special-defense": 80,
        "speed": 50,
        "id": 184
    },
    {
        "hp": 70,
        "attack": 100,
        "defense": 115,
        "special-attack": 30,
        "special-defense": 65,
        "speed": 30,
        "id": 185
    },
    {
        "hp": 90,
        "attack": 75,
        "defense": 75,
        "special-attack": 90,
        "special-defense": 100,
        "speed": 70,
        "id": 186
    },
    {
        "hp": 35,
        "attack": 35,
        "defense": 40,
        "special-attack": 35,
        "special-defense": 55,
        "speed": 50,
        "id": 187
    },
    {
        "hp": 55,
        "attack": 45,
        "defense": 50,
        "special-attack": 45,
        "special-defense": 65,
        "speed": 80,
        "id": 188
    },
    {
        "hp": 75,
        "attack": 55,
        "defense": 70,
        "special-attack": 55,
        "special-defense": 95,
        "speed": 110,
        "id": 189
    },
    {
        "hp": 55,
        "attack": 70,
        "defense": 55,
        "special-attack": 40,
        "special-defense": 55,
        "speed": 85,
        "id": 190
    },
    {
        "hp": 30,
        "attack": 30,
        "defense": 30,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 30,
        "id": 191
    },
    {
        "hp": 75,
        "attack": 75,
        "defense": 55,
        "special-attack": 105,
        "special-defense": 85,
        "speed": 30,
        "id": 192
    },
    {
        "hp": 65,
        "attack": 65,
        "defense": 45,
        "special-attack": 75,
        "special-defense": 45,
        "speed": 95,
        "id": 193
    },
    {
        "hp": 55,
        "attack": 45,
        "defense": 45,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 15,
        "id": 194
    },
    {
        "hp": 95,
        "attack": 85,
        "defense": 85,
        "special-attack": 65,
        "special-defense": 65,
        "speed": 35,
        "id": 195
    },
    {
        "hp": 65,
        "attack": 65,
        "defense": 60,
        "special-attack": 130,
        "special-defense": 95,
        "speed": 110,
        "id": 196
    },
    {
        "hp": 95,
        "attack": 65,
        "defense": 110,
        "special-attack": 60,
        "special-defense": 130,
        "speed": 65,
        "id": 197
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 42,
        "special-attack": 85,
        "special-defense": 42,
        "speed": 91,
        "id": 198
    },
    {
        "hp": 95,
        "attack": 75,
        "defense": 80,
        "special-attack": 100,
        "special-defense": 110,
        "speed": 30,
        "id": 199
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "special-attack": 85,
        "special-defense": 85,
        "speed": 85,
        "id": 200
    },
    {
        "hp": 48,
        "attack": 72,
        "defense": 48,
        "special-attack": 72,
        "special-defense": 48,
        "speed": 48,
        "id": 201
    },
    {
        "hp": 190,
        "attack": 33,
        "defense": 58,
        "special-attack": 33,
        "special-defense": 58,
        "speed": 33,
        "id": 202
    },
    {
        "hp": 70,
        "attack": 80,
        "defense": 65,
        "special-attack": 90,
        "special-defense": 65,
        "speed": 85,
        "id": 203
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 90,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 15,
        "id": 204
    },
    {
        "hp": 75,
        "attack": 90,
        "defense": 140,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 40,
        "id": 205
    },
    {
        "hp": 100,
        "attack": 70,
        "defense": 70,
        "special-attack": 65,
        "special-defense": 65,
        "speed": 45,
        "id": 206
    },
    {
        "hp": 65,
        "attack": 75,
        "defense": 105,
        "special-attack": 35,
        "special-defense": 65,
        "speed": 85,
        "id": 207
    },
    {
        "hp": 75,
        "attack": 85,
        "defense": 200,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 30,
        "id": 208
    },
    {
        "hp": 60,
        "attack": 80,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 30,
        "id": 209
    },
    {
        "hp": 90,
        "attack": 120,
        "defense": 75,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 45,
        "id": 210
    },
    {
        "hp": 65,
        "attack": 95,
        "defense": 85,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 85,
        "id": 211
    },
    {
        "hp": 70,
        "attack": 130,
        "defense": 100,
        "special-attack": 55,
        "special-defense": 80,
        "speed": 65,
        "id": 212
    },
    {
        "hp": 20,
        "attack": 10,
        "defense": 230,
        "special-attack": 10,
        "special-defense": 230,
        "speed": 5,
        "id": 213
    },
    {
        "hp": 80,
        "attack": 125,
        "defense": 75,
        "special-attack": 40,
        "special-defense": 95,
        "speed": 85,
        "id": 214
    },
    {
        "hp": 55,
        "attack": 95,
        "defense": 55,
        "special-attack": 35,
        "special-defense": 75,
        "speed": 115,
        "id": 215
    },
    {
        "hp": 60,
        "attack": 80,
        "defense": 50,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 40,
        "id": 216
    },
    {
        "hp": 90,
        "attack": 130,
        "defense": 75,
        "special-attack": 75,
        "special-defense": 75,
        "speed": 55,
        "id": 217
    },
    {
        "hp": 40,
        "attack": 40,
        "defense": 40,
        "special-attack": 70,
        "special-defense": 40,
        "speed": 20,
        "id": 218
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 120,
        "special-attack": 90,
        "special-defense": 80,
        "speed": 30,
        "id": 219
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 40,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 50,
        "id": 220
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 80,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 50,
        "id": 221
    },
    {
        "hp": 65,
        "attack": 55,
        "defense": 95,
        "special-attack": 65,
        "special-defense": 95,
        "speed": 35,
        "id": 222
    },
    {
        "hp": 35,
        "attack": 65,
        "defense": 35,
        "special-attack": 65,
        "special-defense": 35,
        "speed": 65,
        "id": 223
    },
    {
        "hp": 75,
        "attack": 105,
        "defense": 75,
        "special-attack": 105,
        "special-defense": 75,
        "speed": 45,
        "id": 224
    },
    {
        "hp": 45,
        "attack": 55,
        "defense": 45,
        "special-attack": 65,
        "special-defense": 45,
        "speed": 75,
        "id": 225
    },
    {
        "hp": 85,
        "attack": 40,
        "defense": 70,
        "special-attack": 80,
        "special-defense": 140,
        "speed": 70,
        "id": 226
    },
    {
        "hp": 65,
        "attack": 80,
        "defense": 140,
        "special-attack": 40,
        "special-defense": 70,
        "speed": 70,
        "id": 227
    },
    {
        "hp": 45,
        "attack": 60,
        "defense": 30,
        "special-attack": 80,
        "special-defense": 50,
        "speed": 65,
        "id": 228
    },
    {
        "hp": 75,
        "attack": 90,
        "defense": 50,
        "special-attack": 110,
        "special-defense": 80,
        "speed": 95,
        "id": 229
    },
    {
        "hp": 75,
        "attack": 95,
        "defense": 95,
        "special-attack": 95,
        "special-defense": 95,
        "speed": 85,
        "id": 230
    },
    {
        "hp": 90,
        "attack": 60,
        "defense": 60,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 40,
        "id": 231
    },
    {
        "hp": 90,
        "attack": 120,
        "defense": 120,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 50,
        "id": 232
    },
    {
        "hp": 85,
        "attack": 80,
        "defense": 90,
        "special-attack": 105,
        "special-defense": 95,
        "speed": 60,
        "id": 233
    },
    {
        "hp": 73,
        "attack": 95,
        "defense": 62,
        "special-attack": 85,
        "special-defense": 65,
        "speed": 85,
        "id": 234
    },
    {
        "hp": 55,
        "attack": 20,
        "defense": 35,
        "special-attack": 20,
        "special-defense": 45,
        "speed": 75,
        "id": 235
    },
    {
        "hp": 35,
        "attack": 35,
        "defense": 35,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 35,
        "id": 236
    },
    {
        "hp": 50,
        "attack": 95,
        "defense": 95,
        "special-attack": 35,
        "special-defense": 110,
        "speed": 70,
        "id": 237
    },
    {
        "hp": 45,
        "attack": 30,
        "defense": 15,
        "special-attack": 85,
        "special-defense": 65,
        "speed": 65,
        "id": 238
    },
    {
        "hp": 45,
        "attack": 63,
        "defense": 37,
        "special-attack": 65,
        "special-defense": 55,
        "speed": 95,
        "id": 239
    },
    {
        "hp": 45,
        "attack": 75,
        "defense": 37,
        "special-attack": 70,
        "special-defense": 55,
        "speed": 83,
        "id": 240
    },
    {
        "hp": 95,
        "attack": 80,
        "defense": 105,
        "special-attack": 40,
        "special-defense": 70,
        "speed": 100,
        "id": 241
    },
    {
        "hp": 255,
        "attack": 10,
        "defense": 10,
        "special-attack": 75,
        "special-defense": 135,
        "speed": 55,
        "id": 242
    },
    {
        "hp": 90,
        "attack": 85,
        "defense": 75,
        "special-attack": 115,
        "special-defense": 100,
        "speed": 115,
        "id": 243
    },
    {
        "hp": 115,
        "attack": 115,
        "defense": 85,
        "special-attack": 90,
        "special-defense": 75,
        "speed": 100,
        "id": 244
    },
    {
        "hp": 100,
        "attack": 75,
        "defense": 115,
        "special-attack": 90,
        "special-defense": 115,
        "speed": 85,
        "id": 245
    },
    {
        "hp": 50,
        "attack": 64,
        "defense": 50,
        "special-attack": 45,
        "special-defense": 50,
        "speed": 41,
        "id": 246
    },
    {
        "hp": 70,
        "attack": 84,
        "defense": 70,
        "special-attack": 65,
        "special-defense": 70,
        "speed": 51,
        "id": 247
    },
    {
        "hp": 100,
        "attack": 134,
        "defense": 110,
        "special-attack": 95,
        "special-defense": 100,
        "speed": 61,
        "id": 248
    },
    {
        "hp": 106,
        "attack": 90,
        "defense": 130,
        "special-attack": 90,
        "special-defense": 154,
        "speed": 110,
        "id": 249
    },
    {
        "hp": 106,
        "attack": 130,
        "defense": 90,
        "special-attack": 110,
        "special-defense": 154,
        "speed": 90,
        "id": 250
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 100,
        "id": 251
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "special-attack": 65,
        "special-defense": 55,
        "speed": 70,
        "id": 252
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 45,
        "special-attack": 85,
        "special-defense": 65,
        "speed": 95,
        "id": 253
    },
    {
        "hp": 70,
        "attack": 85,
        "defense": 65,
        "special-attack": 105,
        "special-defense": 85,
        "speed": 120,
        "id": 254
    },
    {
        "hp": 45,
        "attack": 60,
        "defense": 40,
        "special-attack": 70,
        "special-defense": 50,
        "speed": 45,
        "id": 255
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 60,
        "special-attack": 85,
        "special-defense": 60,
        "speed": 55,
        "id": 256
    },
    {
        "hp": 80,
        "attack": 120,
        "defense": 70,
        "special-attack": 110,
        "special-defense": 70,
        "speed": 80,
        "id": 257
    },
    {
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 40,
        "id": 258
    },
    {
        "hp": 70,
        "attack": 85,
        "defense": 70,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 50,
        "id": 259
    },
    {
        "hp": 100,
        "attack": 110,
        "defense": 90,
        "special-attack": 85,
        "special-defense": 90,
        "speed": 60,
        "id": 260
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 35,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 35,
        "id": 261
    },
    {
        "hp": 70,
        "attack": 90,
        "defense": 70,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 70,
        "id": 262
    },
    {
        "hp": 38,
        "attack": 30,
        "defense": 41,
        "special-attack": 30,
        "special-defense": 41,
        "speed": 60,
        "id": 263
    },
    {
        "hp": 78,
        "attack": 70,
        "defense": 61,
        "special-attack": 50,
        "special-defense": 61,
        "speed": 100,
        "id": 264
    },
    {
        "hp": 45,
        "attack": 45,
        "defense": 35,
        "special-attack": 20,
        "special-defense": 30,
        "speed": 20,
        "id": 265
    },
    {
        "hp": 50,
        "attack": 35,
        "defense": 55,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 15,
        "id": 266
    },
    {
        "hp": 60,
        "attack": 70,
        "defense": 50,
        "special-attack": 100,
        "special-defense": 50,
        "speed": 65,
        "id": 267
    },
    {
        "hp": 50,
        "attack": 35,
        "defense": 55,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 15,
        "id": 268
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 70,
        "special-attack": 50,
        "special-defense": 90,
        "speed": 65,
        "id": 269
    },
    {
        "hp": 40,
        "attack": 30,
        "defense": 30,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 30,
        "id": 270
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 50,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 50,
        "id": 271
    },
    {
        "hp": 80,
        "attack": 70,
        "defense": 70,
        "special-attack": 90,
        "special-defense": 100,
        "speed": 70,
        "id": 272
    },
    {
        "hp": 40,
        "attack": 40,
        "defense": 50,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 30,
        "id": 273
    },
    {
        "hp": 70,
        "attack": 70,
        "defense": 40,
        "special-attack": 60,
        "special-defense": 40,
        "speed": 60,
        "id": 274
    },
    {
        "hp": 90,
        "attack": 100,
        "defense": 60,
        "special-attack": 90,
        "special-defense": 60,
        "speed": 80,
        "id": 275
    },
    {
        "hp": 40,
        "attack": 55,
        "defense": 30,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 85,
        "id": 276
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 60,
        "special-attack": 75,
        "special-defense": 50,
        "speed": 125,
        "id": 277
    },
    {
        "hp": 40,
        "attack": 30,
        "defense": 30,
        "special-attack": 55,
        "special-defense": 30,
        "speed": 85,
        "id": 278
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 100,
        "special-attack": 95,
        "special-defense": 70,
        "speed": 65,
        "id": 279
    },
    {
        "hp": 28,
        "attack": 25,
        "defense": 25,
        "special-attack": 45,
        "special-defense": 35,
        "speed": 40,
        "id": 280
    },
    {
        "hp": 38,
        "attack": 35,
        "defense": 35,
        "special-attack": 65,
        "special-defense": 55,
        "speed": 50,
        "id": 281
    },
    {
        "hp": 68,
        "attack": 65,
        "defense": 65,
        "special-attack": 125,
        "special-defense": 115,
        "speed": 80,
        "id": 282
    },
    {
        "hp": 40,
        "attack": 30,
        "defense": 32,
        "special-attack": 50,
        "special-defense": 52,
        "speed": 65,
        "id": 283
    },
    {
        "hp": 70,
        "attack": 60,
        "defense": 62,
        "special-attack": 100,
        "special-defense": 82,
        "speed": 80,
        "id": 284
    },
    {
        "hp": 60,
        "attack": 40,
        "defense": 60,
        "special-attack": 40,
        "special-defense": 60,
        "speed": 35,
        "id": 285
    },
    {
        "hp": 60,
        "attack": 130,
        "defense": 80,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 70,
        "id": 286
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 30,
        "id": 287
    },
    {
        "hp": 80,
        "attack": 80,
        "defense": 80,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 90,
        "id": 288
    },
    {
        "hp": 150,
        "attack": 160,
        "defense": 100,
        "special-attack": 95,
        "special-defense": 65,
        "speed": 100,
        "id": 289
    },
    {
        "hp": 31,
        "attack": 45,
        "defense": 90,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 40,
        "id": 290
    },
    {
        "hp": 61,
        "attack": 90,
        "defense": 45,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 160,
        "id": 291
    },
    {
        "hp": 1,
        "attack": 90,
        "defense": 45,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 40,
        "id": 292
    },
    {
        "hp": 64,
        "attack": 51,
        "defense": 23,
        "special-attack": 51,
        "special-defense": 23,
        "speed": 28,
        "id": 293
    },
    {
        "hp": 84,
        "attack": 71,
        "defense": 43,
        "special-attack": 71,
        "special-defense": 43,
        "speed": 48,
        "id": 294
    },
    {
        "hp": 104,
        "attack": 91,
        "defense": 63,
        "special-attack": 91,
        "special-defense": 73,
        "speed": 68,
        "id": 295
    },
    {
        "hp": 72,
        "attack": 60,
        "defense": 30,
        "special-attack": 20,
        "special-defense": 30,
        "speed": 25,
        "id": 296
    },
    {
        "hp": 144,
        "attack": 120,
        "defense": 60,
        "special-attack": 40,
        "special-defense": 60,
        "speed": 50,
        "id": 297
    },
    {
        "hp": 50,
        "attack": 20,
        "defense": 40,
        "special-attack": 20,
        "special-defense": 40,
        "speed": 20,
        "id": 298
    },
    {
        "hp": 30,
        "attack": 45,
        "defense": 135,
        "special-attack": 45,
        "special-defense": 90,
        "speed": 30,
        "id": 299
    },
    {
        "hp": 50,
        "attack": 45,
        "defense": 45,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 50,
        "id": 300
    },
    {
        "hp": 70,
        "attack": 65,
        "defense": 65,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 90,
        "id": 301
    },
    {
        "hp": 50,
        "attack": 75,
        "defense": 75,
        "special-attack": 65,
        "special-defense": 65,
        "speed": 50,
        "id": 302
    },
    {
        "hp": 50,
        "attack": 85,
        "defense": 85,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 50,
        "id": 303
    },
    {
        "hp": 50,
        "attack": 70,
        "defense": 100,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 30,
        "id": 304
    },
    {
        "hp": 60,
        "attack": 90,
        "defense": 140,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 40,
        "id": 305
    },
    {
        "hp": 70,
        "attack": 110,
        "defense": 180,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 50,
        "id": 306
    },
    {
        "hp": 30,
        "attack": 40,
        "defense": 55,
        "special-attack": 40,
        "special-defense": 55,
        "speed": 60,
        "id": 307
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 75,
        "special-attack": 60,
        "special-defense": 75,
        "speed": 80,
        "id": 308
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "special-attack": 65,
        "special-defense": 40,
        "speed": 65,
        "id": 309
    },
    {
        "hp": 70,
        "attack": 75,
        "defense": 60,
        "special-attack": 105,
        "special-defense": 60,
        "speed": 105,
        "id": 310
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 40,
        "special-attack": 85,
        "special-defense": 75,
        "speed": 95,
        "id": 311
    },
    {
        "hp": 60,
        "attack": 40,
        "defense": 50,
        "special-attack": 75,
        "special-defense": 85,
        "speed": 95,
        "id": 312
    },
    {
        "hp": 65,
        "attack": 73,
        "defense": 75,
        "special-attack": 47,
        "special-defense": 85,
        "speed": 85,
        "id": 313
    },
    {
        "hp": 65,
        "attack": 47,
        "defense": 75,
        "special-attack": 73,
        "special-defense": 85,
        "speed": 85,
        "id": 314
    },
    {
        "hp": 50,
        "attack": 60,
        "defense": 45,
        "special-attack": 100,
        "special-defense": 80,
        "speed": 65,
        "id": 315
    },
    {
        "hp": 70,
        "attack": 43,
        "defense": 53,
        "special-attack": 43,
        "special-defense": 53,
        "speed": 40,
        "id": 316
    },
    {
        "hp": 100,
        "attack": 73,
        "defense": 83,
        "special-attack": 73,
        "special-defense": 83,
        "speed": 55,
        "id": 317
    },
    {
        "hp": 45,
        "attack": 90,
        "defense": 20,
        "special-attack": 65,
        "special-defense": 20,
        "speed": 65,
        "id": 318
    },
    {
        "hp": 70,
        "attack": 120,
        "defense": 40,
        "special-attack": 95,
        "special-defense": 40,
        "speed": 95,
        "id": 319
    },
    {
        "hp": 130,
        "attack": 70,
        "defense": 35,
        "special-attack": 70,
        "special-defense": 35,
        "speed": 60,
        "id": 320
    },
    {
        "hp": 170,
        "attack": 90,
        "defense": 45,
        "special-attack": 90,
        "special-defense": 45,
        "speed": 60,
        "id": 321
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 40,
        "special-attack": 65,
        "special-defense": 45,
        "speed": 35,
        "id": 322
    },
    {
        "hp": 70,
        "attack": 100,
        "defense": 70,
        "special-attack": 105,
        "special-defense": 75,
        "speed": 40,
        "id": 323
    },
    {
        "hp": 70,
        "attack": 85,
        "defense": 140,
        "special-attack": 85,
        "special-defense": 70,
        "speed": 20,
        "id": 324
    },
    {
        "hp": 60,
        "attack": 25,
        "defense": 35,
        "special-attack": 70,
        "special-defense": 80,
        "speed": 60,
        "id": 325
    },
    {
        "hp": 80,
        "attack": 45,
        "defense": 65,
        "special-attack": 90,
        "special-defense": 110,
        "speed": 80,
        "id": 326
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 60,
        "id": 327
    },
    {
        "hp": 45,
        "attack": 100,
        "defense": 45,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 10,
        "id": 328
    },
    {
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 70,
        "id": 329
    },
    {
        "hp": 80,
        "attack": 100,
        "defense": 80,
        "special-attack": 80,
        "special-defense": 80,
        "speed": 100,
        "id": 330
    },
    {
        "hp": 50,
        "attack": 85,
        "defense": 40,
        "special-attack": 85,
        "special-defense": 40,
        "speed": 35,
        "id": 331
    },
    {
        "hp": 70,
        "attack": 115,
        "defense": 60,
        "special-attack": 115,
        "special-defense": 60,
        "speed": 55,
        "id": 332
    },
    {
        "hp": 45,
        "attack": 40,
        "defense": 60,
        "special-attack": 40,
        "special-defense": 75,
        "speed": 50,
        "id": 333
    },
    {
        "hp": 75,
        "attack": 70,
        "defense": 90,
        "special-attack": 70,
        "special-defense": 105,
        "speed": 80,
        "id": 334
    },
    {
        "hp": 73,
        "attack": 115,
        "defense": 60,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 90,
        "id": 335
    },
    {
        "hp": 73,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 65,
        "id": 336
    },
    {
        "hp": 90,
        "attack": 55,
        "defense": 65,
        "special-attack": 95,
        "special-defense": 85,
        "speed": 70,
        "id": 337
    },
    {
        "hp": 90,
        "attack": 95,
        "defense": 85,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 70,
        "id": 338
    },
    {
        "hp": 50,
        "attack": 48,
        "defense": 43,
        "special-attack": 46,
        "special-defense": 41,
        "speed": 60,
        "id": 339
    },
    {
        "hp": 110,
        "attack": 78,
        "defense": 73,
        "special-attack": 76,
        "special-defense": 71,
        "speed": 60,
        "id": 340
    },
    {
        "hp": 43,
        "attack": 80,
        "defense": 65,
        "special-attack": 50,
        "special-defense": 35,
        "speed": 35,
        "id": 341
    },
    {
        "hp": 63,
        "attack": 120,
        "defense": 85,
        "special-attack": 90,
        "special-defense": 55,
        "speed": 55,
        "id": 342
    },
    {
        "hp": 40,
        "attack": 40,
        "defense": 55,
        "special-attack": 40,
        "special-defense": 70,
        "speed": 55,
        "id": 343
    },
    {
        "hp": 60,
        "attack": 70,
        "defense": 105,
        "special-attack": 70,
        "special-defense": 120,
        "speed": 75,
        "id": 344
    },
    {
        "hp": 66,
        "attack": 41,
        "defense": 77,
        "special-attack": 61,
        "special-defense": 87,
        "speed": 23,
        "id": 345
    },
    {
        "hp": 86,
        "attack": 81,
        "defense": 97,
        "special-attack": 81,
        "special-defense": 107,
        "speed": 43,
        "id": 346
    },
    {
        "hp": 45,
        "attack": 95,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 75,
        "id": 347
    },
    {
        "hp": 75,
        "attack": 125,
        "defense": 100,
        "special-attack": 70,
        "special-defense": 80,
        "speed": 45,
        "id": 348
    },
    {
        "hp": 20,
        "attack": 15,
        "defense": 20,
        "special-attack": 10,
        "special-defense": 55,
        "speed": 80,
        "id": 349
    },
    {
        "hp": 95,
        "attack": 60,
        "defense": 79,
        "special-attack": 100,
        "special-defense": 125,
        "speed": 81,
        "id": 350
    },
    {
        "hp": 70,
        "attack": 70,
        "defense": 70,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 70,
        "id": 351
    },
    {
        "hp": 60,
        "attack": 90,
        "defense": 70,
        "special-attack": 60,
        "special-defense": 120,
        "speed": 40,
        "id": 352
    },
    {
        "hp": 44,
        "attack": 75,
        "defense": 35,
        "special-attack": 63,
        "special-defense": 33,
        "speed": 45,
        "id": 353
    },
    {
        "hp": 64,
        "attack": 115,
        "defense": 65,
        "special-attack": 83,
        "special-defense": 63,
        "speed": 65,
        "id": 354
    },
    {
        "hp": 20,
        "attack": 40,
        "defense": 90,
        "special-attack": 30,
        "special-defense": 90,
        "speed": 25,
        "id": 355
    },
    {
        "hp": 40,
        "attack": 70,
        "defense": 130,
        "special-attack": 60,
        "special-defense": 130,
        "speed": 25,
        "id": 356
    },
    {
        "hp": 99,
        "attack": 68,
        "defense": 83,
        "special-attack": 72,
        "special-defense": 87,
        "speed": 51,
        "id": 357
    },
    {
        "hp": 75,
        "attack": 50,
        "defense": 80,
        "special-attack": 95,
        "special-defense": 90,
        "speed": 65,
        "id": 358
    },
    {
        "hp": 65,
        "attack": 130,
        "defense": 60,
        "special-attack": 75,
        "special-defense": 60,
        "speed": 75,
        "id": 359
    },
    {
        "hp": 95,
        "attack": 23,
        "defense": 48,
        "special-attack": 23,
        "special-defense": 48,
        "speed": 23,
        "id": 360
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 50,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 50,
        "id": 361
    },
    {
        "hp": 80,
        "attack": 80,
        "defense": 80,
        "special-attack": 80,
        "special-defense": 80,
        "speed": 80,
        "id": 362
    },
    {
        "hp": 70,
        "attack": 40,
        "defense": 50,
        "special-attack": 55,
        "special-defense": 50,
        "speed": 25,
        "id": 363
    },
    {
        "hp": 90,
        "attack": 60,
        "defense": 70,
        "special-attack": 75,
        "special-defense": 70,
        "speed": 45,
        "id": 364
    },
    {
        "hp": 110,
        "attack": 80,
        "defense": 90,
        "special-attack": 95,
        "special-defense": 90,
        "speed": 65,
        "id": 365
    },
    {
        "hp": 35,
        "attack": 64,
        "defense": 85,
        "special-attack": 74,
        "special-defense": 55,
        "speed": 32,
        "id": 366
    },
    {
        "hp": 55,
        "attack": 104,
        "defense": 105,
        "special-attack": 94,
        "special-defense": 75,
        "speed": 52,
        "id": 367
    },
    {
        "hp": 55,
        "attack": 84,
        "defense": 105,
        "special-attack": 114,
        "special-defense": 75,
        "speed": 52,
        "id": 368
    },
    {
        "hp": 100,
        "attack": 90,
        "defense": 130,
        "special-attack": 45,
        "special-defense": 65,
        "speed": 55,
        "id": 369
    },
    {
        "hp": 43,
        "attack": 30,
        "defense": 55,
        "special-attack": 40,
        "special-defense": 65,
        "speed": 97,
        "id": 370
    },
    {
        "hp": 45,
        "attack": 75,
        "defense": 60,
        "special-attack": 40,
        "special-defense": 30,
        "speed": 50,
        "id": 371
    },
    {
        "hp": 65,
        "attack": 95,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 50,
        "speed": 50,
        "id": 372
    },
    {
        "hp": 95,
        "attack": 135,
        "defense": 80,
        "special-attack": 110,
        "special-defense": 80,
        "speed": 100,
        "id": 373
    },
    {
        "hp": 40,
        "attack": 55,
        "defense": 80,
        "special-attack": 35,
        "special-defense": 60,
        "speed": 30,
        "id": 374
    },
    {
        "hp": 60,
        "attack": 75,
        "defense": 100,
        "special-attack": 55,
        "special-defense": 80,
        "speed": 50,
        "id": 375
    },
    {
        "hp": 80,
        "attack": 135,
        "defense": 130,
        "special-attack": 95,
        "special-defense": 90,
        "speed": 70,
        "id": 376
    },
    {
        "hp": 80,
        "attack": 100,
        "defense": 200,
        "special-attack": 50,
        "special-defense": 100,
        "speed": 50,
        "id": 377
    },
    {
        "hp": 80,
        "attack": 50,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 200,
        "speed": 50,
        "id": 378
    },
    {
        "hp": 80,
        "attack": 75,
        "defense": 150,
        "special-attack": 75,
        "special-defense": 150,
        "speed": 50,
        "id": 379
    },
    {
        "hp": 80,
        "attack": 80,
        "defense": 90,
        "special-attack": 110,
        "special-defense": 130,
        "speed": 110,
        "id": 380
    },
    {
        "hp": 80,
        "attack": 90,
        "defense": 80,
        "special-attack": 130,
        "special-defense": 110,
        "speed": 110,
        "id": 381
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 90,
        "special-attack": 150,
        "special-defense": 140,
        "speed": 90,
        "id": 382
    },
    {
        "hp": 100,
        "attack": 150,
        "defense": 140,
        "special-attack": 100,
        "special-defense": 90,
        "speed": 90,
        "id": 383
    },
    {
        "hp": 105,
        "attack": 150,
        "defense": 90,
        "special-attack": 150,
        "special-defense": 90,
        "speed": 95,
        "id": 384
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 100,
        "id": 385
    },
    {
        "hp": 50,
        "attack": 150,
        "defense": 50,
        "special-attack": 150,
        "special-defense": 50,
        "speed": 150,
        "id": 386
    },
    {
        "hp": 55,
        "attack": 68,
        "defense": 64,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 31,
        "id": 387
    },
    {
        "hp": 75,
        "attack": 89,
        "defense": 85,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 36,
        "id": 388
    },
    {
        "hp": 95,
        "attack": 109,
        "defense": 105,
        "special-attack": 75,
        "special-defense": 85,
        "speed": 56,
        "id": 389
    },
    {
        "hp": 44,
        "attack": 58,
        "defense": 44,
        "special-attack": 58,
        "special-defense": 44,
        "speed": 61,
        "id": 390
    },
    {
        "hp": 64,
        "attack": 78,
        "defense": 52,
        "special-attack": 78,
        "special-defense": 52,
        "speed": 81,
        "id": 391
    },
    {
        "hp": 76,
        "attack": 104,
        "defense": 71,
        "special-attack": 104,
        "special-defense": 71,
        "speed": 108,
        "id": 392
    },
    {
        "hp": 53,
        "attack": 51,
        "defense": 53,
        "special-attack": 61,
        "special-defense": 56,
        "speed": 40,
        "id": 393
    },
    {
        "hp": 64,
        "attack": 66,
        "defense": 68,
        "special-attack": 81,
        "special-defense": 76,
        "speed": 50,
        "id": 394
    },
    {
        "hp": 84,
        "attack": 86,
        "defense": 88,
        "special-attack": 111,
        "special-defense": 101,
        "speed": 60,
        "id": 395
    },
    {
        "hp": 40,
        "attack": 55,
        "defense": 30,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 60,
        "id": 396
    },
    {
        "hp": 55,
        "attack": 75,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 80,
        "id": 397
    },
    {
        "hp": 85,
        "attack": 120,
        "defense": 70,
        "special-attack": 50,
        "special-defense": 60,
        "speed": 100,
        "id": 398
    },
    {
        "hp": 59,
        "attack": 45,
        "defense": 40,
        "special-attack": 35,
        "special-defense": 40,
        "speed": 31,
        "id": 399
    },
    {
        "hp": 79,
        "attack": 85,
        "defense": 60,
        "special-attack": 55,
        "special-defense": 60,
        "speed": 71,
        "id": 400
    },
    {
        "hp": 37,
        "attack": 25,
        "defense": 41,
        "special-attack": 25,
        "special-defense": 41,
        "speed": 25,
        "id": 401
    },
    {
        "hp": 77,
        "attack": 85,
        "defense": 51,
        "special-attack": 55,
        "special-defense": 51,
        "speed": 65,
        "id": 402
    },
    {
        "hp": 45,
        "attack": 65,
        "defense": 34,
        "special-attack": 40,
        "special-defense": 34,
        "speed": 45,
        "id": 403
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 49,
        "special-attack": 60,
        "special-defense": 49,
        "speed": 60,
        "id": 404
    },
    {
        "hp": 80,
        "attack": 120,
        "defense": 79,
        "special-attack": 95,
        "special-defense": 79,
        "speed": 70,
        "id": 405
    },
    {
        "hp": 40,
        "attack": 30,
        "defense": 35,
        "special-attack": 50,
        "special-defense": 70,
        "speed": 55,
        "id": 406
    },
    {
        "hp": 60,
        "attack": 70,
        "defense": 65,
        "special-attack": 125,
        "special-defense": 105,
        "speed": 90,
        "id": 407
    },
    {
        "hp": 67,
        "attack": 125,
        "defense": 40,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 58,
        "id": 408
    },
    {
        "hp": 97,
        "attack": 165,
        "defense": 60,
        "special-attack": 65,
        "special-defense": 50,
        "speed": 58,
        "id": 409
    },
    {
        "hp": 30,
        "attack": 42,
        "defense": 118,
        "special-attack": 42,
        "special-defense": 88,
        "speed": 30,
        "id": 410
    },
    {
        "hp": 60,
        "attack": 52,
        "defense": 168,
        "special-attack": 47,
        "special-defense": 138,
        "speed": 30,
        "id": 411
    },
    {
        "hp": 40,
        "attack": 29,
        "defense": 45,
        "special-attack": 29,
        "special-defense": 45,
        "speed": 36,
        "id": 412
    },
    {
        "hp": 60,
        "attack": 59,
        "defense": 85,
        "special-attack": 79,
        "special-defense": 105,
        "speed": 36,
        "id": 413
    },
    {
        "hp": 70,
        "attack": 94,
        "defense": 50,
        "special-attack": 94,
        "special-defense": 50,
        "speed": 66,
        "id": 414
    },
    {
        "hp": 30,
        "attack": 30,
        "defense": 42,
        "special-attack": 30,
        "special-defense": 42,
        "speed": 70,
        "id": 415
    },
    {
        "hp": 70,
        "attack": 80,
        "defense": 102,
        "special-attack": 80,
        "special-defense": 102,
        "speed": 40,
        "id": 416
    },
    {
        "hp": 60,
        "attack": 45,
        "defense": 70,
        "special-attack": 45,
        "special-defense": 90,
        "speed": 95,
        "id": 417
    },
    {
        "hp": 55,
        "attack": 65,
        "defense": 35,
        "special-attack": 60,
        "special-defense": 30,
        "speed": 85,
        "id": 418
    },
    {
        "hp": 85,
        "attack": 105,
        "defense": 55,
        "special-attack": 85,
        "special-defense": 50,
        "speed": 115,
        "id": 419
    },
    {
        "hp": 45,
        "attack": 35,
        "defense": 45,
        "special-attack": 62,
        "special-defense": 53,
        "speed": 35,
        "id": 420
    },
    {
        "hp": 70,
        "attack": 60,
        "defense": 70,
        "special-attack": 87,
        "special-defense": 78,
        "speed": 85,
        "id": 421
    },
    {
        "hp": 76,
        "attack": 48,
        "defense": 48,
        "special-attack": 57,
        "special-defense": 62,
        "speed": 34,
        "id": 422
    },
    {
        "hp": 111,
        "attack": 83,
        "defense": 68,
        "special-attack": 92,
        "special-defense": 82,
        "speed": 39,
        "id": 423
    },
    {
        "hp": 75,
        "attack": 100,
        "defense": 66,
        "special-attack": 60,
        "special-defense": 66,
        "speed": 115,
        "id": 424
    },
    {
        "hp": 90,
        "attack": 50,
        "defense": 34,
        "special-attack": 60,
        "special-defense": 44,
        "speed": 70,
        "id": 425
    },
    {
        "hp": 150,
        "attack": 80,
        "defense": 44,
        "special-attack": 90,
        "special-defense": 54,
        "speed": 80,
        "id": 426
    },
    {
        "hp": 55,
        "attack": 66,
        "defense": 44,
        "special-attack": 44,
        "special-defense": 56,
        "speed": 85,
        "id": 427
    },
    {
        "hp": 65,
        "attack": 76,
        "defense": 84,
        "special-attack": 54,
        "special-defense": 96,
        "speed": 105,
        "id": 428
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "special-attack": 105,
        "special-defense": 105,
        "speed": 105,
        "id": 429
    },
    {
        "hp": 100,
        "attack": 125,
        "defense": 52,
        "special-attack": 105,
        "special-defense": 52,
        "speed": 71,
        "id": 430
    },
    {
        "hp": 49,
        "attack": 55,
        "defense": 42,
        "special-attack": 42,
        "special-defense": 37,
        "speed": 85,
        "id": 431
    },
    {
        "hp": 71,
        "attack": 82,
        "defense": 64,
        "special-attack": 64,
        "special-defense": 59,
        "speed": 112,
        "id": 432
    },
    {
        "hp": 45,
        "attack": 30,
        "defense": 50,
        "special-attack": 65,
        "special-defense": 50,
        "speed": 45,
        "id": 433
    },
    {
        "hp": 63,
        "attack": 63,
        "defense": 47,
        "special-attack": 41,
        "special-defense": 41,
        "speed": 74,
        "id": 434
    },
    {
        "hp": 103,
        "attack": 93,
        "defense": 67,
        "special-attack": 71,
        "special-defense": 61,
        "speed": 84,
        "id": 435
    },
    {
        "hp": 57,
        "attack": 24,
        "defense": 86,
        "special-attack": 24,
        "special-defense": 86,
        "speed": 23,
        "id": 436
    },
    {
        "hp": 67,
        "attack": 89,
        "defense": 116,
        "special-attack": 79,
        "special-defense": 116,
        "speed": 33,
        "id": 437
    },
    {
        "hp": 50,
        "attack": 80,
        "defense": 95,
        "special-attack": 10,
        "special-defense": 45,
        "speed": 10,
        "id": 438
    },
    {
        "hp": 20,
        "attack": 25,
        "defense": 45,
        "special-attack": 70,
        "special-defense": 90,
        "speed": 60,
        "id": 439
    },
    {
        "hp": 100,
        "attack": 5,
        "defense": 5,
        "special-attack": 15,
        "special-defense": 65,
        "speed": 30,
        "id": 440
    },
    {
        "hp": 76,
        "attack": 65,
        "defense": 45,
        "special-attack": 92,
        "special-defense": 42,
        "speed": 91,
        "id": 441
    },
    {
        "hp": 50,
        "attack": 92,
        "defense": 108,
        "special-attack": 92,
        "special-defense": 108,
        "speed": 35,
        "id": 442
    },
    {
        "hp": 58,
        "attack": 70,
        "defense": 45,
        "special-attack": 40,
        "special-defense": 45,
        "speed": 42,
        "id": 443
    },
    {
        "hp": 68,
        "attack": 90,
        "defense": 65,
        "special-attack": 50,
        "special-defense": 55,
        "speed": 82,
        "id": 444
    },
    {
        "hp": 108,
        "attack": 130,
        "defense": 95,
        "special-attack": 80,
        "special-defense": 85,
        "speed": 102,
        "id": 445
    },
    {
        "hp": 135,
        "attack": 85,
        "defense": 40,
        "special-attack": 40,
        "special-defense": 85,
        "speed": 5,
        "id": 446
    },
    {
        "hp": 40,
        "attack": 70,
        "defense": 40,
        "special-attack": 35,
        "special-defense": 40,
        "speed": 60,
        "id": 447
    },
    {
        "hp": 70,
        "attack": 110,
        "defense": 70,
        "special-attack": 115,
        "special-defense": 70,
        "speed": 90,
        "id": 448
    },
    {
        "hp": 68,
        "attack": 72,
        "defense": 78,
        "special-attack": 38,
        "special-defense": 42,
        "speed": 32,
        "id": 449
    },
    {
        "hp": 108,
        "attack": 112,
        "defense": 118,
        "special-attack": 68,
        "special-defense": 72,
        "speed": 47,
        "id": 450
    },
    {
        "hp": 40,
        "attack": 50,
        "defense": 90,
        "special-attack": 30,
        "special-defense": 55,
        "speed": 65,
        "id": 451
    },
    {
        "hp": 70,
        "attack": 90,
        "defense": 110,
        "special-attack": 60,
        "special-defense": 75,
        "speed": 95,
        "id": 452
    },
    {
        "hp": 48,
        "attack": 61,
        "defense": 40,
        "special-attack": 61,
        "special-defense": 40,
        "speed": 50,
        "id": 453
    },
    {
        "hp": 83,
        "attack": 106,
        "defense": 65,
        "special-attack": 86,
        "special-defense": 65,
        "speed": 85,
        "id": 454
    },
    {
        "hp": 74,
        "attack": 100,
        "defense": 72,
        "special-attack": 90,
        "special-defense": 72,
        "speed": 46,
        "id": 455
    },
    {
        "hp": 49,
        "attack": 49,
        "defense": 56,
        "special-attack": 49,
        "special-defense": 61,
        "speed": 66,
        "id": 456
    },
    {
        "hp": 69,
        "attack": 69,
        "defense": 76,
        "special-attack": 69,
        "special-defense": 86,
        "speed": 91,
        "id": 457
    },
    {
        "hp": 45,
        "attack": 20,
        "defense": 50,
        "special-attack": 60,
        "special-defense": 120,
        "speed": 50,
        "id": 458
    },
    {
        "hp": 60,
        "attack": 62,
        "defense": 50,
        "special-attack": 62,
        "special-defense": 60,
        "speed": 40,
        "id": 459
    },
    {
        "hp": 90,
        "attack": 92,
        "defense": 75,
        "special-attack": 92,
        "special-defense": 85,
        "speed": 60,
        "id": 460
    },
    {
        "hp": 70,
        "attack": 120,
        "defense": 65,
        "special-attack": 45,
        "special-defense": 85,
        "speed": 125,
        "id": 461
    },
    {
        "hp": 70,
        "attack": 70,
        "defense": 115,
        "special-attack": 130,
        "special-defense": 90,
        "speed": 60,
        "id": 462
    },
    {
        "hp": 110,
        "attack": 85,
        "defense": 95,
        "special-attack": 80,
        "special-defense": 95,
        "speed": 50,
        "id": 463
    },
    {
        "hp": 115,
        "attack": 140,
        "defense": 130,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 40,
        "id": 464
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 125,
        "special-attack": 110,
        "special-defense": 50,
        "speed": 50,
        "id": 465
    },
    {
        "hp": 75,
        "attack": 123,
        "defense": 67,
        "special-attack": 95,
        "special-defense": 85,
        "speed": 95,
        "id": 466
    },
    {
        "hp": 75,
        "attack": 95,
        "defense": 67,
        "special-attack": 125,
        "special-defense": 95,
        "speed": 83,
        "id": 467
    },
    {
        "hp": 85,
        "attack": 50,
        "defense": 95,
        "special-attack": 120,
        "special-defense": 115,
        "speed": 80,
        "id": 468
    },
    {
        "hp": 86,
        "attack": 76,
        "defense": 86,
        "special-attack": 116,
        "special-defense": 56,
        "speed": 95,
        "id": 469
    },
    {
        "hp": 65,
        "attack": 110,
        "defense": 130,
        "special-attack": 60,
        "special-defense": 65,
        "speed": 95,
        "id": 470
    },
    {
        "hp": 65,
        "attack": 60,
        "defense": 110,
        "special-attack": 130,
        "special-defense": 95,
        "speed": 65,
        "id": 471
    },
    {
        "hp": 75,
        "attack": 95,
        "defense": 125,
        "special-attack": 45,
        "special-defense": 75,
        "speed": 95,
        "id": 472
    },
    {
        "hp": 110,
        "attack": 130,
        "defense": 80,
        "special-attack": 70,
        "special-defense": 60,
        "speed": 80,
        "id": 473
    },
    {
        "hp": 85,
        "attack": 80,
        "defense": 70,
        "special-attack": 135,
        "special-defense": 75,
        "speed": 90,
        "id": 474
    },
    {
        "hp": 68,
        "attack": 125,
        "defense": 65,
        "special-attack": 65,
        "special-defense": 115,
        "speed": 80,
        "id": 475
    },
    {
        "hp": 60,
        "attack": 55,
        "defense": 145,
        "special-attack": 75,
        "special-defense": 150,
        "speed": 40,
        "id": 476
    },
    {
        "hp": 45,
        "attack": 100,
        "defense": 135,
        "special-attack": 65,
        "special-defense": 135,
        "speed": 45,
        "id": 477
    },
    {
        "hp": 70,
        "attack": 80,
        "defense": 70,
        "special-attack": 80,
        "special-defense": 70,
        "speed": 110,
        "id": 478
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 77,
        "special-attack": 95,
        "special-defense": 77,
        "speed": 91,
        "id": 479
    },
    {
        "hp": 75,
        "attack": 75,
        "defense": 130,
        "special-attack": 75,
        "special-defense": 130,
        "speed": 95,
        "id": 480
    },
    {
        "hp": 80,
        "attack": 105,
        "defense": 105,
        "special-attack": 105,
        "special-defense": 105,
        "speed": 80,
        "id": 481
    },
    {
        "hp": 75,
        "attack": 125,
        "defense": 70,
        "special-attack": 125,
        "special-defense": 70,
        "speed": 115,
        "id": 482
    },
    {
        "hp": 100,
        "attack": 120,
        "defense": 120,
        "special-attack": 150,
        "special-defense": 100,
        "speed": 90,
        "id": 483
    },
    {
        "hp": 90,
        "attack": 120,
        "defense": 100,
        "special-attack": 150,
        "special-defense": 120,
        "speed": 100,
        "id": 484
    },
    {
        "hp": 91,
        "attack": 90,
        "defense": 106,
        "special-attack": 130,
        "special-defense": 106,
        "speed": 77,
        "id": 485
    },
    {
        "hp": 110,
        "attack": 160,
        "defense": 110,
        "special-attack": 80,
        "special-defense": 110,
        "speed": 100,
        "id": 486
    },
    {
        "hp": 150,
        "attack": 100,
        "defense": 120,
        "special-attack": 100,
        "special-defense": 120,
        "speed": 90,
        "id": 487
    },
    {
        "hp": 120,
        "attack": 70,
        "defense": 120,
        "special-attack": 75,
        "special-defense": 130,
        "speed": 85,
        "id": 488
    },
    {
        "hp": 80,
        "attack": 80,
        "defense": 80,
        "special-attack": 80,
        "special-defense": 80,
        "speed": 80,
        "id": 489
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 100,
        "id": 490
    },
    {
        "hp": 70,
        "attack": 90,
        "defense": 90,
        "special-attack": 135,
        "special-defense": 90,
        "speed": 125,
        "id": 491
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 100,
        "id": 492
    },
    {
        "hp": 120,
        "attack": 120,
        "defense": 120,
        "special-attack": 120,
        "special-defense": 120,
        "speed": 120,
        "id": 493
    },
    {
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 100,
        "id": 494
    },
    {
        "hp": 45,
        "attack": 45,
        "defense": 55,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 63,
        "id": 495
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 75,
        "special-attack": 60,
        "special-defense": 75,
        "speed": 83,
        "id": 496
    },
    {
        "hp": 75,
        "attack": 75,
        "defense": 95,
        "special-attack": 75,
        "special-defense": 95,
        "speed": 113,
        "id": 497
    },
    {
        "hp": 65,
        "attack": 63,
        "defense": 45,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 45,
        "id": 498
    },
    {
        "hp": 90,
        "attack": 93,
        "defense": 55,
        "special-attack": 70,
        "special-defense": 55,
        "speed": 55,
        "id": 499
    },
    {
        "hp": 110,
        "attack": 123,
        "defense": 65,
        "special-attack": 100,
        "special-defense": 65,
        "speed": 65,
        "id": 500
    },
    {
        "hp": 55,
        "attack": 55,
        "defense": 45,
        "special-attack": 63,
        "special-defense": 45,
        "speed": 45,
        "id": 501
    },
    {
        "hp": 75,
        "attack": 75,
        "defense": 60,
        "special-attack": 83,
        "special-defense": 60,
        "speed": 60,
        "id": 502
    },
    {
        "hp": 95,
        "attack": 100,
        "defense": 85,
        "special-attack": 108,
        "special-defense": 70,
        "speed": 70,
        "id": 503
    },
    {
        "hp": 45,
        "attack": 55,
        "defense": 39,
        "special-attack": 35,
        "special-defense": 39,
        "speed": 42,
        "id": 504
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 69,
        "special-attack": 60,
        "special-defense": 69,
        "speed": 77,
        "id": 505
    },
    {
        "hp": 45,
        "attack": 60,
        "defense": 45,
        "special-attack": 25,
        "special-defense": 45,
        "speed": 55,
        "id": 506
    },
    {
        "hp": 65,
        "attack": 80,
        "defense": 65,
        "special-attack": 35,
        "special-defense": 65,
        "speed": 60,
        "id": 507
    },
    {
        "hp": 85,
        "attack": 110,
        "defense": 90,
        "special-attack": 45,
        "special-defense": 90,
        "speed": 80,
        "id": 508
    },
    {
        "hp": 41,
        "attack": 50,
        "defense": 37,
        "special-attack": 50,
        "special-defense": 37,
        "speed": 66,
        "id": 509
    },
    {
        "hp": 64,
        "attack": 88,
        "defense": 50,
        "special-attack": 88,
        "special-defense": 50,
        "speed": 106,
        "id": 510
    },
    {
        "hp": 50,
        "attack": 53,
        "defense": 48,
        "special-attack": 53,
        "special-defense": 48,
        "speed": 64,
        "id": 511
    },
    {
        "hp": 75,
        "attack": 98,
        "defense": 63,
        "special-attack": 98,
        "special-defense": 63,
        "speed": 101,
        "id": 512
    },
    {
        "hp": 50,
        "attack": 53,
        "defense": 48,
        "special-attack": 53,
        "special-defense": 48,
        "speed": 64,
        "id": 513
    },
    {
        "hp": 75,
        "attack": 98,
        "defense": 63,
        "special-attack": 98,
        "special-defense": 63,
        "speed": 101,
        "id": 514
    },
    {
        "hp": 50,
        "attack": 53,
        "defense": 48,
        "special-attack": 53,
        "special-defense": 48,
        "speed": 64,
        "id": 515
    },
    {
        "hp": 75,
        "attack": 98,
        "defense": 63,
        "special-attack": 98,
        "special-defense": 63,
        "speed": 101,
        "id": 516
    },
    {
        "hp": 76,
        "attack": 25,
        "defense": 45,
        "special-attack": 67,
        "special-defense": 55,
        "speed": 24,
        "id": 517
    },
    {
        "hp": 116,
        "attack": 55,
        "defense": 85,
        "special-attack": 107,
        "special-defense": 95,
        "speed": 29,
        "id": 518
    },
    {
        "hp": 50,
        "attack": 55,
        "defense": 50,
        "special-attack": 36,
        "special-defense": 30,
        "speed": 43,
        "id": 519
    },
    {
        "hp": 62,
        "attack": 77,
        "defense": 62,
        "special-attack": 50,
        "special-defense": 42,
        "speed": 65,
        "id": 520
    },
    {
        "hp": 80,
        "attack": 115,
        "defense": 80,
        "special-attack": 65,
        "special-defense": 55,
        "speed": 93,
        "id": 521
    },
    {
        "hp": 45,
        "attack": 60,
        "defense": 32,
        "special-attack": 50,
        "special-defense": 32,
        "speed": 76,
        "id": 522
    },
    {
        "hp": 75,
        "attack": 100,
        "defense": 63,
        "special-attack": 80,
        "special-defense": 63,
        "speed": 116,
        "id": 523
    },
    {
        "hp": 55,
        "attack": 75,
        "defense": 85,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 15,
        "id": 524
    },
    {
        "hp": 70,
        "attack": 105,
        "defense": 105,
        "special-attack": 50,
        "special-defense": 40,
        "speed": 20,
        "id": 525
    },
    {
        "hp": 85,
        "attack": 135,
        "defense": 130,
        "special-attack": 60,
        "special-defense": 80,
        "speed": 25,
        "id": 526
    },
    {
        "hp": 65,
        "attack": 45,
        "defense": 43,
        "special-attack": 55,
        "special-defense": 43,
        "speed": 72,
        "id": 527
    },
    {
        "hp": 67,
        "attack": 57,
        "defense": 55,
        "special-attack": 77,
        "special-defense": 55,
        "speed": 114,
        "id": 528
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 40,
        "special-attack": 30,
        "special-defense": 45,
        "speed": 68,
        "id": 529
    },
    {
        "hp": 110,
        "attack": 135,
        "defense": 60,
        "special-attack": 50,
        "special-defense": 65,
        "speed": 88,
        "id": 530
    },
    {
        "hp": 103,
        "attack": 60,
        "defense": 86,
        "special-attack": 60,
        "special-defense": 86,
        "speed": 50,
        "id": 531
    },
    {
        "hp": 75,
        "attack": 80,
        "defense": 55,
        "special-attack": 25,
        "special-defense": 35,
        "speed": 35,
        "id": 532
    },
    {
        "hp": 85,
        "attack": 105,
        "defense": 85,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 40,
        "id": 533
    },
    {
        "hp": 105,
        "attack": 140,
        "defense": 95,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 45,
        "id": 534
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 40,
        "speed": 64,
        "id": 535
    },
    {
        "hp": 75,
        "attack": 65,
        "defense": 55,
        "special-attack": 65,
        "special-defense": 55,
        "speed": 69,
        "id": 536
    },
    {
        "hp": 105,
        "attack": 95,
        "defense": 75,
        "special-attack": 85,
        "special-defense": 75,
        "speed": 74,
        "id": 537
    },
    {
        "hp": 120,
        "attack": 100,
        "defense": 85,
        "special-attack": 30,
        "special-defense": 85,
        "speed": 45,
        "id": 538
    },
    {
        "hp": 75,
        "attack": 125,
        "defense": 75,
        "special-attack": 30,
        "special-defense": 75,
        "speed": 85,
        "id": 539
    },
    {
        "hp": 45,
        "attack": 53,
        "defense": 70,
        "special-attack": 40,
        "special-defense": 60,
        "speed": 42,
        "id": 540
    },
    {
        "hp": 55,
        "attack": 63,
        "defense": 90,
        "special-attack": 50,
        "special-defense": 80,
        "speed": 42,
        "id": 541
    },
    {
        "hp": 75,
        "attack": 103,
        "defense": 80,
        "special-attack": 70,
        "special-defense": 80,
        "speed": 92,
        "id": 542
    },
    {
        "hp": 30,
        "attack": 45,
        "defense": 59,
        "special-attack": 30,
        "special-defense": 39,
        "speed": 57,
        "id": 543
    },
    {
        "hp": 40,
        "attack": 55,
        "defense": 99,
        "special-attack": 40,
        "special-defense": 79,
        "speed": 47,
        "id": 544
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 89,
        "special-attack": 55,
        "special-defense": 69,
        "speed": 112,
        "id": 545
    },
    {
        "hp": 40,
        "attack": 27,
        "defense": 60,
        "special-attack": 37,
        "special-defense": 50,
        "speed": 66,
        "id": 546
    },
    {
        "hp": 60,
        "attack": 67,
        "defense": 85,
        "special-attack": 77,
        "special-defense": 75,
        "speed": 116,
        "id": 547
    },
    {
        "hp": 45,
        "attack": 35,
        "defense": 50,
        "special-attack": 70,
        "special-defense": 50,
        "speed": 30,
        "id": 548
    },
    {
        "hp": 70,
        "attack": 60,
        "defense": 75,
        "special-attack": 110,
        "special-defense": 75,
        "speed": 90,
        "id": 549
    },
    {
        "hp": 70,
        "attack": 92,
        "defense": 65,
        "special-attack": 80,
        "special-defense": 55,
        "speed": 98,
        "id": 550
    },
    {
        "hp": 50,
        "attack": 72,
        "defense": 35,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 65,
        "id": 551
    },
    {
        "hp": 60,
        "attack": 82,
        "defense": 45,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 74,
        "id": 552
    },
    {
        "hp": 95,
        "attack": 117,
        "defense": 80,
        "special-attack": 65,
        "special-defense": 70,
        "speed": 92,
        "id": 553
    },
    {
        "hp": 70,
        "attack": 90,
        "defense": 45,
        "special-attack": 15,
        "special-defense": 45,
        "speed": 50,
        "id": 554
    },
    {
        "hp": 105,
        "attack": 140,
        "defense": 55,
        "special-attack": 30,
        "special-defense": 55,
        "speed": 95,
        "id": 555
    },
    {
        "hp": 75,
        "attack": 86,
        "defense": 67,
        "special-attack": 106,
        "special-defense": 67,
        "speed": 60,
        "id": 556
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 85,
        "special-attack": 35,
        "special-defense": 35,
        "speed": 55,
        "id": 557
    },
    {
        "hp": 70,
        "attack": 105,
        "defense": 125,
        "special-attack": 65,
        "special-defense": 75,
        "speed": 45,
        "id": 558
    },
    {
        "hp": 50,
        "attack": 75,
        "defense": 70,
        "special-attack": 35,
        "special-defense": 70,
        "speed": 48,
        "id": 559
    },
    {
        "hp": 65,
        "attack": 90,
        "defense": 115,
        "special-attack": 45,
        "special-defense": 115,
        "speed": 58,
        "id": 560
    },
    {
        "hp": 72,
        "attack": 58,
        "defense": 80,
        "special-attack": 103,
        "special-defense": 80,
        "speed": 97,
        "id": 561
    },
    {
        "hp": 38,
        "attack": 30,
        "defense": 85,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 30,
        "id": 562
    },
    {
        "hp": 58,
        "attack": 50,
        "defense": 145,
        "special-attack": 95,
        "special-defense": 105,
        "speed": 30,
        "id": 563
    },
    {
        "hp": 54,
        "attack": 78,
        "defense": 103,
        "special-attack": 53,
        "special-defense": 45,
        "speed": 22,
        "id": 564
    },
    {
        "hp": 74,
        "attack": 108,
        "defense": 133,
        "special-attack": 83,
        "special-defense": 65,
        "speed": 32,
        "id": 565
    },
    {
        "hp": 55,
        "attack": 112,
        "defense": 45,
        "special-attack": 74,
        "special-defense": 45,
        "speed": 70,
        "id": 566
    },
    {
        "hp": 75,
        "attack": 140,
        "defense": 65,
        "special-attack": 112,
        "special-defense": 65,
        "speed": 110,
        "id": 567
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 62,
        "special-attack": 40,
        "special-defense": 62,
        "speed": 65,
        "id": 568
    },
    {
        "hp": 80,
        "attack": 95,
        "defense": 82,
        "special-attack": 60,
        "special-defense": 82,
        "speed": 75,
        "id": 569
    },
    {
        "hp": 40,
        "attack": 65,
        "defense": 40,
        "special-attack": 80,
        "special-defense": 40,
        "speed": 65,
        "id": 570
    },
    {
        "hp": 60,
        "attack": 105,
        "defense": 60,
        "special-attack": 120,
        "special-defense": 60,
        "speed": 105,
        "id": 571
    },
    {
        "hp": 55,
        "attack": 50,
        "defense": 40,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 75,
        "id": 572
    },
    {
        "hp": 75,
        "attack": 95,
        "defense": 60,
        "special-attack": 65,
        "special-defense": 60,
        "speed": 115,
        "id": 573
    },
    {
        "hp": 45,
        "attack": 30,
        "defense": 50,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 45,
        "id": 574
    },
    {
        "hp": 60,
        "attack": 45,
        "defense": 70,
        "special-attack": 75,
        "special-defense": 85,
        "speed": 55,
        "id": 575
    },
    {
        "hp": 70,
        "attack": 55,
        "defense": 95,
        "special-attack": 95,
        "special-defense": 110,
        "speed": 65,
        "id": 576
    },
    {
        "hp": 45,
        "attack": 30,
        "defense": 40,
        "special-attack": 105,
        "special-defense": 50,
        "speed": 20,
        "id": 577
    },
    {
        "hp": 65,
        "attack": 40,
        "defense": 50,
        "special-attack": 125,
        "special-defense": 60,
        "speed": 30,
        "id": 578
    },
    {
        "hp": 110,
        "attack": 65,
        "defense": 75,
        "special-attack": 125,
        "special-defense": 85,
        "speed": 30,
        "id": 579
    },
    {
        "hp": 62,
        "attack": 44,
        "defense": 50,
        "special-attack": 44,
        "special-defense": 50,
        "speed": 55,
        "id": 580
    },
    {
        "hp": 75,
        "attack": 87,
        "defense": 63,
        "special-attack": 87,
        "special-defense": 63,
        "speed": 98,
        "id": 581
    },
    {
        "hp": 36,
        "attack": 50,
        "defense": 50,
        "special-attack": 65,
        "special-defense": 60,
        "speed": 44,
        "id": 582
    },
    {
        "hp": 51,
        "attack": 65,
        "defense": 65,
        "special-attack": 80,
        "special-defense": 75,
        "speed": 59,
        "id": 583
    },
    {
        "hp": 71,
        "attack": 95,
        "defense": 85,
        "special-attack": 110,
        "special-defense": 95,
        "speed": 79,
        "id": 584
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 75,
        "id": 585
    },
    {
        "hp": 80,
        "attack": 100,
        "defense": 70,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 95,
        "id": 586
    },
    {
        "hp": 55,
        "attack": 75,
        "defense": 60,
        "special-attack": 75,
        "special-defense": 60,
        "speed": 103,
        "id": 587
    },
    {
        "hp": 50,
        "attack": 75,
        "defense": 45,
        "special-attack": 40,
        "special-defense": 45,
        "speed": 60,
        "id": 588
    },
    {
        "hp": 70,
        "attack": 135,
        "defense": 105,
        "special-attack": 60,
        "special-defense": 105,
        "speed": 20,
        "id": 589
    },
    {
        "hp": 69,
        "attack": 55,
        "defense": 45,
        "special-attack": 55,
        "special-defense": 55,
        "speed": 15,
        "id": 590
    },
    {
        "hp": 114,
        "attack": 85,
        "defense": 70,
        "special-attack": 85,
        "special-defense": 80,
        "speed": 30,
        "id": 591
    },
    {
        "hp": 55,
        "attack": 40,
        "defense": 50,
        "special-attack": 65,
        "special-defense": 85,
        "speed": 40,
        "id": 592
    },
    {
        "hp": 100,
        "attack": 60,
        "defense": 70,
        "special-attack": 85,
        "special-defense": 105,
        "speed": 60,
        "id": 593
    },
    {
        "hp": 165,
        "attack": 75,
        "defense": 80,
        "special-attack": 40,
        "special-defense": 45,
        "speed": 65,
        "id": 594
    },
    {
        "hp": 50,
        "attack": 47,
        "defense": 50,
        "special-attack": 57,
        "special-defense": 50,
        "speed": 65,
        "id": 595
    },
    {
        "hp": 70,
        "attack": 77,
        "defense": 60,
        "special-attack": 97,
        "special-defense": 60,
        "speed": 108,
        "id": 596
    },
    {
        "hp": 44,
        "attack": 50,
        "defense": 91,
        "special-attack": 24,
        "special-defense": 86,
        "speed": 10,
        "id": 597
    },
    {
        "hp": 74,
        "attack": 94,
        "defense": 131,
        "special-attack": 54,
        "special-defense": 116,
        "speed": 20,
        "id": 598
    },
    {
        "hp": 40,
        "attack": 55,
        "defense": 70,
        "special-attack": 45,
        "special-defense": 60,
        "speed": 30,
        "id": 599
    },
    {
        "hp": 60,
        "attack": 80,
        "defense": 95,
        "special-attack": 70,
        "special-defense": 85,
        "speed": 50,
        "id": 600
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 115,
        "special-attack": 70,
        "special-defense": 85,
        "speed": 90,
        "id": 601
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 45,
        "special-defense": 40,
        "speed": 60,
        "id": 602
    },
    {
        "hp": 65,
        "attack": 85,
        "defense": 70,
        "special-attack": 75,
        "special-defense": 70,
        "speed": 40,
        "id": 603
    },
    {
        "hp": 85,
        "attack": 115,
        "defense": 80,
        "special-attack": 105,
        "special-defense": 80,
        "speed": 50,
        "id": 604
    },
    {
        "hp": 55,
        "attack": 55,
        "defense": 55,
        "special-attack": 85,
        "special-defense": 55,
        "speed": 30,
        "id": 605
    },
    {
        "hp": 75,
        "attack": 75,
        "defense": 75,
        "special-attack": 125,
        "special-defense": 95,
        "speed": 40,
        "id": 606
    },
    {
        "hp": 50,
        "attack": 30,
        "defense": 55,
        "special-attack": 65,
        "special-defense": 55,
        "speed": 20,
        "id": 607
    },
    {
        "hp": 60,
        "attack": 40,
        "defense": 60,
        "special-attack": 95,
        "special-defense": 60,
        "speed": 55,
        "id": 608
    },
    {
        "hp": 60,
        "attack": 55,
        "defense": 90,
        "special-attack": 145,
        "special-defense": 90,
        "speed": 80,
        "id": 609
    },
    {
        "hp": 46,
        "attack": 87,
        "defense": 60,
        "special-attack": 30,
        "special-defense": 40,
        "speed": 57,
        "id": 610
    },
    {
        "hp": 66,
        "attack": 117,
        "defense": 70,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 67,
        "id": 611
    },
    {
        "hp": 76,
        "attack": 147,
        "defense": 90,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 97,
        "id": 612
    },
    {
        "hp": 55,
        "attack": 70,
        "defense": 40,
        "special-attack": 60,
        "special-defense": 40,
        "speed": 40,
        "id": 613
    },
    {
        "hp": 95,
        "attack": 130,
        "defense": 80,
        "special-attack": 70,
        "special-defense": 80,
        "speed": 50,
        "id": 614
    },
    {
        "hp": 80,
        "attack": 50,
        "defense": 50,
        "special-attack": 95,
        "special-defense": 135,
        "speed": 105,
        "id": 615
    },
    {
        "hp": 50,
        "attack": 40,
        "defense": 85,
        "special-attack": 40,
        "special-defense": 65,
        "speed": 25,
        "id": 616
    },
    {
        "hp": 80,
        "attack": 70,
        "defense": 40,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 145,
        "id": 617
    },
    {
        "hp": 109,
        "attack": 66,
        "defense": 84,
        "special-attack": 81,
        "special-defense": 99,
        "speed": 32,
        "id": 618
    },
    {
        "hp": 45,
        "attack": 85,
        "defense": 50,
        "special-attack": 55,
        "special-defense": 50,
        "speed": 65,
        "id": 619
    },
    {
        "hp": 65,
        "attack": 125,
        "defense": 60,
        "special-attack": 95,
        "special-defense": 60,
        "speed": 105,
        "id": 620
    },
    {
        "hp": 77,
        "attack": 120,
        "defense": 90,
        "special-attack": 60,
        "special-defense": 90,
        "speed": 48,
        "id": 621
    },
    {
        "hp": 59,
        "attack": 74,
        "defense": 50,
        "special-attack": 35,
        "special-defense": 50,
        "speed": 35,
        "id": 622
    },
    {
        "hp": 89,
        "attack": 124,
        "defense": 80,
        "special-attack": 55,
        "special-defense": 80,
        "speed": 55,
        "id": 623
    },
    {
        "hp": 45,
        "attack": 85,
        "defense": 70,
        "special-attack": 40,
        "special-defense": 40,
        "speed": 60,
        "id": 624
    },
    {
        "hp": 65,
        "attack": 125,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 70,
        "speed": 70,
        "id": 625
    },
    {
        "hp": 95,
        "attack": 110,
        "defense": 95,
        "special-attack": 40,
        "special-defense": 95,
        "speed": 55,
        "id": 626
    },
    {
        "hp": 70,
        "attack": 83,
        "defense": 50,
        "special-attack": 37,
        "special-defense": 50,
        "speed": 60,
        "id": 627
    },
    {
        "hp": 100,
        "attack": 123,
        "defense": 75,
        "special-attack": 57,
        "special-defense": 75,
        "speed": 80,
        "id": 628
    },
    {
        "hp": 70,
        "attack": 55,
        "defense": 75,
        "special-attack": 45,
        "special-defense": 65,
        "speed": 60,
        "id": 629
    },
    {
        "hp": 110,
        "attack": 65,
        "defense": 105,
        "special-attack": 55,
        "special-defense": 95,
        "speed": 80,
        "id": 630
    },
    {
        "hp": 85,
        "attack": 97,
        "defense": 66,
        "special-attack": 105,
        "special-defense": 66,
        "speed": 65,
        "id": 631
    },
    {
        "hp": 58,
        "attack": 109,
        "defense": 112,
        "special-attack": 48,
        "special-defense": 48,
        "speed": 109,
        "id": 632
    },
    {
        "hp": 52,
        "attack": 65,
        "defense": 50,
        "special-attack": 45,
        "special-defense": 50,
        "speed": 38,
        "id": 633
    },
    {
        "hp": 72,
        "attack": 85,
        "defense": 70,
        "special-attack": 65,
        "special-defense": 70,
        "speed": 58,
        "id": 634
    },
    {
        "hp": 92,
        "attack": 105,
        "defense": 90,
        "special-attack": 125,
        "special-defense": 90,
        "speed": 98,
        "id": 635
    },
    {
        "hp": 55,
        "attack": 85,
        "defense": 55,
        "special-attack": 50,
        "special-defense": 55,
        "speed": 60,
        "id": 636
    },
    {
        "hp": 85,
        "attack": 60,
        "defense": 65,
        "special-attack": 135,
        "special-defense": 105,
        "speed": 100,
        "id": 637
    },
    {
        "hp": 91,
        "attack": 90,
        "defense": 129,
        "special-attack": 90,
        "special-defense": 72,
        "speed": 108,
        "id": 638
    },
    {
        "hp": 91,
        "attack": 129,
        "defense": 90,
        "special-attack": 72,
        "special-defense": 90,
        "speed": 108,
        "id": 639
    },
    {
        "hp": 91,
        "attack": 90,
        "defense": 72,
        "special-attack": 90,
        "special-defense": 129,
        "speed": 108,
        "id": 640
    },
    {
        "hp": 79,
        "attack": 115,
        "defense": 70,
        "special-attack": 125,
        "special-defense": 80,
        "speed": 111,
        "id": 641
    },
    {
        "hp": 79,
        "attack": 115,
        "defense": 70,
        "special-attack": 125,
        "special-defense": 80,
        "speed": 111,
        "id": 642
    },
    {
        "hp": 100,
        "attack": 120,
        "defense": 100,
        "special-attack": 150,
        "special-defense": 120,
        "speed": 90,
        "id": 643
    },
    {
        "hp": 100,
        "attack": 150,
        "defense": 120,
        "special-attack": 120,
        "special-defense": 100,
        "speed": 90,
        "id": 644
    },
    {
        "hp": 89,
        "attack": 125,
        "defense": 90,
        "special-attack": 115,
        "special-defense": 80,
        "speed": 101,
        "id": 645
    },
    {
        "hp": 125,
        "attack": 130,
        "defense": 90,
        "special-attack": 130,
        "special-defense": 90,
        "speed": 95,
        "id": 646
    },
    {
        "hp": 91,
        "attack": 72,
        "defense": 90,
        "special-attack": 129,
        "special-defense": 90,
        "speed": 108,
        "id": 647
    },
    {
        "hp": 100,
        "attack": 77,
        "defense": 77,
        "special-attack": 128,
        "special-defense": 128,
        "speed": 90,
        "id": 648
    },
    {
        "hp": 71,
        "attack": 120,
        "defense": 95,
        "special-attack": 120,
        "special-defense": 95,
        "speed": 99,
        "id": 649
    },
    {
        "hp": 56,
        "attack": 61,
        "defense": 65,
        "special-attack": 48,
        "special-defense": 45,
        "speed": 38,
        "id": 650
    },
    {
        "hp": 61,
        "attack": 78,
        "defense": 95,
        "special-attack": 56,
        "special-defense": 58,
        "speed": 57,
        "id": 651
    },
    {
        "hp": 88,
        "attack": 107,
        "defense": 122,
        "special-attack": 74,
        "special-defense": 75,
        "speed": 64,
        "id": 652
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "special-attack": 62,
        "special-defense": 60,
        "speed": 60,
        "id": 653
    },
    {
        "hp": 59,
        "attack": 59,
        "defense": 58,
        "special-attack": 90,
        "special-defense": 70,
        "speed": 73,
        "id": 654
    },
    {
        "hp": 75,
        "attack": 69,
        "defense": 72,
        "special-attack": 114,
        "special-defense": 100,
        "speed": 104,
        "id": 655
    },
    {
        "hp": 41,
        "attack": 56,
        "defense": 40,
        "special-attack": 62,
        "special-defense": 44,
        "speed": 71,
        "id": 656
    },
    {
        "hp": 54,
        "attack": 63,
        "defense": 52,
        "special-attack": 83,
        "special-defense": 56,
        "speed": 97,
        "id": 657
    },
    {
        "hp": 72,
        "attack": 95,
        "defense": 67,
        "special-attack": 103,
        "special-defense": 71,
        "speed": 122,
        "id": 658
    },
    {
        "hp": 38,
        "attack": 36,
        "defense": 38,
        "special-attack": 32,
        "special-defense": 36,
        "speed": 57,
        "id": 659
    },
    {
        "hp": 85,
        "attack": 56,
        "defense": 77,
        "special-attack": 50,
        "special-defense": 77,
        "speed": 78,
        "id": 660
    },
    {
        "hp": 45,
        "attack": 50,
        "defense": 43,
        "special-attack": 40,
        "special-defense": 38,
        "speed": 62,
        "id": 661
    },
    {
        "hp": 62,
        "attack": 73,
        "defense": 55,
        "special-attack": 56,
        "special-defense": 52,
        "speed": 84,
        "id": 662
    },
    {
        "hp": 78,
        "attack": 81,
        "defense": 71,
        "special-attack": 74,
        "special-defense": 69,
        "speed": 126,
        "id": 663
    },
    {
        "hp": 38,
        "attack": 35,
        "defense": 40,
        "special-attack": 27,
        "special-defense": 25,
        "speed": 35,
        "id": 664
    },
    {
        "hp": 45,
        "attack": 22,
        "defense": 60,
        "special-attack": 27,
        "special-defense": 30,
        "speed": 29,
        "id": 665
    },
    {
        "hp": 80,
        "attack": 52,
        "defense": 50,
        "special-attack": 90,
        "special-defense": 50,
        "speed": 89,
        "id": 666
    },
    {
        "hp": 62,
        "attack": 50,
        "defense": 58,
        "special-attack": 73,
        "special-defense": 54,
        "speed": 72,
        "id": 667
    },
    {
        "hp": 86,
        "attack": 68,
        "defense": 72,
        "special-attack": 109,
        "special-defense": 66,
        "speed": 106,
        "id": 668
    },
    {
        "hp": 44,
        "attack": 38,
        "defense": 39,
        "special-attack": 61,
        "special-defense": 79,
        "speed": 42,
        "id": 669
    },
    {
        "hp": 54,
        "attack": 45,
        "defense": 47,
        "special-attack": 75,
        "special-defense": 98,
        "speed": 52,
        "id": 670
    },
    {
        "hp": 78,
        "attack": 65,
        "defense": 68,
        "special-attack": 112,
        "special-defense": 154,
        "speed": 75,
        "id": 671
    },
    {
        "hp": 66,
        "attack": 65,
        "defense": 48,
        "special-attack": 62,
        "special-defense": 57,
        "speed": 52,
        "id": 672
    },
    {
        "hp": 123,
        "attack": 100,
        "defense": 62,
        "special-attack": 97,
        "special-defense": 81,
        "speed": 68,
        "id": 673
    },
    {
        "hp": 67,
        "attack": 82,
        "defense": 62,
        "special-attack": 46,
        "special-defense": 48,
        "speed": 43,
        "id": 674
    },
    {
        "hp": 95,
        "attack": 124,
        "defense": 78,
        "special-attack": 69,
        "special-defense": 71,
        "speed": 58,
        "id": 675
    },
    {
        "hp": 75,
        "attack": 80,
        "defense": 60,
        "special-attack": 65,
        "special-defense": 90,
        "speed": 102,
        "id": 676
    },
    {
        "hp": 62,
        "attack": 48,
        "defense": 54,
        "special-attack": 63,
        "special-defense": 60,
        "speed": 68,
        "id": 677
    },
    {
        "hp": 74,
        "attack": 48,
        "defense": 76,
        "special-attack": 83,
        "special-defense": 81,
        "speed": 104,
        "id": 678
    },
    {
        "hp": 45,
        "attack": 80,
        "defense": 100,
        "special-attack": 35,
        "special-defense": 37,
        "speed": 28,
        "id": 679
    },
    {
        "hp": 59,
        "attack": 110,
        "defense": 150,
        "special-attack": 45,
        "special-defense": 49,
        "speed": 35,
        "id": 680
    },
    {
        "hp": 60,
        "attack": 50,
        "defense": 150,
        "special-attack": 50,
        "special-defense": 150,
        "speed": 60,
        "id": 681
    },
    {
        "hp": 78,
        "attack": 52,
        "defense": 60,
        "special-attack": 63,
        "special-defense": 65,
        "speed": 23,
        "id": 682
    },
    {
        "hp": 101,
        "attack": 72,
        "defense": 72,
        "special-attack": 99,
        "special-defense": 89,
        "speed": 29,
        "id": 683
    },
    {
        "hp": 62,
        "attack": 48,
        "defense": 66,
        "special-attack": 59,
        "special-defense": 57,
        "speed": 49,
        "id": 684
    },
    {
        "hp": 82,
        "attack": 80,
        "defense": 86,
        "special-attack": 85,
        "special-defense": 75,
        "speed": 72,
        "id": 685
    },
    {
        "hp": 53,
        "attack": 54,
        "defense": 53,
        "special-attack": 37,
        "special-defense": 46,
        "speed": 45,
        "id": 686
    },
    {
        "hp": 86,
        "attack": 92,
        "defense": 88,
        "special-attack": 68,
        "special-defense": 75,
        "speed": 73,
        "id": 687
    },
    {
        "hp": 42,
        "attack": 52,
        "defense": 67,
        "special-attack": 39,
        "special-defense": 56,
        "speed": 50,
        "id": 688
    },
    {
        "hp": 72,
        "attack": 105,
        "defense": 115,
        "special-attack": 54,
        "special-defense": 86,
        "speed": 68,
        "id": 689
    },
    {
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "special-attack": 60,
        "special-defense": 60,
        "speed": 30,
        "id": 690
    },
    {
        "hp": 65,
        "attack": 75,
        "defense": 90,
        "special-attack": 97,
        "special-defense": 123,
        "speed": 44,
        "id": 691
    },
    {
        "hp": 50,
        "attack": 53,
        "defense": 62,
        "special-attack": 58,
        "special-defense": 63,
        "speed": 44,
        "id": 692
    },
    {
        "hp": 71,
        "attack": 73,
        "defense": 88,
        "special-attack": 120,
        "special-defense": 89,
        "speed": 59,
        "id": 693
    },
    {
        "hp": 44,
        "attack": 38,
        "defense": 33,
        "special-attack": 61,
        "special-defense": 43,
        "speed": 70,
        "id": 694
    },
    {
        "hp": 62,
        "attack": 55,
        "defense": 52,
        "special-attack": 109,
        "special-defense": 94,
        "speed": 109,
        "id": 695
    },
    {
        "hp": 58,
        "attack": 89,
        "defense": 77,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 48,
        "id": 696
    },
    {
        "hp": 82,
        "attack": 121,
        "defense": 119,
        "special-attack": 69,
        "special-defense": 59,
        "speed": 71,
        "id": 697
    },
    {
        "hp": 77,
        "attack": 59,
        "defense": 50,
        "special-attack": 67,
        "special-defense": 63,
        "speed": 46,
        "id": 698
    },
    {
        "hp": 123,
        "attack": 77,
        "defense": 72,
        "special-attack": 99,
        "special-defense": 92,
        "speed": 58,
        "id": 699
    },
    {
        "hp": 95,
        "attack": 65,
        "defense": 65,
        "special-attack": 110,
        "special-defense": 130,
        "speed": 60,
        "id": 700
    },
    {
        "hp": 78,
        "attack": 92,
        "defense": 75,
        "special-attack": 74,
        "special-defense": 63,
        "speed": 118,
        "id": 701
    },
    {
        "hp": 67,
        "attack": 58,
        "defense": 57,
        "special-attack": 81,
        "special-defense": 67,
        "speed": 101,
        "id": 702
    },
    {
        "hp": 50,
        "attack": 50,
        "defense": 150,
        "special-attack": 50,
        "special-defense": 150,
        "speed": 50,
        "id": 703
    },
    {
        "hp": 45,
        "attack": 50,
        "defense": 35,
        "special-attack": 55,
        "special-defense": 75,
        "speed": 40,
        "id": 704
    },
    {
        "hp": 68,
        "attack": 75,
        "defense": 53,
        "special-attack": 83,
        "special-defense": 113,
        "speed": 60,
        "id": 705
    },
    {
        "hp": 90,
        "attack": 100,
        "defense": 70,
        "special-attack": 110,
        "special-defense": 150,
        "speed": 80,
        "id": 706
    },
    {
        "hp": 57,
        "attack": 80,
        "defense": 91,
        "special-attack": 80,
        "special-defense": 87,
        "speed": 75,
        "id": 707
    },
    {
        "hp": 43,
        "attack": 70,
        "defense": 48,
        "special-attack": 50,
        "special-defense": 60,
        "speed": 38,
        "id": 708
    },
    {
        "hp": 85,
        "attack": 110,
        "defense": 76,
        "special-attack": 65,
        "special-defense": 82,
        "speed": 56,
        "id": 709
    },
    {
        "hp": 49,
        "attack": 66,
        "defense": 70,
        "special-attack": 44,
        "special-defense": 55,
        "speed": 51,
        "id": 710
    },
    {
        "hp": 65,
        "attack": 90,
        "defense": 122,
        "special-attack": 58,
        "special-defense": 75,
        "speed": 84,
        "id": 711
    },
    {
        "hp": 55,
        "attack": 69,
        "defense": 85,
        "special-attack": 32,
        "special-defense": 35,
        "speed": 28,
        "id": 712
    },
    {
        "hp": 95,
        "attack": 117,
        "defense": 184,
        "special-attack": 44,
        "special-defense": 46,
        "speed": 28,
        "id": 713
    },
    {
        "hp": 40,
        "attack": 30,
        "defense": 35,
        "special-attack": 45,
        "special-defense": 40,
        "speed": 55,
        "id": 714
    },
    {
        "hp": 85,
        "attack": 70,
        "defense": 80,
        "special-attack": 97,
        "special-defense": 80,
        "speed": 123,
        "id": 715
    },
    {
        "hp": 126,
        "attack": 131,
        "defense": 95,
        "special-attack": 131,
        "special-defense": 98,
        "speed": 99,
        "id": 716
    },
    {
        "hp": 126,
        "attack": 131,
        "defense": 95,
        "special-attack": 131,
        "special-defense": 98,
        "speed": 99,
        "id": 717
    },
    {
        "hp": 108,
        "attack": 100,
        "defense": 121,
        "special-attack": 81,
        "special-defense": 95,
        "speed": 95,
        "id": 718
    },
    {
        "hp": 50,
        "attack": 100,
        "defense": 150,
        "special-attack": 100,
        "special-defense": 150,
        "speed": 50,
        "id": 719
    },
    {
        "hp": 80,
        "attack": 110,
        "defense": 60,
        "special-attack": 150,
        "special-defense": 130,
        "speed": 70,
        "id": 720
    },
    {
        "hp": 80,
        "attack": 110,
        "defense": 120,
        "special-attack": 130,
        "special-defense": 90,
        "speed": 70,
        "id": 721
    },
    {
        "hp": 68,
        "attack": 55,
        "defense": 55,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 42,
        "id": 722
    },
    {
        "hp": 78,
        "attack": 75,
        "defense": 75,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 52,
        "id": 723
    },
    {
        "hp": 78,
        "attack": 107,
        "defense": 75,
        "special-attack": 100,
        "special-defense": 100,
        "speed": 70,
        "id": 724
    },
    {
        "hp": 45,
        "attack": 65,
        "defense": 40,
        "special-attack": 60,
        "special-defense": 40,
        "speed": 70,
        "id": 725
    },
    {
        "hp": 65,
        "attack": 85,
        "defense": 50,
        "special-attack": 80,
        "special-defense": 50,
        "speed": 90,
        "id": 726
    },
    {
        "hp": 95,
        "attack": 115,
        "defense": 90,
        "special-attack": 80,
        "special-defense": 90,
        "speed": 60,
        "id": 727
    },
    {
        "hp": 50,
        "attack": 54,
        "defense": 54,
        "special-attack": 66,
        "special-defense": 56,
        "speed": 40,
        "id": 728
    },
    {
        "hp": 60,
        "attack": 69,
        "defense": 69,
        "special-attack": 91,
        "special-defense": 81,
        "speed": 50,
        "id": 729
    },
    {
        "hp": 80,
        "attack": 74,
        "defense": 74,
        "special-attack": 126,
        "special-defense": 116,
        "speed": 60,
        "id": 730
    },
    {
        "hp": 35,
        "attack": 75,
        "defense": 30,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 65,
        "id": 731
    },
    {
        "hp": 55,
        "attack": 85,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 75,
        "id": 732
    },
    {
        "hp": 80,
        "attack": 120,
        "defense": 75,
        "special-attack": 75,
        "special-defense": 75,
        "speed": 60,
        "id": 733
    },
    {
        "hp": 48,
        "attack": 70,
        "defense": 30,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 45,
        "id": 734
    },
    {
        "hp": 88,
        "attack": 110,
        "defense": 60,
        "special-attack": 55,
        "special-defense": 60,
        "speed": 45,
        "id": 735
    },
    {
        "hp": 47,
        "attack": 62,
        "defense": 45,
        "special-attack": 55,
        "special-defense": 45,
        "speed": 46,
        "id": 736
    },
    {
        "hp": 57,
        "attack": 82,
        "defense": 95,
        "special-attack": 55,
        "special-defense": 75,
        "speed": 36,
        "id": 737
    },
    {
        "hp": 77,
        "attack": 70,
        "defense": 90,
        "special-attack": 145,
        "special-defense": 75,
        "speed": 43,
        "id": 738
    },
    {
        "hp": 47,
        "attack": 82,
        "defense": 57,
        "special-attack": 42,
        "special-defense": 47,
        "speed": 63,
        "id": 739
    },
    {
        "hp": 97,
        "attack": 132,
        "defense": 77,
        "special-attack": 62,
        "special-defense": 67,
        "speed": 43,
        "id": 740
    },
    {
        "hp": 75,
        "attack": 70,
        "defense": 70,
        "special-attack": 98,
        "special-defense": 70,
        "speed": 93,
        "id": 741
    },
    {
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "special-attack": 55,
        "special-defense": 40,
        "speed": 84,
        "id": 742
    },
    {
        "hp": 60,
        "attack": 55,
        "defense": 60,
        "special-attack": 95,
        "special-defense": 70,
        "speed": 124,
        "id": 743
    },
    {
        "hp": 45,
        "attack": 65,
        "defense": 40,
        "special-attack": 30,
        "special-defense": 40,
        "speed": 60,
        "id": 744
    },
    {
        "hp": 75,
        "attack": 115,
        "defense": 65,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 112,
        "id": 745
    },
    {
        "hp": 45,
        "attack": 20,
        "defense": 20,
        "special-attack": 25,
        "special-defense": 25,
        "speed": 40,
        "id": 746
    },
    {
        "hp": 50,
        "attack": 53,
        "defense": 62,
        "special-attack": 43,
        "special-defense": 52,
        "speed": 45,
        "id": 747
    },
    {
        "hp": 50,
        "attack": 63,
        "defense": 152,
        "special-attack": 53,
        "special-defense": 142,
        "speed": 35,
        "id": 748
    },
    {
        "hp": 70,
        "attack": 100,
        "defense": 70,
        "special-attack": 45,
        "special-defense": 55,
        "speed": 45,
        "id": 749
    },
    {
        "hp": 100,
        "attack": 125,
        "defense": 100,
        "special-attack": 55,
        "special-defense": 85,
        "speed": 35,
        "id": 750
    },
    {
        "hp": 38,
        "attack": 40,
        "defense": 52,
        "special-attack": 40,
        "special-defense": 72,
        "speed": 27,
        "id": 751
    },
    {
        "hp": 68,
        "attack": 70,
        "defense": 92,
        "special-attack": 50,
        "special-defense": 132,
        "speed": 42,
        "id": 752
    },
    {
        "hp": 40,
        "attack": 55,
        "defense": 35,
        "special-attack": 50,
        "special-defense": 35,
        "speed": 35,
        "id": 753
    },
    {
        "hp": 70,
        "attack": 105,
        "defense": 90,
        "special-attack": 80,
        "special-defense": 90,
        "speed": 45,
        "id": 754
    },
    {
        "hp": 40,
        "attack": 35,
        "defense": 55,
        "special-attack": 65,
        "special-defense": 75,
        "speed": 15,
        "id": 755
    },
    {
        "hp": 60,
        "attack": 45,
        "defense": 80,
        "special-attack": 90,
        "special-defense": 100,
        "speed": 30,
        "id": 756
    },
    {
        "hp": 48,
        "attack": 44,
        "defense": 40,
        "special-attack": 71,
        "special-defense": 40,
        "speed": 77,
        "id": 757
    },
    {
        "hp": 68,
        "attack": 64,
        "defense": 60,
        "special-attack": 111,
        "special-defense": 60,
        "speed": 117,
        "id": 758
    },
    {
        "hp": 70,
        "attack": 75,
        "defense": 50,
        "special-attack": 45,
        "special-defense": 50,
        "speed": 50,
        "id": 759
    },
    {
        "hp": 120,
        "attack": 125,
        "defense": 80,
        "special-attack": 55,
        "special-defense": 60,
        "speed": 60,
        "id": 760
    },
    {
        "hp": 42,
        "attack": 30,
        "defense": 38,
        "special-attack": 30,
        "special-defense": 38,
        "speed": 32,
        "id": 761
    },
    {
        "hp": 52,
        "attack": 40,
        "defense": 48,
        "special-attack": 40,
        "special-defense": 48,
        "speed": 62,
        "id": 762
    },
    {
        "hp": 72,
        "attack": 120,
        "defense": 98,
        "special-attack": 50,
        "special-defense": 98,
        "speed": 72,
        "id": 763
    },
    {
        "hp": 51,
        "attack": 52,
        "defense": 90,
        "special-attack": 82,
        "special-defense": 110,
        "speed": 100,
        "id": 764
    },
    {
        "hp": 90,
        "attack": 60,
        "defense": 80,
        "special-attack": 90,
        "special-defense": 110,
        "speed": 60,
        "id": 765
    },
    {
        "hp": 100,
        "attack": 120,
        "defense": 90,
        "special-attack": 40,
        "special-defense": 60,
        "speed": 80,
        "id": 766
    },
    {
        "hp": 25,
        "attack": 35,
        "defense": 40,
        "special-attack": 20,
        "special-defense": 30,
        "speed": 80,
        "id": 767
    },
    {
        "hp": 75,
        "attack": 125,
        "defense": 140,
        "special-attack": 60,
        "special-defense": 90,
        "speed": 40,
        "id": 768
    },
    {
        "hp": 55,
        "attack": 55,
        "defense": 80,
        "special-attack": 70,
        "special-defense": 45,
        "speed": 15,
        "id": 769
    },
    {
        "hp": 85,
        "attack": 75,
        "defense": 110,
        "special-attack": 100,
        "special-defense": 75,
        "speed": 35,
        "id": 770
    },
    {
        "hp": 55,
        "attack": 60,
        "defense": 130,
        "special-attack": 30,
        "special-defense": 130,
        "speed": 5,
        "id": 771
    },
    {
        "hp": 95,
        "attack": 95,
        "defense": 95,
        "special-attack": 95,
        "special-defense": 95,
        "speed": 59,
        "id": 772
    },
    {
        "hp": 95,
        "attack": 95,
        "defense": 95,
        "special-attack": 95,
        "special-defense": 95,
        "speed": 95,
        "id": 773
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 774
    },
    {
        "hp": 65,
        "attack": 115,
        "defense": 65,
        "special-attack": 75,
        "special-defense": 95,
        "speed": 65,
        "id": 775
    },
    {
        "hp": 60,
        "attack": 78,
        "defense": 135,
        "special-attack": 91,
        "special-defense": 85,
        "speed": 36,
        "id": 776
    },
    {
        "hp": 65,
        "attack": 98,
        "defense": 63,
        "special-attack": 40,
        "special-defense": 73,
        "speed": 96,
        "id": 777
    },
    {
        "hp": 55,
        "attack": 90,
        "defense": 80,
        "special-attack": 50,
        "special-defense": 105,
        "speed": 96,
        "id": 778
    },
    {
        "hp": 68,
        "attack": 105,
        "defense": 70,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 92,
        "id": 779
    },
    {
        "hp": 78,
        "attack": 60,
        "defense": 85,
        "special-attack": 135,
        "special-defense": 91,
        "speed": 36,
        "id": 780
    },
    {
        "hp": 70,
        "attack": 131,
        "defense": 100,
        "special-attack": 86,
        "special-defense": 90,
        "speed": 40,
        "id": 781
    },
    {
        "hp": 45,
        "attack": 55,
        "defense": 65,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 45,
        "id": 782
    },
    {
        "hp": 55,
        "attack": 75,
        "defense": 90,
        "special-attack": 65,
        "special-defense": 70,
        "speed": 65,
        "id": 783
    },
    {
        "hp": 75,
        "attack": 110,
        "defense": 125,
        "special-attack": 100,
        "special-defense": 105,
        "speed": 85,
        "id": 784
    },
    {
        "hp": 70,
        "attack": 115,
        "defense": 85,
        "special-attack": 95,
        "special-defense": 75,
        "speed": 130,
        "id": 785
    },
    {
        "hp": 70,
        "attack": 85,
        "defense": 75,
        "special-attack": 130,
        "special-defense": 115,
        "speed": 95,
        "id": 786
    },
    {
        "hp": 70,
        "attack": 130,
        "defense": 115,
        "special-attack": 85,
        "special-defense": 95,
        "speed": 75,
        "id": 787
    },
    {
        "hp": 70,
        "attack": 75,
        "defense": 115,
        "special-attack": 95,
        "special-defense": 130,
        "speed": 85,
        "id": 788
    },
    {
        "hp": 43,
        "attack": 29,
        "defense": 31,
        "special-attack": 29,
        "special-defense": 31,
        "speed": 37,
        "id": 789
    },
    {
        "hp": 43,
        "attack": 29,
        "defense": 131,
        "special-attack": 29,
        "special-defense": 131,
        "speed": 37,
        "id": 790
    },
    {
        "hp": 137,
        "attack": 137,
        "defense": 107,
        "special-attack": 113,
        "special-defense": 89,
        "speed": 97,
        "id": 791
    },
    {
        "hp": 137,
        "attack": 113,
        "defense": 89,
        "special-attack": 137,
        "special-defense": 107,
        "speed": 97,
        "id": 792
    },
    {
        "hp": 109,
        "attack": 53,
        "defense": 47,
        "special-attack": 127,
        "special-defense": 131,
        "speed": 103,
        "id": 793
    },
    {
        "hp": 107,
        "attack": 139,
        "defense": 139,
        "special-attack": 53,
        "special-defense": 53,
        "speed": 79,
        "id": 794
    },
    {
        "hp": 71,
        "attack": 137,
        "defense": 37,
        "special-attack": 137,
        "special-defense": 37,
        "speed": 151,
        "id": 795
    },
    {
        "hp": 83,
        "attack": 89,
        "defense": 71,
        "special-attack": 173,
        "special-defense": 71,
        "speed": 83,
        "id": 796
    },
    {
        "hp": 97,
        "attack": 101,
        "defense": 103,
        "special-attack": 107,
        "special-defense": 101,
        "speed": 61,
        "id": 797
    },
    {
        "hp": 59,
        "attack": 181,
        "defense": 131,
        "special-attack": 59,
        "special-defense": 31,
        "speed": 109,
        "id": 798
    },
    {
        "hp": 223,
        "attack": 101,
        "defense": 53,
        "special-attack": 97,
        "special-defense": 53,
        "speed": 43,
        "id": 799
    },
    {
        "hp": 97,
        "attack": 107,
        "defense": 101,
        "special-attack": 127,
        "special-defense": 89,
        "speed": 79,
        "id": 800
    },
    {
        "hp": 80,
        "attack": 95,
        "defense": 115,
        "special-attack": 130,
        "special-defense": 115,
        "speed": 65,
        "id": 801
    },
    {
        "hp": 90,
        "attack": 125,
        "defense": 80,
        "special-attack": 90,
        "special-defense": 90,
        "speed": 125,
        "id": 802
    },
    {
        "hp": 67,
        "attack": 73,
        "defense": 67,
        "special-attack": 73,
        "special-defense": 67,
        "speed": 73,
        "id": 803
    },
    {
        "hp": 73,
        "attack": 73,
        "defense": 73,
        "special-attack": 127,
        "special-defense": 73,
        "speed": 121,
        "id": 804
    },
    {
        "hp": 61,
        "attack": 131,
        "defense": 211,
        "special-attack": 53,
        "special-defense": 101,
        "speed": 13,
        "id": 805
    },
    {
        "hp": 53,
        "attack": 127,
        "defense": 53,
        "special-attack": 151,
        "special-defense": 79,
        "speed": 107,
        "id": 806
    },
    {
        "hp": 88,
        "attack": 112,
        "defense": 75,
        "special-attack": 102,
        "special-defense": 80,
        "speed": 143,
        "id": 807
    },
    {
        "hp": 50,
        "attack": 180,
        "defense": 20,
        "special-attack": 180,
        "special-defense": 20,
        "speed": 150,
        "id": 10001
    },
    {
        "hp": 50,
        "attack": 70,
        "defense": 160,
        "special-attack": 70,
        "special-defense": 160,
        "speed": 90,
        "id": 10002
    },
    {
        "hp": 50,
        "attack": 95,
        "defense": 90,
        "special-attack": 95,
        "special-defense": 90,
        "speed": 180,
        "id": 10003
    },
    {
        "hp": 60,
        "attack": 79,
        "defense": 105,
        "special-attack": 59,
        "special-defense": 85,
        "speed": 36,
        "id": 10004
    },
    {
        "hp": 60,
        "attack": 69,
        "defense": 95,
        "special-attack": 69,
        "special-defense": 95,
        "speed": 36,
        "id": 10005
    },
    {
        "hp": 100,
        "attack": 103,
        "defense": 75,
        "special-attack": 120,
        "special-defense": 75,
        "speed": 127,
        "id": 10006
    },
    {
        "hp": 150,
        "attack": 120,
        "defense": 100,
        "special-attack": 120,
        "special-defense": 100,
        "speed": 90,
        "id": 10007
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 107,
        "special-attack": 105,
        "special-defense": 107,
        "speed": 86,
        "id": 10008
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 107,
        "special-attack": 105,
        "special-defense": 107,
        "speed": 86,
        "id": 10009
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 107,
        "special-attack": 105,
        "special-defense": 107,
        "speed": 86,
        "id": 10010
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 107,
        "special-attack": 105,
        "special-defense": 107,
        "speed": 86,
        "id": 10011
    },
    {
        "hp": 50,
        "attack": 65,
        "defense": 107,
        "special-attack": 105,
        "special-defense": 107,
        "speed": 86,
        "id": 10012
    },
    {
        "hp": 70,
        "attack": 70,
        "defense": 70,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 70,
        "id": 10013
    },
    {
        "hp": 70,
        "attack": 70,
        "defense": 70,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 70,
        "id": 10014
    },
    {
        "hp": 70,
        "attack": 70,
        "defense": 70,
        "special-attack": 70,
        "special-defense": 70,
        "speed": 70,
        "id": 10015
    },
    {
        "hp": 70,
        "attack": 92,
        "defense": 65,
        "special-attack": 80,
        "special-defense": 55,
        "speed": 98,
        "id": 10016
    },
    {
        "hp": 105,
        "attack": 30,
        "defense": 105,
        "special-attack": 140,
        "special-defense": 105,
        "speed": 55,
        "id": 10017
    },
    {
        "hp": 100,
        "attack": 128,
        "defense": 90,
        "special-attack": 77,
        "special-defense": 77,
        "speed": 128,
        "id": 10018
    },
    {
        "hp": 79,
        "attack": 100,
        "defense": 80,
        "special-attack": 110,
        "special-defense": 90,
        "speed": 121,
        "id": 10019
    },
    {
        "hp": 79,
        "attack": 105,
        "defense": 70,
        "special-attack": 145,
        "special-defense": 80,
        "speed": 101,
        "id": 10020
    },
    {
        "hp": 89,
        "attack": 145,
        "defense": 90,
        "special-attack": 105,
        "special-defense": 80,
        "speed": 91,
        "id": 10021
    },
    {
        "hp": 125,
        "attack": 170,
        "defense": 100,
        "special-attack": 120,
        "special-defense": 90,
        "speed": 95,
        "id": 10022
    },
    {
        "hp": 125,
        "attack": 120,
        "defense": 90,
        "special-attack": 170,
        "special-defense": 100,
        "speed": 95,
        "id": 10023
    },
    {
        "hp": 91,
        "attack": 72,
        "defense": 90,
        "special-attack": 129,
        "special-defense": 90,
        "speed": 108,
        "id": 10024
    },
    {
        "hp": 74,
        "attack": 48,
        "defense": 76,
        "special-attack": 83,
        "special-defense": 81,
        "speed": 104,
        "id": 10025
    },
    {
        "hp": 60,
        "attack": 150,
        "defense": 50,
        "special-attack": 150,
        "special-defense": 50,
        "speed": 60,
        "id": 10026
    },
    {
        "hp": 44,
        "attack": 66,
        "defense": 70,
        "special-attack": 44,
        "special-defense": 55,
        "speed": 56,
        "id": 10027
    },
    {
        "hp": 54,
        "attack": 66,
        "defense": 70,
        "special-attack": 44,
        "special-defense": 55,
        "speed": 46,
        "id": 10028
    },
    {
        "hp": 59,
        "attack": 66,
        "defense": 70,
        "special-attack": 44,
        "special-defense": 55,
        "speed": 41,
        "id": 10029
    },
    {
        "hp": 55,
        "attack": 85,
        "defense": 122,
        "special-attack": 58,
        "special-defense": 75,
        "speed": 99,
        "id": 10030
    },
    {
        "hp": 75,
        "attack": 95,
        "defense": 122,
        "special-attack": 58,
        "special-defense": 75,
        "speed": 69,
        "id": 10031
    },
    {
        "hp": 85,
        "attack": 100,
        "defense": 122,
        "special-attack": 58,
        "special-defense": 75,
        "speed": 54,
        "id": 10032
    },
    {
        "hp": 80,
        "attack": 100,
        "defense": 123,
        "special-attack": 122,
        "special-defense": 120,
        "speed": 80,
        "id": 10033
    },
    {
        "hp": 78,
        "attack": 130,
        "defense": 111,
        "special-attack": 130,
        "special-defense": 85,
        "speed": 100,
        "id": 10034
    },
    {
        "hp": 78,
        "attack": 104,
        "defense": 78,
        "special-attack": 159,
        "special-defense": 115,
        "speed": 100,
        "id": 10035
    },
    {
        "hp": 79,
        "attack": 103,
        "defense": 120,
        "special-attack": 135,
        "special-defense": 115,
        "speed": 78,
        "id": 10036
    },
    {
        "hp": 55,
        "attack": 50,
        "defense": 65,
        "special-attack": 175,
        "special-defense": 105,
        "speed": 150,
        "id": 10037
    },
    {
        "hp": 60,
        "attack": 65,
        "defense": 80,
        "special-attack": 170,
        "special-defense": 95,
        "speed": 130,
        "id": 10038
    },
    {
        "hp": 105,
        "attack": 125,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 100,
        "id": 10039
    },
    {
        "hp": 65,
        "attack": 155,
        "defense": 120,
        "special-attack": 65,
        "special-defense": 90,
        "speed": 105,
        "id": 10040
    },
    {
        "hp": 95,
        "attack": 155,
        "defense": 109,
        "special-attack": 70,
        "special-defense": 130,
        "speed": 81,
        "id": 10041
    },
    {
        "hp": 80,
        "attack": 135,
        "defense": 85,
        "special-attack": 70,
        "special-defense": 95,
        "speed": 150,
        "id": 10042
    },
    {
        "hp": 106,
        "attack": 190,
        "defense": 100,
        "special-attack": 154,
        "special-defense": 100,
        "speed": 130,
        "id": 10043
    },
    {
        "hp": 106,
        "attack": 150,
        "defense": 70,
        "special-attack": 194,
        "special-defense": 120,
        "speed": 140,
        "id": 10044
    },
    {
        "hp": 90,
        "attack": 95,
        "defense": 105,
        "special-attack": 165,
        "special-defense": 110,
        "speed": 45,
        "id": 10045
    },
    {
        "hp": 70,
        "attack": 150,
        "defense": 140,
        "special-attack": 65,
        "special-defense": 100,
        "speed": 75,
        "id": 10046
    },
    {
        "hp": 80,
        "attack": 185,
        "defense": 115,
        "special-attack": 40,
        "special-defense": 105,
        "speed": 75,
        "id": 10047
    },
    {
        "hp": 75,
        "attack": 90,
        "defense": 90,
        "special-attack": 140,
        "special-defense": 90,
        "speed": 115,
        "id": 10048
    },
    {
        "hp": 100,
        "attack": 164,
        "defense": 150,
        "special-attack": 95,
        "special-defense": 120,
        "speed": 71,
        "id": 10049
    },
    {
        "hp": 80,
        "attack": 160,
        "defense": 80,
        "special-attack": 130,
        "special-defense": 80,
        "speed": 100,
        "id": 10050
    },
    {
        "hp": 68,
        "attack": 85,
        "defense": 65,
        "special-attack": 165,
        "special-defense": 135,
        "speed": 100,
        "id": 10051
    },
    {
        "hp": 50,
        "attack": 105,
        "defense": 125,
        "special-attack": 55,
        "special-defense": 95,
        "speed": 50,
        "id": 10052
    },
    {
        "hp": 70,
        "attack": 140,
        "defense": 230,
        "special-attack": 60,
        "special-defense": 80,
        "speed": 50,
        "id": 10053
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 85,
        "special-attack": 80,
        "special-defense": 85,
        "speed": 100,
        "id": 10054
    },
    {
        "hp": 70,
        "attack": 75,
        "defense": 80,
        "special-attack": 135,
        "special-defense": 80,
        "speed": 135,
        "id": 10055
    },
    {
        "hp": 64,
        "attack": 165,
        "defense": 75,
        "special-attack": 93,
        "special-defense": 83,
        "speed": 75,
        "id": 10056
    },
    {
        "hp": 65,
        "attack": 150,
        "defense": 60,
        "special-attack": 115,
        "special-defense": 60,
        "speed": 115,
        "id": 10057
    },
    {
        "hp": 108,
        "attack": 170,
        "defense": 115,
        "special-attack": 120,
        "special-defense": 95,
        "speed": 92,
        "id": 10058
    },
    {
        "hp": 70,
        "attack": 145,
        "defense": 88,
        "special-attack": 140,
        "special-defense": 70,
        "speed": 112,
        "id": 10059
    },
    {
        "hp": 90,
        "attack": 132,
        "defense": 105,
        "special-attack": 132,
        "special-defense": 105,
        "speed": 30,
        "id": 10060
    },
    {
        "hp": 74,
        "attack": 65,
        "defense": 67,
        "special-attack": 125,
        "special-defense": 128,
        "speed": 92,
        "id": 10061
    },
    {
        "hp": 80,
        "attack": 100,
        "defense": 120,
        "special-attack": 140,
        "special-defense": 150,
        "speed": 110,
        "id": 10062
    },
    {
        "hp": 80,
        "attack": 130,
        "defense": 100,
        "special-attack": 160,
        "special-defense": 120,
        "speed": 110,
        "id": 10063
    },
    {
        "hp": 100,
        "attack": 150,
        "defense": 110,
        "special-attack": 95,
        "special-defense": 110,
        "speed": 70,
        "id": 10064
    },
    {
        "hp": 70,
        "attack": 110,
        "defense": 75,
        "special-attack": 145,
        "special-defense": 85,
        "speed": 145,
        "id": 10065
    },
    {
        "hp": 50,
        "attack": 85,
        "defense": 125,
        "special-attack": 85,
        "special-defense": 115,
        "speed": 20,
        "id": 10066
    },
    {
        "hp": 75,
        "attack": 110,
        "defense": 110,
        "special-attack": 110,
        "special-defense": 105,
        "speed": 80,
        "id": 10067
    },
    {
        "hp": 68,
        "attack": 165,
        "defense": 95,
        "special-attack": 65,
        "special-defense": 115,
        "speed": 110,
        "id": 10068
    },
    {
        "hp": 103,
        "attack": 60,
        "defense": 126,
        "special-attack": 80,
        "special-defense": 126,
        "speed": 50,
        "id": 10069
    },
    {
        "hp": 70,
        "attack": 140,
        "defense": 70,
        "special-attack": 110,
        "special-defense": 65,
        "speed": 105,
        "id": 10070
    },
    {
        "hp": 95,
        "attack": 75,
        "defense": 180,
        "special-attack": 130,
        "special-defense": 80,
        "speed": 30,
        "id": 10071
    },
    {
        "hp": 75,
        "attack": 125,
        "defense": 230,
        "special-attack": 55,
        "special-defense": 95,
        "speed": 30,
        "id": 10072
    },
    {
        "hp": 83,
        "attack": 80,
        "defense": 80,
        "special-attack": 135,
        "special-defense": 80,
        "speed": 121,
        "id": 10073
    },
    {
        "hp": 80,
        "attack": 120,
        "defense": 80,
        "special-attack": 120,
        "special-defense": 80,
        "speed": 100,
        "id": 10074
    },
    {
        "hp": 50,
        "attack": 160,
        "defense": 110,
        "special-attack": 160,
        "special-defense": 110,
        "speed": 110,
        "id": 10075
    },
    {
        "hp": 80,
        "attack": 145,
        "defense": 150,
        "special-attack": 105,
        "special-defense": 110,
        "speed": 110,
        "id": 10076
    },
    {
        "hp": 100,
        "attack": 150,
        "defense": 90,
        "special-attack": 180,
        "special-defense": 160,
        "speed": 90,
        "id": 10077
    },
    {
        "hp": 100,
        "attack": 180,
        "defense": 160,
        "special-attack": 150,
        "special-defense": 90,
        "speed": 90,
        "id": 10078
    },
    {
        "hp": 105,
        "attack": 180,
        "defense": 100,
        "special-attack": 180,
        "special-defense": 100,
        "speed": 115,
        "id": 10079
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10080
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10081
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10082
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10083
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10084
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10085
    },
    {
        "hp": 80,
        "attack": 160,
        "defense": 60,
        "special-attack": 170,
        "special-defense": 130,
        "speed": 80,
        "id": 10086
    },
    {
        "hp": 70,
        "attack": 120,
        "defense": 100,
        "special-attack": 145,
        "special-defense": 105,
        "speed": 20,
        "id": 10087
    },
    {
        "hp": 65,
        "attack": 136,
        "defense": 94,
        "special-attack": 54,
        "special-defense": 96,
        "speed": 135,
        "id": 10088
    },
    {
        "hp": 95,
        "attack": 145,
        "defense": 130,
        "special-attack": 120,
        "special-defense": 90,
        "speed": 120,
        "id": 10089
    },
    {
        "hp": 65,
        "attack": 150,
        "defense": 40,
        "special-attack": 15,
        "special-defense": 80,
        "speed": 145,
        "id": 10090
    },
    {
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "special-attack": 25,
        "special-defense": 35,
        "speed": 72,
        "id": 10091
    },
    {
        "hp": 75,
        "attack": 71,
        "defense": 70,
        "special-attack": 40,
        "special-defense": 80,
        "speed": 77,
        "id": 10092
    },
    {
        "hp": 75,
        "attack": 71,
        "defense": 70,
        "special-attack": 40,
        "special-defense": 80,
        "speed": 77,
        "id": 10093
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10094
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10095
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10096
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10097
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10098
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10099
    },
    {
        "hp": 60,
        "attack": 85,
        "defense": 50,
        "special-attack": 95,
        "special-defense": 85,
        "speed": 110,
        "id": 10100
    },
    {
        "hp": 50,
        "attack": 75,
        "defense": 90,
        "special-attack": 10,
        "special-defense": 35,
        "speed": 40,
        "id": 10101
    },
    {
        "hp": 75,
        "attack": 100,
        "defense": 120,
        "special-attack": 25,
        "special-defense": 65,
        "speed": 65,
        "id": 10102
    },
    {
        "hp": 38,
        "attack": 41,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 65,
        "speed": 65,
        "id": 10103
    },
    {
        "hp": 73,
        "attack": 67,
        "defense": 75,
        "special-attack": 81,
        "special-defense": 100,
        "speed": 109,
        "id": 10104
    },
    {
        "hp": 10,
        "attack": 55,
        "defense": 30,
        "special-attack": 35,
        "special-defense": 45,
        "speed": 90,
        "id": 10105
    },
    {
        "hp": 35,
        "attack": 100,
        "defense": 60,
        "special-attack": 50,
        "special-defense": 70,
        "speed": 110,
        "id": 10106
    },
    {
        "hp": 40,
        "attack": 35,
        "defense": 35,
        "special-attack": 50,
        "special-defense": 40,
        "speed": 90,
        "id": 10107
    },
    {
        "hp": 65,
        "attack": 60,
        "defense": 60,
        "special-attack": 75,
        "special-defense": 65,
        "speed": 115,
        "id": 10108
    },
    {
        "hp": 40,
        "attack": 80,
        "defense": 100,
        "special-attack": 30,
        "special-defense": 30,
        "speed": 20,
        "id": 10109
    },
    {
        "hp": 55,
        "attack": 95,
        "defense": 115,
        "special-attack": 45,
        "special-defense": 45,
        "speed": 35,
        "id": 10110
    },
    {
        "hp": 80,
        "attack": 120,
        "defense": 130,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 45,
        "id": 10111
    },
    {
        "hp": 80,
        "attack": 80,
        "defense": 50,
        "special-attack": 40,
        "special-defense": 50,
        "speed": 25,
        "id": 10112
    },
    {
        "hp": 105,
        "attack": 105,
        "defense": 75,
        "special-attack": 65,
        "special-defense": 100,
        "speed": 50,
        "id": 10113
    },
    {
        "hp": 95,
        "attack": 105,
        "defense": 85,
        "special-attack": 125,
        "special-defense": 75,
        "speed": 45,
        "id": 10114
    },
    {
        "hp": 60,
        "attack": 80,
        "defense": 110,
        "special-attack": 50,
        "special-defense": 80,
        "speed": 45,
        "id": 10115
    },
    {
        "hp": 72,
        "attack": 95,
        "defense": 67,
        "special-attack": 103,
        "special-defense": 71,
        "speed": 122,
        "id": 10116
    },
    {
        "hp": 72,
        "attack": 145,
        "defense": 67,
        "special-attack": 153,
        "special-defense": 71,
        "speed": 132,
        "id": 10117
    },
    {
        "hp": 54,
        "attack": 100,
        "defense": 71,
        "special-attack": 61,
        "special-defense": 85,
        "speed": 115,
        "id": 10118
    },
    {
        "hp": 108,
        "attack": 100,
        "defense": 121,
        "special-attack": 81,
        "special-defense": 95,
        "speed": 95,
        "id": 10119
    },
    {
        "hp": 216,
        "attack": 100,
        "defense": 121,
        "special-attack": 91,
        "special-defense": 95,
        "speed": 85,
        "id": 10120
    },
    {
        "hp": 88,
        "attack": 110,
        "defense": 60,
        "special-attack": 55,
        "special-defense": 60,
        "speed": 45,
        "id": 10121
    },
    {
        "hp": 77,
        "attack": 70,
        "defense": 90,
        "special-attack": 145,
        "special-defense": 75,
        "speed": 43,
        "id": 10122
    },
    {
        "hp": 75,
        "attack": 70,
        "defense": 70,
        "special-attack": 98,
        "special-defense": 70,
        "speed": 93,
        "id": 10123
    },
    {
        "hp": 75,
        "attack": 70,
        "defense": 70,
        "special-attack": 98,
        "special-defense": 70,
        "speed": 93,
        "id": 10124
    },
    {
        "hp": 75,
        "attack": 70,
        "defense": 70,
        "special-attack": 98,
        "special-defense": 70,
        "speed": 93,
        "id": 10125
    },
    {
        "hp": 85,
        "attack": 115,
        "defense": 75,
        "special-attack": 55,
        "special-defense": 75,
        "speed": 82,
        "id": 10126
    },
    {
        "hp": 45,
        "attack": 140,
        "defense": 130,
        "special-attack": 140,
        "special-defense": 135,
        "speed": 30,
        "id": 10127
    },
    {
        "hp": 70,
        "attack": 105,
        "defense": 90,
        "special-attack": 80,
        "special-defense": 90,
        "speed": 45,
        "id": 10128
    },
    {
        "hp": 68,
        "attack": 64,
        "defense": 60,
        "special-attack": 111,
        "special-defense": 60,
        "speed": 117,
        "id": 10129
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 10130
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 10131
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 10132
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 10133
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 10134
    },
    {
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "special-attack": 60,
        "special-defense": 100,
        "speed": 60,
        "id": 10135
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10136
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10137
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10138
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10139
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10140
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10141
    },
    {
        "hp": 60,
        "attack": 100,
        "defense": 60,
        "special-attack": 100,
        "special-defense": 60,
        "speed": 120,
        "id": 10142
    },
    {
        "hp": 55,
        "attack": 90,
        "defense": 80,
        "special-attack": 50,
        "special-defense": 105,
        "speed": 96,
        "id": 10143
    },
    {
        "hp": 55,
        "attack": 90,
        "defense": 80,
        "special-attack": 50,
        "special-defense": 105,
        "speed": 96,
        "id": 10144
    },
    {
        "hp": 55,
        "attack": 90,
        "defense": 80,
        "special-attack": 50,
        "special-defense": 105,
        "speed": 96,
        "id": 10145
    },
    {
        "hp": 75,
        "attack": 110,
        "defense": 125,
        "special-attack": 100,
        "special-defense": 105,
        "speed": 85,
        "id": 10146
    },
    {
        "hp": 80,
        "attack": 95,
        "defense": 115,
        "special-attack": 130,
        "special-defense": 115,
        "speed": 65,
        "id": 10147
    },
    {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special-attack": 50,
        "special-defense": 50,
        "speed": 90,
        "id": 10148
    },
    {
        "hp": 60,
        "attack": 80,
        "defense": 110,
        "special-attack": 50,
        "special-defense": 80,
        "speed": 45,
        "id": 10149
    },
    {
        "hp": 60,
        "attack": 55,
        "defense": 60,
        "special-attack": 95,
        "special-defense": 70,
        "speed": 124,
        "id": 10150
    },
    {
        "hp": 45,
        "attack": 65,
        "defense": 40,
        "special-attack": 30,
        "special-defense": 40,
        "speed": 60,
        "id": 10151
    },
    {
        "hp": 75,
        "attack": 117,
        "defense": 65,
        "special-attack": 55,
        "special-defense": 65,
        "speed": 110,
        "id": 10152
    },
    {
        "hp": 68,
        "attack": 70,
        "defense": 92,
        "special-attack": 50,
        "special-defense": 132,
        "speed": 42,
        "id": 10153
    },
    {
        "hp": 65,
        "attack": 98,
        "defense": 63,
        "special-attack": 40,
        "special-defense": 73,
        "speed": 96,
        "id": 10154
    },
    {
        "hp": 97,
        "attack": 157,
        "defense": 127,
        "special-attack": 113,
        "special-defense": 109,
        "speed": 77,
        "id": 10155
    },
    {
        "hp": 97,
        "attack": 113,
        "defense": 109,
        "special-attack": 157,
        "special-defense": 127,
        "speed": 77,
        "id": 10156
    },
    {
        "hp": 97,
        "attack": 167,
        "defense": 97,
        "special-attack": 167,
        "special-defense": 97,
        "speed": 129,
        "id": 10157
    }
]

var evolution_info = {
    'ekans' : {
        'species' : 'ekans',
        'first' : {
            'name' : 'Ekans',
            'id' : 23,
            'types': '[this.$types['poison']]'
        },
        'second' : {
        'name' : 'Arbok',
        'id' : 24,
        'types': '[this.$types['poison']]'
        }
    },
    'sandshrew' : {
        'species' : 'sandshrew',
        'first' : {
            'name' : 'Sandshrew',
            'id' : 27,
            'types' : '[this.$types['ground']]'
        },
        'second' : {
        'name' : 'Sandslash',
        'id' : 28,
        'types': '[this.$types['ground']]'
        }
    },
    'magikarp' : {
        'species': 'magikarp',
        'first': {
            'name': 'Magikarp',
            'id': 129,
            'types': '[this.$types['water']]'
        },
        'second' : {
        'name' : 'Gyarados',
        'id' : 130,
        'types': '[this.$types['water'], this.$types['flying']]'
        }
    }
}

ALL = {
    'ekans': {
        'display_name' : ['Ekans'],
        'id' : 23,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/thumb/f/fa/023Ekans.png/250px-023Ekans.png'],
        'types' : '[this.$types['poison']]',
        'flavor_text' :
            ['Ekans curls itself up in a spiral while it rests. Assuming this position allows it to quickly respond to a threat from any direction with a glare from its upraised head.'],
        'stats' : {
            BASE_STATS['ekans']
            # 'hp' : 35,
            # 'atk' : 60,
            # 'def' : 44,
            # 'sp_atk' : 40,
            # 'sp_def' : 54,
            # 'spd' : 55
        },
        'ev' : evolution_info['ekans']
    },
    'arbok' : {
        'display_name' : ['Arbok'],
        'id' : 24,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/thumb/c/cd/024Arbok.png/250px-024Arbok.png'],
        'types' : '[this.$types['poison']]',
        'flavor_text' :
            ['The latest research has determined that there are over 20 possible arrangements of the patterns on its stomach.'],
        'stats' : {
            BASE_STATS['arbok']
            # 'hp' : 60,
            # 'atk' : 95,
            # 'def' : 69,
            # 'sp_atk' : 65,
            # 'sp_def' : 79,
            # 'spd' : 80
        },
        'ev' : evolution_info['ekans']
    },
    'sandshrew' : {
        'display_name' : ['Sandshrew'],
        'id' : 27,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/9/9e/027Sandshrew.png'],
        'types' : '[this.$types['ground']]',
        'flavor_text' :
            ['Sandshrew has a very dry hide that is extremely tough. The Pokémon can roll into a ball that repels any attack. At night, it burrows into the desert sand to sleep.'],
        'stats' : {
            BASE_STATS['sandshrew']
            # 'hp' : 50,
            # 'atk' : 75,
            # 'def' : 85,
            # 'sp_atk' : 20,
            # 'sp_def' : 30,
            # 'spd' : 40
        },
        'ev' : evolution_info['sandshrew']
    },
    'sandslash' : {
        'display_name' : ['Sandslash'],
        'id' : 28,
        'sprite' :
            ['https://assets.pokemon.com/assets/cms2/img/pokedex/full/028.png'],
        'types': '[this.$types['ground']]',
        'flavor_text' :
            ['Sandslash can roll up its body as if it were a ball covered with large spikes. In battle, this Pokémon will try to make the foe flinch by jabbing it with its spines. It then leaps at the stunned foe to tear wildly with its sharp claws.'],
        'stats' : {
            BASE_STATS['sandslash']
            # 'hp' : 75,
            # 'atk' : 100,
            # 'def' : 110,
            # 'sp_atk' : 45,
            # 'sp_def' : 55,
            # 'spd' : 65
        },
        'ev' : evolution_info['sandshrew']
    },
    'magikarp' : {
        'display_name' : ['Magikarp'],
        'id' : 129,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/thumb/0/02/129Magikarp.png/250px-129Magikarp.png'],
        'types': '[this.$types['water']]',
        'flavor_text' :
            ['Magikarp is virtually useless in battle as it can only splash around. As a result, it is considered to be weak. However, it is actually a very hardy Pokémon that can survive in any body of water no matter how polluted it is.'],
        'stats' : {
            BASE_STATS['magikarp']
            # 'hp' : 20,
            # 'atk' : 10,
            # 'def' : 55,
            # 'sp_atk' : 15,
            # 'sp_def' : 20,
            # 'spd' : 80
        },
        'ev' : evolution_info['magikarp']
    },
    'gyarados' : {
        'display_name' : ['Gyarados'],
        'id' : 130,
        'sprite' :
            ['https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png'],
        'types' : '[this.$types['water'], this.$types['flying']]',
        'flavor_text' :
            ['Once Gyarados goes on a rampage, its ferociously violent blood doesn’t calm until it has burned everything down. There are records of this Pokémon’s rampages lasting a whole month.'],
        'stats' : {
            BASE_STATS['gyarados']
            # 'hp' : 95,
            # 'atk' : 125,
            # 'def' : 79,
            # 'sp_atk' : 60,
            # 'sp_def' : 100,
            # 'spd' : 81
        },
        'ev' : evolution_info['magikarp']
    }
}
