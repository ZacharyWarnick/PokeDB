<template>
  <div class="about">
    <Navbar/>
    <h1>About</h1>
    <p>Repository Information</p>
    <h2>Gold Team</h2>
    <h3>Members:</h3>
    <p>Guillermo Gallegos, Jacob Lubecki, Ian Chang, Tyler Chinn, Zack Warnick</p>
    <h3>Stats:</h3>
    <p>no. commits, issues, unit tests, links to gitlab issue tracker, repo, wiki</p>
    <h3>Data:</h3>
    <p>Link to data sources</p>
    <h3>Tools:</h3>
    <p>Tools used</p>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
  name: "About",
  components: {
    Navbar
  }
};
</script>