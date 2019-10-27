<template>
  <div class="w3-container">
    <h1>{{"Informação do Utilizador"}}</h1>

    <p>&nbsp;</p>
    <div class="component-container w3-light-gray">
      <h4>{{"Nome de Utilizador"}}</h4>
      <p></p>
      <div class="component-container">
        <h5>{{this.userInfo[0].nome}}</h5>
      </div>
      <p>&nbsp;</p>
      <h4>{{"Número de Cartão de Cidadão"}}</h4>
      <p></p>
      <div class="component-container">
        <h5>{{this.userInfo[0].cc}}</h5>
      </div>
      <p>&nbsp;</p>
      <h4>{{"Ocupação"}}</h4>
      <p></p>
      <div class="component-container">
        <h5>{{this.userInfo[0].ocupacao}}</h5>
      </div>
      <p>&nbsp;</p>
      <h4>{{"Distrito"}}</h4>
      <p></p>
      <div class="component-container">
        <h5>{{this.userInfo[0].n_distrito}}</h5>
      </div>
      <p>&nbsp;</p>
      <h4>{{"Palavra passe"}}</h4>
      <p></p>
      <div class="component-container">
        <h5>{{this.userInfo[0].palavrapasse}}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AccountInfo",

  data() {
    return {
      userInfo: []
    };
  },
  methods: {},
  mounted() {
    var userInfo = JSON.parse(localStorage.getItem("userInfo"));
    this.userInfo = userInfo;
    console.log(userInfo);
  }
};
</script>