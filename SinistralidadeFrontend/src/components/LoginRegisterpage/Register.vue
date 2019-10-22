<template>
  <div class="w3-container w3-display-middle" style="width: 500px">
    <h1>Register Page</h1>
    <p>&nbsp;</p>
    <div class="component-container" style="width: 100%;
    margin: 0 auto;">
      <h5>Número de cartão de cidadão</h5>
      <input
        :id="nCC"
        v-model="nCC"
        class="w3-input w3-border-5 w3-hover-border-light-green w3-round w3-light-grey"
        style="border:2px solid grey"
        @keypress="checkNull"
        type="number"
      />
      <p>&nbsp;</p>
      <h5>Nome de Utilizador</h5>
      <input
        :id="userName"
        v-model="userName"
        class="w3-input w3-border-5 w3-hover-border-light-green w3-round w3-light-grey"
        style="border:2px solid grey"
        type="text"
        @keypress="checkNull"
      />
      <p>&nbsp;</p>
      <h5>Email</h5>
      <input
        :id="email"
        v-model="email"
        @keypress="checkNull"
        class="w3-input w3-border-5 w3-hover-border-light-green w3-round w3-light-grey"
        style="border:2px solid grey"
        type="email"
      />
      <p>&nbsp;</p>
      <h5>Password</h5>
      <input
        :id="password"
        v-model="password"
        @keypress="checkNull"
        class="w3-input w3-border-5 w3-hover-border-light-green w3-round w3-light-grey"
        style="border:2px solid grey"
        type="password"
      />
      <p>&nbsp;</p>
      <h5>Ocupação</h5>

      <div class="dropdown">
        <button
          class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
          style="border:2px solid grey"
        >
          {{this.myInput}}
          <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
        </button>
        <div class="dropdown-content">
          <a @click="myInput='Médico'" href="#">Médico</a>
          <a @click="myInput='Policia'" href="#">Polícia</a>
          <a @click="myInput='Civil'" href="#">Civil</a>
        </div>
      </div>
      <p>&nbsp;</p>
      <h5>Distrito</h5>
      <div class="dropdown">
        <button
          class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
          style="border:2px solid grey"
        >
          {{this.myInput2}}
          <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
        </button>
        <div class="dropdown-content" style="max-height:100px;
   overflow:auto;">
          <a @click="myInput2='Aveiro' && checkNull" href="#">Aveiro</a>
          <a @click="myInput2='Braga' && checkNull" href="#">Braga</a>
          <a @click="myInput2='Bragança' && checkNull" href="#">Bragança</a>
          <a @click="myInput2='Beja' && checkNull" href="#">Beja</a>
          <a @click="myInput2='Castelo Branco' && checkNull" href="#">Castelo Branco</a>
          <a @click="myInput2='Coimbra' && checkNull" href="#">Coimbra</a>
          <a @click="myInput2='Évora' && checkNull" href="#">Évora</a>
          <a @click="myInput2='Faro' && checkNull" href="#">Faro</a>
          <a @click="myInput2='Guarda' && checkNull" href="#">Guarda</a>
          <a @click="myInput2='Leiria' && checkNull" href="#">Leiria</a>
          <a @click="myInput2='Lisboa' && checkNull" href="#">Lisboa</a>
          <a @click="myInput2='Portalegre' && checkNull" href="#">Portalegre</a>
          <a @click="myInput2='Porto' && checkNull" href="#">Porto</a>
          <a @click="myInput2='Santarém' && checkNull" href="#">Santarém</a>
          <a @click="myInput2='Setúbal' && checkNull" href="#">Setúbal</a>
          <a @click="myInput2='Viana do Castelo' && checkNull" href="#">Viana do Castelo</a>
          <a @click="myInput2='Vila Real' && checkNull" href="#">Vila Real</a>
          <a @click="myInput2='Viseu' && checkNull" href="#">Viseu</a>
        </div>
      </div>
      <p>&nbsp;</p>
      <div v-if="registFlag==false">
        <button
          class="w3-button w3-round w3-green w3-hover-opacity"
          @click="registration"
          disabled
        >Registar</button>
      </div>
      <div v-else>
        <button class="w3-button w3-round w3-green w3-hover-opacity" @click="registration">Registar</button>
      </div>
      <div class="alert alert-success" style="margin-top:20px" v-if="successFlag">
        <strong>Successo.</strong>
        Submeteu os seus dados de registo com sucesso!
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data: function() {
    return {
      password: "",
      email: "",
      userName: "",
      nCC: 0,
      successFlag: false,
      registFlag: false,
      myInput: "Selecione a sua ocupação",
      myInput2: "Selecione o seu distrito",
      imageUrl: require("../../assets/img/favicon-16x16.png")
    };
  },

  methods: {
    checkNull() {
      if (
        this.myInput != "" &&
        this.myInput2 != "" &&
        this.email != "" &&
        this.userName != "" &&
        this.nCC > 1000 &&
        this.password != ""
      ) {
        this.registFlag = true;
      }
      this.registFlag = false;
    },
    registration() {
      this.password = "";
      this.email = "";
      this.userName = "";
      this.nCC = 0;
      this.registFlag = false;
      this.myInput = "Selecione a sua ocupação";
      this.myInput2 = "Selecione o seu distrito";
      this.successFlag = true;
    }
  }
};
</script>

<style>
/* Dropdown Button */
.dropbtn {
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
  background-color: #3e8e41;
}
</style>