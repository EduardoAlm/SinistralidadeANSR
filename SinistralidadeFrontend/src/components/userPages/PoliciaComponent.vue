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
            v-for="c in this.concelhos"
            v-bind:key="c.id"
            @click="getAc(c.nome); myInput=c.nome"
          >{{c.nome}}</a>
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
        <tr
          v-for="ac in acidentes"
          v-bind:key="ac.id"
          class="w3-hover-light-gray"
          @click="selectAcidente(ac.id, ac.concelho, ac.ocupacao, ac.datahora, ac.mortos, ac.feridosg, ac.via,ac.km, ac.natureza)"
        >
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
      <button
        class="w3-button w3-green w3-round w3-margin-right"
        @click="modalCreateAcidente()"
      >Criar</button>
    </div>
    <modal name="criarAcidenteModal" height="auto" :scrollable="true">
      <div class="w3-container w3-row">
        <div class="w3-cell-row">
          <div class="w3-container w3-cell-top w3-display-topleft">
            <h3 class="w3-text-blue" style="margin-top:10px">Criar Acidente</h3>
          </div>
          <div class="w3-container w3-cell-top w3-display-topright">
            <button
              class="w3-button w3-white w3-border-white w3-shadow-white w3-hover-white"
              style="width:40px;height:30px"
              @click="$modal.hide('criarAcidenteModal')"
            >
              <img src="../../assets/img/cross.png" style="width:20px;heigth:30px" />
            </button>
          </div>
        </div>
        <p></p>
      </div>
      <p>&nbsp;</p>
      <div class="w3-container w3-row">
        <div class="w3-cell-row">
          <h5 class>Concelho:</h5>
          <div class="dropdown">
            <button
              class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
              style="border:2px solid grey"
            >
              {{this.concelho}}
              <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
            </button>
            <div class="dropdown-content" style="max-height:350px;
        overflow:auto;">
              <a v-for="c in this.concelhos" v-bind:key="c.id" @click="concelho=c.nome">{{c.nome}}</a>
            </div>
          </div>

          <hr style="border: 0.7px solid gray;" />
          <h5>Mortos:</h5>
          <input
            :id="mortos"
            v-model="mortos"
            @keyup="checkNull2"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="number"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Feridos Graves:</h5>
          <input
            :id="feridosg"
            v-model="feridosg"
            @keyup="checkNull2"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="number"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Via:</h5>
          <input
            :id="via"
            v-model="via"
            @keyup="checkNull2"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Km:</h5>
          <input
            :id="km"
            v-model="km"
            @keyup="checkNull2"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Natureza:</h5>
          <input
            :id="natureza"
            v-model="natureza"
            @keyup="checkNull2"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
          />
        </div>
      </div>
      <p>&nbsp;</p>
      <div v-if="registFlag==false">
        <button class="w3-button w3-round w3-green w3-hover-opacity" disabled>Criar</button>
      </div>
      <div v-else>
        <button class="w3-button w3-round w3-green w3-hover-opacity" @click="createAcidente">Criar</button>
      </div>
      <div class="alert alert-success" style="margin-top:20px" v-if="successFlag">
        <strong>Successo.</strong>
        Submeteu os seus dados de registo com sucesso!
      </div>
    </modal>
  </div>
</template>

<script>
export default {
  name: "PoliciaComponent",
  data() {
    return {
      myInput: "Selecione o concelho",
      imageUrl: require("../../assets/img/favicon-16x16.png"),
      successFlag: true,
      id: 0,
      concelho: "Selecione o seu concelho",
      datahora: 0,
      mortos: 0,
      feridosg: 0,
      via: "",
      km: "",
      natureza: ""
    };
  },
  computed: {
    concelhos() {
      return this.$store.state.allconcelhos;
    },
    acidentes() {
      return this.$store.state.acidentes;
    }
  },
  methods: {
    selectAcidente(
      id,
      concelho,
      ocupacao,
      datahora,
      mortos,
      feridosg,
      via,
      km,
      natureza
    ) {
      console.log(id);
      console.log(concelho);
      console.log(mortos);
      console.log(feridosg);
      console.log(via);
      console.log(km);
      console.log(natureza);
      this.id = id;
      this.concelho = concelho;
      this.ocupacao = ocupacao;
      this.datahora = datahora;
      this.mortos = mortos;
      this.feridosg = feridosg;
      this.via = via;
      this.km = km;
      this.natureza = natureza;
    },
    modalCreateAcidente: function() {
      this.$modal.show("criarAcidenteModal");
    },
    getAcidente: async function(concelho) {
      await this.$store.dispatch("get_acidente", concelho);
      console.log(this.acidentes);
    },
    getAc(concelho) {
      this.getAcidente(concelho);
    },
    getConcelhos: async function() {
      await this.$store.dispatch("get_concelhoall");
      console.log(this.concelhos);
    },
    checkNull2() {
      console.log(this.concelho);
      console.log(this.mortos);
      console.log(this.feridosg);
      console.log(this.via);
      console.log(this.km);
      console.log(this.natureza);
      if (
        this.concelho != "" &&
        this.mortos >= 0 &&
        this.feridosg >= 0 &&
        this.via != "" &&
        this.km != "" &&
        this.natureza != ""
      ) {
        this.registFlag = true;
        console.log(this.registFlag);
      } else {
        this.registFlag = false;
        console.log(this.registFlag);
      }
    },

    createAcidente: async function() {
      //funcao para devolver o id do ultimo acidente registrado
      var dict = {};
      var date = new Date();
      dict["concelho"] = this.concelho;
      dict["datahora"] =
        date.getYear() +
        "-" +
        date.getMonth() +
        "-" +
        date.getDay() +
        "T" +
        date.getHours() +
        ":" +
        date.getMinutes() +
        ":" +
        date.getSeconds() +
        "Z";
      dict["mortos"] = this.mortos;
      dict["feridosg"] = this.feridosg;
      dict["via"] = this.via;
      dict["km"] = this.km;
      dict["natureza"] = this.natureza;

      console.log(await this.$store.dispatch("post_acidente", dict));
      this.myInput = this.concelho;

      this.id = 0;
      this.concelho = "Selecione o seu concelho";
      this.datahora = 0;
      this.registFlag = false;
      this.mortos = 0;
      this.feridosg = 0;
      this.via = "";
      this.km = "";
      this.natureza = "";
      this.successFlag = true;
    }
  },
  mounted() {
    this.getConcelhos();
  }
};
</script>