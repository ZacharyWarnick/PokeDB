<template>
  <div class="about">
    <Navbar />
    <div class="bg">
      <div class="fade-container">
        <div class="container text-scroll-bg">
          <b-jumbotron header="About">
            <p class="lead text-justify">
              This website develops database (similar to IMDb) has 3 kinds of
              pages or subjects that form the database. All 3 pages or subjects
              are connected and each item in the database belongs to 1 type of
              page or subject and has links to items in the other 2 subjects.
              The database for this group will be a Pokémon database. The 3
              kinds of pages or subjects will be Pokémon, Pokémon Type, and
              Evolution Chain.
            </p>
          </b-jumbotron>

          <section class="text-left section-padding">
            <b-container>
              <h1>Gold Team</h1>
              <br />
              <h3>Members:</h3>
            </b-container>
          </section>

          <section
            v-for="person in people"
            :key="person.full_name"
            class="section-padding"
          >
            <b-container>
              <b-row>
                <b-col lg="4" md="4" sm="6" cols="12">
                  <img class="img-fluid" :src="person.picture" />
                </b-col>
                <b-col class="text-left">
                  <h4>{{ person.full_name }}</h4>
                  <h5>Bio</h5>
                  <p>{{ person.bio }}</p>
                  <br />
                  <h5>Responsibilites</h5>
                  <p>{{ person.responsibilities }}</p>
                </b-col>
                <b-col
                  lg="2"
                  md="3"
                  sm="4"
                  cols="12"
                  class="text-center my-auto"
                >
                  <p>{{ person.commits }} commits</p>
                  <p>{{ person.issues }} issues</p>
                  <p>{{ person.tests }} unit tests</p>
                </b-col>
              </b-row>
            </b-container>
          </section>

          <section class="text-left section-padding">
            <b-container>
              <h3>Repo Information:</h3>
            </b-container>
          </section>

          <section class="section-padding">
            <b-container>
              <b-row>
                <b-col>
                  <b-button
                    href="https://gitlab.com/jacoblubecki/cs329e-idb/issues"
                    variant="outline-secondary"
                  >
                    Gitlab Issue Tracker</b-button
                  >
                </b-col>
                <b-col>
                  <b-button
                    href="https://gitlab.com/jacoblubecki/cs329e-idb"
                    variant="outline-secondary"
                  >
                    Gitlab Repo</b-button
                  >
                </b-col>
                <b-col>
                  <b-button
                    href="https://gitlab.com/jacoblubecki/cs329e-idb/wikis/home"
                    variant="outline-secondary"
                  >
                    Gitlab Technical Report (Wiki)</b-button
                  >
                </b-col>
              </b-row>
            </b-container>
          </section>

          <section class="text-left section-padding">
            <b-container>
              <h3>Data:</h3>
            </b-container>
          </section>

          <section class="section-padding">
            <b-container>
              <b-row class="align-items-stretch">
                <b-col
                  class="data-card"
                  cols="12"
                  sm="6"
                  md="6"
                  lg="3"
                  v-for="data in data"
                  :key="data.name"
                >
                  <b-card class="h-100">
                    <b-card-body class="h-100 d-flex flex-column">
                      <div
                        class="justify-content-center"
                        :style="data.img_bg_style"
                      >
                        <img
                          class="data-image img-fluid"
                          :src="data.image_url"
                        />
                      </div>
                      <b-card-title class="card-padding">{{
                        data.name
                      }}</b-card-title>
                      <b-card-text class="card-padding my-auto">{{
                        data.tagline
                      }}</b-card-text>
                      <b-button
                        :href="data.website"
                        class="mt-auto"
                        variant="outline-secondary"
                        >Website</b-button
                      >
                    </b-card-body>
                  </b-card>
                </b-col>
              </b-row>
            </b-container>
          </section>

          <section class="text-left section-padding">
            <b-container>
              <h3>Tools:</h3>
            </b-container>
          </section>

          <section class="section-padding">
            <b-container>
              <b-row class="align-items-stretch">
                <b-col
                  class="tool-card"
                  cols="12"
                  sm="6"
                  md="6"
                  lg="3"
                  v-for="tool in tools"
                  :key="tool.name"
                >
                  <b-card class="h-100">
                    <b-card-body class="h-100 d-flex flex-column">
                      <div
                        class="justify-content-center"
                        :style="tool.img_bg_style"
                      >
                        <img
                          class="tool-image img-fluid"
                          :src="tool.image_url"
                        />
                      </div>
                      <b-card-title class="card-padding">{{
                        tool.name
                      }}</b-card-title>
                      <b-card-text class="card-padding my-auto">{{
                        tool.tagline
                      }}</b-card-text>
                      <b-button
                        :href="tool.website"
                        class="mt-auto"
                        variant="outline-secondary"
                        >Website</b-button
                      >
                    </b-card-body>
                  </b-card>
                </b-col>
              </b-row>
            </b-container>
          </section>

          <section class="text-left section-padding">
            <b-container>
              <h3>Tests:</h3>
            </b-container>
          </section>

          <section class="section-padding">
            <b-container>
              <b-row>
                <b-col>
                  <b-button
                    to="/api/tests"
                    variant="outline-secondary"
                  >
                    Run Unit Tests</b-button
                  >
                </b-col>
              </b-row>
            </b-container>
          </section>
          <b-jumbotron header="Results">
            <p class="lead text-justify">
              This is the text-box which displays result of api request.
            </p>
          </b-jumbotron>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import { get_test_results } from "@/api";

