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
            v-for="c in this.concelhosdist"
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
          <th>Histórico</th>
          <th></th>
        </tr>
        <tr
          v-for="ac in acidentes"
          v-bind:key="ac.id"
          class="w3-hover-light-gray"
          @click="selectAcidente(ac.id, ac.concelho, ac.ocupacao, ac.datahora, ac.mortos, ac.feridosg, ac.via,ac.km, ac.natureza);getHistorico(ac.id)"
        >
          <td>{{ ac.id }}</td>
          <td>{{ ac.concelho }}</td>
          <td>{{ ac.datahora }}</td>
          <td>{{ ac.mortos }}</td>
          <td>{{ ac.feridosg }}</td>
          <td>{{ ac.via }}</td>
          <td>{{ ac.km }}</td>
          <td>{{ ac.natureza }}</td>
          <td>
            <button class="w3-button w3-orange w3-round" @click="modalHistorico()">Ver histórico</button>
          </td>
          <td>
            <button class="w3-button w3-blue w3-round" @click="modalUpdateAcidente()">Atualizar</button>
          </td>
        </tr>
      </table>
      <p>&nbsp;</p>
    </div>
    <modal name="historicoModal" height="auto" :scrollable="true">
      <div class="w3-container w3-row">
        <div class="w3-cell-row">
          <div class="w3-container w3-cell-top w3-display-topleft">
            <h3 class="w3-text-blue" style="margin-top:10px">Histórico do Acidente</h3>
          </div>
          <div class="w3-container w3-cell-top w3-display-topright">
            <button
              class="w3-button w3-white w3-border-white w3-shadow-white w3-hover-white"
              style="width:40px;height:30px"
              @click="$modal.hide('historicoModal')"
            >
              <img src="../../assets/img/cross.png" style="width:20px;heigth:30px" />
            </button>
          </div>
        </div>
        <p></p>
      </div>
      <p>&nbsp;</p>
      <table class="w3-table w3-bordered w3-centered w3-striped">
        <tr>
          <th>Id do Histórico</th>
          <th>Data e Hora de Alteração</th>
          <th>Alterado Por</th>
          <th>Id do Acidente</th>
        </tr>
        <tr v-for="ac in historicobyid" v-bind:key="ac.id" class="w3-hover-light-gray">
          <td>{{ ac.id }}</td>
          <td>{{ ac.datahora }}</td>
          <td>{{ ac.cc_user }}</td>
          <td>{{ ac.id_acidente }}</td>
        </tr>
      </table>
    </modal>
    <modal name="atualizarAcidenteModal" height="auto" :scrollable="true">
      <div class="w3-container w3-row">
        <div class="w3-cell-row">
          <div class="w3-container w3-cell-top w3-display-topleft">
            <h3 class="w3-text-blue" style="margin-top:10px">Atualizar Acidente</h3>
          </div>
          <div class="w3-container w3-cell-top w3-display-topright">
            <button
              class="w3-button w3-white w3-border-white w3-shadow-white w3-hover-white"
              style="width:40px;height:30px"
              @click="$modal.hide('atualizarAcidenteModal')"
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
              class="w3-opacity dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
              style="border:2px solid grey"
              disabled
            >
              {{this.concelho}}
              <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
            </button>
            <div class="dropdown-content" style="max-height:350px;
        overflow:auto;"></div>
          </div>
          <hr style="border: 0.7px solid gray;" />
          <h5>Data e Hora:</h5>
          <input
            :id="datahora"
            v-model="datahora"
            class="w3-opacity w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
            disabled
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Mortos:</h5>
          <input
            :id="mortos"
            v-model="mortos"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="number"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Feridos Graves:</h5>
          <input
            :id="feridosg"
            v-model="feridosg"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="number"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Via:</h5>
          <input
            :id="via"
            v-model="via"
            class="w3-opacity w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
            disabled
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Km:</h5>
          <input
            :id="km"
            v-model="km"
            class="w3-opacity w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
            disabled
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Natureza:</h5>
          <input
            :id="natureza"
            v-model="natureza"
            class="w3-opacity w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
            disabled
          />
        </div>
      </div>
      <p>&nbsp;</p>

      <button class="w3-button w3-round w3-green w3-hover-opacity" @click="updateAcidente">Atualizar</button>
    </modal>
  </div>
</template>
<script>
export default {
  name: "HospitalComponent",
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
      natureza: "",
      userInfo: [],
      userCC: []
    };
  },
  computed: {
    concelhos() {
      return this.$store.state.allconcelhos;
    },
    concelhosdist() {
      return this.$store.state.concelhosdist;
    },
    acidentes() {
      return this.$store.state.acidentes;
    },
    historicobyid() {
      return this.$store.state.historicobyid;
    },
    historicolastid() {
      return this.$store.state.historicolastid;
    },
    historicof() {
      return this.$store.state.historico;
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
    modalHistorico: function() {
      this.$modal.show("historicoModal");
    },
    modalUpdateAcidente: function() {
      this.$modal.show("atualizarAcidenteModal");
    },
    getAcidente: async function(concelho) {
      await this.$store.dispatch("get_acidente", concelho);
      console.log(this.acidentes);
    },
    getAc(concelho) {
      this.getAcidente(concelho);
    },
    getConcelhos: async function() {
      await this.$store.dispatch("get_concelhodist", this.userInfo);
      console.log(this.concelhosdist);
    },
    getHistorico: async function() {
      await this.$store.dispatch("get_historico", this.id);
      console.log(this.historicobyid);
    },
    getHistoricoLastId: async function() {
      await this.$store.dispatch("get_lastidhistorico");
      console.log(this.historicolastid);
    },
    createHistorico: async function(dict) {
      await this.$store.dispatch("post_historico", dict);
      console.log(this.historico);
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
    updateAcidente: async function() {
      var dict = {};
      dict["id"] = this.id;
      dict["cc"] = this.userCC;
      dict["mortos"] = this.mortos;
      dict["feridosg"] = this.feridosg;
      var dict1 = {};

      await this.$store.dispatch("update_acidentehospital", dict);

      await this.$store.dispatch("get_lastidhistorico");
      console.log(this.historicolastid);
      if (this.historicolastid.status == 404) {
        dict1["id"] = 1;
        dict1["datahora"] = this.datahora;
        dict1["cc_user"] = this.userCC;
        dict1["id_acidente"] = this.id;
        console.log(dict1);
      } else {
        dict1["id"] = this.historicolastid[0].id + 1;
        dict1["datahora"] = this.datahora;
        dict1["cc_user"] = this.userCC;
        dict1["id_acidente"] = this.id;
      }
      this.createHistorico(dict1);
      this.myInput = this.concelho;
      this.getAc(this.concelho);
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
    var userInfo = JSON.parse(localStorage.getItem("userInfo"));
    this.userInfo = userInfo[0].n_distrito;
    this.userCC = userInfo[0].cc;
    console.log(this.userInfo);
    this.getConcelhos();
  }
};
</script>