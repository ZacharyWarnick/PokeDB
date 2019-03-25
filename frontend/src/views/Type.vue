<template>
  <div class="Type" style="padding-left">
    <Navbar/>
    <div class="jumbotron">
      <h1>{{ $route.params.id }}</h1>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <p class="lead">Short description of the type. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime, enim odit! Veritatis quae consectetur voluptate obcaecati, quos est porro autem. Dignissimos libero quam doloribus! Eligendi corporis harum hic similique qui.</p>
        </div>
        <div class="col-md-6">
          <svg class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="300" height="300" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 300x300"><title>Placeholder</title><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" fill="#aaa" dy=".3em">300x300</text></svg>
        </div>
      </div>
    
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis perferendis possimus magnam vel laborum, esse facere laboriosam porro ea blanditiis. Saepe animi consequuntur commodi, at molestias minus quae rem harum!</p>
        </div>

        <div class="col-md-6">
          <div class="container">
          <table class="table">
            <thead>
              <tr>
                <th class="table-strong" scope="col">Strong Against</th>
                <th class="table-weak" scope="col">Weak Against</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="table-strong">Ice</td>
                <td class="table-weak">Rock</td>
              </tr>
              <tr>
                <td class="table-strong">Steel</td>
                <td class="table-weak">Water</td>
              </tr>
            </tbody>
          </table>          
          </div>
        </div>

    <div class="container">
      <h2>Pokemon of this type:</h2>
      <div class="row">
        <div class="col-md-4">
            <div class="card sm-4 shadow-sm">
              <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
              <div class="card-body">
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  </div>
                </div>
              </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card sm-4 shadow-sm">
              <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
              <div class="card-body">
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  </div>
                </div>
              </div>
            </div>
        </div>

        <div class="col-md-4">
          <div class="card sm-4 shadow-sm">
            <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
            <div class="card-body">
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                </div>
              </div>
            </div>
          </div>

        </div>                
      </div>
    </div>

    </div>
    </div>
    </div>
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

<!--
Color of tables or fromatting subject to change
-->
<style scoped>
  .container {
    margin-top: 20px;
    margin-bottom: 10px;
    align-items: center;
  };

  .jumbotron {
    text-align: center;
  }

  .table-strong {
    background-color: rgba(0, 128, 0, 0.7);
  }

  .table-weak {
    background-color: rgba(255, 0, 0, 0.7);

  };
</style>