export default {
  name: "About",
  components: {
    Navbar
  },
  data() {
    return {
      people: [
        {
          full_name: "Ian Chang",
          picture: require("../assets/team/ian.jpg"),
          bio: [
            "Ian Chang was born and raised in Dallas, Texas. He had graduated high",
            "school within the top 5% of his class and was automatically accepted to",
            "the University of Texas at Austin. He is pursuing a major in",
            "Communication Studies, a certificate in Computer Science, and a minor",
            "in Korean Language. His dream is to become a Full-Stack Developer."
          ].join(" "),
          responsibilities: "Back-end and Front-end Development",
          commits: 21,
          issues: 6,
          tests: 0
        },
        {
          full_name: "Tyler Chinn",
          picture: require("../assets/team/tyler.jpg"),
          bio: [
            "I'm a junior biomedical engineering major from Seattle Washington.",
            "I've lived my whole life in Washington before coming to Texas and",
            "Austin for college. I want to go into the software field, hopefully",
            "applying to a healthcare or medical application that will help people",
            "and make a positive impact on their lives.  My two passions are in",
            "software and medicine so I ideally want to combine the two in my work."
          ].join(" "),
          responsibilities: "Back-end and Front-end Development",
          commits: 22,
          issues: 3,
          tests: 0
        },
        {
          full_name: "Guillermo Gallegos",
          picture: require("../assets/team/guillermo.jpg"),
          bio: [
            "Guillermo Gallegos grew up in El Paso, TX. He transferred from the",
            "University of North Texas to get his bachelor degree in Chemistry",
            "and a certificate in Computer Science. He plans to teach after he",
            "graduates while continuing to acquire experience in computer science",
            "with the hope of eventually working in a cybersecurity related job."
          ].join(" "),
          responsibilities: "Back-end Development",
          commits: 20,
          issues: 3,
          tests: 0
        },
        {
          full_name: "Jacob Lubecki",
          picture: require("../assets/team/jacob.jpg"),
          bio: [
            "Jacob Lubecki is the next big thing.",
            "At the age of 3 years old he was developing software for Google and Microsoft.",
            "People say he's like Steve Jobs or Bill Gates, so people have also given him the nickname Bill Jobs."
          ].join(" "),
          responsibilities: "Team Leader, Back-end, Front-end, and Database Development",
          commits: 114,
          issues: 14,
          tests: 0
        },
        {
          full_name: "Zack Warnick",
          picture: require("../assets/team/zack.jpg"),
          bio: [
            "Zack Warnick. The man from the moon. People say he's an alien because of",
            "his amazing coding skills."
          ].join(" "),
          responsibilities: "Back-end, Front-end, and Database Development",
          commits: 42,
          issues: 5,
          tests: 0
        }
      ],
      data: [
          {
            name: "Veekun",
            tagline: "Python library of data scraped from Pokémon games",
            website: "https://github.com/veekun/pokedex",
            image_url: "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
          },
          {
            name: "Bulbapedia",
            tagline: "An encyclopedia about Pokémon to which anyone can contribute",
            website: "https://bulbapedia.bulbagarden.net/wiki/Main_Page",
            image_url: "https://ahost.bulbagarden.net/content/bulbapedia-mobile.png",
          },
          {
            name: "Pokémon Database",
            tagline: "We believe in making Pokémon information as clear and easy to digest as possible",
            website: "https://pokemondb.net/",
            image_url: "https://img.pokemondb.net/design/header2018z-md-2x.png"
          }
        ],
        tools: [
          {
            name: "Vue.js",
            tagline: "The Progressive JavaScript Framework",
            website: "https://vuejs.org",
            image_url: "https://vuejs.org/images/logo.png"
          },
          {
            name: "Bootstrap",
            tagline: "The most popular HTML, CSS, and JS library in the world",
            website: "https://getbootstrap.com",
            image_url:
              "https://getbootstrap.com/docs/4.3/assets/brand/bootstrap-outline.svg",
            img_bg_style: "background-color: #563d7c"
          },
          {
            name: "Flask",
            tagline: "Web development, one drop at a time",
            website: "http://flask.pocoo.org/",
            image_url: "http://flask.pocoo.org/docs/0.12/_static/flask.png"
          },
          {
            name: "Google Cloud Platform",
            tagline: "See what's possible with Google Cloud",
            website: "https://cloud.google.com/",
            image_url:
              "https://cloud.google.com/_static/images/cloud/icons/favicons/onecloud/apple-icon.png"
          },
          {
            name: "PostgreSQL",
            tagline: "The World's Most Advanced Open Source Relational Database",
            website: "https://www.postgresql.org/",
            image_url: "https://www.postgresql.org/media/img/about/press/elephant.png"
          },
          {
            name: "SQLAlchemy",
            tagline: "The Python SQL Toolkit and Object Relational Mapper",
            website: "https://www.sqlalchemy.org/",
            image_url: "https://www.sqlalchemy.org/img/sqla_logo.png"
          },
          {
            name: "BootstrapVue",
            tagline: "Build responsive, mobile-first projects on the web using Vue.js",
            website: "https://bootstrap-vue.js.org/",
            image_url: "https://bootstrap-vue.js.org/_nuxt/img/f0a8c9e.png"
          },
          {
            name: "Namecheap",
            tagline: "Buy a domain and create your pro web presence",
            website: "https://www.namecheap.com/",
            image_url:
              "https://02.files.namecheap.com/cdn/633/assets/img/logos/namecheap.svg"
          }
          ]
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 30px 0;
}

.card-padding {
  padding: 10px 0;
}

.tool-image {
  padding: 25px;
  max-height: 144px;
}

.tool-card {
  margin-top: 15px;
  margin-bottom: 15px;
}

.data-image {
  padding: 25px;
  max-height: 144px;
}

.data-card {
  margin-top: 15px;
  margin-bottom: 15px;
}

.fade-container {
  animation: FadeIn 1.5s 1 forwards;
}
@keyframes FadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}
.text-scroll-bg {
  background-color: white;
  width: 1920px;
  height: 100%;

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
</style>
