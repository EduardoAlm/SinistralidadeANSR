import Vue from "vue";
import Vuex from "vuex";
import api from "./api/api.js";

Vue.use(Vuex); // only required if you're using modules.
// We're using modules, so there you go.
const apiRoot = "http://localhost:8000";

const store = new Vuex.Store({
  state: {
    registry: [],
    user: []
  },
  mutations: {
    GET_USER: function(state, response) {
      console.log(response.body);
      state.user = response.body;
    },
    POST_USER: function(state, response) {
      state.login.push(response.body);
    },
    DEL_USER: function(state) {
      const login = state.login;
      login.splice(0, login.length);
    },
    GET_REGISTRY: function(state, response) {
      state.resgistry = response.body;
    },
    ADD_REGISTRY: function(state, response) {
      state.registry.push(response.body);
    },
    CLEAR_REGISTRY: function(state) {
      const registry = state.registry;
      registry.splice(0, registry.length);
    },
    // Note that we added one more for logging out errors.
    API_FAIL: function(state, error) {
      console.error(error);
    }
  },
  actions: {
    async get_user(store, cc) {
      return await api
        .get(apiRoot + "/user/" + parseInt(cc["text"]) + "/")
        .then(response => store.commit("GET_USER", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async del_user(store, log) {
      return await api
        .post(apiRoot + "/login/", log)
        .then(response => store.commit("ADD_LOGIN", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async post_user(store, reg) {
      return await api
        .post(apiRoot + "/register/", reg)
        .then(response => store.commit("ADD_REGISTRY", response))
        .catch(error => store.commit("API_FAIL", error));
    }
  }
});

export default store;
