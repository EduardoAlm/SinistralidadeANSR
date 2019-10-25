import Vue from "vue";
import Router from "vue-router";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Home from "./views/Home.vue";
import AccountInfo from "./views/AccountInfo.vue";
import MainUserComponent from "./views/MainUserComponent.vue";
Vue.use(Router);

export const router = new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/login",
      name: "Login",
      component: Login
    },
    {
      path: "/register",
      name: "Register",
      component: Register
    },
    {
      path: "/accInfo",
      name: "AccountInfo",
      component: AccountInfo
    },
    {
      path: "/mainUser",
      name: "MainUserComponent",
      component: MainUserComponent
    }
  ]
});

export default router;
