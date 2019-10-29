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
    allconcelhos: []
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
    POST_ACIDENTE:  function(state, response) {
      state.acidente.push(response.body);
    },
    UPDATE_ACIDENTE: function(state, response) {
      console.log(response.body);
    }, 
    DEL_ACIDENTE: function(state, response){
      console.log(response.body);
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
      console.log(parseInt(cc["text"]));
      console.log(parseInt(cc));
      return await api
        .post(apiRoot + "/userdel/"+ parseInt(cc)+"/")
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
    async user_updateall(store, cc, nome, palavrapasse,ocupacao, n_distrito) {
      return await api
        .get(apiRoot + "/userupdate/"+cc+"/"+nome+"/"+palavrapasse+"/"+ocupacao+"/"+n_distrito+"/")
        .then(response => store.commit("UPDATE_USERUPDATE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async post_acidente(store, ac) {
      return await api
        .post(apiRoot + "/registeracidente/", ac)
        .then(response => store.commit("POST_ACIDENTE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async update_acidente(store, id, concelho, mortos, feridosg, via, km, natureza) {
      console.log(concelho);
      console.log(mortos);
      console.log(feridosg);
      console.log(via);
      console.log(km);
      console.log(natureza);
      return await api
        .get(apiRoot + "/acidenteupdate/"+id+"/"+concelho+"/"+mortos+"/"+feridosg+"/"+via+"/"+km+"/"+natureza+"/")
        .then(response => store.commit("UPDATE_ACIDENTE", response))
        .catch(error => store.commit("API_FAIL", error));
    },
    async del_acidente(store, id){
      return await api
        .post(apiRoot + "/acidentedel/" + parseInt(id)+"/")
        .then(response => store.commit("DEL_ACIDENTE", response))
        .catch(error => store.commit("API_FAIL", error));
    }

  }
});

export default store;
