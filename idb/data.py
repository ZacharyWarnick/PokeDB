EVOLUTION_CHAINS = {}

EVOLUTION_STEPS = {}

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

POKEMON = [
    {
        "name": "Bulbasaur",
        "genus": "Seed Pokémon",
        "identifier": "bulbasaur",
        "evolution_chain": 1,
        "color": "green",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun’s rays,\nthe seed grows progressively larger.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 3
    },
    {
        "name": "Charmander",
        "genus": "Lizard Pokémon",
        "identifier": "charmander",
        "evolution_chain": 2,
        "color": "red",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "The flame that burns at the tip of its tail is an indication\nof its emotions. The flame wavers when Charmander\nis enjoying itself. If the Pokémon becomes enraged,\nthe flame burns fiercely.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Charmeleon mercilessly destroys its foes using its sharp\nclaws. If it encounters a strong foe, it turns aggressive.\nIn this excited state, the flame at the tip of its tail flares with\na bluish white color.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 6
    },
    {
        "name": "Squirtle",
        "genus": "Tiny Turtle Pokémon",
        "identifier": "squirtle",
        "evolution_chain": 3,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Squirtle’s shell is not merely used for protection.\nThe shell’s rounded shape and the grooves on its\nsurface help minimize resistance in water,\nenabling this Pokémon to swim at high speeds.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its tail is large and covered with a rich, thick fur. The tail\nbecomes increasingly deeper in color as Wartortle ages.\nThe scratches on its shell are evidence of this Pokémon’s\ntoughness as a battler.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Blastoise has water spouts that protrude from its shell.\nThe water spouts are very accurate.\nThey can shoot bullets of water with enough accuracy\nto strike empty cans from a distance of over 160 feet.",
        "has_alt_form": false,
        "id": 9
    },
    {
        "name": "Caterpie",
        "genus": "Worm Pokémon",
        "identifier": "caterpie",
        "evolution_chain": 4,
        "color": "green",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "Perhaps because it would like to grow up\nquickly, it has a voracious appetite, eating\na hundred leaves a day.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its shell is filled with a thick liquid. All of the\ncells throughout its body are being rebuilt in\npreparation for evolution.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 12
    },
    {
        "name": "Weedle",
        "genus": "Hairy Bug Pokémon",
        "identifier": "weedle",
        "evolution_chain": 5,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Weedle has an extremely acute sense of smell. It is capable\nof distinguishing its favorite kinds of leaves from those it\ndislikes just by sniffing with its big red proboscis (nose).",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 15
    },
    {
        "name": "Pidgey",
        "genus": "Tiny Bird Pokémon",
        "identifier": "pidgey",
        "evolution_chain": 6,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Pidgey has an extremely sharp sense of direction.\nIt is capable of unerringly returning home to its nest,\nhowever far it may be removed from its familiar surroundings.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 18
    },
    {
        "name": "Rattata",
        "genus": "Mouse Pokémon",
        "identifier": "rattata",
        "evolution_chain": 7,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Its incisors grow continuously throughout its life.\nIf its incisors get too long, this Pokémon\nbecomes unable to eat, and it starves to death.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "People say that it fled from its enemies by\nusing its small webbed hind feet to swim\nfrom island to island in Alola.",
        "has_alt_form": false,
        "id": 20
    },
    {
        "name": "Spearow",
        "genus": "Tiny Bird Pokémon",
        "identifier": "spearow",
        "evolution_chain": 8,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Its reckless nature leads it to stand up to\nothers—even large Pokémon—if it has to protect\nits territory.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 22
    },
    {
        "name": "Ekans",
        "genus": "Snake Pokémon",
        "identifier": "ekans",
        "evolution_chain": 9,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "By dislocating its jaw, it can swallow prey larger\nthan itself. After a meal, it curls up and rests.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "The latest research has determined that there\nare over 20 possible arrangements of the\npatterns on its stomach.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its nature is to store up electricity. Forests\nwhere nests of Pikachu live are dangerous,\nsince the trees are so often struck by lightning.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "As electricity builds up inside its body, it\nbecomes more aggressive. One theory is that\nthe electricity buildup is actually causing stress.",
        "has_alt_form": false,
        "id": 26
    },
    {
        "name": "Sandshrew",
        "genus": "Mouse Pokémon",
        "identifier": "sandshrew",
        "evolution_chain": 11,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "It lives in areas of limited rainfall. When danger\napproaches, it curls up into a ball to protect its\nsoft stomach.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its claws and horns often break off. The broken\nclaws and horns can be used to carve plows for\ntilling farm fields.",
        "has_alt_form": false,
        "id": 28
    },
    {
        "name": "Nidoran♀",
        "genus": "Poison Pin Pokémon",
        "identifier": "nidoran-f",
        "evolution_chain": 12,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "Nidoran♀ has barbs that secrete a powerful poison.\nThey are thought to have developed as protection for\nthis small-bodied Pokémon. When enraged, it releases\na horrible toxin from its horn.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "When Nidorina are with their friends or family, they keep\ntheir barbs tucked away to prevent hurting each other.\nThis Pokémon appears to become nervous if separated\nfrom the others.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 31
    },
    {
        "name": "Nidoran♂",
        "genus": "Poison Pin Pokémon",
        "identifier": "nidoran-m",
        "evolution_chain": 13,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "Nidoran♂ has developed muscles for moving its ears. Thanks\nto them, the ears can be freely moved in any direction. Even\nthe slightest sound does not escape this Pokémon’s notice.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Nidorino has a horn that is harder than a diamond. If it senses\na hostile presence, all the barbs on its back bristle up at once,\nand it challenges the foe with all its might.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "They’re popular, but they’re rare. Trainers who\nshow them off recklessly may be targeted\nby thieves.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It can’t help but hear a pin drop from over half\na mile away, so it lives deep in the mountains\nwhere there aren’t many people or Pokémon.",
        "has_alt_form": false,
        "id": 36
    },
    {
        "name": "Vulpix",
        "genus": "Fox Pokémon",
        "identifier": "vulpix",
        "evolution_chain": 15,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "Its beautiful tails have made it very popular.\nHowever, if it’s not brushed diligently, it will\nbe a mass of tangles before you know it.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It is vindictive and relentless by nature.\nThose who cross it even once will be cursed for\na thousand years, along with their descendants.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 40
    },
    {
        "name": "Zubat",
        "genus": "Bat Pokémon",
        "identifier": "zubat",
        "evolution_chain": 17,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 4,
        "type2": 3,
        "flavor_text": "It has no eyeballs, so it can’t see. It checks its\nsurroundings via the ultrasonic waves it emits\nfrom its mouth.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 42
    },
    {
        "name": "Oddish",
        "genus": "Weed Pokémon",
        "identifier": "oddish",
        "evolution_chain": 18,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Oddish searches for fertile, nutrient-rich soil, then plants itself.\nDuring the daytime, while it is planted, this Pokémon’s feet\nare thought to change shape and become similar to the roots\nof trees.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 45
    },
    {
        "name": "Paras",
        "genus": "Mushroom Pokémon",
        "identifier": "paras",
        "evolution_chain": 19,
        "color": "red",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 7,
        "type2": 12,
        "flavor_text": "Whether it’s due to a lack of moisture or a lack\nof nutrients, in Alola the mushrooms on Paras\ndon’t grow up quite right.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 47
    },
    {
        "name": "Venonat",
        "genus": "Insect Pokémon",
        "identifier": "venonat",
        "evolution_chain": 20,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Venonat is said to have evolved with a coat of thin, stiff hair\nthat covers its entire body for protection. It possesses large\neyes that never fail to spot even minuscule prey.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 49
    },
    {
        "name": "Diglett",
        "genus": "Mole Pokémon",
        "identifier": "diglett",
        "evolution_chain": 21,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "It travels through tunnels that it digs\nunderground. It hates sunlight, so it comes\nout only after the sun goes down.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "While the three of them normally get along\nsplendidly, on rare occasions a huge fight will\nbreak out over which head gets to eat first.",
        "has_alt_form": false,
        "id": 51
    },
    {
        "name": "Meowth",
        "genus": "Scratch Cat Pokémon",
        "identifier": "meowth",
        "evolution_chain": 22,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "When visiting a junkyard, you may catch sight\nof it having an intense fight with Murkrow over\nshiny objects.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Although the jewel on its forehead appears to\nbe a different color than those of Alolan\nPersian, it’s mostly made of the same material.",
        "has_alt_form": false,
        "id": 53
    },
    {
        "name": "Psyduck",
        "genus": "Duck Pokémon",
        "identifier": "psyduck",
        "evolution_chain": 23,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Using psychokinesis gives it a headache, so it\nnormally passes the time spacing out and doing\nas little as possible.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Even fast-swimming fish Pokémon can be\ndisabled by Golduck. It brings them to a\nstandstill and seizes them.",
        "has_alt_form": false,
        "id": 55
    },
    {
        "name": "Mankey",
        "genus": "Pig Monkey Pokémon",
        "identifier": "mankey",
        "evolution_chain": 24,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "The smallest of things could cause it to lose its\ntemper. Because it doesn’t hold in its stress,\nthis Pokémon can live a long time.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It will never forgive opponents who have\nangered it. Even after it has beaten them down\nuntil they can’t move, it never ever forgives.",
        "has_alt_form": false,
        "id": 57
    },
    {
        "name": "Growlithe",
        "genus": "Puppy Pokémon",
        "identifier": "growlithe",
        "evolution_chain": 25,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "While it’s quite friendly toward humans once it’s\ngrown used to them, in the wild it must be quite\nfierce to defend its territory from Rockruff.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Legends tell of its fighting alongside a general\nand conquering a whole country.",
        "has_alt_form": false,
        "id": 59
    },
    {
        "name": "Poliwag",
        "genus": "Tadpole Pokémon",
        "identifier": "poliwag",
        "evolution_chain": 26,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Despite the danger, it wants to come up on land.\nSo it does its best to waddle along, but when\nan enemy finds it, it rushes back to the water.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Although it has become capable of living on\nland, it spends its time in the water, where\nits prey, fish Pokémon, are plentiful.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 62
    },
    {
        "name": "Abra",
        "genus": "Psi Pokémon",
        "identifier": "abra",
        "evolution_chain": 27,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It uses various psychic powers even while it’s\nsleeping, so you can’t tell whether or not\nit’s awake.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It stares at a silver spoon to amplify its psychic\npowers before it lets loose. Apparently, gold\nspoons are no good.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Alakazam uses its psychic powers to make the\nspoons it carries. Each spoon is an original that\nthere’s only one of in the whole world.",
        "has_alt_form": false,
        "id": 65
    },
    {
        "name": "Machop",
        "genus": "Superpower Pokémon",
        "identifier": "machop",
        "evolution_chain": 28,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "Once this Pokémon has gained enough\nconfidence and muscle from training with its\nfriends, it challenges Makuhita to a battle.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "When it encounters an enemy that’s truly\nmighty, this Pokémon removes the power-save\nbelt from its waist and unleashes its full power.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It grasps its opponents with its four arms and\ntwists them up in an intricate hold. People call\nit “the Machamp special.”",
        "has_alt_form": false,
        "id": 68
    },
    {
        "name": "Bellsprout",
        "genus": "Flower Pokémon",
        "identifier": "bellsprout",
        "evolution_chain": 29,
        "color": "green",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Bellsprout’s thin and flexible body lets it bend and sway\nto avoid any attack, however strong it may be. From its mouth,\nthis Pokémon spits a corrosive fluid that melts even iron.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 71
    },
    {
        "name": "Tentacool",
        "genus": "Jellyfish Pokémon",
        "identifier": "tentacool",
        "evolution_chain": 30,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": 4,
        "flavor_text": "It drifts through the sea searching for prey.\nIts poisonous tentacles break off sometimes,\nbut after a while, they grow back.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 73
    },
    {
        "name": "Geodude",
        "genus": "Rock Pokémon",
        "identifier": "geodude",
        "evolution_chain": 31,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 6,
        "type2": 5,
        "flavor_text": "Geodude that have lived a long life have had all\ntheir edges smoothed out until they’re totally\nround. They also have a calm, quiet disposition.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 76
    },
    {
        "name": "Ponyta",
        "genus": "Fire Horse Pokémon",
        "identifier": "ponyta",
        "evolution_chain": 32,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "Ponyta is very weak at birth. It can barely stand up.\nThis Pokémon becomes stronger by stumbling and\nfalling to keep up with its parent.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Rapidash usually can be seen casually cantering in the fields\nand plains. However, when this Pokémon turns serious, its\nfiery manes flare and blaze as it gallops its way up to 150 mph.",
        "has_alt_form": false,
        "id": 78
    },
    {
        "name": "Slowpoke",
        "genus": "Dopey Pokémon",
        "identifier": "slowpoke",
        "evolution_chain": 33,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": 14,
        "flavor_text": "There are some places where Slowpoke is\nworshiped because of a long-standing belief\nthat whenever Slowpoke yawns, it rains.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 80
    },
    {
        "name": "Magnemite",
        "genus": "Magnet Pokémon",
        "identifier": "magnemite",
        "evolution_chain": 34,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 13,
        "type2": 9,
        "flavor_text": "It’s frequently the cause of power outages,\nwhich is why some power plants send out\nelectrical signals that it can’t stand.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 82
    },
    {
        "name": "Farfetch’d",
        "genus": "Wild Duck Pokémon",
        "identifier": "farfetchd",
        "evolution_chain": 35,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Farfetch’d is always seen with a stalk from a plant of some\nsort. Apparently, there are good stalks and bad stalks. This\nPokémon has been known to fight with others over stalks.",
        "has_alt_form": false,
        "id": 83
    },
    {
        "name": "Doduo",
        "genus": "Twin Bird Pokémon",
        "identifier": "doduo",
        "evolution_chain": 36,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Doduo’s two heads contain completely identical brains. A\nscientific study reported that on rare occasions, there will be\nexamples of this Pokémon possessing different sets of brains.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 85
    },
    {
        "name": "Seel",
        "genus": "Sea Lion Pokémon",
        "identifier": "seel",
        "evolution_chain": 37,
        "color": "white",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It has always been supposed that Seel live only\nin cold seas. Their having shown up in Alola is\na mystery.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 87
    },
    {
        "name": "Grimer",
        "genus": "Sludge Pokémon",
        "identifier": "grimer",
        "evolution_chain": 38,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "It was born from sludge on the ocean floor. In a\nsterile environment, the germs within its body\ncan’t multiply, and it dies.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Their food sources have decreased, and their\nnumbers have declined sharply. Sludge ponds\nare being built to prevent their extinction.",
        "has_alt_form": false,
        "id": 89
    },
    {
        "name": "Shellder",
        "genus": "Bivalve Pokémon",
        "identifier": "shellder",
        "evolution_chain": 39,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "The sand that accumulates inside its shell\neventually becomes a pearl. But the pearl gets\nin the way, so it spits it out and discards it.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 91
    },
    {
        "name": "Gastly",
        "genus": "Gas Pokémon",
        "identifier": "gastly",
        "evolution_chain": 40,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 8,
        "type2": 4,
        "flavor_text": "It’s said that gas emanating from a graveyard\nwas possessed by the grievances of the\ndeceased and thus became a Pokémon.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 94
    },
    {
        "name": "Onix",
        "genus": "Rock Snake Pokémon",
        "identifier": "onix",
        "evolution_chain": 41,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 6,
        "type2": 5,
        "flavor_text": "Onix has a magnet in its brain. It acts as a compass so that\nthis Pokémon does not lose direction while it is tunneling.\nAs it grows older, its body becomes increasingly rounder\nand smoother.",
        "has_alt_form": false,
        "id": 95
    },
    {
        "name": "Drowzee",
        "genus": "Hypnosis Pokémon",
        "identifier": "drowzee",
        "evolution_chain": 42,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It can be spotted near recreational facilities,\nintending to eat the pleasant dreams of children\nwho enjoyed themselves there that day.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "In Alola, Komala is Hypno’s main target. It rarely\nharms people.",
        "has_alt_form": false,
        "id": 97
    },
    {
        "name": "Krabby",
        "genus": "River Crab Pokémon",
        "identifier": "krabby",
        "evolution_chain": 43,
        "color": "red",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Krabby live on beaches, burrowed inside holes dug into\nthe sand. On sandy beaches with little in the way of food,\nthese Pokémon can be seen squabbling with each other\nover territory.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Kingler has an enormous, oversized claw. It waves this huge\nclaw in the air to communicate with others. However, because\nthe claw is so heavy, the Pokémon quickly tires.",
        "has_alt_form": false,
        "id": 99
    },
    {
        "name": "Voltorb",
        "genus": "Ball Pokémon",
        "identifier": "voltorb",
        "evolution_chain": 44,
        "color": "red",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Voltorb is extremely sensitive—it explodes at the slightest\nof shocks. It is rumored that it was first created when a\nPoké Ball was exposed to a powerful pulse of energy.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "One of Electrode’s characteristics is its attraction to electricity.\nIt is a problematical Pokémon that congregates mostly at\nelectrical power plants to feed on electricity that has just\nbeen generated.",
        "has_alt_form": false,
        "id": 101
    },
    {
        "name": "Exeggcute",
        "genus": "Egg Pokémon",
        "identifier": "exeggcute",
        "evolution_chain": 45,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 12,
        "type2": 14,
        "flavor_text": "Six of them form a single Pokémon. Should one\nof the six be lost, the next morning there will\nonce more be six.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 103
    },
    {
        "name": "Cubone",
        "genus": "Lonely Pokémon",
        "identifier": "cubone",
        "evolution_chain": 46,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "At night, it weeps loudly for its dead mother,\nbut those cries only attract its natural\nenemy—Mandibuzz.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It throws bones at Mandibuzz to knock it down.\nIt’s thought that Marowak is trying to avenge\nits parent.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Hitmonlee’s legs freely contract and stretch. Using these\nspringlike legs, it bowls over foes with devastating kicks.\nAfter battle, it rubs down its legs and loosens the muscles\nto overcome fatigue.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Hitmonchan is said to possess the spirit of a boxer who had\nbeen working toward a world championship. This Pokémon\nhas an indomitable spirit and will never give up in the face\nof adversity.",
        "has_alt_form": false,
        "id": 107
    },
    {
        "name": "Lickitung",
        "genus": "Licking Pokémon",
        "identifier": "lickitung",
        "evolution_chain": 48,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It checks out whatever’s around it by licking\neverything. If you don’t clean off a spot where\nit’s licked you, you’ll break out in a rash!",
        "has_alt_form": false,
        "id": 108
    },
    {
        "name": "Koffing",
        "genus": "Poison Gas Pokémon",
        "identifier": "koffing",
        "evolution_chain": 49,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "Koffing embodies toxic substances. It mixes the toxins with raw\ngarbage to set off a chemical reaction that results in a terribly\npowerful poison gas. The higher the temperature, the more gas\nis concocted by this Pokémon.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Weezing alternately shrinks and inflates its twin bodies to mix\ntogether toxic gases inside. The more the gases are mixed,\nthe more powerful the toxins become. The Pokémon also\nbecomes more putrid.",
        "has_alt_form": false,
        "id": 110
    },
    {
        "name": "Rhyhorn",
        "genus": "Spikes Pokémon",
        "identifier": "rhyhorn",
        "evolution_chain": 50,
        "color": "gray",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 5,
        "type2": 6,
        "flavor_text": "Rhyhorn’s brain is very small. It is so dense, while on a run\nit forgets why it started running in the first place. It apparently\nremembers sometimes if it demolishes something.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It seems that other Pokémon’s efforts to take\nits delicious, nutritious egg away from it caused\nChansey to get faster at fleeing.",
        "has_alt_form": false,
        "id": 113
    },
    {
        "name": "Tangela",
        "genus": "Vine Pokémon",
        "identifier": "tangela",
        "evolution_chain": 52,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Tangela’s vines snap off easily if they are grabbed. This\nhappens without pain, allowing it to make a quick getaway.\nThe lost vines are replaced by newly grown vines the very\nnext day.",
        "has_alt_form": false,
        "id": 114
    },
    {
        "name": "Kangaskhan",
        "genus": "Parent Pokémon",
        "identifier": "kangaskhan",
        "evolution_chain": 53,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Kangaskhan protects its child by keeping it in\nits pouch. It has zero forgiveness for those\nwho harm its child and will beat them down.",
        "has_alt_form": false,
        "id": 115
    },
    {
        "name": "Horsea",
        "genus": "Dragon Pokémon",
        "identifier": "horsea",
        "evolution_chain": 54,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "If Horsea senses danger, it will reflexively spray a dense\nblack ink from its mouth and try to escape. This Pokémon\nswims by cleverly flapping the fin on its back.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Seadra generates whirlpools by spinning its body.\nThe whirlpools are strong enough to swallow even\nfishing boats. This Pokémon weakens prey with\nthese currents, then swallows it whole.",
        "has_alt_form": false,
        "id": 117
    },
    {
        "name": "Goldeen",
        "genus": "Goldfish Pokémon",
        "identifier": "goldeen",
        "evolution_chain": 55,
        "color": "red",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Although known for their splendid tail fins,\nGoldeen apparently compete among themselves\nto see whose horn is thickest and sharpest.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its horn spins like a drill to steadily hollow out\nrocks—even harder ones. The coloration of the\nmale is more vivid.",
        "has_alt_form": false,
        "id": 119
    },
    {
        "name": "Staryu",
        "genus": "Star Shape Pokémon",
        "identifier": "staryu",
        "evolution_chain": 56,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "In many places, there are folktales of stardust\nfalling into the ocean and becoming Staryu.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 122
    },
    {
        "name": "Scyther",
        "genus": "Mantis Pokémon",
        "identifier": "scyther",
        "evolution_chain": 58,
        "color": "green",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Its two sharp scythes are more than just\nweapons. It uses them with dexterity to dress\nits prey before eating.",
        "has_alt_form": false,
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
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Electricity permeates its body. It swings\nits arms round and round to charge up\nelectricity before unleashing a punch.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its entire body is burning. When it breathes,\nthe temperature rises. When it sneezes, flames\nshoot out!",
        "has_alt_form": false,
        "id": 126
    },
    {
        "name": "Pinsir",
        "genus": "Stag Beetle Pokémon",
        "identifier": "pinsir",
        "evolution_chain": 62,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "It gets into territorial disputes with Vikavolt.\nFor some reason, it apparently gets along well\nwith Heracross in Alola.",
        "has_alt_form": false,
        "id": 127
    },
    {
        "name": "Tauros",
        "genus": "Wild Bull Pokémon",
        "identifier": "tauros",
        "evolution_chain": 63,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "They live in groups. The one with the longest,\nthickest, and most-scarred horns is the boss\nof the herd.",
        "has_alt_form": false,
        "id": 128
    },
    {
        "name": "Magikarp",
        "genus": "Fish Pokémon",
        "identifier": "magikarp",
        "evolution_chain": 64,
        "color": "red",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "In the distant past, they were fairly strong, but\nthey have become gradually weaker over time.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 130
    },
    {
        "name": "Lapras",
        "genus": "Transport Pokémon",
        "identifier": "lapras",
        "evolution_chain": 65,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 11,
        "type2": 15,
        "flavor_text": "It likes swimming around with people on its\nback. In the Alola region, it’s an important means\nof transportation over water.",
        "has_alt_form": false,
        "id": 131
    },
    {
        "name": "Ditto",
        "genus": "Transform Pokémon",
        "identifier": "ditto",
        "evolution_chain": 66,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "While it can transform into anything, each Ditto\napparently has its own strengths and\nweaknesses when it comes to transformations.",
        "has_alt_form": false,
        "id": 132
    },
    {
        "name": "Eevee",
        "genus": "Evolution Pokémon",
        "identifier": "eevee",
        "evolution_chain": 67,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "The question of why only Eevee has such\nunstable genes has still not been solved.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Clean, clear waters are its usual habitat. When\nit’s about to be attacked by an invading enemy,\nit dives into the water to hide.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Its lungs contain an organ that creates\nelectricity. The crackling sound of electricity\ncan be heard when it exhales.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "If it inhales deeply, that’s a sign it’s about to\nattack. Prepare to be hit by flames of over\n3,000 degrees Fahrenheit!",
        "has_alt_form": false,
        "id": 136
    },
    {
        "name": "Porygon",
        "genus": "Virtual Pokémon",
        "identifier": "porygon",
        "evolution_chain": 68,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "This Pokémon was created using the\ncutting-edge science of 20 years ago, so\nmany parts of it have since become obsolete.",
        "has_alt_form": false,
        "id": 137
    },
    {
        "name": "Omanyte",
        "genus": "Spiral Pokémon",
        "identifier": "omanyte",
        "evolution_chain": 69,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 6,
        "type2": 11,
        "flavor_text": "Omanyte lived in the seas of antiquity. Its\nfossils have been found bearing bite marks from\nArcheops, so apparently Archeops preyed on it.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 139
    },
    {
        "name": "Kabuto",
        "genus": "Shellfish Pokémon",
        "identifier": "kabuto",
        "evolution_chain": 70,
        "color": "brown",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 6,
        "type2": 11,
        "flavor_text": "This Pokémon thrived 300 million years ago. It’s\nsaid that living specimens can still be seen\nin a certain region—a rare sight.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 141
    },
    {
        "name": "Aerodactyl",
        "genus": "Fossil Pokémon",
        "identifier": "aerodactyl",
        "evolution_chain": 71,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 6,
        "type2": 3,
        "flavor_text": "Restored from DNA found in amber, this\nPokémon exhibited ferocity that was greater\nthan expected. Some casualties resulted.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "It doesn’t do anything other than eat and sleep.\nWhen prompted to make a serious effort,\nthough, it apparently displays awesome power.",
        "has_alt_form": false,
        "id": 143
    },
    {
        "name": "Articuno",
        "genus": "Freeze Pokémon",
        "identifier": "articuno",
        "evolution_chain": 73,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 15,
        "type2": 3,
        "flavor_text": "Articuno is a legendary bird Pokémon that can control ice.\nThe flapping of its wings chills the air. As a result, it is said\nthat when this Pokémon flies, snow will fall.",
        "has_alt_form": false,
        "id": 144
    },
    {
        "name": "Zapdos",
        "genus": "Electric Pokémon",
        "identifier": "zapdos",
        "evolution_chain": 74,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 13,
        "type2": 3,
        "flavor_text": "Zapdos is a legendary bird Pokémon that has the ability\nto control electricity. It usually lives in thunderclouds.\nThe Pokémon gains power if it is stricken by lightning bolts.",
        "has_alt_form": false,
        "id": 145
    },
    {
        "name": "Moltres",
        "genus": "Flame Pokémon",
        "identifier": "moltres",
        "evolution_chain": 75,
        "color": "yellow",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 10,
        "type2": 3,
        "flavor_text": "Moltres is a legendary bird Pokémon that has the ability\nto control fire. If this Pokémon is injured, it is said to dip its\nbody in the molten magma of a volcano to burn and heal itself.",
        "has_alt_form": false,
        "id": 146
    },
    {
        "name": "Dratini",
        "genus": "Dragon Pokémon",
        "identifier": "dratini",
        "evolution_chain": 76,
        "color": "blue",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 16,
        "type2": null,
        "flavor_text": "It’s still weak, so it lurks on the floor of bodies\nof water, eating whatever food sinks down and\nliving a quiet life.",
        "has_alt_form": false,
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
        "type2": null,
        "flavor_text": "Lakes where Dragonair live are filled with\nofferings from people, because they believe this\nPokémon is able to control the weather.",
        "has_alt_form": false,
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
        "has_alt_form": false,
        "id": 149
    },
    {
        "name": "Mewtwo",
        "genus": "Genetic Pokémon",
        "identifier": "mewtwo",
        "evolution_chain": 77,
        "color": "purple",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Mewtwo is a Pokémon that was created by genetic\nmanipulation. However, even though the scientific power\nof humans created this Pokémon’s body, they failed to\nendow Mewtwo with a compassionate heart.",
        "has_alt_form": false,
        "id": 150
    },
    {
        "name": "Mew",
        "genus": "New Species Pokémon",
        "identifier": "mew",
        "evolution_chain": 78,
        "color": "pink",
        "since_gen": 1,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Mew is said to possess the genetic composition of all\nPokémon. It is capable of making itself invisible at will,\nso it entirely avoids notice even if it approaches people.",
        "has_alt_form": false,
        "id": 151
    },
    {
        "name": "Chikorita",
        "genus": "Leaf Pokémon",
        "identifier": "chikorita",
        "evolution_chain": 79,
        "color": "green",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "In battle, Chikorita waves its leaf around to keep the foe at\nbay. However, a sweet fragrance also wafts from the leaf,\nbecalming the battling Pokémon and creating a cozy,\nfriendly atmosphere all around.",
        "has_alt_form": false,
        "id": 152
    },
    {
        "name": "Bayleef",
        "genus": "Leaf Pokémon",
        "identifier": "bayleef",
        "evolution_chain": 79,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 152,
        "type1": 12,
        "type2": null,
        "flavor_text": "Bayleef’s neck is ringed by curled-up leaves. Inside each\ntubular leaf is a small shoot of a tree. The fragrance of this\nshoot makes people peppy.",
        "has_alt_form": false,
        "id": 153
    },
    {
        "name": "Meganium",
        "genus": "Herb Pokémon",
        "identifier": "meganium",
        "evolution_chain": 79,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 153,
        "type1": 12,
        "type2": null,
        "flavor_text": "The fragrance of Meganium’s flower soothes and calms\nemotions. In battle, this Pokémon gives off more of its\nbecalming scent to blunt the foe’s fighting spirit.",
        "has_alt_form": false,
        "id": 154
    },
    {
        "name": "Cyndaquil",
        "genus": "Fire Mouse Pokémon",
        "identifier": "cyndaquil",
        "evolution_chain": 80,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "Cyndaquil protects itself by flaring up the flames on its back.\nThe flames are vigorous if the Pokémon is angry. However, if it\nis tired, the flames splutter fitfully with incomplete combustion.",
        "has_alt_form": false,
        "id": 155
    },
    {
        "name": "Quilava",
        "genus": "Volcano Pokémon",
        "identifier": "quilava",
        "evolution_chain": 80,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": 155,
        "type1": 10,
        "type2": null,
        "flavor_text": "Quilava keeps its foes at bay with the intensity of its flames\nand gusts of superheated air. This Pokémon applies its\noutstanding nimbleness to dodge attacks even while scorching\nthe foe with flames.",
        "has_alt_form": false,
        "id": 156
    },
    {
        "name": "Typhlosion",
        "genus": "Volcano Pokémon",
        "identifier": "typhlosion",
        "evolution_chain": 80,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": 156,
        "type1": 10,
        "type2": null,
        "flavor_text": "Typhlosion obscures itself behind a shimmering heat haze that\nit creates using its intensely hot flames. This Pokémon creates\nblazing explosive blasts that burn everything to cinders.",
        "has_alt_form": false,
        "id": 157
    },
    {
        "name": "Totodile",
        "genus": "Big Jaw Pokémon",
        "identifier": "totodile",
        "evolution_chain": 81,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Despite the smallness of its body, Totodile’s jaws are very\npowerful. While the Pokémon may think it is just playfully\nnipping, its bite has enough power to cause serious injury.",
        "has_alt_form": false,
        "id": 158
    },
    {
        "name": "Croconaw",
        "genus": "Big Jaw Pokémon",
        "identifier": "croconaw",
        "evolution_chain": 81,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 158,
        "type1": 11,
        "type2": null,
        "flavor_text": "Once Croconaw has clamped its jaws on its foe, it will\nabsolutely not let go. Because the tips of its fangs are\nforked back like barbed fishhooks, they become impossible\nto remove when they have sunk in.",
        "has_alt_form": false,
        "id": 159
    },
    {
        "name": "Feraligatr",
        "genus": "Big Jaw Pokémon",
        "identifier": "feraligatr",
        "evolution_chain": 81,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 159,
        "type1": 11,
        "type2": null,
        "flavor_text": "Feraligatr intimidates its foes by opening its huge mouth.\nIn battle, it will kick the ground hard with its thick and powerful\nhind legs to charge at the foe at an incredible speed.",
        "has_alt_form": false,
        "id": 160
    },
    {
        "name": "Sentret",
        "genus": "Scout Pokémon",
        "identifier": "sentret",
        "evolution_chain": 82,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "When Sentret sleeps, it does so while another stands guard.\nThe sentry wakes the others at the first sign of danger. When\nthis Pokémon becomes separated from its pack, it becomes\nincapable of sleep due to fear.",
        "has_alt_form": false,
        "id": 161
    },
    {
        "name": "Furret",
        "genus": "Long Body Pokémon",
        "identifier": "furret",
        "evolution_chain": 82,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": 161,
        "type1": 1,
        "type2": null,
        "flavor_text": "Furret has a very slim build. When under attack, it can slickly\nsquirm through narrow spaces and get away. In spite of its\nshort limbs, this Pokémon is very nimble and fleet.",
        "has_alt_form": false,
        "id": 162
    },
    {
        "name": "Hoothoot",
        "genus": "Owl Pokémon",
        "identifier": "hoothoot",
        "evolution_chain": 83,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Every day, it tilts its head in the same rhythm.\nA long time ago, people raised these Pokémon\nto serve as clocks.",
        "has_alt_form": false,
        "id": 163
    },
    {
        "name": "Noctowl",
        "genus": "Owl Pokémon",
        "identifier": "noctowl",
        "evolution_chain": 83,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": 163,
        "type1": 1,
        "type2": 3,
        "flavor_text": "With eyes that can see in pitch-darkness, it\nnever lets its prey escape. Some even call it\n“the emperor of dark nights.”",
        "has_alt_form": false,
        "id": 164
    },
    {
        "name": "Ledyba",
        "genus": "Five Star Pokémon",
        "identifier": "ledyba",
        "evolution_chain": 84,
        "color": "red",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 7,
        "type2": 3,
        "flavor_text": "This Pokémon is very sensitive to cold. In the\nwarmth of Alola, it appears quite lively.",
        "has_alt_form": false,
        "id": 165
    },
    {
        "name": "Ledian",
        "genus": "Five Star Pokémon",
        "identifier": "ledian",
        "evolution_chain": 84,
        "color": "red",
        "since_gen": 2,
        "evolves_from": 165,
        "type1": 7,
        "type2": 3,
        "flavor_text": "It’s said that the patterns on its back are\nrelated to the stars in the night sky, but the\ndetails of that relationship remain unclear.",
        "has_alt_form": false,
        "id": 166
    },
    {
        "name": "Spinarak",
        "genus": "String Spit Pokémon",
        "identifier": "spinarak",
        "evolution_chain": 85,
        "color": "green",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 7,
        "type2": 4,
        "flavor_text": "With threads from its mouth, it fashions sturdy\nwebs that won’t break even if you set a rock\non them.",
        "has_alt_form": false,
        "id": 167
    },
    {
        "name": "Ariados",
        "genus": "Long Leg Pokémon",
        "identifier": "ariados",
        "evolution_chain": 85,
        "color": "red",
        "since_gen": 2,
        "evolves_from": 167,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Every night, it wanders around in search of\nprey, whose movements it restrains by spewing\nthreads before it bites into them with its fangs.",
        "has_alt_form": false,
        "id": 168
    },
    {
        "name": "Crobat",
        "genus": "Bat Pokémon",
        "identifier": "crobat",
        "evolution_chain": 17,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": 42,
        "type1": 4,
        "type2": 3,
        "flavor_text": "Its fangs are so sharp, if it bites you in the dark\nand sucks your blood, you won’t notice any pain\nor realize you’ve been bitten.",
        "has_alt_form": false,
        "id": 169
    },
    {
        "name": "Chinchou",
        "genus": "Angler Pokémon",
        "identifier": "chinchou",
        "evolution_chain": 86,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": 13,
        "flavor_text": "Its two antennae glow softly to lure in prey,\nmaking it a useful Pokémon for night fishing.",
        "has_alt_form": false,
        "id": 170
    },
    {
        "name": "Lanturn",
        "genus": "Light Pokémon",
        "identifier": "lanturn",
        "evolution_chain": 86,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 170,
        "type1": 11,
        "type2": 13,
        "flavor_text": "When the bacteria living inside its antennae\nabsorb Lanturn’s bodily fluids, a strong\nluminescent effect is produced.",
        "has_alt_form": false,
        "id": 171
    },
    {
        "name": "Pichu",
        "genus": "Tiny Mouse Pokémon",
        "identifier": "pichu",
        "evolution_chain": 10,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "It still can’t use electricity well. When it’s\nsurprised or excited, it discharges\nelectricity unintentionally.",
        "has_alt_form": false,
        "id": 172
    },
    {
        "name": "Cleffa",
        "genus": "Star Shape Pokémon",
        "identifier": "cleffa",
        "evolution_chain": 14,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "On nights with many shooting stars,\nthey gather in packs and dance in circles. If you\nshould see them, something good will happen!",
        "has_alt_form": false,
        "id": 173
    },
    {
        "name": "Igglybuff",
        "genus": "Balloon Pokémon",
        "identifier": "igglybuff",
        "evolution_chain": 16,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": 18,
        "flavor_text": "It’s always practicing its singing because it\nwants to improve. Even when it’s asleep,\nit keeps singing in its dreams!",
        "has_alt_form": false,
        "id": 174
    },
    {
        "name": "Togepi",
        "genus": "Spike Ball Pokémon",
        "identifier": "togepi",
        "evolution_chain": 87,
        "color": "white",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "As its energy, Togepi uses the positive emotions of\ncompassion and pleasure exuded by people and Pokémon.\nThis Pokémon stores up feelings of happiness inside its shell,\nthen shares them with others.",
        "has_alt_form": false,
        "id": 175
    },
    {
        "name": "Togetic",
        "genus": "Happiness Pokémon",
        "identifier": "togetic",
        "evolution_chain": 87,
        "color": "white",
        "since_gen": 2,
        "evolves_from": 175,
        "type1": 18,
        "type2": 3,
        "flavor_text": "Togetic is said to be a Pokémon that brings good fortune.\nWhen the Pokémon spots someone who is pure of heart,\nit is said to appear and share its happiness with that person.",
        "has_alt_form": false,
        "id": 176
    },
    {
        "name": "Natu",
        "genus": "Tiny Bird Pokémon",
        "identifier": "natu",
        "evolution_chain": 88,
        "color": "green",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 14,
        "type2": 3,
        "flavor_text": "Although it still can’t fly, its jumping power is\noutstanding. It jumps way up into trees and\nplucks the buds from the branches.",
        "has_alt_form": false,
        "id": 177
    },
    {
        "name": "Xatu",
        "genus": "Mystic Pokémon",
        "identifier": "xatu",
        "evolution_chain": 88,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 177,
        "type1": 14,
        "type2": 3,
        "flavor_text": "It’s said that while this Pokémon has the power\nto predict the future, it’s not powerful enough\nto change the future it sees.",
        "has_alt_form": false,
        "id": 178
    },
    {
        "name": "Mareep",
        "genus": "Wool Pokémon",
        "identifier": "mareep",
        "evolution_chain": 89,
        "color": "white",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Clothing made from Mareep’s fleece is easily\ncharged with static electricity, so a special\nprocess is used on it.",
        "has_alt_form": false,
        "id": 179
    },
    {
        "name": "Flaaffy",
        "genus": "Wool Pokémon",
        "identifier": "flaaffy",
        "evolution_chain": 89,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": 179,
        "type1": 13,
        "type2": null,
        "flavor_text": "In the places on its body where fleece doesn’t\ngrow, its skin is rubbery and doesn’t conduct\nelectricity. Those spots are safe to touch.",
        "has_alt_form": false,
        "id": 180
    },
    {
        "name": "Ampharos",
        "genus": "Light Pokémon",
        "identifier": "ampharos",
        "evolution_chain": 89,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": 180,
        "type1": 13,
        "type2": null,
        "flavor_text": "The light from its tail can be seen from space.\nThis is why you can always tell exactly where it\nis, which is why it usually keeps the light off.",
        "has_alt_form": false,
        "id": 181
    },
    {
        "name": "Bellossom",
        "genus": "Flower Pokémon",
        "identifier": "bellossom",
        "evolution_chain": 18,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 44,
        "type1": 12,
        "type2": null,
        "flavor_text": "A Bellossom grows flowers more beautifully if it has evolved\nfrom a smelly Gloom—the more stinky the better. At night, this\nPokémon closes its petals and goes to sleep.",
        "has_alt_form": false,
        "id": 182
    },
    {
        "name": "Marill",
        "genus": "Aqua Mouse Pokémon",
        "identifier": "marill",
        "evolution_chain": 90,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 298,
        "type1": 11,
        "type2": 18,
        "flavor_text": "When fishing for food at the edge of a fast-running stream,\nMarill wraps its tail around the trunk of a tree. This Pokémon’s\ntail is flexible and configured to stretch.",
        "has_alt_form": false,
        "id": 183
    },
    {
        "name": "Azumarill",
        "genus": "Aqua Rabbit Pokémon",
        "identifier": "azumarill",
        "evolution_chain": 90,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 183,
        "type1": 11,
        "type2": 18,
        "flavor_text": "Azumarill can make balloons out of air. It makes these air\nballoons if it spots a drowning Pokémon. The air balloons\nenable the Pokémon in trouble to breathe.",
        "has_alt_form": false,
        "id": 184
    },
    {
        "name": "Sudowoodo",
        "genus": "Imitation Pokémon",
        "identifier": "sudowoodo",
        "evolution_chain": 91,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": 438,
        "type1": 6,
        "type2": null,
        "flavor_text": "It’s so popular with the elderly that there’s a\nmagazine devoted to this Pokémon. Fans obsess\nover the particular length and angle of its arms.",
        "has_alt_form": false,
        "id": 185
    },
    {
        "name": "Politoed",
        "genus": "Frog Pokémon",
        "identifier": "politoed",
        "evolution_chain": 26,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 61,
        "type1": 11,
        "type2": null,
        "flavor_text": "Although its cries sound like screams, a\ncomposer created a beautiful ballad that was\ninfluenced by the sounds.",
        "has_alt_form": false,
        "id": 186
    },
    {
        "name": "Hoppip",
        "genus": "Cottonweed Pokémon",
        "identifier": "hoppip",
        "evolution_chain": 92,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 12,
        "type2": 3,
        "flavor_text": "This Pokémon drifts and floats with the wind. If it senses the\napproach of strong winds, Hoppip links its leaves with other\nHoppip to prepare against being blown away.",
        "has_alt_form": false,
        "id": 187
    },
    {
        "name": "Skiploom",
        "genus": "Cottonweed Pokémon",
        "identifier": "skiploom",
        "evolution_chain": 92,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 187,
        "type1": 12,
        "type2": 3,
        "flavor_text": "Skiploom’s flower blossoms when the temperature rises\nabove 64 degrees Fahrenheit. How much the flower opens\ndepends on the temperature. For that reason, this Pokémon\nis sometimes used as a thermometer.",
        "has_alt_form": false,
        "id": 188
    },
    {
        "name": "Jumpluff",
        "genus": "Cottonweed Pokémon",
        "identifier": "jumpluff",
        "evolution_chain": 92,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 188,
        "type1": 12,
        "type2": 3,
        "flavor_text": "Jumpluff rides warm southern winds to cross the sea and fly to\nforeign lands. The Pokémon descends to the ground when it\nencounters cold air while it is floating.",
        "has_alt_form": false,
        "id": 189
    },
    {
        "name": "Aipom",
        "genus": "Long Tail Pokémon",
        "identifier": "aipom",
        "evolution_chain": 93,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "As it did more and more with its tail, its hands\nbecame clumsy. It makes its nest high in\nthe treetops.",
        "has_alt_form": false,
        "id": 190
    },
    {
        "name": "Sunkern",
        "genus": "Seed Pokémon",
        "identifier": "sunkern",
        "evolution_chain": 94,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Sunkern tries to move as little as it possibly can. It does so\nbecause it tries to conserve all the nutrients it has stored in its\nbody for its evolution. It will not eat a thing, subsisting only on\nmorning dew.",
        "has_alt_form": false,
        "id": 191
    },
    {
        "name": "Sunflora",
        "genus": "Sun Pokémon",
        "identifier": "sunflora",
        "evolution_chain": 94,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": 191,
        "type1": 12,
        "type2": null,
        "flavor_text": "Sunflora converts solar energy into nutrition. It moves around\nactively in the daytime when it is warm. It stops moving as\nsoon as the sun goes down for the night.",
        "has_alt_form": false,
        "id": 192
    },
    {
        "name": "Yanma",
        "genus": "Clear Wing Pokémon",
        "identifier": "yanma",
        "evolution_chain": 95,
        "color": "red",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Yanma is capable of seeing 360 degrees without having to\nmove its eyes. It is a great flier that is adept at making sudden\nstops and turning midair. This Pokémon uses its flying ability\nto quickly chase down targeted prey.",
        "has_alt_form": false,
        "id": 193
    },
    {
        "name": "Wooper",
        "genus": "Water Fish Pokémon",
        "identifier": "wooper",
        "evolution_chain": 96,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Wooper usually lives in water. However, it occasionally comes\nout onto land in search of food. On land, it coats its body with\na gooey, toxic film.",
        "has_alt_form": false,
        "id": 194
    },
    {
        "name": "Quagsire",
        "genus": "Water Fish Pokémon",
        "identifier": "quagsire",
        "evolution_chain": 96,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 194,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Quagsire hunts for food by leaving its mouth wide open in\nwater and waiting for its prey to blunder in unaware. Because\nthe Pokémon does not move, it does not get very hungry.",
        "has_alt_form": false,
        "id": 195
    },
    {
        "name": "Espeon",
        "genus": "Sun Pokémon",
        "identifier": "espeon",
        "evolution_chain": 67,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": 133,
        "type1": 14,
        "type2": null,
        "flavor_text": "Although it originally had no powers at all,\npeople say its precognitive faculties were\nawakened by its need to protect itself.",
        "has_alt_form": false,
        "id": 196
    },
    {
        "name": "Umbreon",
        "genus": "Moonlight Pokémon",
        "identifier": "umbreon",
        "evolution_chain": 67,
        "color": "black",
        "since_gen": 2,
        "evolves_from": 133,
        "type1": 17,
        "type2": null,
        "flavor_text": "This Pokémon is nocturnal. Even in total\ndarkness, its large eyes can spot its\nprey clearly!",
        "has_alt_form": false,
        "id": 197
    },
    {
        "name": "Murkrow",
        "genus": "Darkness Pokémon",
        "identifier": "murkrow",
        "evolution_chain": 97,
        "color": "black",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 17,
        "type2": 3,
        "flavor_text": "It has a weakness for shiny things. It’s been\nknown to sneak into the nests of Gabite—noted\ncollectors of jewels—in search of treasure.",
        "has_alt_form": false,
        "id": 198
    },
    {
        "name": "Slowking",
        "genus": "Royal Pokémon",
        "identifier": "slowking",
        "evolution_chain": 33,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": 79,
        "type1": 11,
        "type2": 14,
        "flavor_text": "It’s constantly coming up with new ideas that\nwould change the world, but as soon as it\nhits upon a new idea, it forgets it.",
        "has_alt_form": false,
        "id": 199
    },
    {
        "name": "Misdreavus",
        "genus": "Screech Pokémon",
        "identifier": "misdreavus",
        "evolution_chain": 98,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 8,
        "type2": null,
        "flavor_text": "What gives meaning to its life is surprising\nothers. If you set your ear against the red orbs\naround its neck, you can hear shrieking.",
        "has_alt_form": false,
        "id": 200
    },
    {
        "name": "Unown",
        "genus": "Symbol Pokémon",
        "identifier": "unown",
        "evolution_chain": 99,
        "color": "black",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "This Pokémon is shaped like ancient writing. It is a mystery as\nto which came first, the ancient writings or the various Unown.\nResearch into this topic is ongoing but nothing is known.",
        "has_alt_form": true,
        "id": 201
    },
    {
        "name": "Wobbuffet",
        "genus": "Patient Pokémon",
        "identifier": "wobbuffet",
        "evolution_chain": 100,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 360,
        "type1": 14,
        "type2": null,
        "flavor_text": "Wobbuffet does nothing but endure attacks—it won’t attack on\nits own. However, it won’t endure an attack on its tail. When\nthat happens, the Pokémon will try to take the foe with it using\nDestiny Bond.",
        "has_alt_form": false,
        "id": 202
    },
    {
        "name": "Girafarig",
        "genus": "Long Neck Pokémon",
        "identifier": "girafarig",
        "evolution_chain": 101,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": 14,
        "flavor_text": "Girafarig’s rear head contains a tiny brain that is too small for\nthinking. However, the rear head doesn’t need to sleep, so it\ncan keep watch over its surroundings 24 hours a day.",
        "has_alt_form": false,
        "id": 203
    },
    {
        "name": "Pineco",
        "genus": "Bagworm Pokémon",
        "identifier": "pineco",
        "evolution_chain": 102,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "Motionless, it hangs from trees, waiting for\nits bug Pokémon prey to come to it. Its favorite\nin Alola is Cutiefly.",
        "has_alt_form": false,
        "id": 204
    },
    {
        "name": "Forretress",
        "genus": "Bagworm Pokémon",
        "identifier": "forretress",
        "evolution_chain": 102,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": 204,
        "type1": 7,
        "type2": 9,
        "flavor_text": "When something approaches it, it fires off\nfragments of its steel shell in attack. This is not\na conscious action but a conditioned reflex.",
        "has_alt_form": false,
        "id": 205
    },
    {
        "name": "Dunsparce",
        "genus": "Land Snake Pokémon",
        "identifier": "dunsparce",
        "evolution_chain": 103,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It travels by digging through the ground.\nDiglett and Dunsparce share one another’s\ntunnels happily.",
        "has_alt_form": false,
        "id": 206
    },
    {
        "name": "Gligar",
        "genus": "Fly Scorpion Pokémon",
        "identifier": "gligar",
        "evolution_chain": 104,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 5,
        "type2": 3,
        "flavor_text": "Gligar glides through the air without a sound as if it were\nsliding. This Pokémon hangs on to the face of its foe using\nits clawed hind legs and the large pincers on its forelegs, then\ninjects the prey with its poison barb.",
        "has_alt_form": false,
        "id": 207
    },
    {
        "name": "Steelix",
        "genus": "Iron Snake Pokémon",
        "identifier": "steelix",
        "evolution_chain": 41,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": 95,
        "type1": 9,
        "type2": 5,
        "flavor_text": "Steelix lives even further underground than Onix.\nThis Pokémon is known to dig toward the earth’s core.\nThere are records of this Pokémon reaching a depth of\nover six-tenths of a mile underground.",
        "has_alt_form": false,
        "id": 208
    },
    {
        "name": "Snubbull",
        "genus": "Fairy Pokémon",
        "identifier": "snubbull",
        "evolution_chain": 105,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "It grows close to others easily and is also easily\nspoiled. The disparity between its face and its\nactions makes many young people wild about it.",
        "has_alt_form": false,
        "id": 209
    },
    {
        "name": "Granbull",
        "genus": "Fairy Pokémon",
        "identifier": "granbull",
        "evolution_chain": 105,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": 209,
        "type1": 18,
        "type2": null,
        "flavor_text": "While it has powerful jaws, it doesn’t care for\ndisputes, so it rarely has a chance to display\ntheir might.",
        "has_alt_form": false,
        "id": 210
    },
    {
        "name": "Qwilfish",
        "genus": "Balloon Pokémon",
        "identifier": "qwilfish",
        "evolution_chain": 106,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": 4,
        "flavor_text": "Qwilfish sucks in water, inflating itself. This Pokémon\nuses the pressure of the water it swallowed to shoot toxic\nquills all at once from all over its body. It finds swimming\nsomewhat challenging.",
        "has_alt_form": false,
        "id": 211
    },
    {
        "name": "Scizor",
        "genus": "Pincer Pokémon",
        "identifier": "scizor",
        "evolution_chain": 58,
        "color": "red",
        "since_gen": 2,
        "evolves_from": 123,
        "type1": 7,
        "type2": 9,
        "flavor_text": "Its body is like steel. Its tough, heavy pincers\nare more suited to smashing enemies than\ngrabbing them.",
        "has_alt_form": false,
        "id": 212
    },
    {
        "name": "Shuckle",
        "genus": "Mold Pokémon",
        "identifier": "shuckle",
        "evolution_chain": 107,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 7,
        "type2": 6,
        "flavor_text": "Shuckle quietly hides itself under rocks, keeping its body\nconcealed inside its hard shell while eating berries it has\nstored away. The berries mix with its body fluids to become\na juice.",
        "has_alt_form": false,
        "id": 213
    },
    {
        "name": "Heracross",
        "genus": "Single Horn Pokémon",
        "identifier": "heracross",
        "evolution_chain": 108,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 7,
        "type2": 2,
        "flavor_text": "It’s proud of its thick horn. In Alola, its biggest\nrival is Vikavolt, which it’s always fighting with.",
        "has_alt_form": false,
        "id": 214
    },
    {
        "name": "Sneasel",
        "genus": "Sharp Claw Pokémon",
        "identifier": "sneasel",
        "evolution_chain": 109,
        "color": "black",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 17,
        "type2": 15,
        "flavor_text": "They will cooperate to steal eggs from the nests\nof bird Pokémon, but fights break out to\ndetermine which one gets to eat the eggs.",
        "has_alt_form": false,
        "id": 215
    },
    {
        "name": "Teddiursa",
        "genus": "Little Bear Pokémon",
        "identifier": "teddiursa",
        "evolution_chain": 110,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "This Pokémon likes to lick its palms that are sweetened by\nbeing soaked in honey. Teddiursa concocts its own honey\nby blending fruits and pollen collected by Beedrill.",
        "has_alt_form": false,
        "id": 216
    },
    {
        "name": "Ursaring",
        "genus": "Hibernator Pokémon",
        "identifier": "ursaring",
        "evolution_chain": 110,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": 216,
        "type1": 1,
        "type2": null,
        "flavor_text": "In the forests inhabited by Ursaring, it is said that there are\nmany streams and towering trees where they gather food. This\nPokémon walks through its forest gathering food every day.",
        "has_alt_form": false,
        "id": 217
    },
    {
        "name": "Slugma",
        "genus": "Lava Pokémon",
        "identifier": "slugma",
        "evolution_chain": 111,
        "color": "red",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "Slugma does not have any blood in its body. Instead, intensely\nhot magma circulates throughout this Pokémon’s body,\ncarrying essential nutrients and oxygen to its organs.",
        "has_alt_form": false,
        "id": 218
    },
    {
        "name": "Magcargo",
        "genus": "Lava Pokémon",
        "identifier": "magcargo",
        "evolution_chain": 111,
        "color": "red",
        "since_gen": 2,
        "evolves_from": 218,
        "type1": 10,
        "type2": 6,
        "flavor_text": "Magcargo’s body temperature is approximately\n18,000 degrees Fahrenheit. Water is vaporized on contact.\nIf this Pokémon is caught in the rain, the raindrops instantly\nturn into steam, cloaking the area in a thick fog.",
        "has_alt_form": false,
        "id": 219
    },
    {
        "name": "Swinub",
        "genus": "Pig Pokémon",
        "identifier": "swinub",
        "evolution_chain": 112,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 15,
        "type2": 5,
        "flavor_text": "Swinub roots for food by rubbing its snout against the ground.\nIts favorite food is a mushroom that grows under the cover of\ndead grass. This Pokémon occasionally roots out hot springs.",
        "has_alt_form": false,
        "id": 220
    },
    {
        "name": "Piloswine",
        "genus": "Swine Pokémon",
        "identifier": "piloswine",
        "evolution_chain": 112,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": 220,
        "type1": 15,
        "type2": 5,
        "flavor_text": "Piloswine is covered by a thick coat of long hair that enables\nit to endure the freezing cold. This Pokémon uses its tusks to\ndig up food that has been buried under ice.",
        "has_alt_form": false,
        "id": 221
    },
    {
        "name": "Corsola",
        "genus": "Coral Pokémon",
        "identifier": "corsola",
        "evolution_chain": 113,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": 6,
        "flavor_text": "The pink of Corsola that live in Alola is deep\nand vibrant, thanks to seas filled with nutrition.",
        "has_alt_form": false,
        "id": 222
    },
    {
        "name": "Remoraid",
        "genus": "Jet Pokémon",
        "identifier": "remoraid",
        "evolution_chain": 114,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "This Pokémon clings to Mantine and shares in\nits prosperity. When its Mantine is attacked,\nRemoraid will fight alongside it!",
        "has_alt_form": false,
        "id": 223
    },
    {
        "name": "Octillery",
        "genus": "Jet Pokémon",
        "identifier": "octillery",
        "evolution_chain": 114,
        "color": "red",
        "since_gen": 2,
        "evolves_from": 223,
        "type1": 11,
        "type2": null,
        "flavor_text": "The ink it spits when escaping is special.\nIt contains a substance that dulls the sense of\nsmell, so Pokémon with keen noses get lost.",
        "has_alt_form": false,
        "id": 224
    },
    {
        "name": "Delibird",
        "genus": "Delivery Pokémon",
        "identifier": "delibird",
        "evolution_chain": 115,
        "color": "red",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 15,
        "type2": 3,
        "flavor_text": "It shares its food with people who are stranded.\nBecause Delibird is omnivorous, sometimes\nit gives those people bug Pokémon.",
        "has_alt_form": false,
        "id": 225
    },
    {
        "name": "Mantine",
        "genus": "Kite Pokémon",
        "identifier": "mantine",
        "evolution_chain": 116,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": 458,
        "type1": 11,
        "type2": 3,
        "flavor_text": "Postcards and posters featuring Mantine\nleaping elegantly above the waves are popular\nsouvenirs of Alola.",
        "has_alt_form": false,
        "id": 226
    },
    {
        "name": "Skarmory",
        "genus": "Armor Bird Pokémon",
        "identifier": "skarmory",
        "evolution_chain": 117,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 9,
        "type2": 3,
        "flavor_text": "The wing feathers it sheds can be processed\nand made into knives whose sharpness is\nrecognized by the finest chefs.",
        "has_alt_form": false,
        "id": 227
    },
    {
        "name": "Houndour",
        "genus": "Dark Pokémon",
        "identifier": "houndour",
        "evolution_chain": 118,
        "color": "black",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 17,
        "type2": 10,
        "flavor_text": "It cooperates with others skillfully. When it\nbecomes your partner, it’s very loyal to you as\nits Trainer and will obey your orders.",
        "has_alt_form": false,
        "id": 228
    },
    {
        "name": "Houndoom",
        "genus": "Dark Pokémon",
        "identifier": "houndoom",
        "evolution_chain": 118,
        "color": "black",
        "since_gen": 2,
        "evolves_from": 228,
        "type1": 17,
        "type2": 10,
        "flavor_text": "They spew flames mixed with poison to finish\noff their opponents. They divvy up their prey\nevenly among the members of their pack.",
        "has_alt_form": false,
        "id": 229
    },
    {
        "name": "Kingdra",
        "genus": "Dragon Pokémon",
        "identifier": "kingdra",
        "evolution_chain": 54,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": 117,
        "type1": 11,
        "type2": 16,
        "flavor_text": "Kingdra sleeps on the seafloor where it is otherwise devoid\nof life. When a storm arrives, the Pokémon is said to awaken\nand wander about in search of prey.",
        "has_alt_form": false,
        "id": 230
    },
    {
        "name": "Phanpy",
        "genus": "Long Nose Pokémon",
        "identifier": "phanpy",
        "evolution_chain": 119,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "Phanpy uses its long nose to shower itself. When others\ngather around, they thoroughly douse each other with water.\nThese Pokémon can be seen drying their soaking-wet\nbodies at the edge of water.",
        "has_alt_form": false,
        "id": 231
    },
    {
        "name": "Donphan",
        "genus": "Armor Pokémon",
        "identifier": "donphan",
        "evolution_chain": 119,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": 231,
        "type1": 5,
        "type2": null,
        "flavor_text": "If Donphan were to tackle with its hard body, even a house\ncould be destroyed. Using its massive strength, the Pokémon\nhelps clear rock and mud slides that block mountain trails.",
        "has_alt_form": false,
        "id": 232
    },
    {
        "name": "Porygon2",
        "genus": "Virtual Pokémon",
        "identifier": "porygon2",
        "evolution_chain": 68,
        "color": "red",
        "since_gen": 2,
        "evolves_from": 137,
        "type1": 1,
        "type2": null,
        "flavor_text": "AI has been installed in it. It learns various\nthings all on its own, but it even remembers\nthings it doesn’t need to know.",
        "has_alt_form": false,
        "id": 233
    },
    {
        "name": "Stantler",
        "genus": "Big Horn Pokémon",
        "identifier": "stantler",
        "evolution_chain": 120,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Stantler’s magnificent antlers were traded at high prices as\nworks of art. As a result, this Pokémon was hunted close to\nextinction by those who were after the priceless antlers.",
        "has_alt_form": false,
        "id": 234
    },
    {
        "name": "Smeargle",
        "genus": "Painter Pokémon",
        "identifier": "smeargle",
        "evolution_chain": 121,
        "color": "white",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "The fluid of Smeargle’s tail secretions changes\nin the intensity of its hue as the Pokémon’s\nemotions change.",
        "has_alt_form": false,
        "id": 235
    },
    {
        "name": "Tyrogue",
        "genus": "Scuffle Pokémon",
        "identifier": "tyrogue",
        "evolution_chain": 47,
        "color": "purple",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "Tyrogue becomes stressed out if it does not get to train every\nday. When raising this Pokémon, the Trainer must establish\nand uphold various training methods.",
        "has_alt_form": false,
        "id": 236
    },
    {
        "name": "Hitmontop",
        "genus": "Handstand Pokémon",
        "identifier": "hitmontop",
        "evolution_chain": 47,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": 236,
        "type1": 2,
        "type2": null,
        "flavor_text": "Hitmontop spins on its head at high speed, all the while\ndelivering kicks. This technique is a remarkable mix of both\noffense and defense at the same time. The Pokémon travels\nfaster spinning than it does walking.",
        "has_alt_form": false,
        "id": 237
    },
    {
        "name": "Smoochum",
        "genus": "Kiss Pokémon",
        "identifier": "smoochum",
        "evolution_chain": 59,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 15,
        "type2": 14,
        "flavor_text": "When it examines things, before touching them\nwith its hands, it makes lip contact and then\ndiligently licks all the dirt off its lips.",
        "has_alt_form": false,
        "id": 238
    },
    {
        "name": "Elekid",
        "genus": "Electric Pokémon",
        "identifier": "elekid",
        "evolution_chain": 60,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "When it hears the crash of thunder, Elekid’s\nmood improves. It can be useful to record that\nsound and play it when Elekid’s feeling down.",
        "has_alt_form": false,
        "id": 239
    },
    {
        "name": "Magby",
        "genus": "Live Coal Pokémon",
        "identifier": "magby",
        "evolution_chain": 61,
        "color": "red",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "When flames drip from its nose, that means it\nhas a cold. Have it lie down for a nice rest in\nsome magma.",
        "has_alt_form": false,
        "id": 240
    },
    {
        "name": "Miltank",
        "genus": "Milk Cow Pokémon",
        "identifier": "miltank",
        "evolution_chain": 122,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It produces over five gallons of milk a day. The\nhigher the quality of the pastures it lives in,\nthe richer and tastier its milk becomes.",
        "has_alt_form": false,
        "id": 241
    },
    {
        "name": "Blissey",
        "genus": "Happiness Pokémon",
        "identifier": "blissey",
        "evolution_chain": 51,
        "color": "pink",
        "since_gen": 2,
        "evolves_from": 113,
        "type1": 1,
        "type2": null,
        "flavor_text": "Their eggs are such a delicacy that some say\neating one will bring you happiness. These eggs\nfetch the highest prices on the market.",
        "has_alt_form": false,
        "id": 242
    },
    {
        "name": "Raikou",
        "genus": "Thunder Pokémon",
        "identifier": "raikou",
        "evolution_chain": 123,
        "color": "yellow",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Raikou embodies the speed of lightning. The roars of\nthis Pokémon send shock waves shuddering through the\nair and shake the ground as if lightning bolts had come\ncrashing down.",
        "has_alt_form": false,
        "id": 243
    },
    {
        "name": "Entei",
        "genus": "Volcano Pokémon",
        "identifier": "entei",
        "evolution_chain": 124,
        "color": "brown",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "Entei embodies the passion of magma. This Pokémon is\nthought to have been born in the eruption of a volcano.\nIt sends up massive bursts of fire that utterly consume all\nthat they touch.",
        "has_alt_form": false,
        "id": 244
    },
    {
        "name": "Suicune",
        "genus": "Aurora Pokémon",
        "identifier": "suicune",
        "evolution_chain": 125,
        "color": "blue",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Suicune embodies the compassion of a pure spring of water.\nIt runs across the land with gracefulness. This Pokémon has\nthe power to purify dirty water.",
        "has_alt_form": false,
        "id": 245
    },
    {
        "name": "Larvitar",
        "genus": "Rock Skin Pokémon",
        "identifier": "larvitar",
        "evolution_chain": 126,
        "color": "green",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 6,
        "type2": 5,
        "flavor_text": "Born underground, it eats its way through dirt to\nthe surface, where its parents are. It doesn’t\ndeal well with the bright light it finds there.",
        "has_alt_form": false,
        "id": 246
    },
    {
        "name": "Pupitar",
        "genus": "Hard Shell Pokémon",
        "identifier": "pupitar",
        "evolution_chain": 126,
        "color": "gray",
        "since_gen": 2,
        "evolves_from": 246,
        "type1": 6,
        "type2": 5,
        "flavor_text": "This troublesome Pokémon can’t wait to evolve,\nso it relieves its stress by wildly propelling itself\naround using compressed gas.",
        "has_alt_form": false,
        "id": 247
    },
    {
        "name": "Tyranitar",
        "genus": "Armor Pokémon",
        "identifier": "tyranitar",
        "evolution_chain": 126,
        "color": "green",
        "since_gen": 2,
        "evolves_from": 247,
        "type1": 6,
        "type2": 17,
        "flavor_text": "It wanders through the mountains seeking\nopponents to fight. If it finds an opponent that’s\nnot worthy, Tyranitar ignores it and wanders on.",
        "has_alt_form": false,
        "id": 248
    },
    {
        "name": "Lugia",
        "genus": "Diving Pokémon",
        "identifier": "lugia",
        "evolution_chain": 127,
        "color": "white",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 14,
        "type2": 3,
        "flavor_text": "Lugia’s wings pack devastating power—a light fluttering of its\nwings can blow apart regular houses. As a result, this\nPokémon chooses to live out of sight deep under the sea.",
        "has_alt_form": false,
        "id": 249
    },
    {
        "name": "Ho-Oh",
        "genus": "Rainbow Pokémon",
        "identifier": "ho-oh",
        "evolution_chain": 128,
        "color": "red",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 10,
        "type2": 3,
        "flavor_text": "Ho-Oh’s feathers glow in seven colors depending on the angle\nat which they are struck by light. These feathers are said to\nbring happiness to the bearers. This Pokémon is said to live at\nthe foot of a rainbow.",
        "has_alt_form": false,
        "id": 250
    },
    {
        "name": "Celebi",
        "genus": "Time Travel Pokémon",
        "identifier": "celebi",
        "evolution_chain": 129,
        "color": "green",
        "since_gen": 2,
        "evolves_from": null,
        "type1": 14,
        "type2": 12,
        "flavor_text": "This Pokémon came from the future by crossing over time.\nIt is thought that so long as Celebi appears, a bright and\nshining future awaits us.",
        "has_alt_form": false,
        "id": 251
    },
    {
        "name": "Treecko",
        "genus": "Wood Gecko Pokémon",
        "identifier": "treecko",
        "evolution_chain": 130,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Treecko is cool, calm, and collected—it never panics under\nany situation. If a bigger foe were to glare at this Pokémon,\nit would glare right back without conceding an inch of ground.",
        "has_alt_form": false,
        "id": 252
    },
    {
        "name": "Grovyle",
        "genus": "Wood Gecko Pokémon",
        "identifier": "grovyle",
        "evolution_chain": 130,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 252,
        "type1": 12,
        "type2": null,
        "flavor_text": "This Pokémon adeptly flies from branch to branch in trees.\nIn a forest, no Pokémon can ever hope to catch a fleeing\nGrovyle however fast they may be.",
        "has_alt_form": false,
        "id": 253
    },
    {
        "name": "Sceptile",
        "genus": "Forest Pokémon",
        "identifier": "sceptile",
        "evolution_chain": 130,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 253,
        "type1": 12,
        "type2": null,
        "flavor_text": "Sceptile has seeds growing on its back. They are said to be\nbursting with nutrients that revitalize trees. This Pokémon\nraises the trees in a forest with loving care.",
        "has_alt_form": false,
        "id": 254
    },
    {
        "name": "Torchic",
        "genus": "Chick Pokémon",
        "identifier": "torchic",
        "evolution_chain": 131,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "Torchic has a place inside its body where it keeps its flame.\nGive it a hug—it will be glowing with warmth. This Pokémon is\ncovered all over by a fluffy coat of down.",
        "has_alt_form": false,
        "id": 255
    },
    {
        "name": "Combusken",
        "genus": "Young Fowl Pokémon",
        "identifier": "combusken",
        "evolution_chain": 131,
        "color": "red",
        "since_gen": 3,
        "evolves_from": 255,
        "type1": 10,
        "type2": 2,
        "flavor_text": "Combusken battles with the intensely hot flames it spews from\nits beak and with outstandingly destructive kicks. This\nPokémon’s cry is very loud and distracting.",
        "has_alt_form": false,
        "id": 256
    },
    {
        "name": "Blaziken",
        "genus": "Blaze Pokémon",
        "identifier": "blaziken",
        "evolution_chain": 131,
        "color": "red",
        "since_gen": 3,
        "evolves_from": 256,
        "type1": 10,
        "type2": 2,
        "flavor_text": "Blaziken has incredibly strong legs—it can easily clear a\n30-story building in one leap. This Pokémon’s blazing punches\nleave its foes scorched and blackened.",
        "has_alt_form": false,
        "id": 257
    },
    {
        "name": "Mudkip",
        "genus": "Mud Fish Pokémon",
        "identifier": "mudkip",
        "evolution_chain": 132,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "In water, Mudkip breathes using the gills on its cheeks. If it is\nfaced with a tight situation in battle, this Pokémon will unleash\nits amazing power—it can crush rocks bigger than itself.",
        "has_alt_form": false,
        "id": 258
    },
    {
        "name": "Marshtomp",
        "genus": "Mud Fish Pokémon",
        "identifier": "marshtomp",
        "evolution_chain": 132,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 258,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Marshtomp is much faster at traveling through mud than it is at\nswimming. This Pokémon’s hindquarters exhibit obvious\ndevelopment, giving it the ability to walk on just its hind legs.",
        "has_alt_form": false,
        "id": 259
    },
    {
        "name": "Swampert",
        "genus": "Mud Fish Pokémon",
        "identifier": "swampert",
        "evolution_chain": 132,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 259,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Swampert predicts storms by sensing subtle differences in the\nsounds of waves and tidal winds with its fins. If a storm is\napproaching, it piles up boulders to protect itself.",
        "has_alt_form": false,
        "id": 260
    },
    {
        "name": "Poochyena",
        "genus": "Bite Pokémon",
        "identifier": "poochyena",
        "evolution_chain": 133,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 17,
        "type2": null,
        "flavor_text": "Poochyena is an omnivore—it will eat anything. A distinguishing\nfeature is how large its fangs are compared to its body. This\nPokémon tries to intimidate its foes by making the hair on its\ntail bristle out.",
        "has_alt_form": false,
        "id": 261
    },
    {
        "name": "Mightyena",
        "genus": "Bite Pokémon",
        "identifier": "mightyena",
        "evolution_chain": 133,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": 261,
        "type1": 17,
        "type2": null,
        "flavor_text": "Mightyena travel and act as a pack in the wild. The memory\nof its life in the wild compels the Pokémon to obey only\nthose Trainers that it recognizes to possess superior skill.",
        "has_alt_form": false,
        "id": 262
    },
    {
        "name": "Zigzagoon",
        "genus": "Tiny Raccoon Pokémon",
        "identifier": "zigzagoon",
        "evolution_chain": 134,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "The hair on Zigzagoon’s back is bristly. It rubs the hard back\nhair against trees to leave its territorial markings. This Pokémon\nmay play dead to fool foes in battle.",
        "has_alt_form": false,
        "id": 263
    },
    {
        "name": "Linoone",
        "genus": "Rushing Pokémon",
        "identifier": "linoone",
        "evolution_chain": 134,
        "color": "white",
        "since_gen": 3,
        "evolves_from": 263,
        "type1": 1,
        "type2": null,
        "flavor_text": "When hunting, Linoone will make a beeline straight for the\nprey at a full run. While this Pokémon is capable of topping\n60 mph, it has to come to a screeching halt before it can turn.",
        "has_alt_form": false,
        "id": 264
    },
    {
        "name": "Wurmple",
        "genus": "Worm Pokémon",
        "identifier": "wurmple",
        "evolution_chain": 135,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "Wurmple is targeted by Swellow as prey. This Pokémon\nwill try to resist by pointing the spikes on its rear at the\nattacking predator. It will weaken the foe by leaking poison\nfrom the spikes.",
        "has_alt_form": false,
        "id": 265
    },
    {
        "name": "Silcoon",
        "genus": "Cocoon Pokémon",
        "identifier": "silcoon",
        "evolution_chain": 135,
        "color": "white",
        "since_gen": 3,
        "evolves_from": 265,
        "type1": 7,
        "type2": null,
        "flavor_text": "Silcoon was thought to endure hunger and not consume\nanything before its evolution. However, it is now thought\nthat this Pokémon slakes its thirst by drinking rainwater\nthat collects on its silk.",
        "has_alt_form": false,
        "id": 266
    },
    {
        "name": "Beautifly",
        "genus": "Butterfly Pokémon",
        "identifier": "beautifly",
        "evolution_chain": 135,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": 266,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Beautifly has a long mouth like a coiled needle, which is very\nconvenient for collecting pollen from flowers. This Pokémon\nrides the spring winds as it flits around gathering pollen.",
        "has_alt_form": false,
        "id": 267
    },
    {
        "name": "Cascoon",
        "genus": "Cocoon Pokémon",
        "identifier": "cascoon",
        "evolution_chain": 135,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": 265,
        "type1": 7,
        "type2": null,
        "flavor_text": "If it is attacked, Cascoon remains motionless however badly it\nmay be hurt. It does so because if it were to move, its body\nwould be weak upon evolution. This Pokémon will also not\nforget the pain it endured.",
        "has_alt_form": false,
        "id": 268
    },
    {
        "name": "Dustox",
        "genus": "Poison Moth Pokémon",
        "identifier": "dustox",
        "evolution_chain": 135,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 268,
        "type1": 7,
        "type2": 4,
        "flavor_text": "When Dustox flaps its wings, a fine dust is scattered all over.\nThis dust is actually a powerful poison that will even make a\npro wrestler sick. This Pokémon searches for food using its\nantennae like radar.",
        "has_alt_form": false,
        "id": 269
    },
    {
        "name": "Lotad",
        "genus": "Water Weed Pokémon",
        "identifier": "lotad",
        "evolution_chain": 136,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": 12,
        "flavor_text": "Lotad is said to have dwelled on land before. However, this\nPokémon is thought to have returned to water because the\nleaf on its head grew large and heavy. It now lives by floating\natop the water.",
        "has_alt_form": false,
        "id": 270
    },
    {
        "name": "Lombre",
        "genus": "Jolly Pokémon",
        "identifier": "lombre",
        "evolution_chain": 136,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 270,
        "type1": 11,
        "type2": 12,
        "flavor_text": "Lombre’s entire body is covered by a slippery, slimy film.\nIt feels horribly unpleasant to be touched by this Pokémon’s\nhands. Lombre is often mistaken for a human child.",
        "has_alt_form": false,
        "id": 271
    },
    {
        "name": "Ludicolo",
        "genus": "Carefree Pokémon",
        "identifier": "ludicolo",
        "evolution_chain": 136,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 271,
        "type1": 11,
        "type2": 12,
        "flavor_text": "Upon hearing an upbeat and cheerful rhythm, the cells in\nLudicolo’s body become very energetic and active. Even\nin battle, this Pokémon will exhibit an amazing amount\nof power.",
        "has_alt_form": false,
        "id": 272
    },
    {
        "name": "Seedot",
        "genus": "Acorn Pokémon",
        "identifier": "seedot",
        "evolution_chain": 137,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Seedot looks exactly like an acorn when it is dangling from a\ntree branch. It startles other Pokémon by suddenly moving.\nThis Pokémon polishes its body once a day using leaves.",
        "has_alt_form": false,
        "id": 273
    },
    {
        "name": "Nuzleaf",
        "genus": "Wily Pokémon",
        "identifier": "nuzleaf",
        "evolution_chain": 137,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": 273,
        "type1": 12,
        "type2": 17,
        "flavor_text": "This Pokémon pulls out the leaf on its head and makes a flute\nwith it. The sound of Nuzleaf’s flute strikes fear and uncertainty\nin the hearts of people lost in a forest.",
        "has_alt_form": false,
        "id": 274
    },
    {
        "name": "Shiftry",
        "genus": "Wicked Pokémon",
        "identifier": "shiftry",
        "evolution_chain": 137,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": 274,
        "type1": 12,
        "type2": 17,
        "flavor_text": "Shiftry’s large fans generate awesome gusts of wind at a\nspeed close to 100 feet per second. The whipped-up wind\nblows anything away. This Pokémon chooses to live quietly\ndeep in forests.",
        "has_alt_form": false,
        "id": 275
    },
    {
        "name": "Taillow",
        "genus": "Tiny Swallow Pokémon",
        "identifier": "taillow",
        "evolution_chain": 138,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Taillow is young—it has only just left its nest. As a result,\nit sometimes becomes lonesome and cries at night.\nThis Pokémon feeds on Wurmple that live in forests.",
        "has_alt_form": false,
        "id": 276
    },
    {
        "name": "Swellow",
        "genus": "Swallow Pokémon",
        "identifier": "swellow",
        "evolution_chain": 138,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 276,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Swellow is very conscientious about the upkeep of its glossy\nwings. Once two Swellow are gathered, they diligently take\ncare of cleaning each other’s wings.",
        "has_alt_form": false,
        "id": 277
    },
    {
        "name": "Wingull",
        "genus": "Seagull Pokémon",
        "identifier": "wingull",
        "evolution_chain": 139,
        "color": "white",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": 3,
        "flavor_text": "With its long, thin wings, it catches updrafts\nand flies like a glider high up into the sky.",
        "has_alt_form": false,
        "id": 278
    },
    {
        "name": "Pelipper",
        "genus": "Water Bird Pokémon",
        "identifier": "pelipper",
        "evolution_chain": 139,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": 278,
        "type1": 11,
        "type2": 3,
        "flavor_text": "It places small Pokémon into its spacious beak\nand carries them around. No one knows where\nit’s taking them.",
        "has_alt_form": false,
        "id": 279
    },
    {
        "name": "Ralts",
        "genus": "Feeling Pokémon",
        "identifier": "ralts",
        "evolution_chain": 140,
        "color": "white",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 14,
        "type2": 18,
        "flavor_text": "Ralts has the ability to sense the emotions of people. If its\nTrainer is in a cheerful mood, this Pokémon grows cheerful\nand joyous in the same way.",
        "has_alt_form": false,
        "id": 280
    },
    {
        "name": "Kirlia",
        "genus": "Emotion Pokémon",
        "identifier": "kirlia",
        "evolution_chain": 140,
        "color": "white",
        "since_gen": 3,
        "evolves_from": 280,
        "type1": 14,
        "type2": 18,
        "flavor_text": "Kirlia uses the horns on its head to amplify its psychokinetic\npower. When the Pokémon uses its power, the air around it\nbecomes distorted, creating mirages of nonexistent scenery.",
        "has_alt_form": false,
        "id": 281
    },
    {
        "name": "Gardevoir",
        "genus": "Embrace Pokémon",
        "identifier": "gardevoir",
        "evolution_chain": 140,
        "color": "white",
        "since_gen": 3,
        "evolves_from": 281,
        "type1": 14,
        "type2": 18,
        "flavor_text": "Gardevoir has the psychokinetic power to distort the\ndimensions and create a small black hole. This Pokémon\nwill try to protect its Trainer even at the risk of its own life.",
        "has_alt_form": false,
        "id": 282
    },
    {
        "name": "Surskit",
        "genus": "Pond Skater Pokémon",
        "identifier": "surskit",
        "evolution_chain": 141,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 7,
        "type2": 11,
        "flavor_text": "If it’s in a pinch, it will secrete a sweet liquid\nfrom the tip of its head. Syrup made from\ngathering that liquid is tasty on bread.",
        "has_alt_form": false,
        "id": 283
    },
    {
        "name": "Masquerain",
        "genus": "Eyeball Pokémon",
        "identifier": "masquerain",
        "evolution_chain": 141,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 283,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Masquerain intimidates enemies with the eyelike\npatterns of its eyespots. If that doesn’t work, it\ndeftly makes its escape on its set of four wings.",
        "has_alt_form": false,
        "id": 284
    },
    {
        "name": "Shroomish",
        "genus": "Mushroom Pokémon",
        "identifier": "shroomish",
        "evolution_chain": 142,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "If Shroomish senses danger, it shakes its body and scatters\nspores from the top of its head. This Pokémon’s spores are\nso toxic, they make trees and weeds wilt.",
        "has_alt_form": false,
        "id": 285
    },
    {
        "name": "Breloom",
        "genus": "Mushroom Pokémon",
        "identifier": "breloom",
        "evolution_chain": 142,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 285,
        "type1": 12,
        "type2": 2,
        "flavor_text": "The seeds ringing Breloom’s tail are made of hardened toxic\nspores. It is horrible to eat the seeds. Just taking a bite of this\nPokémon’s seed will cause your stomach to rumble.",
        "has_alt_form": false,
        "id": 286
    },
    {
        "name": "Slakoth",
        "genus": "Slacker Pokémon",
        "identifier": "slakoth",
        "evolution_chain": 143,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Slakoth’s heart beats just once a minute. Whatever happens,\nit is content to loaf around motionless. It is rare to see this\nPokémon in motion.",
        "has_alt_form": false,
        "id": 287
    },
    {
        "name": "Vigoroth",
        "genus": "Wild Monkey Pokémon",
        "identifier": "vigoroth",
        "evolution_chain": 143,
        "color": "white",
        "since_gen": 3,
        "evolves_from": 287,
        "type1": 1,
        "type2": null,
        "flavor_text": "Vigoroth is simply incapable of remaining still. Even when it\ntries to sleep, the blood in its veins grows agitated, compelling\nthis Pokémon to run wild throughout the jungle before it can\nsettle down.",
        "has_alt_form": false,
        "id": 288
    },
    {
        "name": "Slaking",
        "genus": "Lazy Pokémon",
        "identifier": "slaking",
        "evolution_chain": 143,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": 288,
        "type1": 1,
        "type2": null,
        "flavor_text": "Wherever Slaking live, rings of over a yard in diameter appear\nin grassy fields. They are made by the Pokémon as it eats all\nthe grass within reach while lying prone on the ground.",
        "has_alt_form": false,
        "id": 289
    },
    {
        "name": "Nincada",
        "genus": "Trainee Pokémon",
        "identifier": "nincada",
        "evolution_chain": 144,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 7,
        "type2": 5,
        "flavor_text": "Nincada lives underground. It uses its sharp claws to carve the\nroots of trees and absorb moisture and nutrients.\nThis Pokémon can’t withstand bright sunlight so avoids it.",
        "has_alt_form": false,
        "id": 290
    },
    {
        "name": "Ninjask",
        "genus": "Ninja Pokémon",
        "identifier": "ninjask",
        "evolution_chain": 144,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": 290,
        "type1": 7,
        "type2": 3,
        "flavor_text": "If Ninjask is not trained properly, it will refuse to obey\nthe Trainer and cry loudly continuously. Because of this\nquality, this Pokémon is said to be one that puts the\nTrainer’s abilities to the test.",
        "has_alt_form": false,
        "id": 291
    },
    {
        "name": "Shedinja",
        "genus": "Shed Pokémon",
        "identifier": "shedinja",
        "evolution_chain": 144,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": 290,
        "type1": 7,
        "type2": 8,
        "flavor_text": "Shedinja is a peculiar Pokémon. It seems to appear unsought\nin a Poké Ball after a Nincada evolves. This bizarre Pokémon\nis entirely immobile—it doesn’t even breathe.",
        "has_alt_form": false,
        "id": 292
    },
    {
        "name": "Whismur",
        "genus": "Whisper Pokémon",
        "identifier": "whismur",
        "evolution_chain": 145,
        "color": "pink",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Whismur is very timid. If it starts to cry loudly, it becomes\nstartled by its own crying and cries even harder. When it finally\nstops crying, the Pokémon goes to sleep, all tired out.",
        "has_alt_form": false,
        "id": 293
    },
    {
        "name": "Loudred",
        "genus": "Big Voice Pokémon",
        "identifier": "loudred",
        "evolution_chain": 145,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 293,
        "type1": 1,
        "type2": null,
        "flavor_text": "Loudred shouts while stamping its feet. After it finishes\nshouting, this Pokémon becomes incapable of hearing\nanything for a while. This is considered to be a weak point.",
        "has_alt_form": false,
        "id": 294
    },
    {
        "name": "Exploud",
        "genus": "Loud Noise Pokémon",
        "identifier": "exploud",
        "evolution_chain": 145,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 294,
        "type1": 1,
        "type2": null,
        "flavor_text": "Exploud communicates its feelings to the others by emitting\nwhistle-like sounds from the tubes on its body. This Pokémon\nonly raises its voice when it is in battle.",
        "has_alt_form": false,
        "id": 295
    },
    {
        "name": "Makuhita",
        "genus": "Guts Pokémon",
        "identifier": "makuhita",
        "evolution_chain": 146,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "It practices its slaps by repeatedly slapping\ntree trunks. It has been known to slap an\nExeggutor and get flung away.",
        "has_alt_form": false,
        "id": 296
    },
    {
        "name": "Hariyama",
        "genus": "Arm Thrust Pokémon",
        "identifier": "hariyama",
        "evolution_chain": 146,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": 296,
        "type1": 2,
        "type2": null,
        "flavor_text": "Although they enjoy comparing their strength,\nthey’re also kind. They value etiquette, praising\nopponents they battle.",
        "has_alt_form": false,
        "id": 297
    },
    {
        "name": "Azurill",
        "genus": "Polka Dot Pokémon",
        "identifier": "azurill",
        "evolution_chain": 90,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": 18,
        "flavor_text": "Azurill’s tail is large and bouncy. It is packed full of the\nnutrients this Pokémon needs to grow. Azurill can be seen\nbouncing and playing on its big, rubbery tail.",
        "has_alt_form": false,
        "id": 298
    },
    {
        "name": "Nosepass",
        "genus": "Compass Pokémon",
        "identifier": "nosepass",
        "evolution_chain": 147,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 6,
        "type2": null,
        "flavor_text": "It moves less than an inch a year, but when\nit’s in a jam, it will spin and drill down into the\nground in a split second.",
        "has_alt_form": false,
        "id": 299
    },
    {
        "name": "Skitty",
        "genus": "Kitten Pokémon",
        "identifier": "skitty",
        "evolution_chain": 148,
        "color": "pink",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Skitty is known to chase around playfully after its own tail.\nIn the wild, this Pokémon lives in holes in the trees of forests.\nIt is very popular as a pet because of its adorable looks.",
        "has_alt_form": false,
        "id": 300
    },
    {
        "name": "Delcatty",
        "genus": "Prim Pokémon",
        "identifier": "delcatty",
        "evolution_chain": 148,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": 300,
        "type1": 1,
        "type2": null,
        "flavor_text": "Delcatty sleeps anywhere it wants without keeping a permanent\nnest. If other Pokémon approach it as it sleeps, this Pokémon\nwill never fight—it will just move away somewhere else.",
        "has_alt_form": false,
        "id": 301
    },
    {
        "name": "Sableye",
        "genus": "Darkness Pokémon",
        "identifier": "sableye",
        "evolution_chain": 149,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 17,
        "type2": 8,
        "flavor_text": "It digs through the ground with its hard claws\nand crunches down gems with its thick pointy\nteeth. Carbink is its favorite food.",
        "has_alt_form": false,
        "id": 302
    },
    {
        "name": "Mawile",
        "genus": "Deceiver Pokémon",
        "identifier": "mawile",
        "evolution_chain": 150,
        "color": "black",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 9,
        "type2": 18,
        "flavor_text": "A cunning and terrifying Pokémon, its cuteness\nmakes opponents let down their guard—and\nthen it swallows them whole with its huge jaws.",
        "has_alt_form": false,
        "id": 303
    },
    {
        "name": "Aron",
        "genus": "Iron Armor Pokémon",
        "identifier": "aron",
        "evolution_chain": 151,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 9,
        "type2": 6,
        "flavor_text": "Aron has a body of steel. With one all-out charge, this\nPokémon can demolish even a heavy dump truck.\nThe destroyed dump truck then becomes a handy meal\nfor the Pokémon.",
        "has_alt_form": false,
        "id": 304
    },
    {
        "name": "Lairon",
        "genus": "Iron Armor Pokémon",
        "identifier": "lairon",
        "evolution_chain": 151,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": 304,
        "type1": 9,
        "type2": 6,
        "flavor_text": "Lairon feeds on iron contained in rocks and water. It makes\nits nest on mountains where iron ore is buried. As a result,\nthe Pokémon often clashes with humans mining the iron ore.",
        "has_alt_form": false,
        "id": 305
    },
    {
        "name": "Aggron",
        "genus": "Iron Armor Pokémon",
        "identifier": "aggron",
        "evolution_chain": 151,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": 305,
        "type1": 9,
        "type2": 6,
        "flavor_text": "Aggron is protective of its environment. If its mountain is\nravaged by a landslide or a fire, this Pokémon will haul\ntopsoil to the area, plant trees, and beautifully restore its\nown territory.",
        "has_alt_form": false,
        "id": 306
    },
    {
        "name": "Meditite",
        "genus": "Meditate Pokémon",
        "identifier": "meditite",
        "evolution_chain": 152,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 2,
        "type2": 14,
        "flavor_text": "Meditite heightens its inner energy through meditation.\nIt survives on just one berry a day. Minimal eating is another\naspect of this Pokémon’s training.",
        "has_alt_form": false,
        "id": 307
    },
    {
        "name": "Medicham",
        "genus": "Meditate Pokémon",
        "identifier": "medicham",
        "evolution_chain": 152,
        "color": "red",
        "since_gen": 3,
        "evolves_from": 307,
        "type1": 2,
        "type2": 14,
        "flavor_text": "Through the power of meditation, Medicham developed its\nsixth sense. It gained the ability to use psychokinetic powers.\nThis Pokémon is known to meditate for a whole month\nwithout eating.",
        "has_alt_form": false,
        "id": 308
    },
    {
        "name": "Electrike",
        "genus": "Lightning Pokémon",
        "identifier": "electrike",
        "evolution_chain": 153,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Friction between the air and its fur produces\nstatic electricity. When Electrike runs, it makes\na crackling sound.",
        "has_alt_form": false,
        "id": 309
    },
    {
        "name": "Manectric",
        "genus": "Discharge Pokémon",
        "identifier": "manectric",
        "evolution_chain": 153,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": 309,
        "type1": 13,
        "type2": null,
        "flavor_text": "Manectric can be found beneath unnatural\nthunderclouds. People say it can run at the\nsame speed as lightning striking.",
        "has_alt_form": false,
        "id": 310
    },
    {
        "name": "Plusle",
        "genus": "Cheering Pokémon",
        "identifier": "plusle",
        "evolution_chain": 154,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "When Plusle is cheering on its partner, it flashes with electric\nsparks from all over its body. If its partner loses, this Pokémon\ncries loudly.",
        "has_alt_form": false,
        "id": 311
    },
    {
        "name": "Minun",
        "genus": "Cheering Pokémon",
        "identifier": "minun",
        "evolution_chain": 155,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Minun loves to cheer on its partner in battle. It gives off sparks\nfrom its body while it is doing so. If its partner is in trouble,\nthis Pokémon gives off increasing amounts of sparks.",
        "has_alt_form": false,
        "id": 312
    },
    {
        "name": "Volbeat",
        "genus": "Firefly Pokémon",
        "identifier": "volbeat",
        "evolution_chain": 156,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "Volbeat’s tail glows like a lightbulb. With other Volbeat,\nit uses its tail to draw geometric shapes in the night sky.\nThis Pokémon loves the sweet aroma given off by Illumise.",
        "has_alt_form": false,
        "id": 313
    },
    {
        "name": "Illumise",
        "genus": "Firefly Pokémon",
        "identifier": "illumise",
        "evolution_chain": 157,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "Illumise leads a flight of illuminated Volbeat to draw signs in\nthe night sky. This Pokémon is said to earn greater respect\nfrom its peers by composing more complex designs in the sky.",
        "has_alt_form": false,
        "id": 314
    },
    {
        "name": "Roselia",
        "genus": "Thorn Pokémon",
        "identifier": "roselia",
        "evolution_chain": 158,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 406,
        "type1": 12,
        "type2": 4,
        "flavor_text": "On extremely rare occasions, a Roselia is said to appear with\nits flowers in unusual colors. The thorns on this Pokémon’s\nhead contain a vicious poison.",
        "has_alt_form": false,
        "id": 315
    },
    {
        "name": "Gulpin",
        "genus": "Stomach Pokémon",
        "identifier": "gulpin",
        "evolution_chain": 159,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "Most of Gulpin’s body is made up of its stomach—its heart and\nbrain are very small in comparison. This Pokémon’s stomach\ncontains special enzymes that dissolve anything.",
        "has_alt_form": false,
        "id": 316
    },
    {
        "name": "Swalot",
        "genus": "Poison Bag Pokémon",
        "identifier": "swalot",
        "evolution_chain": 159,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": 316,
        "type1": 4,
        "type2": null,
        "flavor_text": "Swalot has no teeth, so what it eats, it swallows whole, no\nmatter what. Its cavernous mouth yawns widely. An automobile\ntire could easily fit inside this Pokémon’s mouth.",
        "has_alt_form": false,
        "id": 317
    },
    {
        "name": "Carvanha",
        "genus": "Savage Pokémon",
        "identifier": "carvanha",
        "evolution_chain": 160,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": 17,
        "flavor_text": "They’re such cowards that they won’t hunt\nalone. When five or so of them get together,\nthey suddenly turn ferocious!",
        "has_alt_form": false,
        "id": 318
    },
    {
        "name": "Sharpedo",
        "genus": "Brutal Pokémon",
        "identifier": "sharpedo",
        "evolution_chain": 160,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 318,
        "type1": 11,
        "type2": 17,
        "flavor_text": "People believe that carrying one of its\ndiscarded fangs will prevent mishaps at sea,\nso the fangs are made into accessories.",
        "has_alt_form": false,
        "id": 319
    },
    {
        "name": "Wailmer",
        "genus": "Ball Whale Pokémon",
        "identifier": "wailmer",
        "evolution_chain": 161,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It swims along with its mouth open and\nswallows down seawater along with its food.\nIt sprays excess water out of its nostrils.",
        "has_alt_form": false,
        "id": 320
    },
    {
        "name": "Wailord",
        "genus": "Float Whale Pokémon",
        "identifier": "wailord",
        "evolution_chain": 161,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 320,
        "type1": 11,
        "type2": null,
        "flavor_text": "They eat so many fish Pokémon that when\nWailord become too numerous, fishermen have\nto chase them off.",
        "has_alt_form": false,
        "id": 321
    },
    {
        "name": "Numel",
        "genus": "Numb Pokémon",
        "identifier": "numel",
        "evolution_chain": 162,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 10,
        "type2": 5,
        "flavor_text": "Numel stores magma of almost 2,200 degrees Fahrenheit\nwithin its body. If it gets wet, the magma cools and hardens.\nIn that event, the Pokémon’s body grows heavy and its\nmovements become sluggish.",
        "has_alt_form": false,
        "id": 322
    },
    {
        "name": "Camerupt",
        "genus": "Eruption Pokémon",
        "identifier": "camerupt",
        "evolution_chain": 162,
        "color": "red",
        "since_gen": 3,
        "evolves_from": 322,
        "type1": 10,
        "type2": 5,
        "flavor_text": "The humps on Camerupt’s back are formed by a transformation\nof its bones. They sometimes blast out molten magma.\nThis Pokémon apparently erupts often when it is enraged.",
        "has_alt_form": false,
        "id": 323
    },
    {
        "name": "Torkoal",
        "genus": "Coal Pokémon",
        "identifier": "torkoal",
        "evolution_chain": 163,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "You can tell how it’s feeling by the smoke\nspouting from its shell. Tremendous velocity\nis a sign of good health.",
        "has_alt_form": false,
        "id": 324
    },
    {
        "name": "Spoink",
        "genus": "Bounce Pokémon",
        "identifier": "spoink",
        "evolution_chain": 164,
        "color": "black",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Spoink keeps a pearl on top of its head. The pearl functions to\namplify this Pokémon’s psychokinetic powers. It is therefore on\na constant search for a bigger pearl.",
        "has_alt_form": false,
        "id": 325
    },
    {
        "name": "Grumpig",
        "genus": "Manipulate Pokémon",
        "identifier": "grumpig",
        "evolution_chain": 164,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": 325,
        "type1": 14,
        "type2": null,
        "flavor_text": "Grumpig uses the black pearls on its body to wield\nits fantastic powers. When it is doing so, it dances bizarrely.\nThis Pokémon’s black pearls are valuable as works of art.",
        "has_alt_form": false,
        "id": 326
    },
    {
        "name": "Spinda",
        "genus": "Spot Panda Pokémon",
        "identifier": "spinda",
        "evolution_chain": 165,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Its steps are shaky and stumbling. Walking for a\nlong time makes it feel sick.",
        "has_alt_form": false,
        "id": 327
    },
    {
        "name": "Trapinch",
        "genus": "Ant Pit Pokémon",
        "identifier": "trapinch",
        "evolution_chain": 166,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "Its jaws are strong enough to crush rocks but\nso heavy that it can’t get up if it flips over.\nSandile seize those moments as their chance.",
        "has_alt_form": false,
        "id": 328
    },
    {
        "name": "Vibrava",
        "genus": "Vibration Pokémon",
        "identifier": "vibrava",
        "evolution_chain": 166,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 328,
        "type1": 5,
        "type2": 16,
        "flavor_text": "It vibrates its wings to generate ultrasonic\nwaves, causing its prey to faint. Then it buries\nthe prey alive in the sand to preserve it.",
        "has_alt_form": false,
        "id": 329
    },
    {
        "name": "Flygon",
        "genus": "Mystic Pokémon",
        "identifier": "flygon",
        "evolution_chain": 166,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 329,
        "type1": 5,
        "type2": 16,
        "flavor_text": "By flapping their wings, Flygon cause\nsandstorms that conceal Krookodile.\nThe team then splits the prey they catch.",
        "has_alt_form": false,
        "id": 330
    },
    {
        "name": "Cacnea",
        "genus": "Cactus Pokémon",
        "identifier": "cacnea",
        "evolution_chain": 167,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "The more arid and harsh the environment, the more pretty and\nfragrant a flower Cacnea grows. This Pokémon battles by\nwildly swinging its thorny arms.",
        "has_alt_form": false,
        "id": 331
    },
    {
        "name": "Cacturne",
        "genus": "Scarecrow Pokémon",
        "identifier": "cacturne",
        "evolution_chain": 167,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 331,
        "type1": 12,
        "type2": 17,
        "flavor_text": "If a traveler is going through a desert in the thick of night,\nCacturne will follow in a ragtag group. The Pokémon are\nbiding their time, waiting for the traveler to tire and become\nincapable of moving.",
        "has_alt_form": false,
        "id": 332
    },
    {
        "name": "Swablu",
        "genus": "Cotton Bird Pokémon",
        "identifier": "swablu",
        "evolution_chain": 168,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Swablu loves to make things clean. If it spots something dirty,\nit will wipe and polish it with its cottony wings. If its wings\nbecome dirty, this Pokémon finds a stream and showers itself.",
        "has_alt_form": false,
        "id": 333
    },
    {
        "name": "Altaria",
        "genus": "Humming Pokémon",
        "identifier": "altaria",
        "evolution_chain": 168,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 333,
        "type1": 16,
        "type2": 3,
        "flavor_text": "Altaria sings in a gorgeous soprano. Its wings are like cotton\nclouds. This Pokémon catches updrafts with its buoyant wings\nand soars way up into the wild blue yonder.",
        "has_alt_form": false,
        "id": 334
    },
    {
        "name": "Zangoose",
        "genus": "Cat Ferret Pokémon",
        "identifier": "zangoose",
        "evolution_chain": 169,
        "color": "white",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Zangoose usually stays on all fours, but when angered, it gets\nup on its hind legs and extends its claws. This Pokémon shares\na bitter rivalry with Seviper that dates back over generations.",
        "has_alt_form": false,
        "id": 335
    },
    {
        "name": "Seviper",
        "genus": "Fang Snake Pokémon",
        "identifier": "seviper",
        "evolution_chain": 170,
        "color": "black",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "Seviper’s swordlike tail serves two purposes—it slashes foes\nand douses them with secreted poison. This Pokémon will not\ngive up its long-running blood feud with Zangoose.",
        "has_alt_form": false,
        "id": 336
    },
    {
        "name": "Lunatone",
        "genus": "Meteorite Pokémon",
        "identifier": "lunatone",
        "evolution_chain": 171,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 6,
        "type2": 14,
        "flavor_text": "Lunatone becomes active around the time of the full moon.\nInstead of walking, it moves by floating in midair.\nThe Pokémon’s intimidating red eyes cause all those who\nsee it to become transfixed with fear.",
        "has_alt_form": false,
        "id": 337
    },
    {
        "name": "Solrock",
        "genus": "Meteorite Pokémon",
        "identifier": "solrock",
        "evolution_chain": 172,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 6,
        "type2": 14,
        "flavor_text": "Sunlight is the source of Solrock’s power. It is said to possess\nthe ability to read the emotions of others. This Pokémon gives\noff intense heat while rotating its body.",
        "has_alt_form": false,
        "id": 338
    },
    {
        "name": "Barboach",
        "genus": "Whiskers Pokémon",
        "identifier": "barboach",
        "evolution_chain": 173,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Its entire body is gooey. When pecked at by\nbird Pokémon, it slips and slides its way\nto freedom.",
        "has_alt_form": false,
        "id": 339
    },
    {
        "name": "Whiscash",
        "genus": "Whiskers Pokémon",
        "identifier": "whiscash",
        "evolution_chain": 173,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 339,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Whiscash shakes the ground at high intensities\nto intimidate its opponents. It swallows its prey\nwhole—along with mud from the swamp floor.",
        "has_alt_form": false,
        "id": 340
    },
    {
        "name": "Corphish",
        "genus": "Ruffian Pokémon",
        "identifier": "corphish",
        "evolution_chain": 174,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Individuals that have been set free by Trainers\nwho could no longer raise them have become\ncommon, and they can now be found in Alola.",
        "has_alt_form": false,
        "id": 341
    },
    {
        "name": "Crawdaunt",
        "genus": "Rogue Pokémon",
        "identifier": "crawdaunt",
        "evolution_chain": 174,
        "color": "red",
        "since_gen": 3,
        "evolves_from": 341,
        "type1": 11,
        "type2": 17,
        "flavor_text": "Its temperament is rough and it loves to fight,\nbut as soon as its pincers break off, it turns\ncowardly. It stays timid until they grow back.",
        "has_alt_form": false,
        "id": 342
    },
    {
        "name": "Baltoy",
        "genus": "Clay Doll Pokémon",
        "identifier": "baltoy",
        "evolution_chain": 175,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 5,
        "type2": 14,
        "flavor_text": "Depictions of Pokémon similar to Baltoy have\nbeen found on the walls of caves where\nprimitive humans lived.",
        "has_alt_form": false,
        "id": 343
    },
    {
        "name": "Claydol",
        "genus": "Clay Doll Pokémon",
        "identifier": "claydol",
        "evolution_chain": 175,
        "color": "black",
        "since_gen": 3,
        "evolves_from": 343,
        "type1": 5,
        "type2": 14,
        "flavor_text": "If it gets wet, its body melts. When rain starts\nto fall, it wraps its whole body up with its\npsychic powers to protect itself.",
        "has_alt_form": false,
        "id": 344
    },
    {
        "name": "Lileep",
        "genus": "Sea Lily Pokémon",
        "identifier": "lileep",
        "evolution_chain": 176,
        "color": "purple",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 6,
        "type2": 12,
        "flavor_text": "In ancient times, it lived in warm seas. It\ndisguised itself as seaweed to ambush its prey\nand devoured them whole when they got close.",
        "has_alt_form": false,
        "id": 345
    },
    {
        "name": "Cradily",
        "genus": "Barnacle Pokémon",
        "identifier": "cradily",
        "evolution_chain": 176,
        "color": "green",
        "since_gen": 3,
        "evolves_from": 345,
        "type1": 6,
        "type2": 12,
        "flavor_text": "Normally, it lived on shallow sea shoals. When\nthe tide went out, this Pokémon came up on\nland to search for prey.",
        "has_alt_form": false,
        "id": 346
    },
    {
        "name": "Anorith",
        "genus": "Old Shrimp Pokémon",
        "identifier": "anorith",
        "evolution_chain": 177,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 6,
        "type2": 7,
        "flavor_text": "When restored Anorith are released into the\nocean, they don’t thrive, because the water\ncomposition has changed since their era.",
        "has_alt_form": false,
        "id": 347
    },
    {
        "name": "Armaldo",
        "genus": "Plate Pokémon",
        "identifier": "armaldo",
        "evolution_chain": 177,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": 347,
        "type1": 6,
        "type2": 7,
        "flavor_text": "It lived on land and went out into the sea to\nhunt for prey. Its sharp claws were its\ngreatest weapon.",
        "has_alt_form": false,
        "id": 348
    },
    {
        "name": "Feebas",
        "genus": "Fish Pokémon",
        "identifier": "feebas",
        "evolution_chain": 178,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "They look ragged, so no one catches them. They\nlook like they’d taste bad, so predators won’t\neat them. And their numbers continue to grow.",
        "has_alt_form": false,
        "id": 349
    },
    {
        "name": "Milotic",
        "genus": "Tender Pokémon",
        "identifier": "milotic",
        "evolution_chain": 178,
        "color": "pink",
        "since_gen": 3,
        "evolves_from": 349,
        "type1": 11,
        "type2": null,
        "flavor_text": "While Milotic is said to be the most beautiful\nPokémon, Trainers who like Feebas and have\nraised it are seemingly disappointed by Milotic.",
        "has_alt_form": false,
        "id": 350
    },
    {
        "name": "Castform",
        "genus": "Weather Pokémon",
        "identifier": "castform",
        "evolution_chain": 179,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Although its form changes with the weather,\nthat is apparently the result of a chemical\nreaction and not the result of its own free will.",
        "has_alt_form": false,
        "id": 351
    },
    {
        "name": "Kecleon",
        "genus": "Color Swap Pokémon",
        "identifier": "kecleon",
        "evolution_chain": 180,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It changes its hue to blend into its surroundings.\nIf no one takes notice of it for too long, it will\npout and never reveal itself.",
        "has_alt_form": false,
        "id": 352
    },
    {
        "name": "Shuppet",
        "genus": "Puppet Pokémon",
        "identifier": "shuppet",
        "evolution_chain": 181,
        "color": "black",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 8,
        "type2": null,
        "flavor_text": "It eats up emotions like malice, jealousy, and\nresentment, so some people are grateful for\nits presence.",
        "has_alt_form": false,
        "id": 353
    },
    {
        "name": "Banette",
        "genus": "Marionette Pokémon",
        "identifier": "banette",
        "evolution_chain": 181,
        "color": "black",
        "since_gen": 3,
        "evolves_from": 353,
        "type1": 8,
        "type2": null,
        "flavor_text": "It’s a stuffed toy that was thrown away and\nbecame possessed, ever searching for the one\nwho threw it away so it can exact its revenge.",
        "has_alt_form": false,
        "id": 354
    },
    {
        "name": "Duskull",
        "genus": "Requiem Pokémon",
        "identifier": "duskull",
        "evolution_chain": 182,
        "color": "black",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 8,
        "type2": null,
        "flavor_text": "Duskull wanders lost among the deep darkness of midnight.\nThere is an oft-told admonishment given to misbehaving\nchildren that this Pokémon will spirit away bad children who\nearn scoldings from their mothers.",
        "has_alt_form": false,
        "id": 355
    },
    {
        "name": "Dusclops",
        "genus": "Beckon Pokémon",
        "identifier": "dusclops",
        "evolution_chain": 182,
        "color": "black",
        "since_gen": 3,
        "evolves_from": 355,
        "type1": 8,
        "type2": null,
        "flavor_text": "Dusclops absorbs anything, however large the object may be.\nThis Pokémon hypnotizes its foe by waving its hands in a\nmacabre manner and by bringing its single eye to bear.\nThe hypnotized foe is made to do Dusclops’s bidding.",
        "has_alt_form": false,
        "id": 356
    },
    {
        "name": "Tropius",
        "genus": "Fruit Pokémon",
        "identifier": "tropius",
        "evolution_chain": 183,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 12,
        "type2": 3,
        "flavor_text": "The bunches of fruit growing around the necks\nof Tropius in Alola are especially sweet\ncompared to those in other regions.",
        "has_alt_form": false,
        "id": 357
    },
    {
        "name": "Chimecho",
        "genus": "Wind Chime Pokémon",
        "identifier": "chimecho",
        "evolution_chain": 184,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 433,
        "type1": 14,
        "type2": null,
        "flavor_text": "In high winds, Chimecho cries as it hangs from a tree branch or\nthe eaves of a building using a suction cup on its head. This\nPokémon plucks berries with its long tail and eats them.",
        "has_alt_form": false,
        "id": 358
    },
    {
        "name": "Absol",
        "genus": "Disaster Pokémon",
        "identifier": "absol",
        "evolution_chain": 185,
        "color": "white",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 17,
        "type2": null,
        "flavor_text": "The only thing unlucky about Absol is its\nappearance. It protects fields and warns people\nof disaster, so one ought to be grateful for it.",
        "has_alt_form": false,
        "id": 359
    },
    {
        "name": "Wynaut",
        "genus": "Bright Pokémon",
        "identifier": "wynaut",
        "evolution_chain": 100,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Wynaut gather on moonlit nights to play by squeezing up\nagainst each other. By being squeezed, this Pokémon gains\nendurance and is trained to dole out powerful counterattacks.",
        "has_alt_form": false,
        "id": 360
    },
    {
        "name": "Snorunt",
        "genus": "Snow Hat Pokémon",
        "identifier": "snorunt",
        "evolution_chain": 186,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 15,
        "type2": null,
        "flavor_text": "It feeds mainly on ice and snow. It’s only able to\nsurvive in a limited number of places in the\nwarm Alola region.",
        "has_alt_form": false,
        "id": 361
    },
    {
        "name": "Glalie",
        "genus": "Face Pokémon",
        "identifier": "glalie",
        "evolution_chain": 186,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": 361,
        "type1": 15,
        "type2": null,
        "flavor_text": "It freezes its prey and chews them whole.\nHowever, it prefers to eat Pokémon like Vanillite\nthat are already frozen.",
        "has_alt_form": false,
        "id": 362
    },
    {
        "name": "Spheal",
        "genus": "Clap Pokémon",
        "identifier": "spheal",
        "evolution_chain": 187,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 15,
        "type2": 11,
        "flavor_text": "Spheal always travels by rolling around on its ball-like body.\nWhen the season for ice floes arrives, this Pokémon can be\nseen rolling about on ice and crossing the sea.",
        "has_alt_form": false,
        "id": 363
    },
    {
        "name": "Sealeo",
        "genus": "Ball Roll Pokémon",
        "identifier": "sealeo",
        "evolution_chain": 187,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 363,
        "type1": 15,
        "type2": 11,
        "flavor_text": "Sealeo often balances and rolls things on the tip of its\nnose. While the Pokémon is rolling something, it checks\nthe object’s aroma and texture to determine whether it likes\nthe object or not.",
        "has_alt_form": false,
        "id": 364
    },
    {
        "name": "Walrein",
        "genus": "Ice Break Pokémon",
        "identifier": "walrein",
        "evolution_chain": 187,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 364,
        "type1": 15,
        "type2": 11,
        "flavor_text": "Walrein swims all over in frigid seawater while crushing\nicebergs with its grand, imposing tusks. Its thick layer of\nblubber makes enemy attacks bounce off harmlessly.",
        "has_alt_form": false,
        "id": 365
    },
    {
        "name": "Clamperl",
        "genus": "Bivalve Pokémon",
        "identifier": "clamperl",
        "evolution_chain": 188,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Despite its appearance, it’s carnivorous. It\nclamps down on its prey with both sides of its\nshell and doesn’t let go until they stop moving.",
        "has_alt_form": false,
        "id": 366
    },
    {
        "name": "Huntail",
        "genus": "Deep Sea Pokémon",
        "identifier": "huntail",
        "evolution_chain": 188,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 366,
        "type1": 11,
        "type2": null,
        "flavor_text": "It’s not the strongest swimmer. It wags its tail to\nlure in its prey and then gulps them down as\nsoon as they get close.",
        "has_alt_form": false,
        "id": 367
    },
    {
        "name": "Gorebyss",
        "genus": "South Sea Pokémon",
        "identifier": "gorebyss",
        "evolution_chain": 188,
        "color": "pink",
        "since_gen": 3,
        "evolves_from": 366,
        "type1": 11,
        "type2": null,
        "flavor_text": "The color of its body changes with the water\ntemperature. The coloration of Gorebyss in Alola\nis almost blindingly vivid.",
        "has_alt_form": false,
        "id": 368
    },
    {
        "name": "Relicanth",
        "genus": "Longevity Pokémon",
        "identifier": "relicanth",
        "evolution_chain": 189,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": 6,
        "flavor_text": "Thought to have gone extinct, Relicanth was\ngiven a name that is a variation of the name of\nthe person who discovered it.",
        "has_alt_form": false,
        "id": 369
    },
    {
        "name": "Luvdisc",
        "genus": "Rendezvous Pokémon",
        "identifier": "luvdisc",
        "evolution_chain": 190,
        "color": "pink",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "There was an era when it was overfished due to\nthe rumor that having one of its heart-shaped\nscales would enable you to find a sweetheart.",
        "has_alt_form": false,
        "id": 370
    },
    {
        "name": "Bagon",
        "genus": "Rock Head Pokémon",
        "identifier": "bagon",
        "evolution_chain": 191,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 16,
        "type2": null,
        "flavor_text": "Whenever it sees bird Pokémon flying through\nthe sky, it becomes envious and smashes its\nsurroundings to bits with headbutts.",
        "has_alt_form": false,
        "id": 371
    },
    {
        "name": "Shelgon",
        "genus": "Endurance Pokémon",
        "identifier": "shelgon",
        "evolution_chain": 191,
        "color": "white",
        "since_gen": 3,
        "evolves_from": 371,
        "type1": 16,
        "type2": null,
        "flavor_text": "The cells within its body are changing at a\nbewildering pace. Its hard shell is made from\nthe same substance as bone.",
        "has_alt_form": false,
        "id": 372
    },
    {
        "name": "Salamence",
        "genus": "Dragon Pokémon",
        "identifier": "salamence",
        "evolution_chain": 191,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 372,
        "type1": 16,
        "type2": 3,
        "flavor_text": "Overjoyed at finally being able to fly, it flies all\nover the place and usually doesn’t land until it’s\ncompletely exhausted and needs to sleep.",
        "has_alt_form": false,
        "id": 373
    },
    {
        "name": "Beldum",
        "genus": "Iron Ball Pokémon",
        "identifier": "beldum",
        "evolution_chain": 192,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 9,
        "type2": 14,
        "flavor_text": "Instead of blood, magnetism flows through its\nbody. When it’s feeling bad, try giving it\na magnet.",
        "has_alt_form": false,
        "id": 374
    },
    {
        "name": "Metang",
        "genus": "Iron Claw Pokémon",
        "identifier": "metang",
        "evolution_chain": 192,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 374,
        "type1": 9,
        "type2": 14,
        "flavor_text": "With its two brains, it fires powerful psychic\nenergy to stop its prey in their tracks.",
        "has_alt_form": false,
        "id": 375
    },
    {
        "name": "Metagross",
        "genus": "Iron Leg Pokémon",
        "identifier": "metagross",
        "evolution_chain": 192,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": 375,
        "type1": 9,
        "type2": 14,
        "flavor_text": "It boasts not only psychic powers but also\nfantastic strength. It grabs its prey with its four\nlegs and holds them in place with its claws.",
        "has_alt_form": false,
        "id": 376
    },
    {
        "name": "Regirock",
        "genus": "Rock Peak Pokémon",
        "identifier": "regirock",
        "evolution_chain": 193,
        "color": "brown",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 6,
        "type2": null,
        "flavor_text": "Regirock’s body is composed entirely of rocks. Recently,\na study made the startling discovery that the rocks were all\nunearthed from different locations.",
        "has_alt_form": false,
        "id": 377
    },
    {
        "name": "Regice",
        "genus": "Iceberg Pokémon",
        "identifier": "regice",
        "evolution_chain": 194,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 15,
        "type2": null,
        "flavor_text": "Regice cloaks itself with frigid air of -328 degrees Fahrenheit.\nThings will freeze solid just by going near this Pokémon.\nIts icy body is so cold, it will not melt even if it is immersed\nin magma.",
        "has_alt_form": false,
        "id": 378
    },
    {
        "name": "Registeel",
        "genus": "Iron Pokémon",
        "identifier": "registeel",
        "evolution_chain": 195,
        "color": "gray",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 9,
        "type2": null,
        "flavor_text": "Registeel was imprisoned by people in ancient times.\nThe metal composing its body is thought to be a curious\nsubstance that is not of this earth.",
        "has_alt_form": false,
        "id": 379
    },
    {
        "name": "Latias",
        "genus": "Eon Pokémon",
        "identifier": "latias",
        "evolution_chain": 196,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 16,
        "type2": 14,
        "flavor_text": "Latias is highly intelligent and capable of understanding\nhuman speech. It is covered with a glass-like down.\nThe Pokémon enfolds its body with its down and refracts\nlight to alter its appearance.",
        "has_alt_form": false,
        "id": 380
    },
    {
        "name": "Latios",
        "genus": "Eon Pokémon",
        "identifier": "latios",
        "evolution_chain": 197,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 16,
        "type2": 14,
        "flavor_text": "Latios will only open its heart to a Trainer with a\ncompassionate spirit. This Pokémon can fly faster than a\njet plane by folding its forelegs to minimize air resistance.",
        "has_alt_form": false,
        "id": 381
    },
    {
        "name": "Kyogre",
        "genus": "Sea Basin Pokémon",
        "identifier": "kyogre",
        "evolution_chain": 198,
        "color": "blue",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Kyogre is said to be the personification of the sea itself.\nLegends tell of its many clashes against Groudon,\nas each sought to gain the power of nature.",
        "has_alt_form": false,
        "id": 382
    },
    {
        "name": "Groudon",
        "genus": "Continent Pokémon",
        "identifier": "groudon",
        "evolution_chain": 199,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "Through Primal Reversion and with nature’s full power,\nit will take back its true form. It can cause magma to\nerupt and expand the landmass of the world.",
        "has_alt_form": false,
        "id": 383
    },
    {
        "name": "Rayquaza",
        "genus": "Sky High Pokémon",
        "identifier": "rayquaza",
        "evolution_chain": 200,
        "color": "green",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 16,
        "type2": 3,
        "flavor_text": "It flies forever through the ozone layer, consuming\nmeteoroids for sustenance. The many meteoroids\nin its body provide the energy it needs to Mega Evolve.",
        "has_alt_form": false,
        "id": 384
    },
    {
        "name": "Jirachi",
        "genus": "Wish Pokémon",
        "identifier": "jirachi",
        "evolution_chain": 201,
        "color": "yellow",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 9,
        "type2": 14,
        "flavor_text": "Jirachi will awaken from its sleep of a thousand years if you\nsing to it in a voice of purity. It is said to make true any wish\nthat people desire.",
        "has_alt_form": false,
        "id": 385
    },
    {
        "name": "Deoxys",
        "genus": "DNA Pokémon",
        "identifier": "deoxys",
        "evolution_chain": 202,
        "color": "red",
        "since_gen": 3,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Deoxys emerged from a virus that came from space. It is highly\nintelligent and wields psychokinetic powers. This Pokémon\nshoots lasers from the crystalline organ on its chest.",
        "has_alt_form": true,
        "id": 386
    },
    {
        "name": "Turtwig",
        "genus": "Tiny Leaf Pokémon",
        "identifier": "turtwig",
        "evolution_chain": 203,
        "color": "green",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "It undertakes photosynthesis with its body, making\noxygen. The leaf on its head wilts if it is thirsty.",
        "has_alt_form": false,
        "id": 387
    },
    {
        "name": "Grotle",
        "genus": "Grove Pokémon",
        "identifier": "grotle",
        "evolution_chain": 203,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 387,
        "type1": 12,
        "type2": null,
        "flavor_text": "It knows where pure water wells up. It carries fellow\nPokémon there on its back.",
        "has_alt_form": false,
        "id": 388
    },
    {
        "name": "Torterra",
        "genus": "Continent Pokémon",
        "identifier": "torterra",
        "evolution_chain": 203,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 388,
        "type1": 12,
        "type2": 5,
        "flavor_text": "Small Pokémon occasionally gather on its unmoving\nback to begin building their nests.",
        "has_alt_form": false,
        "id": 389
    },
    {
        "name": "Chimchar",
        "genus": "Chimp Pokémon",
        "identifier": "chimchar",
        "evolution_chain": 204,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "The gas made in its belly burns from its rear end.\nThe fire burns weakly when it feels sick.",
        "has_alt_form": false,
        "id": 390
    },
    {
        "name": "Monferno",
        "genus": "Playful Pokémon",
        "identifier": "monferno",
        "evolution_chain": 204,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 390,
        "type1": 10,
        "type2": 2,
        "flavor_text": "It uses ceilings and walls to launch aerial attacks.\nIts fiery tail is but one weapon.",
        "has_alt_form": false,
        "id": 391
    },
    {
        "name": "Infernape",
        "genus": "Flame Pokémon",
        "identifier": "infernape",
        "evolution_chain": 204,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 391,
        "type1": 10,
        "type2": 2,
        "flavor_text": "It tosses its enemies around with agility. It uses all\nits limbs to fight in its own unique style.",
        "has_alt_form": false,
        "id": 392
    },
    {
        "name": "Piplup",
        "genus": "Penguin Pokémon",
        "identifier": "piplup",
        "evolution_chain": 205,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Because it is very proud, it hates accepting food\nfrom people. Its thick down guards it from cold.",
        "has_alt_form": false,
        "id": 393
    },
    {
        "name": "Prinplup",
        "genus": "Penguin Pokémon",
        "identifier": "prinplup",
        "evolution_chain": 205,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 393,
        "type1": 11,
        "type2": null,
        "flavor_text": "It lives a solitary life. Its wings deliver wicked blows\nthat can snap even the thickest of trees.",
        "has_alt_form": false,
        "id": 394
    },
    {
        "name": "Empoleon",
        "genus": "Emperor Pokémon",
        "identifier": "empoleon",
        "evolution_chain": 205,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 394,
        "type1": 11,
        "type2": 9,
        "flavor_text": "The three horns that extend from its beak attest to\nits power. The leader has the biggest horns.",
        "has_alt_form": false,
        "id": 395
    },
    {
        "name": "Starly",
        "genus": "Starling Pokémon",
        "identifier": "starly",
        "evolution_chain": 206,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "They flock around mountains and fields, chasing\nafter bug Pokémon. Their singing is noisy\nand annoying.",
        "has_alt_form": false,
        "id": 396
    },
    {
        "name": "Staravia",
        "genus": "Starling Pokémon",
        "identifier": "staravia",
        "evolution_chain": 206,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 396,
        "type1": 1,
        "type2": 3,
        "flavor_text": "It lives in forests and fields. Squabbles over\nterritory occur when flocks collide.",
        "has_alt_form": false,
        "id": 397
    },
    {
        "name": "Staraptor",
        "genus": "Predator Pokémon",
        "identifier": "staraptor",
        "evolution_chain": 206,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 397,
        "type1": 1,
        "type2": 3,
        "flavor_text": "When Staravia evolve into Staraptor, they leave the\nflock to live alone. They have sturdy wings.",
        "has_alt_form": false,
        "id": 398
    },
    {
        "name": "Bidoof",
        "genus": "Plump Mouse Pokémon",
        "identifier": "bidoof",
        "evolution_chain": 207,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It constantly gnaws on logs and rocks to whittle\ndown its front teeth. It nests alongside water.",
        "has_alt_form": false,
        "id": 399
    },
    {
        "name": "Bibarel",
        "genus": "Beaver Pokémon",
        "identifier": "bibarel",
        "evolution_chain": 207,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 399,
        "type1": 1,
        "type2": 11,
        "flavor_text": "It makes its nest by damming streams with bark and\nmud. It is known as an industrious worker.",
        "has_alt_form": false,
        "id": 400
    },
    {
        "name": "Kricketot",
        "genus": "Cricket Pokémon",
        "identifier": "kricketot",
        "evolution_chain": 208,
        "color": "red",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "When its antennae hit each other, it sounds like the\nmusic of a xylophone.",
        "has_alt_form": false,
        "id": 401
    },
    {
        "name": "Kricketune",
        "genus": "Cricket Pokémon",
        "identifier": "kricketune",
        "evolution_chain": 208,
        "color": "red",
        "since_gen": 4,
        "evolves_from": 401,
        "type1": 7,
        "type2": null,
        "flavor_text": "It signals its emotions with its melodies. Scientists\nare studying these melodic patterns.",
        "has_alt_form": false,
        "id": 402
    },
    {
        "name": "Shinx",
        "genus": "Flash Pokémon",
        "identifier": "shinx",
        "evolution_chain": 209,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "All of its fur dazzles if danger is sensed. It flees\nwhile the foe is momentarily blinded.",
        "has_alt_form": false,
        "id": 403
    },
    {
        "name": "Luxio",
        "genus": "Spark Pokémon",
        "identifier": "luxio",
        "evolution_chain": 209,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 403,
        "type1": 13,
        "type2": null,
        "flavor_text": "Strong electricity courses through the tips of its\nsharp claws. A light scratch causes fainting in foes.",
        "has_alt_form": false,
        "id": 404
    },
    {
        "name": "Luxray",
        "genus": "Gleam Eyes Pokémon",
        "identifier": "luxray",
        "evolution_chain": 209,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 404,
        "type1": 13,
        "type2": null,
        "flavor_text": "Luxray’s ability to see through objects comes in\nhandy when it’s scouting for danger.",
        "has_alt_form": false,
        "id": 405
    },
    {
        "name": "Budew",
        "genus": "Bud Pokémon",
        "identifier": "budew",
        "evolution_chain": 158,
        "color": "green",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 12,
        "type2": 4,
        "flavor_text": "Over the winter, it closes its bud and endures the\ncold. In spring, the bud opens and releases pollen.",
        "has_alt_form": false,
        "id": 406
    },
    {
        "name": "Roserade",
        "genus": "Bouquet Pokémon",
        "identifier": "roserade",
        "evolution_chain": 158,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 315,
        "type1": 12,
        "type2": 4,
        "flavor_text": "With the movements of a dancer, it strikes with\nwhips that are densely lined with poison thorns.",
        "has_alt_form": false,
        "id": 407
    },
    {
        "name": "Cranidos",
        "genus": "Head Butt Pokémon",
        "identifier": "cranidos",
        "evolution_chain": 211,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 6,
        "type2": null,
        "flavor_text": "A primeval Pokémon, it possesses a hard and\nsturdy skull, lacking any intelligence within.",
        "has_alt_form": false,
        "id": 408
    },
    {
        "name": "Rampardos",
        "genus": "Head Butt Pokémon",
        "identifier": "rampardos",
        "evolution_chain": 211,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 408,
        "type1": 6,
        "type2": null,
        "flavor_text": "In ancient times, people would dig up fossils of\nthis Pokémon and use its skull, which is harder\nthan steel, to make helmets.",
        "has_alt_form": false,
        "id": 409
    },
    {
        "name": "Shieldon",
        "genus": "Shield Pokémon",
        "identifier": "shieldon",
        "evolution_chain": 212,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 6,
        "type2": 9,
        "flavor_text": "A mild-mannered, herbivorous Pokémon, it used\nits face to dig up tree roots to eat. The skin on\nits face was plenty tough.",
        "has_alt_form": false,
        "id": 410
    },
    {
        "name": "Bastiodon",
        "genus": "Shield Pokémon",
        "identifier": "bastiodon",
        "evolution_chain": 212,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": 410,
        "type1": 6,
        "type2": 9,
        "flavor_text": "The bones of its face are huge and hard, so\nthey were mistaken for its spine until after this\nPokémon was successfully restored.",
        "has_alt_form": false,
        "id": 411
    },
    {
        "name": "Burmy",
        "genus": "Bagworm Pokémon",
        "identifier": "burmy",
        "evolution_chain": 213,
        "color": "green",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "If its cloak is broken in battle, it quickly remakes\nthe cloak with materials nearby.",
        "has_alt_form": true,
        "id": 412
    },
    {
        "name": "Wormadam",
        "genus": "Bagworm Pokémon",
        "identifier": "wormadam",
        "evolution_chain": 213,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 412,
        "type1": 7,
        "type2": 12,
        "flavor_text": "When Burmy evolved, its cloak became a part of\nthis Pokémon’s body. The cloak is never shed.",
        "has_alt_form": true,
        "id": 413
    },
    {
        "name": "Mothim",
        "genus": "Moth Pokémon",
        "identifier": "mothim",
        "evolution_chain": 213,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": 412,
        "type1": 7,
        "type2": 3,
        "flavor_text": "It flutters around at night and steals honey from\nthe Combee hive.",
        "has_alt_form": false,
        "id": 414
    },
    {
        "name": "Combee",
        "genus": "Tiny Bee Pokémon",
        "identifier": "combee",
        "evolution_chain": 214,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 7,
        "type2": 3,
        "flavor_text": "It collects and delivers honey to its colony.\nAt night, they cluster to form a beehive and sleep.",
        "has_alt_form": false,
        "id": 415
    },
    {
        "name": "Vespiquen",
        "genus": "Beehive Pokémon",
        "identifier": "vespiquen",
        "evolution_chain": 214,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": 415,
        "type1": 7,
        "type2": 3,
        "flavor_text": "Its abdomen is a honeycomb for grubs. It raises its\ngrubs on honey collected by Combee.",
        "has_alt_form": false,
        "id": 416
    },
    {
        "name": "Pachirisu",
        "genus": "EleSquirrel Pokémon",
        "identifier": "pachirisu",
        "evolution_chain": 215,
        "color": "white",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "A pair may be seen rubbing their cheek pouches\ntogether in an effort to share stored electricity.",
        "has_alt_form": false,
        "id": 417
    },
    {
        "name": "Buizel",
        "genus": "Sea Weasel Pokémon",
        "identifier": "buizel",
        "evolution_chain": 216,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It inflates the flotation sac around its neck and\npokes its head out of the water to see what is\ngoing on.",
        "has_alt_form": false,
        "id": 418
    },
    {
        "name": "Floatzel",
        "genus": "Sea Weasel Pokémon",
        "identifier": "floatzel",
        "evolution_chain": 216,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 418,
        "type1": 11,
        "type2": null,
        "flavor_text": "Its flotation sac developed as a result of pursuing\naquatic prey. It can double as a rubber raft.",
        "has_alt_form": false,
        "id": 419
    },
    {
        "name": "Cherubi",
        "genus": "Cherry Pokémon",
        "identifier": "cherubi",
        "evolution_chain": 217,
        "color": "pink",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "It evolves by sucking the energy out of the small\nball where it had been storing nutrients.",
        "has_alt_form": false,
        "id": 420
    },
    {
        "name": "Cherrim",
        "genus": "Blossom Pokémon",
        "identifier": "cherrim",
        "evolution_chain": 217,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 420,
        "type1": 12,
        "type2": null,
        "flavor_text": "If it senses strong sunlight, it opens its folded\npetals to absorb the sun’s rays with its whole body.",
        "has_alt_form": true,
        "id": 421
    },
    {
        "name": "Shellos",
        "genus": "Sea Slug Pokémon",
        "identifier": "shellos",
        "evolution_chain": 218,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "While they normally live in the sea, they can\nfunction on land, too, until their skin dries out.",
        "has_alt_form": true,
        "id": 422
    },
    {
        "name": "Gastrodon",
        "genus": "Sea Slug Pokémon",
        "identifier": "gastrodon",
        "evolution_chain": 218,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 422,
        "type1": 11,
        "type2": 5,
        "flavor_text": "Long ago, it had a shell on its back. There’s now\na vestigial plate on its back that’s hard but thin.",
        "has_alt_form": true,
        "id": 423
    },
    {
        "name": "Ambipom",
        "genus": "Long Tail Pokémon",
        "identifier": "ambipom",
        "evolution_chain": 93,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 190,
        "type1": 1,
        "type2": null,
        "flavor_text": "In their search for comfortable trees, they get\ninto territorial disputes with groups of\nPassimian. They win about half the time.",
        "has_alt_form": false,
        "id": 424
    },
    {
        "name": "Drifloon",
        "genus": "Balloon Pokémon",
        "identifier": "drifloon",
        "evolution_chain": 219,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 8,
        "type2": 3,
        "flavor_text": "Its round body is stuffed with souls and\nexpands each time it leads someone away.",
        "has_alt_form": false,
        "id": 425
    },
    {
        "name": "Drifblim",
        "genus": "Blimp Pokémon",
        "identifier": "drifblim",
        "evolution_chain": 219,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 425,
        "type1": 8,
        "type2": 3,
        "flavor_text": "There’s a rumor that if you catch a Drifblim\nfloating on the wind at dusk, you’ll be carried\naway to the afterlife.",
        "has_alt_form": false,
        "id": 426
    },
    {
        "name": "Buneary",
        "genus": "Rabbit Pokémon",
        "identifier": "buneary",
        "evolution_chain": 220,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Its arms and legs are weak, but when it rolls its\nears up tight and then unleashes them with its\nfull force, it can smash boulders to dust.",
        "has_alt_form": false,
        "id": 427
    },
    {
        "name": "Lopunny",
        "genus": "Rabbit Pokémon",
        "identifier": "lopunny",
        "evolution_chain": 220,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 427,
        "type1": 1,
        "type2": null,
        "flavor_text": "Lopunny regrows its coat twice a year. Mufflers\nand hats made from its fur are really warm.",
        "has_alt_form": false,
        "id": 428
    },
    {
        "name": "Mismagius",
        "genus": "Magical Pokémon",
        "identifier": "mismagius",
        "evolution_chain": 98,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 200,
        "type1": 8,
        "type2": null,
        "flavor_text": "Feared for its wrath and the curses it spreads,\nthis Pokémon will also, on a whim, cast spells\nthat help people.",
        "has_alt_form": false,
        "id": 429
    },
    {
        "name": "Honchkrow",
        "genus": "Big Boss Pokémon",
        "identifier": "honchkrow",
        "evolution_chain": 97,
        "color": "black",
        "since_gen": 4,
        "evolves_from": 198,
        "type1": 17,
        "type2": 3,
        "flavor_text": "It will absolutely not forgive failure from or\nbetrayal by its goons. It has no choice in this\nif it wants to maintain the order of the flock.",
        "has_alt_form": false,
        "id": 430
    },
    {
        "name": "Glameow",
        "genus": "Catty Pokémon",
        "identifier": "glameow",
        "evolution_chain": 221,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "When it’s happy, Glameow demonstrates beautiful\nmovements of its tail, like a dancing ribbon.",
        "has_alt_form": false,
        "id": 431
    },
    {
        "name": "Purugly",
        "genus": "Tiger Cat Pokémon",
        "identifier": "purugly",
        "evolution_chain": 221,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": 431,
        "type1": 1,
        "type2": null,
        "flavor_text": "To make itself appear intimidatingly beefy, it tightly\ncinches its waist with its twin tails.",
        "has_alt_form": false,
        "id": 432
    },
    {
        "name": "Chingling",
        "genus": "Bell Pokémon",
        "identifier": "chingling",
        "evolution_chain": 184,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "There is an orb inside its mouth. When it hops,\nthe orb bounces all over and makes a\nringing sound.",
        "has_alt_form": false,
        "id": 433
    },
    {
        "name": "Stunky",
        "genus": "Skunk Pokémon",
        "identifier": "stunky",
        "evolution_chain": 223,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 4,
        "type2": 17,
        "flavor_text": "It protects itself by spraying a noxious fluid from its\nrear. The stench lingers for 24 hours.",
        "has_alt_form": false,
        "id": 434
    },
    {
        "name": "Skuntank",
        "genus": "Skunk Pokémon",
        "identifier": "skuntank",
        "evolution_chain": 223,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 434,
        "type1": 4,
        "type2": 17,
        "flavor_text": "It sprays a stinky fluid from its tail. The fluid smells\nworse the longer it is allowed to fester.",
        "has_alt_form": false,
        "id": 435
    },
    {
        "name": "Bronzor",
        "genus": "Bronze Pokémon",
        "identifier": "bronzor",
        "evolution_chain": 224,
        "color": "green",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 9,
        "type2": 14,
        "flavor_text": "Implements shaped like it were discovered in\nancient tombs. It is unknown if they are related.",
        "has_alt_form": false,
        "id": 436
    },
    {
        "name": "Bronzong",
        "genus": "Bronze Bell Pokémon",
        "identifier": "bronzong",
        "evolution_chain": 224,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 436,
        "type1": 9,
        "type2": 14,
        "flavor_text": "Ancient people believed that petitioning Bronzong\nfor rain was the way to make crops grow.",
        "has_alt_form": false,
        "id": 437
    },
    {
        "name": "Bonsly",
        "genus": "Bonsai Pokémon",
        "identifier": "bonsly",
        "evolution_chain": 91,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 6,
        "type2": null,
        "flavor_text": "It discharges moisture from its eyes, making it\nlook like it’s crying—apparently an effective way\nof getting enemies to let down their guard.",
        "has_alt_form": false,
        "id": 438
    },
    {
        "name": "Mime Jr.",
        "genus": "Mime Pokémon",
        "identifier": "mime-jr",
        "evolution_chain": 57,
        "color": "pink",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 14,
        "type2": 18,
        "flavor_text": "It does its absolute best to mimic the\nmovements and expressions of its opponents,\nbut it’s still not very good at it.",
        "has_alt_form": false,
        "id": 439
    },
    {
        "name": "Happiny",
        "genus": "Playhouse Pokémon",
        "identifier": "happiny",
        "evolution_chain": 51,
        "color": "pink",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Usually it’s a well-behaved Pokémon, but if you\ntake its round rock away, it will cry and fuss\nand throw a big old tantrum.",
        "has_alt_form": false,
        "id": 440
    },
    {
        "name": "Chatot",
        "genus": "Music Note Pokémon",
        "identifier": "chatot",
        "evolution_chain": 228,
        "color": "black",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "It can learn and speak human words. If they gather,\nthey all learn the same saying.",
        "has_alt_form": false,
        "id": 441
    },
    {
        "name": "Spiritomb",
        "genus": "Forbidden Pokémon",
        "identifier": "spiritomb",
        "evolution_chain": 229,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 8,
        "type2": 17,
        "flavor_text": "It was bound to a fissure in an odd keystone as\npunishment for misdeeds 500 years ago.",
        "has_alt_form": false,
        "id": 442
    },
    {
        "name": "Gible",
        "genus": "Land Shark Pokémon",
        "identifier": "gible",
        "evolution_chain": 230,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 16,
        "type2": 5,
        "flavor_text": "It reacts to anything that moves—flies right at it\nand bites it. Sometimes it injures itself, but it\ndoesn’t care too much.",
        "has_alt_form": false,
        "id": 443
    },
    {
        "name": "Gabite",
        "genus": "Cave Pokémon",
        "identifier": "gabite",
        "evolution_chain": 230,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 443,
        "type1": 16,
        "type2": 5,
        "flavor_text": "It loves shiny things. When it finds a Sableye\ntrying to catch a Carbink, Gabite becomes\nfuriously angry and attacks the Sableye.",
        "has_alt_form": false,
        "id": 444
    },
    {
        "name": "Garchomp",
        "genus": "Mach Pokémon",
        "identifier": "garchomp",
        "evolution_chain": 230,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 444,
        "type1": 16,
        "type2": 5,
        "flavor_text": "It flies at the speed of sound while searching\nfor prey, and it has midair battles with\nSalamence as the two compete for food.",
        "has_alt_form": false,
        "id": 445
    },
    {
        "name": "Munchlax",
        "genus": "Big Eater Pokémon",
        "identifier": "munchlax",
        "evolution_chain": 72,
        "color": "black",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It hides food under its long fur, but it\nsometimes forgets about it and causes\na stinky disturbance.",
        "has_alt_form": false,
        "id": 446
    },
    {
        "name": "Riolu",
        "genus": "Emanation Pokémon",
        "identifier": "riolu",
        "evolution_chain": 232,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "It knows how people and Pokémon feel by\nlooking at their auras. It doesn’t approach\ndangerous opponents.",
        "has_alt_form": false,
        "id": 447
    },
    {
        "name": "Lucario",
        "genus": "Aura Pokémon",
        "identifier": "lucario",
        "evolution_chain": 232,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 447,
        "type1": 2,
        "type2": 9,
        "flavor_text": "It concentrates its mental energy and fires off\nmysterious waves called auras, which can crush\nboulders of large size to dust.",
        "has_alt_form": false,
        "id": 448
    },
    {
        "name": "Hippopotas",
        "genus": "Hippo Pokémon",
        "identifier": "hippopotas",
        "evolution_chain": 233,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "It enshrouds itself with sand to protect itself from\ngerms. It does not enjoy getting wet.",
        "has_alt_form": false,
        "id": 449
    },
    {
        "name": "Hippowdon",
        "genus": "Heavyweight Pokémon",
        "identifier": "hippowdon",
        "evolution_chain": 233,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 449,
        "type1": 5,
        "type2": null,
        "flavor_text": "It blasts internally stored sand from ports on its\nbody to create a towering twister for attack.",
        "has_alt_form": false,
        "id": 450
    },
    {
        "name": "Skorupi",
        "genus": "Scorpion Pokémon",
        "identifier": "skorupi",
        "evolution_chain": 234,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 4,
        "type2": 7,
        "flavor_text": "It burrows under the sand to lie in wait for prey.\nIts tail claws can inject its prey with a\nsavage poison.",
        "has_alt_form": false,
        "id": 451
    },
    {
        "name": "Drapion",
        "genus": "Ogre Scorpion Pokémon",
        "identifier": "drapion",
        "evolution_chain": 234,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 451,
        "type1": 4,
        "type2": 17,
        "flavor_text": "It has the power in its clawed arms to make scrap\nof a car. The tips of its claws release poison.",
        "has_alt_form": false,
        "id": 452
    },
    {
        "name": "Croagunk",
        "genus": "Toxic Mouth Pokémon",
        "identifier": "croagunk",
        "evolution_chain": 235,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 4,
        "type2": 2,
        "flavor_text": "Inflating its poison sacs, it fills the area with an odd\nsound and hits flinching opponents with a\npoison jab.",
        "has_alt_form": false,
        "id": 453
    },
    {
        "name": "Toxicroak",
        "genus": "Toxic Mouth Pokémon",
        "identifier": "toxicroak",
        "evolution_chain": 235,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 453,
        "type1": 4,
        "type2": 2,
        "flavor_text": "Its knuckle claws secrete a toxin so vile that even a\nscratch could prove fatal.",
        "has_alt_form": false,
        "id": 454
    },
    {
        "name": "Carnivine",
        "genus": "Bug Catcher Pokémon",
        "identifier": "carnivine",
        "evolution_chain": 236,
        "color": "green",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "It binds itself to trees in marshes. It attracts prey\nwith its sweet-smelling drool and gulps them down.",
        "has_alt_form": false,
        "id": 455
    },
    {
        "name": "Finneon",
        "genus": "Wing Fish Pokémon",
        "identifier": "finneon",
        "evolution_chain": 237,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "When night falls, their pink patterns begin to\nshine. They’re popular with divers, so there are\nresorts that feed them to keep them close.",
        "has_alt_form": false,
        "id": 456
    },
    {
        "name": "Lumineon",
        "genus": "Neon Pokémon",
        "identifier": "lumineon",
        "evolution_chain": 237,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 456,
        "type1": 11,
        "type2": null,
        "flavor_text": "Deep down at the bottom of the ocean, prey is\nscarce. Lumineon get into fierce disputes with\nLanturn over food.",
        "has_alt_form": false,
        "id": 457
    },
    {
        "name": "Mantyke",
        "genus": "Kite Pokémon",
        "identifier": "mantyke",
        "evolution_chain": 116,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": 3,
        "flavor_text": "It’s highly friendly and easily tamed. Tours that\ntake people swimming with Mantyke are a\nsuper-popular beach activity.",
        "has_alt_form": false,
        "id": 458
    },
    {
        "name": "Snover",
        "genus": "Frost Tree Pokémon",
        "identifier": "snover",
        "evolution_chain": 239,
        "color": "white",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 12,
        "type2": 15,
        "flavor_text": "In the spring, it grows berries with the texture of\nfrozen treats around its belly.",
        "has_alt_form": false,
        "id": 459
    },
    {
        "name": "Abomasnow",
        "genus": "Frost Tree Pokémon",
        "identifier": "abomasnow",
        "evolution_chain": 239,
        "color": "white",
        "since_gen": 4,
        "evolves_from": 459,
        "type1": 12,
        "type2": 15,
        "flavor_text": "It lives a quiet life on mountains that are perpetually\ncovered in snow. It hides itself by whipping\nup blizzards.",
        "has_alt_form": false,
        "id": 460
    },
    {
        "name": "Weavile",
        "genus": "Sharp Claw Pokémon",
        "identifier": "weavile",
        "evolution_chain": 109,
        "color": "black",
        "since_gen": 4,
        "evolves_from": 215,
        "type1": 17,
        "type2": 15,
        "flavor_text": "One Weavile will trip a Sandshrew and flip it\nover, and then another Weavile will deal the\nfinishing blow with its sharp claws.",
        "has_alt_form": false,
        "id": 461
    },
    {
        "name": "Magnezone",
        "genus": "Magnet Area Pokémon",
        "identifier": "magnezone",
        "evolution_chain": 34,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": 82,
        "type1": 13,
        "type2": 9,
        "flavor_text": "It uses radar to monitor its territory. Intruders\nare quickly disposed of with a hyper beam.",
        "has_alt_form": false,
        "id": 462
    },
    {
        "name": "Lickilicky",
        "genus": "Licking Pokémon",
        "identifier": "lickilicky",
        "evolution_chain": 48,
        "color": "pink",
        "since_gen": 4,
        "evolves_from": 108,
        "type1": 1,
        "type2": null,
        "flavor_text": "A contest is under way to determine which one\ncan stick its tongue out the farthest. The\ncurrent record is...more than 82 feet.",
        "has_alt_form": false,
        "id": 463
    },
    {
        "name": "Rhyperior",
        "genus": "Drill Pokémon",
        "identifier": "rhyperior",
        "evolution_chain": 50,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": 112,
        "type1": 5,
        "type2": 6,
        "flavor_text": "It puts rocks in holes in its palms and uses its\nmuscles to shoot them. Geodude are shot at\nrare times.",
        "has_alt_form": false,
        "id": 464
    },
    {
        "name": "Tangrowth",
        "genus": "Vine Pokémon",
        "identifier": "tangrowth",
        "evolution_chain": 52,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 114,
        "type1": 12,
        "type2": null,
        "flavor_text": "Its vines grow so profusely that, in the warm\nseason, you can’t even see its eyes.",
        "has_alt_form": false,
        "id": 465
    },
    {
        "name": "Electivire",
        "genus": "Thunderbolt Pokémon",
        "identifier": "electivire",
        "evolution_chain": 60,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": 125,
        "type1": 13,
        "type2": null,
        "flavor_text": "It grips its tail, which spews electricity, and\nthen beats down opponents with the power of\nits electrified fist.",
        "has_alt_form": false,
        "id": 466
    },
    {
        "name": "Magmortar",
        "genus": "Blast Pokémon",
        "identifier": "magmortar",
        "evolution_chain": 61,
        "color": "red",
        "since_gen": 4,
        "evolves_from": 126,
        "type1": 10,
        "type2": null,
        "flavor_text": "There are still quite a few factories that rely on\nthe flames provided by Magmortar to\nprocess metals.",
        "has_alt_form": false,
        "id": 467
    },
    {
        "name": "Togekiss",
        "genus": "Jubilee Pokémon",
        "identifier": "togekiss",
        "evolution_chain": 87,
        "color": "white",
        "since_gen": 4,
        "evolves_from": 176,
        "type1": 18,
        "type2": 3,
        "flavor_text": "It shares many blessings with people who respect\none another’s rights and avoid needless strife.",
        "has_alt_form": false,
        "id": 468
    },
    {
        "name": "Yanmega",
        "genus": "Ogre Darner Pokémon",
        "identifier": "yanmega",
        "evolution_chain": 95,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 193,
        "type1": 7,
        "type2": 3,
        "flavor_text": "This six-legged Pokémon is easily capable of\ntransporting an adult in flight. The wings on its tail\nhelp it stay balanced.",
        "has_alt_form": false,
        "id": 469
    },
    {
        "name": "Leafeon",
        "genus": "Verdant Pokémon",
        "identifier": "leafeon",
        "evolution_chain": 67,
        "color": "green",
        "since_gen": 4,
        "evolves_from": 133,
        "type1": 12,
        "type2": null,
        "flavor_text": "Although it doesn’t like disputes, it will sharpen\nthe leaf on its tail into a blade and fight if it has\nto protect its friends.",
        "has_alt_form": false,
        "id": 470
    },
    {
        "name": "Glaceon",
        "genus": "Fresh Snow Pokémon",
        "identifier": "glaceon",
        "evolution_chain": 67,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": 133,
        "type1": 15,
        "type2": null,
        "flavor_text": "It protects itself by freezing its fur into sharp\nneedles. It can drop its body temperature below\n–75 degrees Fahrenheit.",
        "has_alt_form": false,
        "id": 471
    },
    {
        "name": "Gliscor",
        "genus": "Fang Scorpion Pokémon",
        "identifier": "gliscor",
        "evolution_chain": 104,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": 207,
        "type1": 5,
        "type2": 3,
        "flavor_text": "Its flight is soundless. It uses its lengthy tail to\ncarry off its prey... Then its elongated fangs do\nthe rest.",
        "has_alt_form": false,
        "id": 472
    },
    {
        "name": "Mamoswine",
        "genus": "Twin Tusk Pokémon",
        "identifier": "mamoswine",
        "evolution_chain": 112,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": 221,
        "type1": 15,
        "type2": 5,
        "flavor_text": "Its impressive tusks are made of ice. The population\nthinned when it turned warm after the ice age.",
        "has_alt_form": false,
        "id": 473
    },
    {
        "name": "Porygon-Z",
        "genus": "Virtual Pokémon",
        "identifier": "porygon-z",
        "evolution_chain": 68,
        "color": "red",
        "since_gen": 4,
        "evolves_from": 233,
        "type1": 1,
        "type2": null,
        "flavor_text": "Its behavior is noticeably unstable, which is\napparently due to the incompetence of the\nengineer who updated its programming.",
        "has_alt_form": false,
        "id": 474
    },
    {
        "name": "Gallade",
        "genus": "Blade Pokémon",
        "identifier": "gallade",
        "evolution_chain": 140,
        "color": "white",
        "since_gen": 4,
        "evolves_from": 281,
        "type1": 14,
        "type2": 2,
        "flavor_text": "A master of courtesy and swordsmanship, it fights\nusing extending swords on its elbows.",
        "has_alt_form": false,
        "id": 475
    },
    {
        "name": "Probopass",
        "genus": "Compass Pokémon",
        "identifier": "probopass",
        "evolution_chain": 147,
        "color": "gray",
        "since_gen": 4,
        "evolves_from": 299,
        "type1": 6,
        "type2": 9,
        "flavor_text": "Although it can control its units known as\nMini-Noses, they sometimes get lost and don’t\ncome back.",
        "has_alt_form": false,
        "id": 476
    },
    {
        "name": "Dusknoir",
        "genus": "Gripper Pokémon",
        "identifier": "dusknoir",
        "evolution_chain": 182,
        "color": "black",
        "since_gen": 4,
        "evolves_from": 356,
        "type1": 8,
        "type2": null,
        "flavor_text": "The antenna on its head captures radio waves from\nthe world of spirits that command it to take\npeople there.",
        "has_alt_form": false,
        "id": 477
    },
    {
        "name": "Froslass",
        "genus": "Snow Land Pokémon",
        "identifier": "froslass",
        "evolution_chain": 186,
        "color": "white",
        "since_gen": 4,
        "evolves_from": 361,
        "type1": 15,
        "type2": 8,
        "flavor_text": "It freezes hikers who have come to climb snowy\nmountains and carries them back to its home. It\nonly goes after men it thinks are handsome.",
        "has_alt_form": false,
        "id": 478
    },
    {
        "name": "Rotom",
        "genus": "Plasma Pokémon",
        "identifier": "rotom",
        "evolution_chain": 240,
        "color": "red",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 13,
        "type2": 8,
        "flavor_text": "Its body is composed of plasma. It is known to\ninfiltrate electronic devices and wreak havoc.",
        "has_alt_form": false,
        "id": 479
    },
    {
        "name": "Uxie",
        "genus": "Knowledge Pokémon",
        "identifier": "uxie",
        "evolution_chain": 241,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It is said that its emergence gave humans the\nintelligence to improve their quality of life.",
        "has_alt_form": false,
        "id": 480
    },
    {
        "name": "Mesprit",
        "genus": "Emotion Pokémon",
        "identifier": "mesprit",
        "evolution_chain": 242,
        "color": "pink",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It sleeps at the bottom of a lake. Its spirit is said to\nleave its body to fly on the lake’s surface.",
        "has_alt_form": false,
        "id": 481
    },
    {
        "name": "Azelf",
        "genus": "Willpower Pokémon",
        "identifier": "azelf",
        "evolution_chain": 243,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It is thought that Uxie, Mesprit, and Azelf all came\nfrom the same egg.",
        "has_alt_form": false,
        "id": 482
    },
    {
        "name": "Dialga",
        "genus": "Temporal Pokémon",
        "identifier": "dialga",
        "evolution_chain": 244,
        "color": "white",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 9,
        "type2": 16,
        "flavor_text": "It has the power to control time. It appears in\nSinnoh-region myths as an ancient deity.",
        "has_alt_form": false,
        "id": 483
    },
    {
        "name": "Palkia",
        "genus": "Spatial Pokémon",
        "identifier": "palkia",
        "evolution_chain": 245,
        "color": "purple",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": 16,
        "flavor_text": "It has the ability to distort space. It is described as\na deity in Sinnoh-region mythology.",
        "has_alt_form": false,
        "id": 484
    },
    {
        "name": "Heatran",
        "genus": "Lava Dome Pokémon",
        "identifier": "heatran",
        "evolution_chain": 246,
        "color": "brown",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 10,
        "type2": 9,
        "flavor_text": "Boiling blood, like magma, circulates through its\nbody. It makes its dwelling place in volcanic caves.",
        "has_alt_form": false,
        "id": 485
    },
    {
        "name": "Regigigas",
        "genus": "Colossal Pokémon",
        "identifier": "regigigas",
        "evolution_chain": 247,
        "color": "white",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "There is an enduring legend that states this\nPokémon towed continents with ropes.",
        "has_alt_form": false,
        "id": 486
    },
    {
        "name": "Giratina",
        "genus": "Renegade Pokémon",
        "identifier": "giratina",
        "evolution_chain": 248,
        "color": "black",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 8,
        "type2": 16,
        "flavor_text": "It was banished for its violence. It silently gazed\nupon the old world from the Distortion World.",
        "has_alt_form": true,
        "id": 487
    },
    {
        "name": "Cresselia",
        "genus": "Lunar Pokémon",
        "identifier": "cresselia",
        "evolution_chain": 249,
        "color": "yellow",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Those who sleep holding Cresselia’s feather are\nassured of joyful dreams. It is said to represent\nthe crescent moon.",
        "has_alt_form": false,
        "id": 488
    },
    {
        "name": "Phione",
        "genus": "Sea Drifter Pokémon",
        "identifier": "phione",
        "evolution_chain": 250,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It drifts in warm seas. It always returns to where it\nwas born, no matter how far it may have drifted.",
        "has_alt_form": false,
        "id": 489
    },
    {
        "name": "Manaphy",
        "genus": "Seafaring Pokémon",
        "identifier": "manaphy",
        "evolution_chain": 250,
        "color": "blue",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It starts its life with a wondrous power that permits\nit to bond with any kind of Pokémon.",
        "has_alt_form": false,
        "id": 490
    },
    {
        "name": "Darkrai",
        "genus": "Pitch-Black Pokémon",
        "identifier": "darkrai",
        "evolution_chain": 252,
        "color": "black",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 17,
        "type2": null,
        "flavor_text": "It can lull people to sleep and make them dream.\nIt is active during nights of the new moon.",
        "has_alt_form": false,
        "id": 491
    },
    {
        "name": "Shaymin",
        "genus": "Gratitude Pokémon",
        "identifier": "shaymin",
        "evolution_chain": 253,
        "color": "green",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "The blooming of Gracidea flowers confers the\npower of flight upon it. Feelings of gratitude are\nthe message it delivers.",
        "has_alt_form": true,
        "id": 492
    },
    {
        "name": "Arceus",
        "genus": "Alpha Pokémon",
        "identifier": "arceus",
        "evolution_chain": 254,
        "color": "white",
        "since_gen": 4,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It is told in mythology that this Pokémon was born\nbefore the universe even existed.",
        "has_alt_form": true,
        "id": 493
    },
    {
        "name": "Victini",
        "genus": "Victory Pokémon",
        "identifier": "victini",
        "evolution_chain": 255,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": 10,
        "flavor_text": "When it shares the infinite energy it creates,\nthat being’s entire body will be overflowing\nwith power.",
        "has_alt_form": false,
        "id": 494
    },
    {
        "name": "Snivy",
        "genus": "Grass Snake Pokémon",
        "identifier": "snivy",
        "evolution_chain": 256,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "They photosynthesize by bathing their tails in\nsunlight. When they are not feeling well, their\ntails droop.",
        "has_alt_form": false,
        "id": 495
    },
    {
        "name": "Servine",
        "genus": "Grass Snake Pokémon",
        "identifier": "servine",
        "evolution_chain": 256,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 495,
        "type1": 12,
        "type2": null,
        "flavor_text": "When it gets dirty, its leaves can’t be used in\nphotosynthesis, so it always keeps itself clean.",
        "has_alt_form": false,
        "id": 496
    },
    {
        "name": "Serperior",
        "genus": "Regal Pokémon",
        "identifier": "serperior",
        "evolution_chain": 256,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 496,
        "type1": 12,
        "type2": null,
        "flavor_text": "It can stop its opponents’ movements with just a\nglare. It takes in solar energy and boosts\nit internally.",
        "has_alt_form": false,
        "id": 497
    },
    {
        "name": "Tepig",
        "genus": "Fire Pig Pokémon",
        "identifier": "tepig",
        "evolution_chain": 257,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "It loves to eat roasted berries, but sometimes it\ngets too excited and burns them to a crisp.",
        "has_alt_form": false,
        "id": 498
    },
    {
        "name": "Pignite",
        "genus": "Fire Pig Pokémon",
        "identifier": "pignite",
        "evolution_chain": 257,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 498,
        "type1": 10,
        "type2": 2,
        "flavor_text": "When its internal fire flares up, its movements grow\nsharper and faster. When in trouble, it emits smoke.",
        "has_alt_form": false,
        "id": 499
    },
    {
        "name": "Emboar",
        "genus": "Mega Fire Pig Pokémon",
        "identifier": "emboar",
        "evolution_chain": 257,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 499,
        "type1": 10,
        "type2": 2,
        "flavor_text": "It has mastered fast and powerful fighting moves.\nIt grows a beard of fire.",
        "has_alt_form": false,
        "id": 500
    },
    {
        "name": "Oshawott",
        "genus": "Sea Otter Pokémon",
        "identifier": "oshawott",
        "evolution_chain": 258,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It fights using the scalchop on its stomach.\nIn response to an attack, it retaliates immediately\nby slashing.",
        "has_alt_form": false,
        "id": 501
    },
    {
        "name": "Dewott",
        "genus": "Discipline Pokémon",
        "identifier": "dewott",
        "evolution_chain": 258,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 501,
        "type1": 11,
        "type2": null,
        "flavor_text": "As a result of strict training, each Dewott learns\ndifferent forms for using the scalchops.",
        "has_alt_form": false,
        "id": 502
    },
    {
        "name": "Samurott",
        "genus": "Formidable Pokémon",
        "identifier": "samurott",
        "evolution_chain": 258,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 502,
        "type1": 11,
        "type2": null,
        "flavor_text": "One swing of the sword incorporated in its armor\ncan fell an opponent. A simple glare from one of\nthem quiets everybody.",
        "has_alt_form": false,
        "id": 503
    },
    {
        "name": "Patrat",
        "genus": "Scout Pokémon",
        "identifier": "patrat",
        "evolution_chain": 259,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Extremely cautious, one of them will always be on\nthe lookout, but it won’t notice a foe coming\nfrom behind.",
        "has_alt_form": false,
        "id": 504
    },
    {
        "name": "Watchog",
        "genus": "Lookout Pokémon",
        "identifier": "watchog",
        "evolution_chain": 259,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": 504,
        "type1": 1,
        "type2": null,
        "flavor_text": "When they see an enemy, their tails stand high,\nand they spit the seeds of berries stored in their\ncheek pouches.",
        "has_alt_form": false,
        "id": 505
    },
    {
        "name": "Lillipup",
        "genus": "Puppy Pokémon",
        "identifier": "lillipup",
        "evolution_chain": 260,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "This Pokémon has excellent judgment.\nIf it decides it can’t defeat an opponent,\nit immediately turns tail and vamooses.",
        "has_alt_form": false,
        "id": 506
    },
    {
        "name": "Herdier",
        "genus": "Loyal Dog Pokémon",
        "identifier": "herdier",
        "evolution_chain": 260,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 506,
        "type1": 1,
        "type2": null,
        "flavor_text": "The longer its black fur grows, the harder and\nmore impervious it gets. Claws and fangs can’t\neasily penetrate it.",
        "has_alt_form": false,
        "id": 507
    },
    {
        "name": "Stoutland",
        "genus": "Big-Hearted Pokémon",
        "identifier": "stoutland",
        "evolution_chain": 260,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 507,
        "type1": 1,
        "type2": null,
        "flavor_text": "It pays no mind to the cold, thanks to its long\nwarm coat. Stoutland in Alola look a\nlittle uncomfortable.",
        "has_alt_form": false,
        "id": 508
    },
    {
        "name": "Purrloin",
        "genus": "Devious Pokémon",
        "identifier": "purrloin",
        "evolution_chain": 261,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 17,
        "type2": null,
        "flavor_text": "They steal from people for fun, but their victims\ncan’t help but forgive them. Their deceptively cute\nact is perfect.",
        "has_alt_form": false,
        "id": 509
    },
    {
        "name": "Liepard",
        "genus": "Cruel Pokémon",
        "identifier": "liepard",
        "evolution_chain": 261,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": 509,
        "type1": 17,
        "type2": null,
        "flavor_text": "Stealthily, it sneaks up on its target, striking from\nbehind before its victim has a chance to react.",
        "has_alt_form": false,
        "id": 510
    },
    {
        "name": "Pansage",
        "genus": "Grass Monkey Pokémon",
        "identifier": "pansage",
        "evolution_chain": 262,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "It’s good at finding berries and gathers them from\nall over. It’s kind enough to share them\nwith friends.",
        "has_alt_form": false,
        "id": 511
    },
    {
        "name": "Simisage",
        "genus": "Thorn Monkey Pokémon",
        "identifier": "simisage",
        "evolution_chain": 262,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 511,
        "type1": 12,
        "type2": null,
        "flavor_text": "Ill tempered, it fights by swinging its barbed tail\naround wildly. The leaf growing on its head is\nvery bitter.",
        "has_alt_form": false,
        "id": 512
    },
    {
        "name": "Pansear",
        "genus": "High Temp Pokémon",
        "identifier": "pansear",
        "evolution_chain": 263,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "This Pokémon lives in caves in volcanoes.\nThe fire within the tuft on its head can reach\n600 degrees Fahrenheit.",
        "has_alt_form": false,
        "id": 513
    },
    {
        "name": "Simisear",
        "genus": "Ember Pokémon",
        "identifier": "simisear",
        "evolution_chain": 263,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 513,
        "type1": 10,
        "type2": null,
        "flavor_text": "When it gets excited, embers rise from its head\nand tail and it gets hot. For some reason, it\nloves sweets.",
        "has_alt_form": false,
        "id": 514
    },
    {
        "name": "Panpour",
        "genus": "Spray Pokémon",
        "identifier": "panpour",
        "evolution_chain": 264,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "The water stored inside the tuft on its head is full of\nnutrients. Plants that receive its water grow large.",
        "has_alt_form": false,
        "id": 515
    },
    {
        "name": "Simipour",
        "genus": "Geyser Pokémon",
        "identifier": "simipour",
        "evolution_chain": 264,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 515,
        "type1": 11,
        "type2": null,
        "flavor_text": "It prefers places with clean water. When its tuft runs\nlow, it replenishes it by siphoning up water with\nits tail.",
        "has_alt_form": false,
        "id": 516
    },
    {
        "name": "Munna",
        "genus": "Dream Eater Pokémon",
        "identifier": "munna",
        "evolution_chain": 265,
        "color": "pink",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It eats the dreams of people and Pokémon. When it\neats a pleasant dream, it expels pink-colored mist.",
        "has_alt_form": false,
        "id": 517
    },
    {
        "name": "Musharna",
        "genus": "Drowsing Pokémon",
        "identifier": "musharna",
        "evolution_chain": 265,
        "color": "pink",
        "since_gen": 5,
        "evolves_from": 517,
        "type1": 14,
        "type2": null,
        "flavor_text": "The dream mist coming from its forehead changes\ninto many different colors depending on the dream\nthat was eaten.",
        "has_alt_form": false,
        "id": 518
    },
    {
        "name": "Pidove",
        "genus": "Tiny Pigeon Pokémon",
        "identifier": "pidove",
        "evolution_chain": 266,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "These Pokémon live in cities. They are accustomed\nto people. Flocks often gather in parks and plazas.",
        "has_alt_form": false,
        "id": 519
    },
    {
        "name": "Tranquill",
        "genus": "Wild Pigeon Pokémon",
        "identifier": "tranquill",
        "evolution_chain": 266,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 519,
        "type1": 1,
        "type2": 3,
        "flavor_text": "No matter where in the world it goes, it knows\nwhere its nest is, so it never gets separated from\nits Trainer.",
        "has_alt_form": false,
        "id": 520
    },
    {
        "name": "Unfezant",
        "genus": "Proud Pokémon",
        "identifier": "unfezant",
        "evolution_chain": 266,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 520,
        "type1": 1,
        "type2": 3,
        "flavor_text": "Males have plumage on their heads. They will never\nlet themselves feel close to anyone other than\ntheir Trainers.",
        "has_alt_form": false,
        "id": 521
    },
    {
        "name": "Blitzle",
        "genus": "Electrified Pokémon",
        "identifier": "blitzle",
        "evolution_chain": 267,
        "color": "black",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Its mane shines when it discharges electricity.\nThey use the frequency and rhythm of these flashes\nto communicate.",
        "has_alt_form": false,
        "id": 522
    },
    {
        "name": "Zebstrika",
        "genus": "Thunderbolt Pokémon",
        "identifier": "zebstrika",
        "evolution_chain": 267,
        "color": "black",
        "since_gen": 5,
        "evolves_from": 522,
        "type1": 13,
        "type2": null,
        "flavor_text": "They have lightning-like movements.\nWhen Zebstrika run at full speed, the sound of\nthunder reverberates.",
        "has_alt_form": false,
        "id": 523
    },
    {
        "name": "Roggenrola",
        "genus": "Mantle Pokémon",
        "identifier": "roggenrola",
        "evolution_chain": 268,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 6,
        "type2": null,
        "flavor_text": "The hexagonal hole is its ear. Deep in that ear is\nan energy core, so if you stick your hand in\nthere, Roggenrola will be very angry!",
        "has_alt_form": false,
        "id": 524
    },
    {
        "name": "Boldore",
        "genus": "Ore Pokémon",
        "identifier": "boldore",
        "evolution_chain": 268,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 524,
        "type1": 6,
        "type2": null,
        "flavor_text": "The energy overflowing from its body has\nturned into orange crystals that are hard\nenough to smash diamonds.",
        "has_alt_form": false,
        "id": 525
    },
    {
        "name": "Gigalith",
        "genus": "Compressed Pokémon",
        "identifier": "gigalith",
        "evolution_chain": 268,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 525,
        "type1": 6,
        "type2": null,
        "flavor_text": "When it fires off energy with all its might, the\npower creates countless fissures on its body.",
        "has_alt_form": false,
        "id": 526
    },
    {
        "name": "Woobat",
        "genus": "Bat Pokémon",
        "identifier": "woobat",
        "evolution_chain": 269,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": 3,
        "flavor_text": "The heart-shaped mark left on a body after a\nWoobat has been attached to it is said to bring\ngood fortune.",
        "has_alt_form": false,
        "id": 527
    },
    {
        "name": "Swoobat",
        "genus": "Courting Pokémon",
        "identifier": "swoobat",
        "evolution_chain": 269,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 527,
        "type1": 14,
        "type2": 3,
        "flavor_text": "Anyone who comes into contact with the ultrasonic\nwaves emitted by a courting male experiences a\npositive mood shift.",
        "has_alt_form": false,
        "id": 528
    },
    {
        "name": "Drilbur",
        "genus": "Mole Pokémon",
        "identifier": "drilbur",
        "evolution_chain": 270,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "By spinning its body, it can dig straight through the\nground at a speed of 30 mph.",
        "has_alt_form": false,
        "id": 529
    },
    {
        "name": "Excadrill",
        "genus": "Subterrene Pokémon",
        "identifier": "excadrill",
        "evolution_chain": 270,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 529,
        "type1": 5,
        "type2": 9,
        "flavor_text": "More than 300 feet below the surface, they build\nmazelike nests. Their activity can be destructive to\nsubway tunnels.",
        "has_alt_form": false,
        "id": 530
    },
    {
        "name": "Audino",
        "genus": "Hearing Pokémon",
        "identifier": "audino",
        "evolution_chain": 271,
        "color": "pink",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It touches others with the feelers on its ears, using\nthe sound of their heartbeats to tell how they\nare feeling.",
        "has_alt_form": false,
        "id": 531
    },
    {
        "name": "Timburr",
        "genus": "Muscular Pokémon",
        "identifier": "timburr",
        "evolution_chain": 272,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "Always carrying squared logs, they help out with\nconstruction. As they grow, they carry bigger logs.",
        "has_alt_form": false,
        "id": 532
    },
    {
        "name": "Gurdurr",
        "genus": "Muscular Pokémon",
        "identifier": "gurdurr",
        "evolution_chain": 272,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 532,
        "type1": 2,
        "type2": null,
        "flavor_text": "This Pokémon is so muscular and strongly built that\neven a group of wrestlers could not make it budge\nan inch.",
        "has_alt_form": false,
        "id": 533
    },
    {
        "name": "Conkeldurr",
        "genus": "Muscular Pokémon",
        "identifier": "conkeldurr",
        "evolution_chain": 272,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": 533,
        "type1": 2,
        "type2": null,
        "flavor_text": "Rather than rely on force, they master moves that\nutilize the centrifugal force of spinning concrete.",
        "has_alt_form": false,
        "id": 534
    },
    {
        "name": "Tympole",
        "genus": "Tadpole Pokémon",
        "identifier": "tympole",
        "evolution_chain": 273,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "By vibrating its cheeks, it emits sound waves\nimperceptible to humans. It uses the rhythm of\nthese sounds to talk.",
        "has_alt_form": false,
        "id": 535
    },
    {
        "name": "Palpitoad",
        "genus": "Vibration Pokémon",
        "identifier": "palpitoad",
        "evolution_chain": 273,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 535,
        "type1": 11,
        "type2": 5,
        "flavor_text": "It lives in the water and on land. It uses its long,\nsticky tongue to immobilize its opponents.",
        "has_alt_form": false,
        "id": 536
    },
    {
        "name": "Seismitoad",
        "genus": "Vibration Pokémon",
        "identifier": "seismitoad",
        "evolution_chain": 273,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 536,
        "type1": 11,
        "type2": 5,
        "flavor_text": "They shoot paralyzing liquid from their head bumps.\nThey use vibration to hurt their opponents.",
        "has_alt_form": false,
        "id": 537
    },
    {
        "name": "Throh",
        "genus": "Judo Pokémon",
        "identifier": "throh",
        "evolution_chain": 274,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "When it encounters a foe bigger than itself, it wants\nto throw it. It changes belts as it gets stronger.",
        "has_alt_form": false,
        "id": 538
    },
    {
        "name": "Sawk",
        "genus": "Karate Pokémon",
        "identifier": "sawk",
        "evolution_chain": 275,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "Tying their belts gets them pumped and makes their\npunches more destructive. Disturbing their training\nangers them.",
        "has_alt_form": false,
        "id": 539
    },
    {
        "name": "Sewaddle",
        "genus": "Sewing Pokémon",
        "identifier": "sewaddle",
        "evolution_chain": 276,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 12,
        "flavor_text": "Since this Pokémon makes its own clothes out of\nleaves, it is a popular mascot for fashion designers.",
        "has_alt_form": false,
        "id": 540
    },
    {
        "name": "Swadloon",
        "genus": "Leaf-Wrapped Pokémon",
        "identifier": "swadloon",
        "evolution_chain": 276,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 540,
        "type1": 7,
        "type2": 12,
        "flavor_text": "It protects itself from the cold by wrapping up in\nleaves. It stays on the move, eating leaves\nin forests.",
        "has_alt_form": false,
        "id": 541
    },
    {
        "name": "Leavanny",
        "genus": "Nurturing Pokémon",
        "identifier": "leavanny",
        "evolution_chain": 276,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": 541,
        "type1": 7,
        "type2": 12,
        "flavor_text": "It keeps its eggs warm with heat from fermenting\nleaves. It also uses leaves to make warm wrappings\nfor Sewaddle.",
        "has_alt_form": false,
        "id": 542
    },
    {
        "name": "Venipede",
        "genus": "Centipede Pokémon",
        "identifier": "venipede",
        "evolution_chain": 277,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 4,
        "flavor_text": "Its bite injects a potent poison, enough to paralyze\nlarge bird Pokémon that try to prey on it.",
        "has_alt_form": false,
        "id": 543
    },
    {
        "name": "Whirlipede",
        "genus": "Curlipede Pokémon",
        "identifier": "whirlipede",
        "evolution_chain": 277,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 543,
        "type1": 7,
        "type2": 4,
        "flavor_text": "It is usually motionless, but when attacked,\nit rotates at high speed and then crashes into\nits opponent.",
        "has_alt_form": false,
        "id": 544
    },
    {
        "name": "Scolipede",
        "genus": "Megapede Pokémon",
        "identifier": "scolipede",
        "evolution_chain": 277,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 544,
        "type1": 7,
        "type2": 4,
        "flavor_text": "With quick movements, it chases down its foes,\nattacking relentlessly with its horns until it prevails.",
        "has_alt_form": false,
        "id": 545
    },
    {
        "name": "Cottonee",
        "genus": "Cotton Puff Pokémon",
        "identifier": "cottonee",
        "evolution_chain": 278,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": 18,
        "flavor_text": "To protect itself, it shoots cotton from its body.\nWhen it gets wet in the rain, its cotton grows\nmoist and heavy, and it can’t move as well.",
        "has_alt_form": false,
        "id": 546
    },
    {
        "name": "Whimsicott",
        "genus": "Windveiled Pokémon",
        "identifier": "whimsicott",
        "evolution_chain": 278,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 546,
        "type1": 12,
        "type2": 18,
        "flavor_text": "This nuisance sneaks into people’s homes,\nwhere it hides important things and scatters\ncotton all over the place.",
        "has_alt_form": false,
        "id": 547
    },
    {
        "name": "Petilil",
        "genus": "Bulb Pokémon",
        "identifier": "petilil",
        "evolution_chain": 279,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Some say if you dry the leaves on its head, boil\nthem down, and drink the infusion, your vigor\nwill return, so Petilil is popular with the elderly.",
        "has_alt_form": false,
        "id": 548
    },
    {
        "name": "Lilligant",
        "genus": "Flowering Pokémon",
        "identifier": "lilligant",
        "evolution_chain": 279,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 548,
        "type1": 12,
        "type2": null,
        "flavor_text": "The fragrance of its flower differs slightly\ndepending on the soil where it grew up.\nSniffing the aroma calms your heart and mind.",
        "has_alt_form": false,
        "id": 549
    },
    {
        "name": "Basculin",
        "genus": "Hostile Pokémon",
        "identifier": "basculin",
        "evolution_chain": 280,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Savage, violent Pokémon, red and blue Basculin\nare always fighting each other over territory.",
        "has_alt_form": true,
        "id": 550
    },
    {
        "name": "Sandile",
        "genus": "Desert Croc Pokémon",
        "identifier": "sandile",
        "evolution_chain": 281,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 5,
        "type2": 17,
        "flavor_text": "Alola, where it’s warm all year round, is a\ncomfortable environment for this Pokémon.\nSometimes you’ll even see it outside of deserts.",
        "has_alt_form": false,
        "id": 551
    },
    {
        "name": "Krokorok",
        "genus": "Desert Croc Pokémon",
        "identifier": "krokorok",
        "evolution_chain": 281,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": 551,
        "type1": 5,
        "type2": 17,
        "flavor_text": "Krokorok really hates it when its body gets\ncold. On nights when the temperature drops,\nit digs deep into the desert sands.",
        "has_alt_form": false,
        "id": 552
    },
    {
        "name": "Krookodile",
        "genus": "Intimidation Pokémon",
        "identifier": "krookodile",
        "evolution_chain": 281,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 552,
        "type1": 5,
        "type2": 17,
        "flavor_text": "When it spots prey, even at a distance of over\n30 miles, it swims through the desert as if it\nwere water, then jumps out and chomps them.",
        "has_alt_form": false,
        "id": 553
    },
    {
        "name": "Darumaka",
        "genus": "Zen Charm Pokémon",
        "identifier": "darumaka",
        "evolution_chain": 282,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "When it sleeps, it pulls its limbs into its\nbody and its internal fire goes down to\n1,100 degrees Fahrenheit.",
        "has_alt_form": false,
        "id": 554
    },
    {
        "name": "Darmanitan",
        "genus": "Blazing Pokémon",
        "identifier": "darmanitan",
        "evolution_chain": 282,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 554,
        "type1": 10,
        "type2": null,
        "flavor_text": "Its internal fire burns at 2,500 degrees Fahrenheit,\nmaking enough power that it can destroy a dump\ntruck with one punch.",
        "has_alt_form": true,
        "id": 555
    },
    {
        "name": "Maractus",
        "genus": "Cactus Pokémon",
        "identifier": "maractus",
        "evolution_chain": 283,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Arid regions are their habitat. They move\nrhythmically, making a sound similar to maracas.",
        "has_alt_form": false,
        "id": 556
    },
    {
        "name": "Dwebble",
        "genus": "Rock Inn Pokémon",
        "identifier": "dwebble",
        "evolution_chain": 284,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 6,
        "flavor_text": "When it finds a stone of a suitable size, it secretes\na liquid from its mouth to open up a hole to\ncrawl into.",
        "has_alt_form": false,
        "id": 557
    },
    {
        "name": "Crustle",
        "genus": "Stone Home Pokémon",
        "identifier": "crustle",
        "evolution_chain": 284,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 557,
        "type1": 7,
        "type2": 6,
        "flavor_text": "Competing for territory, Crustle fight viciously.\nThe one whose boulder is broken is the loser of\nthe battle.",
        "has_alt_form": false,
        "id": 558
    },
    {
        "name": "Scraggy",
        "genus": "Shedding Pokémon",
        "identifier": "scraggy",
        "evolution_chain": 285,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 17,
        "type2": 2,
        "flavor_text": "They move in small groups, walking around lazily.\nAnyone who makes eye contact gets smacked\nwith a headbutt.",
        "has_alt_form": false,
        "id": 559
    },
    {
        "name": "Scrafty",
        "genus": "Hoodlum Pokémon",
        "identifier": "scrafty",
        "evolution_chain": 285,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 559,
        "type1": 17,
        "type2": 2,
        "flavor_text": "This Pokémon may be rude, but it takes very\ngood care of its family, its friends, and its turf.",
        "has_alt_form": false,
        "id": 560
    },
    {
        "name": "Sigilyph",
        "genus": "Avianoid Pokémon",
        "identifier": "sigilyph",
        "evolution_chain": 286,
        "color": "black",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": 3,
        "flavor_text": "The guardians of an ancient city, they always fly\nthe same route while keeping watch for invaders.",
        "has_alt_form": false,
        "id": 561
    },
    {
        "name": "Yamask",
        "genus": "Spirit Pokémon",
        "identifier": "yamask",
        "evolution_chain": 287,
        "color": "black",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 8,
        "type2": null,
        "flavor_text": "Each of them carries a mask that used to be its face\nwhen it was human. Sometimes they look at it\nand cry.",
        "has_alt_form": false,
        "id": 562
    },
    {
        "name": "Cofagrigus",
        "genus": "Coffin Pokémon",
        "identifier": "cofagrigus",
        "evolution_chain": 287,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": 562,
        "type1": 8,
        "type2": null,
        "flavor_text": "Grave robbers who mistake them for real coffins and\nget too close end up trapped inside their bodies.",
        "has_alt_form": false,
        "id": 563
    },
    {
        "name": "Tirtouga",
        "genus": "Prototurtle Pokémon",
        "identifier": "tirtouga",
        "evolution_chain": 288,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": 6,
        "flavor_text": "It was restored from an ancient fossil. Tirtouga\nlived in the sea but came up onto the land to\nsearch for prey.",
        "has_alt_form": false,
        "id": 564
    },
    {
        "name": "Carracosta",
        "genus": "Prototurtle Pokémon",
        "identifier": "carracosta",
        "evolution_chain": 288,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 564,
        "type1": 11,
        "type2": 6,
        "flavor_text": "Its jaws are terrifyingly powerful. It could eat\nOmastar and Omanyte whole and not be\nbothered in the slightest by their shells.",
        "has_alt_form": false,
        "id": 565
    },
    {
        "name": "Archen",
        "genus": "First Bird Pokémon",
        "identifier": "archen",
        "evolution_chain": 289,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 6,
        "type2": 3,
        "flavor_text": "Once thought to be the ancestor of all bird\nPokémon, some of the latest research suggests\nthat may not be the case.",
        "has_alt_form": false,
        "id": 566
    },
    {
        "name": "Archeops",
        "genus": "First Bird Pokémon",
        "identifier": "archeops",
        "evolution_chain": 289,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": 566,
        "type1": 6,
        "type2": 3,
        "flavor_text": "This ancient Pokémon’s plumage is delicate,\nso if anyone other than an experienced\nprofessional tries to restore it, they will fail.",
        "has_alt_form": false,
        "id": 567
    },
    {
        "name": "Trubbish",
        "genus": "Trash Bag Pokémon",
        "identifier": "trubbish",
        "evolution_chain": 290,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "Poisonous gas leaks out of it when it breathes.\nMuk that catch a whiff of that stench will\ncome drooling.",
        "has_alt_form": false,
        "id": 568
    },
    {
        "name": "Garbodor",
        "genus": "Trash Heap Pokémon",
        "identifier": "garbodor",
        "evolution_chain": 290,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 568,
        "type1": 4,
        "type2": null,
        "flavor_text": "It locks opponents in place with its left hand,\nimmobilizing them by entirely dousing their\nbodies with poisonous liquid.",
        "has_alt_form": false,
        "id": 569
    },
    {
        "name": "Zorua",
        "genus": "Tricky Fox Pokémon",
        "identifier": "zorua",
        "evolution_chain": 291,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 17,
        "type2": null,
        "flavor_text": "This Pokémon has a cowardly disposition, so\nwhen it’s not around friends, it basically\nalways stays transformed as something else.",
        "has_alt_form": false,
        "id": 570
    },
    {
        "name": "Zoroark",
        "genus": "Illusion Fox Pokémon",
        "identifier": "zoroark",
        "evolution_chain": 291,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 570,
        "type1": 17,
        "type2": null,
        "flavor_text": "It doesn’t just transform itself—it also has the\npower to make hundreds of people see\nits illusions.",
        "has_alt_form": false,
        "id": 571
    },
    {
        "name": "Minccino",
        "genus": "Chinchilla Pokémon",
        "identifier": "minccino",
        "evolution_chain": 292,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "A clean freak that will not allow even the\nslightest mess, it uses its tail like a mop to\nthoroughly clean any and all filth.",
        "has_alt_form": false,
        "id": 572
    },
    {
        "name": "Cinccino",
        "genus": "Scarf Pokémon",
        "identifier": "cinccino",
        "evolution_chain": 292,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 572,
        "type1": 1,
        "type2": null,
        "flavor_text": "The white parts of its coat are covered in an oil\nsecreted from its body, so this Pokémon can\nslide right away from its enemies’ attacks.",
        "has_alt_form": false,
        "id": 573
    },
    {
        "name": "Gothita",
        "genus": "Fixation Pokémon",
        "identifier": "gothita",
        "evolution_chain": 293,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "They intently observe both Trainers and Pokémon.\nApparently, they are looking at something that only\nGothita can see.",
        "has_alt_form": false,
        "id": 574
    },
    {
        "name": "Gothorita",
        "genus": "Manipulate Pokémon",
        "identifier": "gothorita",
        "evolution_chain": 293,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": 574,
        "type1": 14,
        "type2": null,
        "flavor_text": "According to many old tales, it creates friends for\nitself by controlling sleeping children on\nstarry nights.",
        "has_alt_form": false,
        "id": 575
    },
    {
        "name": "Gothitelle",
        "genus": "Astral Body Pokémon",
        "identifier": "gothitelle",
        "evolution_chain": 293,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": 575,
        "type1": 14,
        "type2": null,
        "flavor_text": "They can predict the future from the placement and\nmovement of the stars. They can see Trainers’\nlife spans.",
        "has_alt_form": false,
        "id": 576
    },
    {
        "name": "Solosis",
        "genus": "Cell Pokémon",
        "identifier": "solosis",
        "evolution_chain": 294,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "They drive away attackers by unleashing psychic\npower. They can use telepathy to talk with others.",
        "has_alt_form": false,
        "id": 577
    },
    {
        "name": "Duosion",
        "genus": "Mitosis Pokémon",
        "identifier": "duosion",
        "evolution_chain": 294,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 577,
        "type1": 14,
        "type2": null,
        "flavor_text": "When their two divided brains think the same\nthoughts, their psychic power is maximized.",
        "has_alt_form": false,
        "id": 578
    },
    {
        "name": "Reuniclus",
        "genus": "Multiplying Pokémon",
        "identifier": "reuniclus",
        "evolution_chain": 294,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 578,
        "type1": 14,
        "type2": null,
        "flavor_text": "When Reuniclus shake hands, a network forms\nbetween their brains, increasing their\npsychic power.",
        "has_alt_form": false,
        "id": 579
    },
    {
        "name": "Ducklett",
        "genus": "Water Bird Pokémon",
        "identifier": "ducklett",
        "evolution_chain": 295,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": 3,
        "flavor_text": "They are better at swimming than flying, and they\nhappily eat their favorite food, peat moss, as they\ndive underwater.",
        "has_alt_form": false,
        "id": 580
    },
    {
        "name": "Swanna",
        "genus": "White Bird Pokémon",
        "identifier": "swanna",
        "evolution_chain": 295,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 580,
        "type1": 11,
        "type2": 3,
        "flavor_text": "Swanna start to dance at dusk. The one dancing in\nthe middle is the leader of the flock.",
        "has_alt_form": false,
        "id": 581
    },
    {
        "name": "Vanillite",
        "genus": "Fresh Snow Pokémon",
        "identifier": "vanillite",
        "evolution_chain": 296,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 15,
        "type2": null,
        "flavor_text": "It exhales cold air that is at –58 degrees\nFahrenheit. When it’s in a warm place, it shrinks\nlittle by little.",
        "has_alt_form": false,
        "id": 582
    },
    {
        "name": "Vanillish",
        "genus": "Icy Snow Pokémon",
        "identifier": "vanillish",
        "evolution_chain": 296,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 582,
        "type1": 15,
        "type2": null,
        "flavor_text": "It sprays its enemies with grains of ice to freeze\nthem. Most Vanillish in Alola are smaller\nthan average.",
        "has_alt_form": false,
        "id": 583
    },
    {
        "name": "Vanilluxe",
        "genus": "Snowstorm Pokémon",
        "identifier": "vanilluxe",
        "evolution_chain": 296,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 583,
        "type1": 15,
        "type2": null,
        "flavor_text": "It blasts blizzards from its two mouths. It can\ncreate snow anywhere, so it gets a lot of love\nfrom skiers and snowboarders.",
        "has_alt_form": false,
        "id": 584
    },
    {
        "name": "Deerling",
        "genus": "Season Pokémon",
        "identifier": "deerling",
        "evolution_chain": 297,
        "color": "pink",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": 12,
        "flavor_text": "The turning of the seasons changes the color and\nscent of this Pokémon’s fur. People use it to mark\nthe seasons.",
        "has_alt_form": true,
        "id": 585
    },
    {
        "name": "Sawsbuck",
        "genus": "Season Pokémon",
        "identifier": "sawsbuck",
        "evolution_chain": 297,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": 585,
        "type1": 1,
        "type2": 12,
        "flavor_text": "They migrate according to the seasons, so some\npeople call Sawsbuck the harbingers of spring.",
        "has_alt_form": true,
        "id": 586
    },
    {
        "name": "Emolga",
        "genus": "Sky Squirrel Pokémon",
        "identifier": "emolga",
        "evolution_chain": 298,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 13,
        "type2": 3,
        "flavor_text": "They store up electricity to fly through the air.\nWhen thunder cracks at night, sometimes there\nare almost enough of them to blot out the sky.",
        "has_alt_form": false,
        "id": 587
    },
    {
        "name": "Karrablast",
        "genus": "Clamping Pokémon",
        "identifier": "karrablast",
        "evolution_chain": 299,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "For some reason they evolve when they receive\nelectrical energy while they are attacking Shelmet.",
        "has_alt_form": false,
        "id": 588
    },
    {
        "name": "Escavalier",
        "genus": "Cavalry Pokémon",
        "identifier": "escavalier",
        "evolution_chain": 299,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 588,
        "type1": 7,
        "type2": 9,
        "flavor_text": "These Pokémon evolve by wearing the shell\ncovering of a Shelmet. The steel armor protects\ntheir whole body.",
        "has_alt_form": false,
        "id": 589
    },
    {
        "name": "Foongus",
        "genus": "Mushroom Pokémon",
        "identifier": "foongus",
        "evolution_chain": 300,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": 4,
        "flavor_text": "It lures Pokémon with its pattern that looks just like\na Poké Ball, then releases poison spores.",
        "has_alt_form": false,
        "id": 590
    },
    {
        "name": "Amoonguss",
        "genus": "Mushroom Pokémon",
        "identifier": "amoonguss",
        "evolution_chain": 300,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 590,
        "type1": 12,
        "type2": 4,
        "flavor_text": "It lures prey close by dancing and waving its\narm caps, which resemble Poké Balls, in a\nswaying motion.",
        "has_alt_form": false,
        "id": 591
    },
    {
        "name": "Frillish",
        "genus": "Floating Pokémon",
        "identifier": "frillish",
        "evolution_chain": 301,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": 8,
        "flavor_text": "It wraps its veillike arms and legs around prey\nswimming by and drags them down to the\ndepths of the ocean.",
        "has_alt_form": false,
        "id": 592
    },
    {
        "name": "Jellicent",
        "genus": "Floating Pokémon",
        "identifier": "jellicent",
        "evolution_chain": 301,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 592,
        "type1": 11,
        "type2": 8,
        "flavor_text": "Jellicent is always hanging around fancy cruise\nships and tankers, hoping to drag away its prey.",
        "has_alt_form": false,
        "id": 593
    },
    {
        "name": "Alomomola",
        "genus": "Caring Pokémon",
        "identifier": "alomomola",
        "evolution_chain": 302,
        "color": "pink",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Fishermen take them along on long voyages,\nbecause if you have an Alomomola with you,\nthere’ll be no need for a doctor or medicine.",
        "has_alt_form": false,
        "id": 594
    },
    {
        "name": "Joltik",
        "genus": "Attaching Pokémon",
        "identifier": "joltik",
        "evolution_chain": 303,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 13,
        "flavor_text": "They attach themselves to large-bodied Pokémon\nand absorb static electricity, which they store in an\nelectric pouch.",
        "has_alt_form": false,
        "id": 595
    },
    {
        "name": "Galvantula",
        "genus": "EleSpider Pokémon",
        "identifier": "galvantula",
        "evolution_chain": 303,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": 595,
        "type1": 7,
        "type2": 13,
        "flavor_text": "When attacked, they create an electric barrier by\nspitting out many electrically charged threads.",
        "has_alt_form": false,
        "id": 596
    },
    {
        "name": "Ferroseed",
        "genus": "Thorn Seed Pokémon",
        "identifier": "ferroseed",
        "evolution_chain": 304,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": 9,
        "flavor_text": "It absorbs the iron it finds in the rock while clinging\nto the ceiling. It shoots spikes when in danger.",
        "has_alt_form": false,
        "id": 597
    },
    {
        "name": "Ferrothorn",
        "genus": "Thorn Pod Pokémon",
        "identifier": "ferrothorn",
        "evolution_chain": 304,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 597,
        "type1": 12,
        "type2": 9,
        "flavor_text": "They attach themselves to cave ceilings, firing steel\nspikes at targets passing beneath them.",
        "has_alt_form": false,
        "id": 598
    },
    {
        "name": "Klink",
        "genus": "Gear Pokémon",
        "identifier": "klink",
        "evolution_chain": 305,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 9,
        "type2": null,
        "flavor_text": "The two minigears that mesh together are\npredetermined. Each will rebound from other\nminigears without meshing.",
        "has_alt_form": false,
        "id": 599
    },
    {
        "name": "Klang",
        "genus": "Gear Pokémon",
        "identifier": "klang",
        "evolution_chain": 305,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 599,
        "type1": 9,
        "type2": null,
        "flavor_text": "A minigear and big gear comprise its body. If the\nminigear it launches at a foe doesn’t return, it\nwill die.",
        "has_alt_form": false,
        "id": 600
    },
    {
        "name": "Klinklang",
        "genus": "Gear Pokémon",
        "identifier": "klinklang",
        "evolution_chain": 305,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": 600,
        "type1": 9,
        "type2": null,
        "flavor_text": "Its red core functions as an energy tank. It fires the\ncharged energy through its spikes into an area.",
        "has_alt_form": false,
        "id": 601
    },
    {
        "name": "Tynamo",
        "genus": "EleFish Pokémon",
        "identifier": "tynamo",
        "evolution_chain": 306,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "One alone can emit only a trickle of electricity,\nso a group of them gathers to unleash a powerful\nelectric shock.",
        "has_alt_form": false,
        "id": 602
    },
    {
        "name": "Eelektrik",
        "genus": "EleFish Pokémon",
        "identifier": "eelektrik",
        "evolution_chain": 306,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 602,
        "type1": 13,
        "type2": null,
        "flavor_text": "These Pokémon have a big appetite. When they\nspot their prey, they attack it and paralyze it\nwith electricity.",
        "has_alt_form": false,
        "id": 603
    },
    {
        "name": "Eelektross",
        "genus": "EleFish Pokémon",
        "identifier": "eelektross",
        "evolution_chain": 306,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 603,
        "type1": 13,
        "type2": null,
        "flavor_text": "They crawl out of the ocean using their arms.\nThey will attack prey on shore and immediately drag\nit into the ocean.",
        "has_alt_form": false,
        "id": 604
    },
    {
        "name": "Elgyem",
        "genus": "Cerebral Pokémon",
        "identifier": "elgyem",
        "evolution_chain": 307,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It controls tremendous psychic power. Most\nreports of alien sightings are actually just\npeople mistaking Elgyem for an alien.",
        "has_alt_form": false,
        "id": 605
    },
    {
        "name": "Beheeyem",
        "genus": "Cerebral Pokémon",
        "identifier": "beheeyem",
        "evolution_chain": 307,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": 605,
        "type1": 14,
        "type2": null,
        "flavor_text": "With its psychic powers, it rewrites its\nopponents’ memories. You, too, may have\nalready had your memories rewritten.",
        "has_alt_form": false,
        "id": 606
    },
    {
        "name": "Litwick",
        "genus": "Candle Pokémon",
        "identifier": "litwick",
        "evolution_chain": 308,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 8,
        "type2": 10,
        "flavor_text": "Litwick shines a light that absorbs the life energy of\npeople and Pokémon, which becomes the fuel that\nit burns.",
        "has_alt_form": false,
        "id": 607
    },
    {
        "name": "Lampent",
        "genus": "Lamp Pokémon",
        "identifier": "lampent",
        "evolution_chain": 308,
        "color": "black",
        "since_gen": 5,
        "evolves_from": 607,
        "type1": 8,
        "type2": 10,
        "flavor_text": "It arrives near the moment of death and steals spirit\nfrom the body.",
        "has_alt_form": false,
        "id": 608
    },
    {
        "name": "Chandelure",
        "genus": "Luring Pokémon",
        "identifier": "chandelure",
        "evolution_chain": 308,
        "color": "black",
        "since_gen": 5,
        "evolves_from": 608,
        "type1": 8,
        "type2": 10,
        "flavor_text": "The spirits burned up in its ominous flame lose their\nway and wander this world forever.",
        "has_alt_form": false,
        "id": 609
    },
    {
        "name": "Axew",
        "genus": "Tusk Pokémon",
        "identifier": "axew",
        "evolution_chain": 309,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 16,
        "type2": null,
        "flavor_text": "They mark their territory by leaving gashes in trees\nwith their tusks. If a tusk breaks, a new one grows\nin quickly.",
        "has_alt_form": false,
        "id": 610
    },
    {
        "name": "Fraxure",
        "genus": "Axe Jaw Pokémon",
        "identifier": "fraxure",
        "evolution_chain": 309,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 610,
        "type1": 16,
        "type2": null,
        "flavor_text": "A broken tusk will not grow back, so it diligently\nsharpens its tusks on river rocks after the end of\na battle.",
        "has_alt_form": false,
        "id": 611
    },
    {
        "name": "Haxorus",
        "genus": "Axe Jaw Pokémon",
        "identifier": "haxorus",
        "evolution_chain": 309,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": 611,
        "type1": 16,
        "type2": null,
        "flavor_text": "Their sturdy tusks will stay sharp even if used to cut\nsteel beams. These Pokémon are covered in\nhard armor.",
        "has_alt_form": false,
        "id": 612
    },
    {
        "name": "Cubchoo",
        "genus": "Chill Pokémon",
        "identifier": "cubchoo",
        "evolution_chain": 310,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 15,
        "type2": null,
        "flavor_text": "Their snot is a barometer of health. When healthy,\ntheir snot is sticky and the power of their ice\nmoves increases.",
        "has_alt_form": false,
        "id": 613
    },
    {
        "name": "Beartic",
        "genus": "Freezing Pokémon",
        "identifier": "beartic",
        "evolution_chain": 310,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 613,
        "type1": 15,
        "type2": null,
        "flavor_text": "It freezes its breath to create fangs and claws of ice\nto fight with. Cold northern areas are its habitat.",
        "has_alt_form": false,
        "id": 614
    },
    {
        "name": "Cryogonal",
        "genus": "Crystallizing Pokémon",
        "identifier": "cryogonal",
        "evolution_chain": 311,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 15,
        "type2": null,
        "flavor_text": "They are composed of ice crystals. They capture\nprey with chains of ice, freezing the prey at\n-148 degrees Fahrenheit.",
        "has_alt_form": false,
        "id": 615
    },
    {
        "name": "Shelmet",
        "genus": "Snail Pokémon",
        "identifier": "shelmet",
        "evolution_chain": 312,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "It evolves when bathed in an electric-like energy\nalong with Karrablast. The reason is still unknown.",
        "has_alt_form": false,
        "id": 616
    },
    {
        "name": "Accelgor",
        "genus": "Shell Out Pokémon",
        "identifier": "accelgor",
        "evolution_chain": 312,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 616,
        "type1": 7,
        "type2": null,
        "flavor_text": "When its body dries out, it weakens. So, to prevent\ndehydration, it wraps itself in many layers of\nthin membrane.",
        "has_alt_form": false,
        "id": 617
    },
    {
        "name": "Stunfisk",
        "genus": "Trap Pokémon",
        "identifier": "stunfisk",
        "evolution_chain": 313,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 5,
        "type2": 13,
        "flavor_text": "It conceals itself in the mud of the seashore.\nThen it waits. When prey touch it, it delivers a jolt\nof electricity.",
        "has_alt_form": false,
        "id": 618
    },
    {
        "name": "Mienfoo",
        "genus": "Martial Arts Pokémon",
        "identifier": "mienfoo",
        "evolution_chain": 314,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "They can often be seen in packs in the morning,\nslowly moving their bodies through a series\nof poses.",
        "has_alt_form": false,
        "id": 619
    },
    {
        "name": "Mienshao",
        "genus": "Martial Arts Pokémon",
        "identifier": "mienshao",
        "evolution_chain": 314,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": 619,
        "type1": 2,
        "type2": null,
        "flavor_text": "It overwhelms its opponents with continuous\nattacks and then slowly stores up power\nbefore delivering the finishing blow.",
        "has_alt_form": false,
        "id": 620
    },
    {
        "name": "Druddigon",
        "genus": "Cave Pokémon",
        "identifier": "druddigon",
        "evolution_chain": 315,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 16,
        "type2": null,
        "flavor_text": "The red skin on its face is harder than rock.\nIn narrow caves, it squares off against its\nenemies and charges face-first right into them.",
        "has_alt_form": false,
        "id": 621
    },
    {
        "name": "Golett",
        "genus": "Automaton Pokémon",
        "identifier": "golett",
        "evolution_chain": 316,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 5,
        "type2": 8,
        "flavor_text": "Its movements are powered by a mysterious\nenergy. It has continued to move since ancient\ntimes, so its power may soon run out.",
        "has_alt_form": false,
        "id": 622
    },
    {
        "name": "Golurk",
        "genus": "Automaton Pokémon",
        "identifier": "golurk",
        "evolution_chain": 316,
        "color": "green",
        "since_gen": 5,
        "evolves_from": 622,
        "type1": 5,
        "type2": 8,
        "flavor_text": "Some say that ancient people invented Golurk\nto serve as a laborer. It follows its master’s\norders faithfully.",
        "has_alt_form": false,
        "id": 623
    },
    {
        "name": "Pawniard",
        "genus": "Sharp Blade Pokémon",
        "identifier": "pawniard",
        "evolution_chain": 317,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 17,
        "type2": 9,
        "flavor_text": "After shredding its prey, it sharpens its blades\non a stone by the river. Each Pawniard has its\nown favorite sharpening stone.",
        "has_alt_form": false,
        "id": 624
    },
    {
        "name": "Bisharp",
        "genus": "Sword Blade Pokémon",
        "identifier": "bisharp",
        "evolution_chain": 317,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 624,
        "type1": 17,
        "type2": 9,
        "flavor_text": "No matter how strong the Bisharp, it’s said\nthat if the blade on its head is chipped, it will\nretire from its position as the boss.",
        "has_alt_form": false,
        "id": 625
    },
    {
        "name": "Bouffalant",
        "genus": "Bash Buffalo Pokémon",
        "identifier": "bouffalant",
        "evolution_chain": 318,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Their fluffy fur absorbs damage, even if they strike\nfoes with a fierce headbutt.",
        "has_alt_form": false,
        "id": 626
    },
    {
        "name": "Rufflet",
        "genus": "Eaglet Pokémon",
        "identifier": "rufflet",
        "evolution_chain": 319,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "With its powerful legs and sturdy claws, it can\ncrack even the hard shells of Shellder and pluck\nout their insides.",
        "has_alt_form": false,
        "id": 627
    },
    {
        "name": "Braviary",
        "genus": "Valiant Pokémon",
        "identifier": "braviary",
        "evolution_chain": 319,
        "color": "red",
        "since_gen": 5,
        "evolves_from": 627,
        "type1": 1,
        "type2": 3,
        "flavor_text": "The more scars it has on its front, the more\nheroic it’s considered to be. Those with many\nscars on their back are mocked by the flock.",
        "has_alt_form": false,
        "id": 628
    },
    {
        "name": "Vullaby",
        "genus": "Diapered Pokémon",
        "identifier": "vullaby",
        "evolution_chain": 320,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 17,
        "type2": 3,
        "flavor_text": "Mandibuzz gives it the bones it wears. Vullaby’s\nwings are short, so it can’t fly yet, but it jumps\naround, dreaming of wide open skies.",
        "has_alt_form": false,
        "id": 629
    },
    {
        "name": "Mandibuzz",
        "genus": "Bone Vulture Pokémon",
        "identifier": "mandibuzz",
        "evolution_chain": 320,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": 629,
        "type1": 17,
        "type2": 3,
        "flavor_text": "It skillfully arranges the bones of its prey to\nconstruct its nest. Most of the bones\nare Cubone.",
        "has_alt_form": false,
        "id": 630
    },
    {
        "name": "Heatmor",
        "genus": "Anteater Pokémon",
        "identifier": "heatmor",
        "evolution_chain": 321,
        "color": "red",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "It draws in air through its tail, transforms it into fire,\nand uses it like a tongue. It melts Durant and\neats them.",
        "has_alt_form": false,
        "id": 631
    },
    {
        "name": "Durant",
        "genus": "Iron Ant Pokémon",
        "identifier": "durant",
        "evolution_chain": 322,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 9,
        "flavor_text": "They attack in groups, covering themselves in steel\narmor to protect themselves from Heatmor.",
        "has_alt_form": false,
        "id": 632
    },
    {
        "name": "Deino",
        "genus": "Irate Pokémon",
        "identifier": "deino",
        "evolution_chain": 323,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 17,
        "type2": 16,
        "flavor_text": "Lacking sight, it’s unaware of its surroundings,\nso it bumps into things and eats anything\nthat moves.",
        "has_alt_form": false,
        "id": 633
    },
    {
        "name": "Zweilous",
        "genus": "Hostile Pokémon",
        "identifier": "zweilous",
        "evolution_chain": 323,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 633,
        "type1": 17,
        "type2": 16,
        "flavor_text": "After it has eaten up all the food in its territory,\nit moves to another area. Its two heads do not\nget along.",
        "has_alt_form": false,
        "id": 634
    },
    {
        "name": "Hydreigon",
        "genus": "Brutal Pokémon",
        "identifier": "hydreigon",
        "evolution_chain": 323,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": 634,
        "type1": 17,
        "type2": 16,
        "flavor_text": "It responds to movement by attacking. This scary,\nthree-headed Pokémon devours everything in\nits path!",
        "has_alt_form": false,
        "id": 635
    },
    {
        "name": "Larvesta",
        "genus": "Torch Pokémon",
        "identifier": "larvesta",
        "evolution_chain": 324,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 10,
        "flavor_text": "When battling opponents, it sprays fire from its\nfive horns. The max temperature of the flames\ncan reach nearly 5,500 degrees Fahrenheit.",
        "has_alt_form": false,
        "id": 636
    },
    {
        "name": "Volcarona",
        "genus": "Sun Pokémon",
        "identifier": "volcarona",
        "evolution_chain": 324,
        "color": "white",
        "since_gen": 5,
        "evolves_from": 636,
        "type1": 7,
        "type2": 10,
        "flavor_text": "As it flies, it scatters its flaming scales. It was\nfeared by ancient people, who referred to it as\n“the rage of the sun.”",
        "has_alt_form": false,
        "id": 637
    },
    {
        "name": "Cobalion",
        "genus": "Iron Will Pokémon",
        "identifier": "cobalion",
        "evolution_chain": 325,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 9,
        "type2": 2,
        "flavor_text": "It has a body and heart of steel. It worked with its\nallies to punish people when they hurt Pokémon.",
        "has_alt_form": false,
        "id": 638
    },
    {
        "name": "Terrakion",
        "genus": "Cavern Pokémon",
        "identifier": "terrakion",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 6,
        "type2": 2,
        "flavor_text": "Spoken of in legend, this Pokémon used its\nphenomenal power to destroy a castle in its effort\nto protect Pokémon.",
        "has_alt_form": false,
        "id": 639
    },
    {
        "name": "Virizion",
        "genus": "Grassland Pokémon",
        "identifier": "virizion",
        "evolution_chain": 327,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 12,
        "type2": 2,
        "flavor_text": "Legends say this Pokémon confounded opponents\nwith its swift movements.",
        "has_alt_form": false,
        "id": 640
    },
    {
        "name": "Tornadus",
        "genus": "Cyclone Pokémon",
        "identifier": "tornadus",
        "evolution_chain": 328,
        "color": "green",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 3,
        "type2": null,
        "flavor_text": "Tornadus expels massive energy from its tail,\ncausing severe storms. Its power is great enough\nto blow houses away.",
        "has_alt_form": true,
        "id": 641
    },
    {
        "name": "Thundurus",
        "genus": "Bolt Strike Pokémon",
        "identifier": "thundurus",
        "evolution_chain": 329,
        "color": "blue",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 13,
        "type2": 3,
        "flavor_text": "As it flies around, it shoots lightning all over\nthe place and causes forest fires. It is\ntherefore disliked.",
        "has_alt_form": true,
        "id": 642
    },
    {
        "name": "Reshiram",
        "genus": "Vast White Pokémon",
        "identifier": "reshiram",
        "evolution_chain": 330,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 16,
        "type2": 10,
        "flavor_text": "When Reshiram’s tail flares, the heat energy moves\nthe atmosphere and changes the world’s weather.",
        "has_alt_form": false,
        "id": 643
    },
    {
        "name": "Zekrom",
        "genus": "Deep Black Pokémon",
        "identifier": "zekrom",
        "evolution_chain": 331,
        "color": "black",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 16,
        "type2": 13,
        "flavor_text": "Concealing itself in lightning clouds, it flies\nthroughout the Unova region. It creates electricity\nin its tail.",
        "has_alt_form": false,
        "id": 644
    },
    {
        "name": "Landorus",
        "genus": "Abundance Pokémon",
        "identifier": "landorus",
        "evolution_chain": 332,
        "color": "brown",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 5,
        "type2": 3,
        "flavor_text": "From the forces of lightning and wind, it creates\nenergy to give nutrients to the soil and make the\nland abundant.",
        "has_alt_form": true,
        "id": 645
    },
    {
        "name": "Kyurem",
        "genus": "Boundary Pokémon",
        "identifier": "kyurem",
        "evolution_chain": 333,
        "color": "gray",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 16,
        "type2": 15,
        "flavor_text": "It generates a powerful, freezing energy inside\nitself, but its body became frozen when the energy\nleaked out.",
        "has_alt_form": false,
        "id": 646
    },
    {
        "name": "Keldeo",
        "genus": "Colt Pokémon",
        "identifier": "keldeo",
        "evolution_chain": 334,
        "color": "yellow",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 11,
        "type2": 2,
        "flavor_text": "When it is resolute, its body fills with power and it\nbecomes swifter. Its jumps are then too fast\nto follow.",
        "has_alt_form": true,
        "id": 647
    },
    {
        "name": "Meloetta",
        "genus": "Melody Pokémon",
        "identifier": "meloetta",
        "evolution_chain": 335,
        "color": "white",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 1,
        "type2": 14,
        "flavor_text": "Its melodies are sung with a special vocalization\nmethod that can control the feelings of those who\nhear it.",
        "has_alt_form": true,
        "id": 648
    },
    {
        "name": "Genesect",
        "genus": "Paleozoic Pokémon",
        "identifier": "genesect",
        "evolution_chain": 336,
        "color": "purple",
        "since_gen": 5,
        "evolves_from": null,
        "type1": 7,
        "type2": 9,
        "flavor_text": "This Pokémon existed 300 million years ago. Team\nPlasma altered it and attached a cannon to its back.",
        "has_alt_form": false,
        "id": 649
    },
    {
        "name": "Chespin",
        "genus": "Spiny Nut Pokémon",
        "identifier": "chespin",
        "evolution_chain": 337,
        "color": "green",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Such a thick shell of wood covers its head and back\nthat even a direct hit from a truck wouldn’t faze it.",
        "has_alt_form": false,
        "id": 650
    },
    {
        "name": "Quilladin",
        "genus": "Spiny Armor Pokémon",
        "identifier": "quilladin",
        "evolution_chain": 337,
        "color": "green",
        "since_gen": 6,
        "evolves_from": 650,
        "type1": 12,
        "type2": null,
        "flavor_text": "They strengthen their lower bodies by\nrunning into one another. They are very\nkind and won’t start fights.",
        "has_alt_form": false,
        "id": 651
    },
    {
        "name": "Chesnaught",
        "genus": "Spiny Armor Pokémon",
        "identifier": "chesnaught",
        "evolution_chain": 337,
        "color": "green",
        "since_gen": 6,
        "evolves_from": 651,
        "type1": 12,
        "type2": 2,
        "flavor_text": "When it takes a defensive posture with its fists\nguarding its face, it could withstand a bomb blast.",
        "has_alt_form": false,
        "id": 652
    },
    {
        "name": "Fennekin",
        "genus": "Fox Pokémon",
        "identifier": "fennekin",
        "evolution_chain": 338,
        "color": "red",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "As it walks, it munches on a twig in place\nof a snack. It intimidates opponents\nby puffing hot air out of its ears.",
        "has_alt_form": false,
        "id": 653
    },
    {
        "name": "Braixen",
        "genus": "Fox Pokémon",
        "identifier": "braixen",
        "evolution_chain": 338,
        "color": "red",
        "since_gen": 6,
        "evolves_from": 653,
        "type1": 10,
        "type2": null,
        "flavor_text": "When the twig is plucked from its tail,\nfriction sets the twig alight. The flame\nis used to send signals to its allies.",
        "has_alt_form": false,
        "id": 654
    },
    {
        "name": "Delphox",
        "genus": "Fox Pokémon",
        "identifier": "delphox",
        "evolution_chain": 338,
        "color": "red",
        "since_gen": 6,
        "evolves_from": 654,
        "type1": 10,
        "type2": 14,
        "flavor_text": "Using psychic power, it generates a\nfiery vortex of 5,400 degrees Fahrenheit,\nincinerating foes swept into this whirl of flame.",
        "has_alt_form": false,
        "id": 655
    },
    {
        "name": "Froakie",
        "genus": "Bubble Frog Pokémon",
        "identifier": "froakie",
        "evolution_chain": 339,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "It protects its skin by covering its body in\ndelicate bubbles. Beneath its happy-go-lucky air,\nit keeps a watchful eye on its surroundings.",
        "has_alt_form": false,
        "id": 656
    },
    {
        "name": "Frogadier",
        "genus": "Bubble Frog Pokémon",
        "identifier": "frogadier",
        "evolution_chain": 339,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 656,
        "type1": 11,
        "type2": null,
        "flavor_text": "Its swiftness is unparalleled.\nIt can scale a tower of more\nthan 2,000 feet in a minute’s time.",
        "has_alt_form": false,
        "id": 657
    },
    {
        "name": "Greninja",
        "genus": "Ninja Pokémon",
        "identifier": "greninja",
        "evolution_chain": 339,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 657,
        "type1": 11,
        "type2": 17,
        "flavor_text": "It appears and vanishes with a ninja’s grace.\nIt toys with its enemies using swift movements, while\nslicing them with throwing stars of sharpest water.",
        "has_alt_form": false,
        "id": 658
    },
    {
        "name": "Bunnelby",
        "genus": "Digging Pokémon",
        "identifier": "bunnelby",
        "evolution_chain": 340,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It has ears like shovels. Digging holes\nstrengthens its ears so much that they\ncan sever thick roots effortlessly.",
        "has_alt_form": false,
        "id": 659
    },
    {
        "name": "Diggersby",
        "genus": "Digging Pokémon",
        "identifier": "diggersby",
        "evolution_chain": 340,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 659,
        "type1": 1,
        "type2": 5,
        "flavor_text": "As powerful as an excavator, its ears\ncan reduce dense bedrock to rubble.\nWhen it’s finished digging, it lounges lazily.",
        "has_alt_form": false,
        "id": 660
    },
    {
        "name": "Fletchling",
        "genus": "Tiny Robin Pokémon",
        "identifier": "fletchling",
        "evolution_chain": 341,
        "color": "red",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "While it’s an amiable Pokémon, if you touch it\nunexpectedly, it will heat up its body in an\ninstant, and you’ll be burned.",
        "has_alt_form": false,
        "id": 661
    },
    {
        "name": "Fletchinder",
        "genus": "Ember Pokémon",
        "identifier": "fletchinder",
        "evolution_chain": 341,
        "color": "red",
        "since_gen": 6,
        "evolves_from": 661,
        "type1": 10,
        "type2": 3,
        "flavor_text": "It scatters embers in the tall grass. Then bug\nPokémon, frightened by the flames, come\nflying out, and Fletchinder gobbles them up.",
        "has_alt_form": false,
        "id": 662
    },
    {
        "name": "Talonflame",
        "genus": "Scorching Pokémon",
        "identifier": "talonflame",
        "evolution_chain": 341,
        "color": "red",
        "since_gen": 6,
        "evolves_from": 662,
        "type1": 10,
        "type2": 3,
        "flavor_text": "Its tough wings don’t allow fire to pass through\nthem. A long time ago, firefighters’ outfits were\nmade from Talonflame wings.",
        "has_alt_form": false,
        "id": 663
    },
    {
        "name": "Scatterbug",
        "genus": "Scatterdust Pokémon",
        "identifier": "scatterbug",
        "evolution_chain": 342,
        "color": "black",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "The powder that covers its body\nregulates its temperature, so it\ncan live in any region or climate.",
        "has_alt_form": false,
        "id": 664
    },
    {
        "name": "Spewpa",
        "genus": "Scatterdust Pokémon",
        "identifier": "spewpa",
        "evolution_chain": 342,
        "color": "black",
        "since_gen": 6,
        "evolves_from": 664,
        "type1": 7,
        "type2": null,
        "flavor_text": "The beaks of bird Pokémon can’t begin\nto scratch its stalwart body.\nTo defend itself, it spews powder.",
        "has_alt_form": false,
        "id": 665
    },
    {
        "name": "Vivillon",
        "genus": "Scale Pokémon",
        "identifier": "vivillon",
        "evolution_chain": 342,
        "color": "white",
        "since_gen": 6,
        "evolves_from": 665,
        "type1": 7,
        "type2": 3,
        "flavor_text": "The patterns on this Pokémon’s wings\ndepend on the climate and topography\nof its habitat. It scatters colorful scales.",
        "has_alt_form": true,
        "id": 666
    },
    {
        "name": "Litleo",
        "genus": "Lion Cub Pokémon",
        "identifier": "litleo",
        "evolution_chain": 343,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 10,
        "type2": 1,
        "flavor_text": "When they’re young, they live with a pride. Once\nthey’re able to hunt prey on their own, they’re\nkicked out and have to make their own way.",
        "has_alt_form": false,
        "id": 667
    },
    {
        "name": "Pyroar",
        "genus": "Royal Pokémon",
        "identifier": "pyroar",
        "evolution_chain": 343,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 667,
        "type1": 10,
        "type2": 1,
        "flavor_text": "The males are usually lazy, but when attacked\nby a strong foe, a male will protect its friends\nwith no regard for its own safety.",
        "has_alt_form": false,
        "id": 668
    },
    {
        "name": "Flabébé",
        "genus": "Single Bloom Pokémon",
        "identifier": "flabebe",
        "evolution_chain": 344,
        "color": "white",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "It’s not safe without the power of a flower, but\nit will keep traveling around until it finds one\nwith the color and shape it wants.",
        "has_alt_form": true,
        "id": 669
    },
    {
        "name": "Floette",
        "genus": "Single Bloom Pokémon",
        "identifier": "floette",
        "evolution_chain": 344,
        "color": "white",
        "since_gen": 6,
        "evolves_from": 669,
        "type1": 18,
        "type2": null,
        "flavor_text": "It raises flowers and uses them as weapons.\nThe more gorgeous the blossom, the more\npower it contains.",
        "has_alt_form": true,
        "id": 670
    },
    {
        "name": "Florges",
        "genus": "Garden Pokémon",
        "identifier": "florges",
        "evolution_chain": 344,
        "color": "white",
        "since_gen": 6,
        "evolves_from": 670,
        "type1": 18,
        "type2": null,
        "flavor_text": "It controls the flowers it grows. The petal\nblizzards that Florges triggers are overwhelming\nin their beauty and power.",
        "has_alt_form": true,
        "id": 671
    },
    {
        "name": "Skiddo",
        "genus": "Mount Pokémon",
        "identifier": "skiddo",
        "evolution_chain": 345,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "If it has sunshine and water, it doesn’t\nneed to eat, because it can generate\nenergy from the leaves on its back.",
        "has_alt_form": false,
        "id": 672
    },
    {
        "name": "Gogoat",
        "genus": "Mount Pokémon",
        "identifier": "gogoat",
        "evolution_chain": 345,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 672,
        "type1": 12,
        "type2": null,
        "flavor_text": "They inhabit mountainous regions.\nThe leader of the herd is decided by\na battle of clashing horns.",
        "has_alt_form": false,
        "id": 673
    },
    {
        "name": "Pancham",
        "genus": "Playful Pokémon",
        "identifier": "pancham",
        "evolution_chain": 346,
        "color": "white",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "It follows Pangoro around like a henchman.\nWhen Pancham makes a big mistake, its leaf\ngets taken away.",
        "has_alt_form": false,
        "id": 674
    },
    {
        "name": "Pangoro",
        "genus": "Daunting Pokémon",
        "identifier": "pangoro",
        "evolution_chain": 346,
        "color": "white",
        "since_gen": 6,
        "evolves_from": 674,
        "type1": 2,
        "type2": 17,
        "flavor_text": "This rowdy Pokémon boasts great physical\nstrength. Many Trainers are also smitten by its\nlively character.",
        "has_alt_form": false,
        "id": 675
    },
    {
        "name": "Furfrou",
        "genus": "Poodle Pokémon",
        "identifier": "furfrou",
        "evolution_chain": 347,
        "color": "white",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "There was an era when aristocrats would\ncompete to see who could trim their Furfrou’s\nfur into the most exquisite style.",
        "has_alt_form": true,
        "id": 676
    },
    {
        "name": "Espurr",
        "genus": "Restraint Pokémon",
        "identifier": "espurr",
        "evolution_chain": 348,
        "color": "gray",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It has enough psychic energy to blast\neverything within 300 feet of itself,\nbut it has no control over its power.",
        "has_alt_form": false,
        "id": 677
    },
    {
        "name": "Meowstic",
        "genus": "Constraint Pokémon",
        "identifier": "meowstic",
        "evolution_chain": 348,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 677,
        "type1": 14,
        "type2": null,
        "flavor_text": "The eyeball patterns on the interior of its ears\nemit psychic energy. It keeps the patterns tightly\ncovered because that power is too immense.",
        "has_alt_form": true,
        "id": 678
    },
    {
        "name": "Honedge",
        "genus": "Sword Pokémon",
        "identifier": "honedge",
        "evolution_chain": 349,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 9,
        "type2": 8,
        "flavor_text": "If anyone dares to grab its hilt, it wraps\na blue cloth around that person’s arm and\ndrains that person’s life energy completely.",
        "has_alt_form": false,
        "id": 679
    },
    {
        "name": "Doublade",
        "genus": "Sword Pokémon",
        "identifier": "doublade",
        "evolution_chain": 349,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 679,
        "type1": 9,
        "type2": 8,
        "flavor_text": "The complex attack patterns of its two swords\nare unstoppable, even for an opponent\ngreatly accomplished at swordplay.",
        "has_alt_form": false,
        "id": 680
    },
    {
        "name": "Aegislash",
        "genus": "Royal Sword Pokémon",
        "identifier": "aegislash",
        "evolution_chain": 349,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 680,
        "type1": 9,
        "type2": 8,
        "flavor_text": "Apparently, it can detect the innate qualities\nof leadership. According to legend, whoever it\nrecognizes is destined to become king.",
        "has_alt_form": true,
        "id": 681
    },
    {
        "name": "Spritzee",
        "genus": "Perfume Pokémon",
        "identifier": "spritzee",
        "evolution_chain": 350,
        "color": "pink",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "In the past, rather than using perfume,\nroyal ladies carried a Spritzee\nthat would waft a fragrance they liked.",
        "has_alt_form": false,
        "id": 682
    },
    {
        "name": "Aromatisse",
        "genus": "Fragrance Pokémon",
        "identifier": "aromatisse",
        "evolution_chain": 350,
        "color": "pink",
        "since_gen": 6,
        "evolves_from": 682,
        "type1": 18,
        "type2": null,
        "flavor_text": "Its scent is so overpowering that, unless a Trainer\nhappens to really enjoy the smell, he or she will\nhave a hard time walking alongside it.",
        "has_alt_form": false,
        "id": 683
    },
    {
        "name": "Swirlix",
        "genus": "Cotton Candy Pokémon",
        "identifier": "swirlix",
        "evolution_chain": 351,
        "color": "white",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "Because it eats nothing but sweets,\nits fur is as sticky sweet as cotton candy.",
        "has_alt_form": false,
        "id": 684
    },
    {
        "name": "Slurpuff",
        "genus": "Meringue Pokémon",
        "identifier": "slurpuff",
        "evolution_chain": 351,
        "color": "white",
        "since_gen": 6,
        "evolves_from": 684,
        "type1": 18,
        "type2": null,
        "flavor_text": "Its sense of smell is 100 million times better than\na human’s, so even the faintest scent tells it about\neverything in the area. It’s like it can see with its nose!",
        "has_alt_form": false,
        "id": 685
    },
    {
        "name": "Inkay",
        "genus": "Revolving Pokémon",
        "identifier": "inkay",
        "evolution_chain": 352,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 17,
        "type2": 14,
        "flavor_text": "It draws prey near with its blinking lights and\nthen wraps them up in its long tentacles and\nholds them in place.",
        "has_alt_form": false,
        "id": 686
    },
    {
        "name": "Malamar",
        "genus": "Overturning Pokémon",
        "identifier": "malamar",
        "evolution_chain": 352,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 686,
        "type1": 17,
        "type2": 14,
        "flavor_text": "When it comes to strong hypnosis, there’s an\nendless number of people who utilize Malamar\nfor their nefarious deeds.",
        "has_alt_form": false,
        "id": 687
    },
    {
        "name": "Binacle",
        "genus": "Two-Handed Pokémon",
        "identifier": "binacle",
        "evolution_chain": 353,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 6,
        "type2": 11,
        "flavor_text": "They stretch and then contract, yanking their\nrocks along with them in bold hops. They eat\nseaweed that washes up on the shoreline.",
        "has_alt_form": false,
        "id": 688
    },
    {
        "name": "Barbaracle",
        "genus": "Collective Pokémon",
        "identifier": "barbaracle",
        "evolution_chain": 353,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 688,
        "type1": 6,
        "type2": 11,
        "flavor_text": "Barbaracle’s legs and hands have minds\nof their own, and they will move independently.\nBut they usually follow the head’s orders.",
        "has_alt_form": false,
        "id": 689
    },
    {
        "name": "Skrelp",
        "genus": "Mock Kelp Pokémon",
        "identifier": "skrelp",
        "evolution_chain": 354,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 4,
        "type2": 11,
        "flavor_text": "It vanishes into seaweed and remains perfectly\nstill to avoid attacks from large Pokémon.\nRotten seaweed is its main food source.",
        "has_alt_form": false,
        "id": 690
    },
    {
        "name": "Dragalge",
        "genus": "Mock Kelp Pokémon",
        "identifier": "dragalge",
        "evolution_chain": 354,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 690,
        "type1": 4,
        "type2": 16,
        "flavor_text": "This vicious Pokémon sprays a poisonous liquid\non opponents that come near. For whatever\nreason, it gets along really well with Dhelmise.",
        "has_alt_form": false,
        "id": 691
    },
    {
        "name": "Clauncher",
        "genus": "Water Gun Pokémon",
        "identifier": "clauncher",
        "evolution_chain": 355,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "Its claws occasionally fall off, and it keeps a low\nprofile until they grow back. The meat of its\nclaws is so delicious!",
        "has_alt_form": false,
        "id": 692
    },
    {
        "name": "Clawitzer",
        "genus": "Howitzer Pokémon",
        "identifier": "clawitzer",
        "evolution_chain": 355,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 692,
        "type1": 11,
        "type2": null,
        "flavor_text": "It compresses the water it has sucked up and\nthen projects it with enough power to punch a\nhole right through a thick sheet of iron.",
        "has_alt_form": false,
        "id": 693
    },
    {
        "name": "Helioptile",
        "genus": "Generator Pokémon",
        "identifier": "helioptile",
        "evolution_chain": 356,
        "color": "yellow",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 13,
        "type2": 1,
        "flavor_text": "The frills on either side of its head have cells\nthat generate electricity when exposed to sunlight.",
        "has_alt_form": false,
        "id": 694
    },
    {
        "name": "Heliolisk",
        "genus": "Generator Pokémon",
        "identifier": "heliolisk",
        "evolution_chain": 356,
        "color": "yellow",
        "since_gen": 6,
        "evolves_from": 694,
        "type1": 13,
        "type2": 1,
        "flavor_text": "It stimulates its muscles with electricity,\nboosting the strength in its legs and enabling\nit to run 100 yards in five seconds.",
        "has_alt_form": false,
        "id": 695
    },
    {
        "name": "Tyrunt",
        "genus": "Royal Heir Pokémon",
        "identifier": "tyrunt",
        "evolution_chain": 357,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 6,
        "type2": 16,
        "flavor_text": "Its large jaw has incredible destructive power.\nSome theories suggest that its restored form is\ndifferent from its form of long ago.",
        "has_alt_form": false,
        "id": 696
    },
    {
        "name": "Tyrantrum",
        "genus": "Despot Pokémon",
        "identifier": "tyrantrum",
        "evolution_chain": 357,
        "color": "red",
        "since_gen": 6,
        "evolves_from": 696,
        "type1": 6,
        "type2": 16,
        "flavor_text": "Complete restoration is impossible, allowing\nroom for theories that its entire body was\nonce covered in a feather-like coat.",
        "has_alt_form": false,
        "id": 697
    },
    {
        "name": "Amaura",
        "genus": "Tundra Pokémon",
        "identifier": "amaura",
        "evolution_chain": 358,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 6,
        "type2": 15,
        "flavor_text": "It lived in cold areas in ancient times. It’s said\nthat when Amaura whinnies, auroras appear in\nthe night sky.",
        "has_alt_form": false,
        "id": 698
    },
    {
        "name": "Aurorus",
        "genus": "Tundra Pokémon",
        "identifier": "aurorus",
        "evolution_chain": 358,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 698,
        "type1": 6,
        "type2": 15,
        "flavor_text": "An Aurorus was found frozen solid within a\nglacier, just as it appeared long ago, which\nbecame quite a big event in the news.",
        "has_alt_form": false,
        "id": 699
    },
    {
        "name": "Sylveon",
        "genus": "Intertwining Pokémon",
        "identifier": "sylveon",
        "evolution_chain": 67,
        "color": "pink",
        "since_gen": 6,
        "evolves_from": 133,
        "type1": 18,
        "type2": null,
        "flavor_text": "Once a fight breaks out, it will unflinchingly\ncharge at dragon Pokémon that are many times\nlarger than itself.",
        "has_alt_form": false,
        "id": 700
    },
    {
        "name": "Hawlucha",
        "genus": "Wrestling Pokémon",
        "identifier": "hawlucha",
        "evolution_chain": 359,
        "color": "green",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 2,
        "type2": 3,
        "flavor_text": "It overwhelms opponents with quick moves, but\nsometimes it showboats for too long when it’s\nusing a special move and gets itself into a pinch.",
        "has_alt_form": false,
        "id": 701
    },
    {
        "name": "Dedenne",
        "genus": "Antenna Pokémon",
        "identifier": "dedenne",
        "evolution_chain": 360,
        "color": "yellow",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 13,
        "type2": 18,
        "flavor_text": "It sneaks into people’s homes and steals\nelectricity from their outlets. When your electric\nbill seems off, it’s the handiwork of this rascal.",
        "has_alt_form": false,
        "id": 702
    },
    {
        "name": "Carbink",
        "genus": "Jewel Pokémon",
        "identifier": "carbink",
        "evolution_chain": 361,
        "color": "gray",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 6,
        "type2": 18,
        "flavor_text": "Some say that deep beneath the surface of the\nworld, a pack of Carbink live with their queen in\na kingdom of jewels.",
        "has_alt_form": false,
        "id": 703
    },
    {
        "name": "Goomy",
        "genus": "Soft Tissue Pokémon",
        "identifier": "goomy",
        "evolution_chain": 362,
        "color": "purple",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 16,
        "type2": null,
        "flavor_text": "It uses its horns to check out its surroundings.\nThey’re very sensitive, so if you grab them, it\nwill feel a strong shock and be unable to move.",
        "has_alt_form": false,
        "id": 704
    },
    {
        "name": "Sliggoo",
        "genus": "Soft Tissue Pokémon",
        "identifier": "sliggoo",
        "evolution_chain": 362,
        "color": "purple",
        "since_gen": 6,
        "evolves_from": 704,
        "type1": 16,
        "type2": null,
        "flavor_text": "It crawls along sluggishly. The swirly protrusion\non its back is filled with its brain and\nother organs.",
        "has_alt_form": false,
        "id": 705
    },
    {
        "name": "Goodra",
        "genus": "Dragon Pokémon",
        "identifier": "goodra",
        "evolution_chain": 362,
        "color": "purple",
        "since_gen": 6,
        "evolves_from": 705,
        "type1": 16,
        "type2": null,
        "flavor_text": "It’s very friendly toward people. If you grow\nclose to it, Goodra will hug you with its sticky,\nslime-covered body. Don’t get mad.",
        "has_alt_form": false,
        "id": 706
    },
    {
        "name": "Klefki",
        "genus": "Key Ring Pokémon",
        "identifier": "klefki",
        "evolution_chain": 363,
        "color": "gray",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 9,
        "type2": 18,
        "flavor_text": "Although it’s unclear why it collects keys, giving\nit a key makes Klefki very happy. However, it\napparently only likes master keys.",
        "has_alt_form": false,
        "id": 707
    },
    {
        "name": "Phantump",
        "genus": "Stump Pokémon",
        "identifier": "phantump",
        "evolution_chain": 364,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 8,
        "type2": 12,
        "flavor_text": "By imitating the voice of a child, it causes\npeople to get hopelessly lost deep in the forest.\nIt’s trying to make friends with them.",
        "has_alt_form": false,
        "id": 708
    },
    {
        "name": "Trevenant",
        "genus": "Elder Tree Pokémon",
        "identifier": "trevenant",
        "evolution_chain": 364,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 708,
        "type1": 8,
        "type2": 12,
        "flavor_text": "It’s feared as a ghost of the forest.\nLumberjacks bring along Fire types, which\nTrevenant hates, when they enter the forest.",
        "has_alt_form": false,
        "id": 709
    },
    {
        "name": "Pumpkaboo",
        "genus": "Pumpkin Pokémon",
        "identifier": "pumpkaboo",
        "evolution_chain": 365,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 8,
        "type2": 12,
        "flavor_text": "It is said to carry wandering spirits\nto the place where they belong\nso they can move on.",
        "has_alt_form": true,
        "id": 710
    },
    {
        "name": "Gourgeist",
        "genus": "Pumpkin Pokémon",
        "identifier": "gourgeist",
        "evolution_chain": 365,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": 710,
        "type1": 8,
        "type2": 12,
        "flavor_text": "It enwraps its prey in its hairlike arms.\nIt sings joyfully as it observes the\nsuffering of its prey.",
        "has_alt_form": true,
        "id": 711
    },
    {
        "name": "Bergmite",
        "genus": "Ice Chunk Pokémon",
        "identifier": "bergmite",
        "evolution_chain": 366,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 15,
        "type2": null,
        "flavor_text": "Using air of -150 degrees Fahrenheit, they\nfreeze opponents solid. They live in herds\nabove the snow line on mountains.",
        "has_alt_form": false,
        "id": 712
    },
    {
        "name": "Avalugg",
        "genus": "Iceberg Pokémon",
        "identifier": "avalugg",
        "evolution_chain": 366,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": 712,
        "type1": 15,
        "type2": null,
        "flavor_text": "The way several Bergmite huddle\non its back makes it look like\nan aircraft carrier made of ice.",
        "has_alt_form": false,
        "id": 713
    },
    {
        "name": "Noibat",
        "genus": "Sound Wave Pokémon",
        "identifier": "noibat",
        "evolution_chain": 367,
        "color": "purple",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 3,
        "type2": 16,
        "flavor_text": "Fruits are its favorite foods. This gourmet\ncarefully picks out just the ripe ones using\nits sonar.",
        "has_alt_form": false,
        "id": 714
    },
    {
        "name": "Noivern",
        "genus": "Sound Wave Pokémon",
        "identifier": "noivern",
        "evolution_chain": 367,
        "color": "purple",
        "since_gen": 6,
        "evolves_from": 714,
        "type1": 3,
        "type2": 16,
        "flavor_text": "Although it has a violent disposition, if you give\nit a nice ripe fruit that it loves, Noivern will\nsuddenly become tame.",
        "has_alt_form": false,
        "id": 715
    },
    {
        "name": "Xerneas",
        "genus": "Life Pokémon",
        "identifier": "xerneas",
        "evolution_chain": 368,
        "color": "blue",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "When the horns on its head shine\nin seven colors, it is said to be\nsharing everlasting life.",
        "has_alt_form": true,
        "id": 716
    },
    {
        "name": "Yveltal",
        "genus": "Destruction Pokémon",
        "identifier": "yveltal",
        "evolution_chain": 369,
        "color": "red",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 17,
        "type2": 3,
        "flavor_text": "When its life comes to an end, it absorbs\nthe life energy of every living thing\nand turns into a cocoon once more.",
        "has_alt_form": false,
        "id": 717
    },
    {
        "name": "Zygarde",
        "genus": "Order Pokémon",
        "identifier": "zygarde",
        "evolution_chain": 370,
        "color": "green",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 16,
        "type2": 5,
        "flavor_text": "This is Zygarde’s form when about half of its\npieces have been assembled. It plays the role of\nmonitoring the ecosystem.",
        "has_alt_form": false,
        "id": 718
    },
    {
        "name": "Diancie",
        "genus": "Jewel Pokémon",
        "identifier": "diancie",
        "evolution_chain": 371,
        "color": "pink",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 6,
        "type2": 18,
        "flavor_text": "It can instantly create many diamonds\nby compressing the carbon in the air\nbetween its hands.",
        "has_alt_form": false,
        "id": 719
    },
    {
        "name": "Hoopa",
        "genus": "Mischief Pokémon",
        "identifier": "hoopa",
        "evolution_chain": 372,
        "color": "purple",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 14,
        "type2": 8,
        "flavor_text": "It is said to be able to seize anything it desires\nwith its six rings and six huge arms. With its power\nsealed, it is transformed into a much smaller form.",
        "has_alt_form": true,
        "id": 720
    },
    {
        "name": "Volcanion",
        "genus": "Steam Pokémon",
        "identifier": "volcanion",
        "evolution_chain": 373,
        "color": "brown",
        "since_gen": 6,
        "evolves_from": null,
        "type1": 10,
        "type2": 11,
        "flavor_text": "It expels its internal steam from the\narms on its back. It has enough\npower to blow away a mountain.",
        "has_alt_form": false,
        "id": 721
    },
    {
        "name": "Rowlet",
        "genus": "Grass Quill Pokémon",
        "identifier": "rowlet",
        "evolution_chain": 374,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 12,
        "type2": 3,
        "flavor_text": "It sends its feathers, which are as sharp as\nblades, flying in attack. Its legs are strong,\nso its kicks are also formidable.",
        "has_alt_form": false,
        "id": 722
    },
    {
        "name": "Dartrix",
        "genus": "Blade Quill Pokémon",
        "identifier": "dartrix",
        "evolution_chain": 374,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": 722,
        "type1": 12,
        "type2": 3,
        "flavor_text": "This narcissistic Pokémon is a clean freak.\nIf you don’t groom it diligently, it will stop\nlistening to you.",
        "has_alt_form": false,
        "id": 723
    },
    {
        "name": "Decidueye",
        "genus": "Arrow Quill Pokémon",
        "identifier": "decidueye",
        "evolution_chain": 374,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": 723,
        "type1": 12,
        "type2": 8,
        "flavor_text": "It nocks its arrow quills and shoots them at\nopponents. When it simply can’t afford to miss,\nit tugs the vine on its head to improve its focus.",
        "has_alt_form": false,
        "id": 724
    },
    {
        "name": "Litten",
        "genus": "Fire Cat Pokémon",
        "identifier": "litten",
        "evolution_chain": 375,
        "color": "red",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 10,
        "type2": null,
        "flavor_text": "If you try too hard to get close to it, it won’t\nopen up to you. Even if you do grow close, giving\nit too much affection is still a no-no.",
        "has_alt_form": false,
        "id": 725
    },
    {
        "name": "Torracat",
        "genus": "Fire Cat Pokémon",
        "identifier": "torracat",
        "evolution_chain": 375,
        "color": "red",
        "since_gen": 7,
        "evolves_from": 725,
        "type1": 10,
        "type2": null,
        "flavor_text": "It can act spoiled if it grows close to its Trainer.\nA powerful Pokémon, its sharp claws can leave\nits Trainer’s whole body covered in scratches.",
        "has_alt_form": false,
        "id": 726
    },
    {
        "name": "Incineroar",
        "genus": "Heel Pokémon",
        "identifier": "incineroar",
        "evolution_chain": 375,
        "color": "red",
        "since_gen": 7,
        "evolves_from": 726,
        "type1": 10,
        "type2": 17,
        "flavor_text": "Although it’s rough mannered and egotistical, it\nfinds beating down unworthy opponents boring.\nIt gets motivated for stronger opponents.",
        "has_alt_form": false,
        "id": 727
    },
    {
        "name": "Popplio",
        "genus": "Sea Lion Pokémon",
        "identifier": "popplio",
        "evolution_chain": 376,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "The balloons it inflates with its nose grow\nlarger and larger as it practices day by day.",
        "has_alt_form": false,
        "id": 728
    },
    {
        "name": "Brionne",
        "genus": "Pop Star Pokémon",
        "identifier": "brionne",
        "evolution_chain": 376,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": 728,
        "type1": 11,
        "type2": null,
        "flavor_text": "It gets excited when it sees a dance it doesn’t\nknow. This hard worker practices diligently until\nit can learn that dance.",
        "has_alt_form": false,
        "id": 729
    },
    {
        "name": "Primarina",
        "genus": "Soloist Pokémon",
        "identifier": "primarina",
        "evolution_chain": 376,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": 729,
        "type1": 11,
        "type2": 18,
        "flavor_text": "To Primarina, every battle is a stage. It takes\ndown its prey with beautiful singing\nand dancing.",
        "has_alt_form": false,
        "id": 730
    },
    {
        "name": "Pikipek",
        "genus": "Woodpecker Pokémon",
        "identifier": "pikipek",
        "evolution_chain": 377,
        "color": "black",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": 3,
        "flavor_text": "It pecks at trees with its hard beak. You can\nget some idea of its mood or condition from the\nrhythm of its pecking.",
        "has_alt_form": false,
        "id": 731
    },
    {
        "name": "Trumbeak",
        "genus": "Bugle Beak Pokémon",
        "identifier": "trumbeak",
        "evolution_chain": 377,
        "color": "black",
        "since_gen": 7,
        "evolves_from": 731,
        "type1": 1,
        "type2": 3,
        "flavor_text": "It can bend the tip of its beak to produce over\na hundred different cries at will.",
        "has_alt_form": false,
        "id": 732
    },
    {
        "name": "Toucannon",
        "genus": "Cannon Pokémon",
        "identifier": "toucannon",
        "evolution_chain": 377,
        "color": "black",
        "since_gen": 7,
        "evolves_from": 732,
        "type1": 1,
        "type2": 3,
        "flavor_text": "They smack beaks with others of their kind to\ncommunicate. The strength and number of hits\ntell each other how they feel.",
        "has_alt_form": false,
        "id": 733
    },
    {
        "name": "Yungoos",
        "genus": "Loitering Pokémon",
        "identifier": "yungoos",
        "evolution_chain": 378,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "Its stomach takes up most of its long torso.\nIt’s a big eater, so the amount Trainers have to\nspend on its food is no laughing matter.",
        "has_alt_form": false,
        "id": 734
    },
    {
        "name": "Gumshoos",
        "genus": "Stakeout Pokémon",
        "identifier": "gumshoos",
        "evolution_chain": 378,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": 734,
        "type1": 1,
        "type2": null,
        "flavor_text": "Although it wasn’t originally found in Alola, this\nPokémon was brought over a long time ago\nwhen there was a huge Rattata outbreak.",
        "has_alt_form": false,
        "id": 735
    },
    {
        "name": "Grubbin",
        "genus": "Larva Pokémon",
        "identifier": "grubbin",
        "evolution_chain": 379,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 7,
        "type2": null,
        "flavor_text": "If you find its nest, you shouldn’t stick your\nhand inside. You’ll get bitten by an\nirritated Grubbin.",
        "has_alt_form": false,
        "id": 736
    },
    {
        "name": "Charjabug",
        "genus": "Battery Pokémon",
        "identifier": "charjabug",
        "evolution_chain": 379,
        "color": "green",
        "since_gen": 7,
        "evolves_from": 736,
        "type1": 7,
        "type2": 13,
        "flavor_text": "It buries itself in fallen leaves and barely\nmoves, munching away on humus. If you\naccidentally step on one, you’ll get a shock!",
        "has_alt_form": false,
        "id": 737
    },
    {
        "name": "Vikavolt",
        "genus": "Stag Beetle Pokémon",
        "identifier": "vikavolt",
        "evolution_chain": 379,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": 737,
        "type1": 7,
        "type2": 13,
        "flavor_text": "It has an organ that generates electricity in its\nabdomen. It concentrates energy in its strong\njaws and fires off powerful jolts of electricity.",
        "has_alt_form": false,
        "id": 738
    },
    {
        "name": "Crabrawler",
        "genus": "Boxing Pokémon",
        "identifier": "crabrawler",
        "evolution_chain": 380,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "Its hard pincers are well suited to both offense\nand defense. Fights between two Crabrawler\nare like boxing matches.",
        "has_alt_form": false,
        "id": 739
    },
    {
        "name": "Crabominable",
        "genus": "Woolly Crab Pokémon",
        "identifier": "crabominable",
        "evolution_chain": 380,
        "color": "white",
        "since_gen": 7,
        "evolves_from": 739,
        "type1": 2,
        "type2": 15,
        "flavor_text": "It stores coldness in its pincers and pummels its\nfoes. It can even smash thick walls of ice\nto bits!",
        "has_alt_form": false,
        "id": 740
    },
    {
        "name": "Oricorio",
        "genus": "Dancing Pokémon",
        "identifier": "oricorio",
        "evolution_chain": 381,
        "color": "red",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 10,
        "type2": 3,
        "flavor_text": "It wins the hearts of its enemies with its\npassionate dancing and then uses the opening\nit creates to burn them up with blazing flames.",
        "has_alt_form": true,
        "id": 741
    },
    {
        "name": "Cutiefly",
        "genus": "Bee Fly Pokémon",
        "identifier": "cutiefly",
        "evolution_chain": 382,
        "color": "yellow",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 7,
        "type2": 18,
        "flavor_text": "Nectar and pollen are its favorite fare. In fields\nof flowers, it gets into skirmishes with\nButterfree over food.",
        "has_alt_form": false,
        "id": 742
    },
    {
        "name": "Ribombee",
        "genus": "Bee Fly Pokémon",
        "identifier": "ribombee",
        "evolution_chain": 382,
        "color": "yellow",
        "since_gen": 7,
        "evolves_from": 742,
        "type1": 7,
        "type2": 18,
        "flavor_text": "Rain makes pollen damp, so Ribombee hates\nrain. When it sees ominous clouds, it finds a\nhollow in a tree, where it waits stock-still.",
        "has_alt_form": false,
        "id": 743
    },
    {
        "name": "Rockruff",
        "genus": "Puppy Pokémon",
        "identifier": "rockruff",
        "evolution_chain": 383,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 6,
        "type2": null,
        "flavor_text": "As they develop, their disposition grows more\nviolent and aggressive. Many Trainers find them\ntoo much to handle and abandon them.",
        "has_alt_form": false,
        "id": 744
    },
    {
        "name": "Lycanroc",
        "genus": "Wolf Pokémon",
        "identifier": "lycanroc",
        "evolution_chain": 383,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": 744,
        "type1": 6,
        "type2": null,
        "flavor_text": "The sharp rocks in its mane can cut like knives.\nLycanroc wears its prey down by degrees\nbefore finishing them off.",
        "has_alt_form": true,
        "id": 745
    },
    {
        "name": "Wishiwashi",
        "genus": "Small Fry Pokémon",
        "identifier": "wishiwashi",
        "evolution_chain": 384,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "They’re weak, so they move in schools.\nHowever, they can also often be seen all alone,\nhaving strayed from the school.",
        "has_alt_form": true,
        "id": 746
    },
    {
        "name": "Mareanie",
        "genus": "Brutal Star Pokémon",
        "identifier": "mareanie",
        "evolution_chain": 385,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 4,
        "type2": 11,
        "flavor_text": "They eat Corsola branches, so Mareanie are\nhated by craftsmen who work with Corsola\nbranches that have naturally fallen off.",
        "has_alt_form": false,
        "id": 747
    },
    {
        "name": "Toxapex",
        "genus": "Brutal Star Pokémon",
        "identifier": "toxapex",
        "evolution_chain": 385,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": 747,
        "type1": 4,
        "type2": 11,
        "flavor_text": "To attack, this Pokémon sends toxic spikes\nflying at its enemies. Ones that come close get\nmown down by the claws on its feet.",
        "has_alt_form": false,
        "id": 748
    },
    {
        "name": "Mudbray",
        "genus": "Donkey Pokémon",
        "identifier": "mudbray",
        "evolution_chain": 386,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 5,
        "type2": null,
        "flavor_text": "It loves playing in the mud. If it isn’t showered\nwith mud on a daily basis, it gets stressed\nout and stops listening to its Trainer.",
        "has_alt_form": false,
        "id": 749
    },
    {
        "name": "Mudsdale",
        "genus": "Draft Horse Pokémon",
        "identifier": "mudsdale",
        "evolution_chain": 386,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": 749,
        "type1": 5,
        "type2": null,
        "flavor_text": "It remains calm and unmoving no matter the\nsituation. It mixes dirt with the saliva in its\nmouth to make a special kind of mud.",
        "has_alt_form": false,
        "id": 750
    },
    {
        "name": "Dewpider",
        "genus": "Water Bubble Pokémon",
        "identifier": "dewpider",
        "evolution_chain": 387,
        "color": "green",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 11,
        "type2": 7,
        "flavor_text": "When two Dewpider meet, they display their\nwater bubbles to each other. Then the one with\nthe smaller bubble gets out of the other’s way.",
        "has_alt_form": false,
        "id": 751
    },
    {
        "name": "Araquanid",
        "genus": "Water Bubble Pokémon",
        "identifier": "araquanid",
        "evolution_chain": 387,
        "color": "green",
        "since_gen": 7,
        "evolves_from": 751,
        "type1": 11,
        "type2": 7,
        "flavor_text": "It usually passes its time in the water. When its\nbelly is full, it stores its subdued prey in the\nwater bubble on its head.",
        "has_alt_form": false,
        "id": 752
    },
    {
        "name": "Fomantis",
        "genus": "Sickle Grass Pokémon",
        "identifier": "fomantis",
        "evolution_chain": 388,
        "color": "pink",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "When the sun rises, Fomantis spreads its four\nleaves and bathes in the sunlight. The tip of its\nhead has a pleasant aroma.",
        "has_alt_form": false,
        "id": 753
    },
    {
        "name": "Lurantis",
        "genus": "Bloom Sickle Pokémon",
        "identifier": "lurantis",
        "evolution_chain": 388,
        "color": "pink",
        "since_gen": 7,
        "evolves_from": 753,
        "type1": 12,
        "type2": null,
        "flavor_text": "For self-protection, it pretends to be a bug\nPokémon. Both of its arms bear\nkeen-edged petals.",
        "has_alt_form": false,
        "id": 754
    },
    {
        "name": "Morelull",
        "genus": "Illuminating Pokémon",
        "identifier": "morelull",
        "evolution_chain": 389,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 12,
        "type2": 18,
        "flavor_text": "It scatters its shining spores around itself.\nEven though they’re dangerous, nighttime tours\nof forests where Morelull live are popular.",
        "has_alt_form": false,
        "id": 755
    },
    {
        "name": "Shiinotic",
        "genus": "Illuminating Pokémon",
        "identifier": "shiinotic",
        "evolution_chain": 389,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": 755,
        "type1": 12,
        "type2": 18,
        "flavor_text": "It puts its prey to sleep and siphons off their\nvitality through the tip of its arms. If one of its\nkind is weakened, it helps by sending it vitality.",
        "has_alt_form": false,
        "id": 756
    },
    {
        "name": "Salandit",
        "genus": "Toxic Lizard Pokémon",
        "identifier": "salandit",
        "evolution_chain": 390,
        "color": "black",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 4,
        "type2": 10,
        "flavor_text": "The males will do whatever the females tell\nthem. They give the females most of their food.\nDue to malnutrition, the males can’t evolve.",
        "has_alt_form": false,
        "id": 757
    },
    {
        "name": "Salazzle",
        "genus": "Toxic Lizard Pokémon",
        "identifier": "salazzle",
        "evolution_chain": 390,
        "color": "black",
        "since_gen": 7,
        "evolves_from": 757,
        "type1": 4,
        "type2": 10,
        "flavor_text": "Salazzle lives deep in caves and forces the\nSalandit it has attracted with its pheromones\nto serve it.",
        "has_alt_form": false,
        "id": 758
    },
    {
        "name": "Stufful",
        "genus": "Flailing Pokémon",
        "identifier": "stufful",
        "evolution_chain": 391,
        "color": "pink",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": 2,
        "flavor_text": "It boasts power enough to split large trees in\nhalf. The organ on its rear releases an odor that\nit uses to communicate with others of its kind.",
        "has_alt_form": false,
        "id": 759
    },
    {
        "name": "Bewear",
        "genus": "Strong Arm Pokémon",
        "identifier": "bewear",
        "evolution_chain": 391,
        "color": "pink",
        "since_gen": 7,
        "evolves_from": 759,
        "type1": 1,
        "type2": 2,
        "flavor_text": "It waves its hands wildly in intimidation and\nwarning. Life is over for anyone who doesn’t\nrun away as fast as possible.",
        "has_alt_form": false,
        "id": 760
    },
    {
        "name": "Bounsweet",
        "genus": "Fruit Pokémon",
        "identifier": "bounsweet",
        "evolution_chain": 392,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 12,
        "type2": null,
        "flavor_text": "Because of its sweet, delicious aroma, bird\nPokémon are always after it, but it’s not\nintelligent enough to care.",
        "has_alt_form": false,
        "id": 761
    },
    {
        "name": "Steenee",
        "genus": "Fruit Pokémon",
        "identifier": "steenee",
        "evolution_chain": 392,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": 761,
        "type1": 12,
        "type2": null,
        "flavor_text": "It’s protected by its hard sepals, so it plays\nwith bird Pokémon without worry. They peck it\nrelentlessly, but it doesn’t care.",
        "has_alt_form": false,
        "id": 762
    },
    {
        "name": "Tsareena",
        "genus": "Fruit Pokémon",
        "identifier": "tsareena",
        "evolution_chain": 392,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": 762,
        "type1": 12,
        "type2": null,
        "flavor_text": "A master of grand and beautiful kicks, it can\nknock out even kickboxing champions with a\nsingle blow.",
        "has_alt_form": false,
        "id": 763
    },
    {
        "name": "Comfey",
        "genus": "Posy Picker Pokémon",
        "identifier": "comfey",
        "evolution_chain": 393,
        "color": "green",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 18,
        "type2": null,
        "flavor_text": "It stretches sticky vines out from its head and\npicks flowers to adorn itself with. When it\ndoesn’t have any flowers, it feels uneasy.",
        "has_alt_form": false,
        "id": 764
    },
    {
        "name": "Oranguru",
        "genus": "Sage Pokémon",
        "identifier": "oranguru",
        "evolution_chain": 394,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": 14,
        "flavor_text": "It normally spends its time meditating in the\ntreetops. It throws Poké Balls and gives other\nPokémon orders as it pleases.",
        "has_alt_form": false,
        "id": 765
    },
    {
        "name": "Passimian",
        "genus": "Teamwork Pokémon",
        "identifier": "passimian",
        "evolution_chain": 395,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 2,
        "type2": null,
        "flavor_text": "They use their saliva to stick leaves to their\nshoulders. You can tell what troop they belong\nto from the position of the leaves.",
        "has_alt_form": false,
        "id": 766
    },
    {
        "name": "Wimpod",
        "genus": "Turn Tail Pokémon",
        "identifier": "wimpod",
        "evolution_chain": 396,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 7,
        "type2": 11,
        "flavor_text": "It will pick up anything it finds on the ground.\nSometimes it finds coins, so Murkrow and\nMeowth will go after it.",
        "has_alt_form": false,
        "id": 767
    },
    {
        "name": "Golisopod",
        "genus": "Hard Scale Pokémon",
        "identifier": "golisopod",
        "evolution_chain": 396,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": 767,
        "type1": 7,
        "type2": 11,
        "flavor_text": "The shell covering its body is as hard as\ndiamond. This Pokémon will do anything it\ntakes to win.",
        "has_alt_form": false,
        "id": 768
    },
    {
        "name": "Sandygast",
        "genus": "Sand Heap Pokémon",
        "identifier": "sandygast",
        "evolution_chain": 397,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 8,
        "type2": 5,
        "flavor_text": "It likes the shovel on its head, so Sandygast\nwill get serious and fight any children who come\nto take it back.",
        "has_alt_form": false,
        "id": 769
    },
    {
        "name": "Palossand",
        "genus": "Sand Castle Pokémon",
        "identifier": "palossand",
        "evolution_chain": 397,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": 769,
        "type1": 8,
        "type2": 5,
        "flavor_text": "Each of its grains of sand has its own will.\nPalossand eats small Pokémon and siphons\naway their vital essence while they’re still alive.",
        "has_alt_form": false,
        "id": 770
    },
    {
        "name": "Pyukumuku",
        "genus": "Sea Cucumber Pokémon",
        "identifier": "pyukumuku",
        "evolution_chain": 398,
        "color": "black",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 11,
        "type2": null,
        "flavor_text": "The tradition known as Pyukumuku chucking\nstarted from the custom of throwing Pyukumuku\nback into the sea after they wash onshore.",
        "has_alt_form": false,
        "id": 771
    },
    {
        "name": "Type: Null",
        "genus": "Synthetic Pokémon",
        "identifier": "type-null",
        "evolution_chain": 399,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "A Pokémon weapon developed for a specific\nmission, it went berserk during an experiment,\nso it was cryogenically frozen.",
        "has_alt_form": false,
        "id": 772
    },
    {
        "name": "Silvally",
        "genus": "Synthetic Pokémon",
        "identifier": "silvally",
        "evolution_chain": 399,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": 772,
        "type1": 1,
        "type2": null,
        "flavor_text": "This is its form once it has awakened and\nevolved. Freed from its heavy mask, its speed is\ngreatly increased.",
        "has_alt_form": false,
        "id": 773
    },
    {
        "name": "Minior",
        "genus": "Meteor Pokémon",
        "identifier": "minior",
        "evolution_chain": 400,
        "color": "brown",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 6,
        "type2": 3,
        "flavor_text": "It lives in the ozone layer, where it becomes\nfood for stronger Pokémon. When it tries to run\naway, it falls to the ground.",
        "has_alt_form": true,
        "id": 774
    },
    {
        "name": "Komala",
        "genus": "Drowsing Pokémon",
        "identifier": "komala",
        "evolution_chain": 401,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": null,
        "flavor_text": "It stays asleep from the moment it’s born.\nWhen it falls into a deep sleep, it stops\nmoving altogether.",
        "has_alt_form": false,
        "id": 775
    },
    {
        "name": "Turtonator",
        "genus": "Blast Turtle Pokémon",
        "identifier": "turtonator",
        "evolution_chain": 402,
        "color": "red",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 10,
        "type2": 16,
        "flavor_text": "It lives in volcanoes and eats sulfur and other\nminerals. Materials from the food it eats form\nthe basis of its explosive shell.",
        "has_alt_form": false,
        "id": 776
    },
    {
        "name": "Togedemaru",
        "genus": "Roly-Poly Pokémon",
        "identifier": "togedemaru",
        "evolution_chain": 403,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 13,
        "type2": 9,
        "flavor_text": "When it’s surprised or agitated, the 14 fur\nspikes on its back will stand up involuntarily.",
        "has_alt_form": false,
        "id": 777
    },
    {
        "name": "Mimikyu",
        "genus": "Disguise Pokémon",
        "identifier": "mimikyu",
        "evolution_chain": 404,
        "color": "yellow",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 8,
        "type2": 18,
        "flavor_text": "Although it’s a quiet, lonely Pokémon, if you try\nto look at what’s under its rag, it will become\nagitated and resist violently.",
        "has_alt_form": true,
        "id": 778
    },
    {
        "name": "Bruxish",
        "genus": "Gnash Teeth Pokémon",
        "identifier": "bruxish",
        "evolution_chain": 405,
        "color": "pink",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 11,
        "type2": 14,
        "flavor_text": "It burrows beneath the sand, radiating\npsychic power from the protuberance on its\nhead. It waits for prey as it surveys the area.",
        "has_alt_form": false,
        "id": 779
    },
    {
        "name": "Drampa",
        "genus": "Placid Pokémon",
        "identifier": "drampa",
        "evolution_chain": null,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 1,
        "type2": 16,
        "flavor_text": "If a child it has made friends with is bullied,\nDrampa will find the bully’s house and burn it to\nthe ground.",
        "has_alt_form": false,
        "id": 780
    },
    {
        "name": "Dhelmise",
        "genus": "Sea Creeper Pokémon",
        "identifier": "dhelmise",
        "evolution_chain": null,
        "color": "green",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 8,
        "type2": 12,
        "flavor_text": "It wraps its prey in green seaweed and sucks\naway their vitality. It only likes to go after big\nprey like Wailord.",
        "has_alt_form": false,
        "id": 781
    },
    {
        "name": "Jangmo-o",
        "genus": "Scaly Pokémon",
        "identifier": "jangmo-o",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 16,
        "type2": null,
        "flavor_text": "It smacks the scales on its head against rocks\nor against the ground to frighten its opponents.\nIt can also contact its friends with these noises.",
        "has_alt_form": false,
        "id": 782
    },
    {
        "name": "Hakamo-o",
        "genus": "Scaly Pokémon",
        "identifier": "hakamo-o",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": 782,
        "type1": 16,
        "type2": 2,
        "flavor_text": "It makes noise by clanging its scales together.\nWhen the rhythm has reached its peak,\nHakamo-o attacks.",
        "has_alt_form": false,
        "id": 783
    },
    {
        "name": "Kommo-o",
        "genus": "Scaly Pokémon",
        "identifier": "kommo-o",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": 783,
        "type1": 16,
        "type2": 2,
        "flavor_text": "When it howls after finishing off its prey, the\nmetallic sounds of its celebrating comrades can\nbe heard from all around.",
        "has_alt_form": false,
        "id": 784
    },
    {
        "name": "Tapu Koko",
        "genus": "Land Spirit Pokémon",
        "identifier": "tapu-koko",
        "evolution_chain": null,
        "color": "yellow",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 13,
        "type2": 18,
        "flavor_text": "Although it’s called a guardian deity, if a person\nor Pokémon puts it in a bad mood, it will become\na malevolent deity and attack.",
        "has_alt_form": false,
        "id": 785
    },
    {
        "name": "Tapu Lele",
        "genus": "Land Spirit Pokémon",
        "identifier": "tapu-lele",
        "evolution_chain": null,
        "color": "pink",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 14,
        "type2": 18,
        "flavor_text": "It heals the wounds of people and Pokémon by\nsprinkling them with its sparkling scales. This\nguardian deity is worshiped on Akala.",
        "has_alt_form": false,
        "id": 786
    },
    {
        "name": "Tapu Bulu",
        "genus": "Land Spirit Pokémon",
        "identifier": "tapu-bulu",
        "evolution_chain": null,
        "color": "red",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 12,
        "type2": 18,
        "flavor_text": "Although it’s called a guardian deity, it’s violent\nenough to crush anyone it sees as an enemy.",
        "has_alt_form": false,
        "id": 787
    },
    {
        "name": "Tapu Fini",
        "genus": "Land Spirit Pokémon",
        "identifier": "tapu-fini",
        "evolution_chain": null,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 11,
        "type2": 18,
        "flavor_text": "This guardian deity of Poni Island manipulates\nwater. Because it lives deep within a thick fog,\nit came to be both feared and revered.",
        "has_alt_form": false,
        "id": 788
    },
    {
        "name": "Cosmog",
        "genus": "Nebula Pokémon",
        "identifier": "cosmog",
        "evolution_chain": null,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "Even though its helpless, gaseous body can be\nblown away by the slightest breeze, it doesn’t\nseem to care.",
        "has_alt_form": false,
        "id": 789
    },
    {
        "name": "Cosmoem",
        "genus": "Protostar Pokémon",
        "identifier": "cosmoem",
        "evolution_chain": null,
        "color": "blue",
        "since_gen": 7,
        "evolves_from": 789,
        "type1": 14,
        "type2": null,
        "flavor_text": "The king who ruled Alola in times of antiquity\ncalled it the “cocoon of the stars” and built\nan altar to worship it.",
        "has_alt_form": false,
        "id": 790
    },
    {
        "name": "Solgaleo",
        "genus": "Sunne Pokémon",
        "identifier": "solgaleo",
        "evolution_chain": null,
        "color": "white",
        "since_gen": 7,
        "evolves_from": 790,
        "type1": 14,
        "type2": 9,
        "flavor_text": "Sometimes the result of its opening an Ultra\nWormhole is that energy and life-forms from\nother worlds are called here to this world.",
        "has_alt_form": false,
        "id": 791
    },
    {
        "name": "Lunala",
        "genus": "Moone Pokémon",
        "identifier": "lunala",
        "evolution_chain": null,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": 790,
        "type1": 14,
        "type2": 8,
        "flavor_text": "Records of it exist in writings from long, long\nago, where it was known by the name\n“the beast that calls the moon.”",
        "has_alt_form": false,
        "id": 792
    },
    {
        "name": "Nihilego",
        "genus": "Parasite Pokémon",
        "identifier": "nihilego",
        "evolution_chain": null,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 6,
        "type2": 4,
        "flavor_text": "A life-form from another world, it was dubbed\na UB and is thought to produce a\nstrong neurotoxin.",
        "has_alt_form": false,
        "id": 793
    },
    {
        "name": "Buzzwole",
        "genus": "Swollen Pokémon",
        "identifier": "buzzwole",
        "evolution_chain": null,
        "color": "red",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 7,
        "type2": 2,
        "flavor_text": "Although it’s alien to this world and a danger\nhere, it’s apparently a common organism in the\nworld where it normally lives.",
        "has_alt_form": false,
        "id": 794
    },
    {
        "name": "Pheromosa",
        "genus": "Lissome Pokémon",
        "identifier": "pheromosa",
        "evolution_chain": null,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 7,
        "type2": 2,
        "flavor_text": "A life-form that lives in another world, its body\nis thin and supple, but it also possesses\ngreat power.",
        "has_alt_form": false,
        "id": 795
    },
    {
        "name": "Xurkitree",
        "genus": "Glowing Pokémon",
        "identifier": "xurkitree",
        "evolution_chain": null,
        "color": "black",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "Although it’s alien to this world and a danger\nhere, it’s apparently a common organism in the\nworld where it normally lives.",
        "has_alt_form": false,
        "id": 796
    },
    {
        "name": "Celesteela",
        "genus": "Launch Pokémon",
        "identifier": "celesteela",
        "evolution_chain": null,
        "color": "green",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 9,
        "type2": 3,
        "flavor_text": "One of the dangerous UBs, high energy readings\ncan be detected coming from both of its\nhuge arms.",
        "has_alt_form": false,
        "id": 797
    },
    {
        "name": "Kartana",
        "genus": "Drawn Sword Pokémon",
        "identifier": "kartana",
        "evolution_chain": null,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 12,
        "type2": 9,
        "flavor_text": "This Ultra Beast’s body, which is as thin as\npaper, is like a sharpened sword.",
        "has_alt_form": false,
        "id": 798
    },
    {
        "name": "Guzzlord",
        "genus": "Junkivore Pokémon",
        "identifier": "guzzlord",
        "evolution_chain": null,
        "color": "black",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 17,
        "type2": 16,
        "flavor_text": "Although it’s alien to this world and a danger\nhere, it’s apparently a common organism in the\nworld where it normally lives.",
        "has_alt_form": false,
        "id": 799
    },
    {
        "name": "Necrozma",
        "genus": "Prism Pokémon",
        "identifier": "necrozma",
        "evolution_chain": null,
        "color": "black",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 14,
        "type2": null,
        "flavor_text": "It looks somehow pained as it rages around in\nsearch of light, which serves as its energy.\nIt’s apparently from another world.",
        "has_alt_form": false,
        "id": 800
    },
    {
        "name": "Magearna",
        "genus": "Artificial Pokémon",
        "identifier": "magearna",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 9,
        "type2": 18,
        "flavor_text": "It synchronizes its consciousness with others\nto understand their feelings. This faculty makes\nit useful for taking care of people.",
        "has_alt_form": false,
        "id": 801
    },
    {
        "name": "Marshadow",
        "genus": "Gloomdweller Pokémon",
        "identifier": "marshadow",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 2,
        "type2": 8,
        "flavor_text": "It slips into the shadows of others and mimics\ntheir powers and movements. As it improves, it\nbecomes stronger than those it’s imitating.",
        "has_alt_form": false,
        "id": 802
    },
    {
        "name": "Poipole",
        "genus": "Poison Pin Pokémon",
        "identifier": "poipole",
        "evolution_chain": null,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 4,
        "type2": null,
        "flavor_text": "This Ultra Beast is well enough liked to be\nchosen as a first partner in its own world.",
        "has_alt_form": false,
        "id": 803
    },
    {
        "name": "Naganadel",
        "genus": "Poison Pin Pokémon",
        "identifier": "naganadel",
        "evolution_chain": null,
        "color": "purple",
        "since_gen": 7,
        "evolves_from": 803,
        "type1": 4,
        "type2": 16,
        "flavor_text": "It stores hundreds of liters of poisonous liquid\ninside its body. It is one of the organisms known\nas UBs.",
        "has_alt_form": false,
        "id": 804
    },
    {
        "name": "Stakataka",
        "genus": "Rampart Pokémon",
        "identifier": "stakataka",
        "evolution_chain": null,
        "color": "gray",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 6,
        "type2": 9,
        "flavor_text": "It appeared from an Ultra Wormhole. Each one\nappears to be made up of many life-forms\nstacked one on top of each other.",
        "has_alt_form": false,
        "id": 805
    },
    {
        "name": "Blacephalon",
        "genus": "Fireworks Pokémon",
        "identifier": "blacephalon",
        "evolution_chain": null,
        "color": "white",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 10,
        "type2": 8,
        "flavor_text": "It slithers toward people. Then, without warning,\nit triggers the explosion of its own head.\nIt’s apparently one kind of Ultra Beast.",
        "has_alt_form": false,
        "id": 806
    },
    {
        "name": "Zeraora",
        "genus": "Thunderclap Pokémon",
        "identifier": "zeraora",
        "evolution_chain": null,
        "color": "yellow",
        "since_gen": 7,
        "evolves_from": null,
        "type1": 13,
        "type2": null,
        "flavor_text": "It electrifies its claws and tears its opponents\napart with them. Even if they dodge its attack,\nthey’ll be electrocuted by the flying sparks.",
        "has_alt_form": false,
        "id": 807
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
    },
}


