<template>
  <div id="app">
    <div v-if="this.loggedIn == 1">
      <Nav2></Nav2>
    </div>
    <div v-else>
      <Nav></Nav>
    </div>

    <router-view></router-view>
  </div>
</template>

<script>
import Nav from "./components/mainPage/Nav.vue";
import Nav2 from "./components/mainPage/Nav2.vue";
import * as Cookies from "js-cookie";

export default {
  name: "app",
  data() {
    return {
      loggedIn: 0
    };
  },
  mounted() {
    this.loggedIn = Cookies.get("loggedIn");
  },
  components: {
    Nav: Nav,
    Nav2: Nav2
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
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
</style>
