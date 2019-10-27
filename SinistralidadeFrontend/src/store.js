import Vue from "vue";
import Vuex from "vuex";
import api from "./api/api.js";

Vue.use(Vuex); // only required if you're using modules.
// We're using modules, so there you go.
const apiRoot = "http://localhost:8000";

const store = new Vuex.Store({
  state: {
    acidentes: [],
    user: []
  },
  mutations: {
    GET_USER: function(state, response) {
      console.log(state.user);
      state.user = response.body;
    },
    POST_USER: function(state, response) {
      state.user.push(response.body);
    },
    DEL_USER: function(state) {
      const user = state.user;
      user.splice(0, user.length);
    },
    GET_ACIDENTES: function(state, response) {
      console.log(response.body);
      state.acidentes = response.body;
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
        .post(apiRoot + "/user/", log)
        .then(response => store.commit("DEL_USER", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async post_user(store, reg) {
      return await api
        .post(apiRoot + "/register/", reg)
        .then(response => store.commit("POST_USER", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_acidentes(store, concelho) {
      return await api
        .get(apiRoot + "/acidentes/" + concelho + "/")
        .then(response => store.commit("GET_ACIDENTES", response))
        .catch(error => store.commit("API_FAIL", error));
    }
  }
});

export default store;
