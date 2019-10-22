import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

const v = new Vue({
  router,
  store: store,
  render: h => h(App)
}).$mount("#app");

v.$store.dispatch("getLogin");
v.$store.dispatch("getRegistry");
