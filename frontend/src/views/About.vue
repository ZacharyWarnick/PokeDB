<template>
  <div class="about">
    <Navbar />
    <img class="bg" src="../assets/home-background.jpg" />
    <b-container id="main-content">
      <div class="text-scroll-bg fade-container">
        <b-jumbotron header="About">
          <p class="lead text-justify">
            This website develops database (similar to IMDb) has 3 kinds of
            pages or subjects that form the database. All 3 pages or subjects
            are connected and each item in the database belongs to 1 type of
            page or subject and has links to items in the other 2 subjects. The
            database for this group will be a Pokémon database. The 3 kinds of
            pages or subjects will be Pokémon, Pokémon Type, and Evolution
            Chain.
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
              <b-col lg="2" md="3" sm="4" cols="12" class="text-center my-auto">
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

        <InfoCards :items="info_sources" />

        <section class="text-left section-padding">
          <b-container>
            <h3>Tools:</h3>
          </b-container>
        </section>

        <InfoCards :items="tools" />

        <section class="text-left section-padding">
          <b-container>
            <b-row>
              <b-col>
                <h3>Tests:</h3>
              </b-col>
              <b-col class="ml-auto">
                <img
                  id="help-icon"
                  align="right"
                  src="@/assets/ic-help.svg"
                  class="svg"
                  v-b-tooltip.hover.topleft="term_tooltip"
                />
              </b-col>
            </b-row>
          </b-container>
          <TestResults />
          <b-container>
            <p class="hint-text">
              <strong>Note:</strong> It may take a few seconds.
            </p>
          </b-container>
        </section>
      </div>
    </b-container>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import InfoCards from "@/components/InfoCards.vue";
import TestResults from "@/components/TestResults.vue";

export default {
  name: "About",
  components: {
    Navbar,
    InfoCards,
    TestResults
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
          responsibilities:
            "Team Leader, Back-end, Front-end, and Database Development",
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
      info_sources: [
        {
          name: "Veekun Pokédex",
          tagline: "More than you ever wanted to know about Pokémon",
          website: "https://github.com/veekun/pokedex",
          image_url:
            "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
        },
        {
          name: "Bulbapedia",
          tagline: "The community-driven Pokémon encyclopedia",
          website: "https://bulbapedia.bulbagarden.net/wiki/Main_Page",
          image_url:
            "https://cdn.bulbagarden.net/upload/thumb/d/d4/Bulbapedia_bulb.png/120px-Bulbapedia_bulb.png"
        },
        {
          name: "Pokémon Database",
          tagline: "The fastest way to get your Pokémon information",
          website: "https://pokemondb.net/",
          image_url:
            "https://archives.bulbagarden.net/media/upload/4/40/493Arceus_Normal_Dream.png"
        }
      ],
      tools: [
        {
          name: "Flask",
          tagline: "Web development, one drop at a time",
          website: "http://flask.pocoo.org/",
          image_url: "http://flask.pocoo.org/docs/0.12/_static/flask.png"
        },
        {
          name: "Flask SQLAlchemy",
          tagline: "Extending Flask with the database toolkit for Python",
          website: "https://flask-sqlalchemy.palletsprojects.com/en/2.x/",
          image_url:
            "https://flask-sqlalchemy.palletsprojects.com/en/2.x/_static/flask-sqlalchemy-logo.png"
        },
        {
          name: "PostgreSQL",
          tagline: "The world's most advanced open source relational database",
          website: "https://www.postgresql.org/",
          image_url:
            "https://www.postgresql.org/media/img/about/press/elephant.png"
        },
        {
          name: "Namecheap",
          tagline: "Every website starts with a great domain name",
          website: "https://www.namecheap.com/",
          image_url:
            "https://cdn.shopify.com/s/files/1/0286/7496/t/4/assets/logo.png"
        },
        {
          name: "Vue.js",
          tagline: "The progressive JavaScript framework",
          website: "https://vuejs.org",
          image_url: "https://vuejs.org/images/logo.png"
        },
        {
          name: "BootstrapVue",
          tagline:
            "The most comprehensive implementation of Bootstrap for Vue.js",
          website: "https://bootstrap-vue.js.org/",
          image_url: "https://bootstrap-vue.js.org/_nuxt/img/f0a8c9e.png"
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
          name: "Google Cloud Platform",
          tagline: "See what's possible with Google Cloud",
          website: "https://cloud.google.com/",
          image_url:
            "https://cloud.google.com/_static/images/cloud/icons/favicons/onecloud/apple-icon.png"
        }
      ],
      term_tooltip:
        "Click the terminal, type until it stops adding characters, then press enter."
    };
  }
};
</script>

<style scoped>
#main-content {
  height: 100%;
  padding-top: 56px;
}

.section-padding {
  padding: 30px 0;
}

.hint-text {
  font-size: 0.85em;
}

#help-icon {
  position: relative;
  bottom: -40px;
  height: 24px;
  margin: 4px;
  width: auto;
  opacity: 0.25;
}

#help-icon:hover {
  opacity: 0.5;
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
  width: auto;

  margin-top: 10px;
  margin-bottom: 10px;
  padding: 30px;
  align-items: center;
  box-shadow: 4px 4px 4px;
}

.bg {
  min-width: 100%;
  height: 100%;

  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}
</style>
