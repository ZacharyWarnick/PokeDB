<template>
  <div class="about">
    <Navbar />
    <b-jumbotron header="About">
      <p class="lead">
        This website develops database (similar to IMDb) has 3 kinds of pages or
        subjects that form the database.<br />
        All 3 pages or subjects are connected and each item in the database
        belongs to 1 type of page or subject and has links to items in the other
        2 subjects.<br />
        The database for this group will be a Pokémon database. The 3 kinds of
        pages or subjects will be Pokémon, Pokémon Type, and Evolution Chain.
      </p>
    </b-jumbotron>

    <section class="text-left section-padding">
      <h1>Gold Team</h1>
      <br />
      <h3>Members:</h3>
    </section>

    <section
      v-for="person in data"
      :key="person.full_name"
      class="section-padding"
    >
      <b-container fluid>
        <b-row>
          <b-col lg="2" md="3" sm="6" cols="12">
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
          <b-col lg="2" md="3" sm="3" cols="6" class="text-center my-auto">
            <p>{{ person.commits }} of commits</p>
            <p>{{ person.issues }} of issues</p>
            <p>{{ person.tests }} unit tests</p>
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="text-left section-padding">
      <h3>Repo Information:</h3>
    </section>

    <section class="section-padding">
      <b-container>
        <b-row>
          <b-col>
            <a href="https://gitlab.com/jacoblubecki/cs329e-idb/issues">
              Gitlab Issue Tracker</a
            >
          </b-col>
          <b-col>
            <a href="https://gitlab.com/jacoblubecki/cs329e-idb">
              Gitlab Repo</a
            >
          </b-col>
          <b-col>
            <a href="https://gitlab.com/jacoblubecki/cs329e-idb/wikis/home">
              Gitlab Technical Report (Wiki)</a
            >
          </b-col>
        </b-row>
      </b-container>
    </section>

    <section class="text-left section-padding">
      <h3>Tools:</h3>
    </section>

    <section class="section-padding">
      <b-container>
        <b-row class="align-items-stretch">
          <b-col>
            <b-card class="h-100">
              <div>
                <img
                  class="tool-image"
                  src="https://vuejs.org/images/logo.png"
                />
                <b-card-title class="section-padding">Vue.js</b-card-title>
                <b-card-text>The Progressive JavaScript Framework</b-card-text>
                <b-button
                  href="https://vuejs.org/"
                  variant="outline-primary-dark"
                  >Website</b-button
                >
              </div>
            </b-card>
          </b-col>
          <b-col>
            <b-card class="h-100">
              <div style="background-color: #563d7c">
                <img
                  class="svg tool-image"
                  src="https://getbootstrap.com/docs/4.3/assets/brand/bootstrap-outline.svg"
                />
              </div>
              <b-card-title class="section-padding">Bootstrap</b-card-title>
              <b-card-text
                >The most popular HTML, CSS, and JS library in the
                world.</b-card-text
              >
              <b-button
                href="https://getbootstrap.com"
                variant="outline-primary-dark"
                >Website</b-button
              >
            </b-card>
          </b-col>
          <b-col>
            <b-card class="h-100">
              <div>
                <img
                  class="svg tool-image"
                  src="http://flask.pocoo.org/docs/0.12/_static/flask.png"
                />
              </div>
              <b-card-title class="section-padding">Flask</b-card-title>
              <b-card-text>Web development, one drop at a time.</b-card-text>
              <b-button
                href="http://flask.pocoo.org/"
                variant="outline-primary-dark"
                >Website</b-button
              >
            </b-card>
          </b-col>
          <b-col>
            <b-card class="h-100">
              <div>
                <img
                  class="tool-image"
                  src="https://cloud.google.com/_static/images/cloud/icons/favicons/onecloud/apple-icon.png"
                />
              </div>
              <b-card-title class="section-padding"
                >Google Cloud Platform</b-card-title
              >
              <b-card-text>See what's possible with Google Cloud.</b-card-text>
              <b-button
                href="https://getbootstrap.com"
                variant="outline-primary-dark"
                >Website</b-button
              >
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>
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
      data: [
        {
          full_name: "Ian Chang",
          picture: require("../assets/team/ian.jpg"),
          bio: [
            "Ian Chang is pretty dumb. I don't know how he made it this far. He's",
            "getting carried and will probably have to drop out."
          ].join(" "),
          responsibilities: "",
          commits: 0,
          issues: 0,
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
          commits: 0,
          issues: 0,
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
          commits: 0,
          issues: 0,
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
          commits: 0,
          issues: 0,
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
          commits: 0,
          issues: 0,
          tests: 0
        }
      ]
    };
  }
};
</script>

<style scoped>
.section-padding {
  padding: 30px;
}

.tool-image {
  margin: 16px;
  width: 144px;
  height: 144px;
}
</style>

