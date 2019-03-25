<template>
  <div class="Type" style="padding-left">
    <Navbar/>
    <div class="container">
      <h1>Individual Type</h1>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <table>
            <tr>
              <th><h3>Strong Against</h3></th>
            </tr>
            <tr>
              Ice
            </tr>
            <br/>
            <tr>
              Water
            </tr>
          </table>
        </div>
        <div class="col-sm">
          <table>
            <tr>
              <th><h3>Weak Against</h3></th>        
            </tr>
            <tr>
              Rock
            </tr>
            <br/>
            <tr>
              Steel
            </tr>        
          </table>
        </div>
        <div class="col-sm">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Gatto_europeo4.jpg/250px-Gatto_europeo4.jpg">
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md" style="text-align: left; padding-left: 10px">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta illo velit error ex? Atque quasi vel iste iure voluptatibus. Similique delectus quam expedita eius, dolore optio at nobis ab dolorem?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus velit exercitationem omnis ad eos. Nesciunt repudiandae consequatur vitae molestiae omnis pariatur dolorem delectus, minus perferendis nisi maxime similique ducimus et?
          </div>
      </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-sm">
        <CardItem
          title="Card 1"
          msg="Message for card 1."
          link="/about"
          link_text="About"
        />
       </div>             
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import CardItem from "@/components/CardItem.vue";

export default {
  name: "About",
  components: {
    Navbar
  }
};
</script>

<style scoped>
  .container {
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: aqua
  };
  .table {
    text-align: center
  }
</style>