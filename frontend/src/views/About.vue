<template>
  <div class="about">
    <Navbar />
    <div class="fade-container">
    <b-jumbotron header="About">
      <p class="lead text-justify">
        This website develops database (similar to IMDb) has 3 kinds of pages or
        subjects that form the database.
        All 3 pages or subjects are connected and each item in the database
        belongs to 1 type of page or subject and has links to items in the other
        2 subjects.
        The database for this group will be a Pokémon database. The 3 kinds of
        pages or subjects will be Pokémon, Pokémon Type, and Evolution Chain.
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
                <div class="justify-content-center" :style="tool.img_bg_style">
                  <img class="tool-image img-fluid" :src="tool.image_url" />
                </div>
                <b-card-title class="card-padding">{{
                  tool.name
                }}</b-card-title>
                <b-card-text class="card-padding my-auto">{{ tool.tagline }}</b-card-text>
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
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

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
            "Ian Chang is pretty dumb. I don't know how he made it this far. He's",
            "getting carried and will probably have to drop out."
          ].join(" "),
          responsibilities: "",
          commits: 5,
          issues: 3,
          tests: 0
        },
        {
          full_name: "Tyler Chinn",
          picture: require("../assets/team/tyler.jpg"),
          bio: [
            "Tyler Chinn born and raised in the Sahara Desert. There he found his",
            "calling to be a software engineer."
          ].join(" "),
          responsibilities: "",
          commits: 19,
          issues: 3,
          tests: 0
        },
        {
          full_name: "Guillermo Gallegos",
          picture: require("../assets/team/guillermo.jpg"),
          bio: [
            "Guillermo Gallegos grew up in Antartica. He fought polar bears for",
            "a living, but now he found his passion as a web developer."
          ].join(" "),
          responsibilities: "",
          commits: 7,
          issues: 2,
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
          responsibilities: "",
          commits: 68,
          issues: 5,
          tests: 0
        },
        {
          full_name: "Zack Warnick",
          picture: require("../assets/team/zack.jpg"),
          bio: [
            "Zack Warnick. The man from the moon. People say he's an alien because of",
            "his amazing coding skills."
          ].join(" "),
          responsibilities: "",
          commits: 22,
          issues: 1,
          tests: 0
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
          tagline: "The most popular HTML, CSS, and JS library in the world.",
          website: "https://getbootstrap.com",
          image_url:
            "https://getbootstrap.com/docs/4.3/assets/brand/bootstrap-outline.svg",
          img_bg_style: "background-color: #563d7c"
        },
        {
          name: "Flask",
          tagline: "Web development, one drop at a time.",
          website: "http://flask.pocoo.org/",
          image_url: "http://flask.pocoo.org/docs/0.12/_static/flask.png"
        },
        {
          name: "Google Cloud Platform",
          tagline: "See what's possible with Google Cloud.",
          website: "https://cloud.google.com/",
          image_url:
            "https://cloud.google.com/_static/images/cloud/icons/favicons/onecloud/apple-icon.png"
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
.fade-container {
	animation: FadeIn 1.5s 1 forwards;
}
@keyframes FadeIn {
  0%{
    opacity: 0
  }
  
  100% {
    opacity: 1;
  }
}
</style>

