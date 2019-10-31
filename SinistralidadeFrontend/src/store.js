import Vue from "vue";
import Vuex from "vuex";
import api from "./api/api.js";

Vue.use(Vuex); // only required if you're using modules.
// We're using modules, so there you go.
const apiRoot = "http://localhost:8000";

const store = new Vuex.Store({
  state: {
    acidentes: [],
    acidente: [],
    user: [],
    allusers: [],
    allconcelhos: [],
    lastAcID: [],
    concelhosdist: [],
    historicos: [],
    historicolastid: [],
    historico: []
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
    GET_ALLUSER: function(state, response) {
      console.log(response.body);
      state.allusers = response.body;
    },
    GET_ALLCONCELHO: function(state, response) {
      console.log(response.body);
      state.allconcelhos = response.body;
    },
    UPDATE_USERUPDATE: function(state, response) {
      console.log(response.body);
    },
    POST_ACIDENTE: function(state, response) {
      state.acidente.push(response.body);
    },
    UPDATE_ACIDENTE: function(state, response) {
      console.log(response.body);
    },
    UPDATE_ACIDENTEHOSPITAL: function(state, response) {
      console.log(response.body);
    },
    DEL_ACIDENTE: function(state, response) {
      console.log(response.body);
    },
    GET_LASTIDACIDENTES: function(state, response) {
      state.lastAcID = response.body;
      console.log(state.lastAcID);
    },
    GET_CONCELHODIST: function(state, response) {
      state.concelhosdist = response.body;
      console.log(state.concelhosdist);
    },
    GET_HISTORICO: function(state, response) {
      state.historicos = response.body;
      console.log(state.historicos);
    },
    GET_HISTORICOLASTID: function(state, response) {
      state.historicolastid = response.body;
      console.log(state.historicolastid);
    },
    POST_HISTORICO: function(state, response) {
      state.historico.push(response.body);
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
    async del_user(store, cc) {
      console.log(cc);
      return await api
        .post(apiRoot + "/userdel/" + parseInt(cc) + "/")
        .then(response => store.commit("DEL_USER", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async post_user(store, reg) {
      return await api
        .post(apiRoot + "/register/", reg)
        .then(response => store.commit("POST_USER", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_acidente(store, concelho) {
      return await api
        .get(apiRoot + "/acidente/" + concelho + "/")
        .then(response => store.commit("GET_ACIDENTES", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_alluser(store) {
      return await api
        .get(apiRoot + "/userall/")
        .then(response => store.commit("GET_ALLUSER", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_concelhoall(store) {
      return await api
        .get(apiRoot + "/concelhoall/")
        .then(response => store.commit("GET_ALLCONCELHO", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async user_updateall(store, dict) {
      return await api
        .get(
          apiRoot +
            "/userupdate/" +
            dict["cc"] +
            "/" +
            dict["nome"] +
            "/" +
            dict["palavrapassedict"] +
            "/" +
            dict["ocupacao"] +
            "/" +
            dict["n_distrito"] +
            "/"
        )
        .then(response => store.commit("UPDATE_USERUPDATE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async post_acidente(store, ac) {
      return await api
        .post(apiRoot + "/registeracidente/", ac)
        .then(response => store.commit("POST_ACIDENTE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async update_acidente(store, dict) {
      return await api
        .get(
          apiRoot +
            "/acidenteupdate/" +
            parseInt(dict["id"]) +
            "/" +
            dict["concelho"] +
            "/" +
            parseInt(dict["mortos"]) +
            "/" +
            parseInt(dict["feridosg"]) +
            "/" +
            dict["via"] +
            "/" +
            dict["km"] +
            "/" +
            dict["natureza"] +
            "/"
        )
        .then(response => store.commit("UPDATE_ACIDENTE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async update_acidentehospital(store, dict) {
      return await api
        .get(
          apiRoot +
            "/acidenteuphospital/" +
            parseInt(dict["id"]) +
            "/" +
            parseInt(dict["mortos"]) +
            "/" +
            parseInt(dict["feridosg"]) +
            "/"
        )
        .then(response => store.commit("UPDATE_ACIDENTEHOSPITAL", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async del_acidente(store, id) {
      return await api
        .post(apiRoot + "/acidentedel/" + parseInt(id) + "/")
        .then(response => store.commit("DEL_ACIDENTE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async acidenteget_lastid(store) {
      return await api
        .get(apiRoot + "/acidentelastid/")
        .then(response => store.commit("GET_LASTIDACIDENTES", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_concelhodist(store, distrito) {
      return await api
        .get(apiRoot + "/concelhodist/" + distrito + "/")
        .then(response => store.commit("GET_CONCELHODIST", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_historico(store, id) {
      return await api
        .get(apiRoot + "/historicoget/" + id + "/")
        .then(response => store.commit("GET_HISTORICO", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async get_lastidhistorico(store) {
      return await api
        .get(apiRoot + "/historicogetlastid/")
        .then(response => store.commit("GET_HISTORICOLASTID", response))
        .catch(error => store.commit("API_FAIL", error));
    },

    async post_historico(store, his) {
      return await api
        .post(apiRoot + "/historicopost/", his)
        .then(response => store.commit("POST_HISTORICO", response))
        .catch(error => store.commit("API_FAIL", error));
    }
  }
});

export default store;
