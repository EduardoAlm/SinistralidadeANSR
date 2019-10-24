import Vue from "vue";
import Vuex from "vuex";
import api from "./api/api.js";

Vue.use(Vuex); // only required if you're using modules.
// We're using modules, so there you go.
const apiRoot = "http://localhost:8000";

const store = new Vuex.Store({
  state: {
    login: [],
    registry: []
  },
  mutations: {
    LOGIN: function(state, response) {
      state.login.push(response.body);
    },
    GET_USER: function(state, response) {
      state.login.push(response.body);
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
    login(store) {
      return api
        .get(apiRoot + "/userlogin/")
        .then(response => store.commit("LOGIN", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    get_user(store) {
      return api
        .get(apiRoot + "/user/(?P<cc>.*)/")
        .then(response => store.commit("LOGIN", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    del_user(store, log) {
      return api
        .post(apiRoot + "/login/", log)
        .then(response => store.commit("ADD_LOGIN", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    clearLogin(store) {
      return api
        .delete(apiRoot + "/login/clear_login/")
        .then(response => store.commit("CLEAR_LOGIN", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    getRegistry(store) {
      return api
        .get(apiRoot + "/registry/")
        .then(response => store.commit("GET_REGISTRY", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    addRegistry(store, reg) {
      return api
        .post(apiRoot + "/registry/", reg)
        .then(response => store.commit("ADD_REGISTRY", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    clearRegistry(store) {
      return api
        .delete(apiRoot + "/registry/clear_registry/")
        .then(response => store.commit("CLEAR_REGISTRY", response))
        .catch(error => store.commit("API_FAIL", error));
    }
  }
});

export default store;
