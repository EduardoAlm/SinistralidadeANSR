import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex); // only required if you're using modules.
// We're using modules, so there you go.

const store = new Vuex.Store({
  state: {
    login: [{ text: "John Doe" }],
    registry: [{}]
  },
  mutations: {
    ADD_LOGIN: function(state, log) {
      state.login.push(log);
    },
    CLEAR_LOGIN: function(state) {
      const login = state.login;
      login.splice(0, login.length);
    },
    ADD_REGISTRY: function(state, reg) {
      state.registry.push(reg);
    },
    CLEAR_REGISTRY: function(state) {
      const registry = state.registry;
      registry.splice(0, registry.length);
    }
  },
  actions: {
    addLogin(store, log) {
      store.commit("ADD_LOGIN", log);
    },
    clearLogin(store) {
      store.commit("CLEAR_LOGIN");
    },
    addRegistry(store, reg) {
      store.commit("ADD_REGISTRY", reg);
    },
    clearRegistry(store) {
      store.commit("CLEAR_REGISTRY");
    }
  }
});

export default store;
