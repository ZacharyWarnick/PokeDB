<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#main-content {
  height: 100%;
  padding-top: 56px;
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

.section-padding {
  padding: 15px 0;
}

.fade-container {
  padding-top: 0px;
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
</style>
