<template>
  <div class="w3-container">
    <div class="component-container" style="width: 100%">
      <div class="dropdown">
        <button
          class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
          style="border:2px solid grey"
        >
          {{this.myInput}}
          <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
        </button>
        <div class="dropdown-content" style="max-height:350px;
   overflow:auto;">
          <a
            v-for="concelho in this.concelhos"
            v-bind:key="concelho.id"
            @click="getAc(concelho.nome)"
          >{{concelho.nome}}</a>
        </div>
      </div>

      <p>&nbsp;</p>
      <table class="w3-table w3-bordered w3-centered w3-striped">
        <tr>
          <th>Id</th>
          <th>Concelho</th>
          <th>Data e Hora</th>
          <th>Mortos</th>
          <th>Feridos Graves</th>
          <th>Via</th>
          <th>Km</th>
          <th>Natureza</th>
        </tr>
        <tr v-for="ac in acidentes" v-bind:key="ac.id" class="w3-hover-light-gray">
          <td>{{ ac.id }}</td>
          <td>{{ ac.concelho }}</td>
          <td>{{ ac.datahora }}</td>
          <td>{{ ac.mortos }}</td>
          <td>{{ ac.feridosg }}</td>
          <td>{{ ac.via }}</td>
          <td>{{ ac.km }}</td>
          <td>{{ ac.natureza }}</td>
        </tr>
      </table>
      <p>&nbsp;</p>
      <button class="w3-button w3-green w3-round w3-margin-right">Criar</button>
      <button class="w3-button w3-green w3-round">Atualizar</button>
      <button class="w3-button w3-green w3-round w3-margin-left">Apagar</button>
    </div>
    <p>&nbsp;</p>
    <div class="component-container" style="width: 100%">
      <table class="w3-table w3-bordered w3-centered w3-striped">
        <tr>
          <th>Número de Cartão de Cidadão</th>
          <th>Nome</th>
          <th>Ocupação</th>
          <th>Distrito</th>
        </tr>
        <tr v-for="user in this.users" v-bind:key="user.id" class="w3-hover-light-gray">
          <td>{{ user.cc }}</td>
          <td>{{ user.nome }}</td>
          <td>{{ user.ocupacao }}</td>
          <td>{{ user.n_distrito }}</td>
        </tr>
      </table>
      <p>&nbsp;</p>
      <button class="w3-button w3-green w3-round w3-margin-right">Criar</button>
      <button class="w3-button w3-green w3-round">Atualizar</button>
      <button class="w3-button w3-green w3-round w3-margin-left">Apagar</button>
    </div>
  </div>
</template>
<script>
export default {
  name: "GestorComponent",
  data() {
    return {
      myInput: "Selecione o concelho",
      imageUrl: require("../../assets/img/favicon-16x16.png")
    };
  },
  computed: {
    concelhos() {
      return this.$store.state.allconcelhos;
    },
    users() {
      return this.$store.state.allusers;
    },
    acidentes() {
      return this.$store.state.acidentes;
    }
  },
  methods: {
    getAcidente: async function(concelho) {
      await this.$store.dispatch("get_acidente", concelho);
      console.log(this.acidentes);
    },
    getAc(concelho) {
      this.getAcidente(concelho);
    },
    getUtilizadores: async function() {
      await this.$store.dispatch("get_alluser");

      console.log(this.users);
    },
    getConcelhos: async function() {
      await this.$store.dispatch("get_concelhoall");

      console.log(this.concelhos);
    }
  },
  mounted() {
    this.getUtilizadores();
    this.getConcelhos();
  }
};
</script>