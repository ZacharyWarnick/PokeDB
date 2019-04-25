<template>
  <section class="section-padding">
    <b-container>
      <b-row class="align-items-stretch justify-content-center">
        <b-col
          class="data-card"
          cols="12"
          sm="6"
          md="6"
          lg="3"
          v-for="item in items"
          :key="item.name"
        >
          <b-card class="h-100">
            <b-card-body class="h-100 d-flex flex-column">
              <div
                class="card-img-box justify-content-center"
                :style="item.img_bg_style"
              >
                <img class="data-image img-fluid" :src="item.image_url" />
              </div>
              <b-card-title class="info-title my-auto">{{
                item.name
              }}</b-card-title>
              <b-card-text class="card-padding">{{ item.tagline }}</b-card-text>
              <b-button
                :href="item.website"
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
</template>

<script>
export default {
  name: "InfoCards",
  props: {
    items: Array
  }
};
</script>

<style scoped>
.info-title {
  padding: 10px 0;
}

.card-padding {
  padding-top: 0.75rem;
}

.card-img-box {
  height: 144px;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.data-image {
  padding: 0 15px;
  max-height: 120px;
  max-width: 150px;
}

.data-card {
  margin-top: 15px;
  margin-bottom: 15px;
}
</style>
