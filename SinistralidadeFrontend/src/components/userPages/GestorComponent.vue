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
      <button class="w3-button w3-green w3-round" @click="modalUpdateAcidente()">Atualizar</button>
      <button class="w3-button w3-green w3-round w3-margin-left" @click="deleteAcidente">Apagar</button>
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
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Km:</h5>
          <input
            :id="km"
            v-model="km"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
          />
          <hr style="border: 0.7px solid gray;" />
          <h5>Natureza:</h5>
          <input
            :id="natureza"
            v-model="natureza"
            class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
            style="border:2px solid grey"
            type="text"
          />
        </div>
      </div>
      <p>&nbsp;</p>

      <button class="w3-button w3-round w3-green w3-hover-opacity" @click="updateAcidente">Atualizar</button>
    </modal>
    <p>&nbsp;</p>
    <div class="component-container" style="width: 100%">
      <table class="w3-table w3-bordered w3-centered w3-striped">
        <tr>
          <th>Número de Cartão de Cidadão</th>
          <th>Nome</th>
          <th>Ocupação</th>
          <th>Distrito</th>
        </tr>
        <tr
          v-for="user in this.users"
          v-bind:key="user.id"
          class="w3-hover-light-gray"
          @click="selectUser(user.cc, user.nome, user.ocupacao, user.palavrapasse, user.n_distrito)"
        >
          <td>{{ user.cc }}</td>
          <td>{{ user.nome }}</td>
          <td>{{ user.ocupacao }}</td>
          <td>{{ user.n_distrito }}</td>
        </tr>
      </table>
      <p>&nbsp;</p>
      <button class="w3-button w3-green w3-round w3-margin-right" @click="modalCreateUser()">Criar</button>
      <button class="w3-button w3-green w3-round" @click="modalUpdateUser()">Atualizar</button>
      <button class="w3-button w3-green w3-round w3-margin-left" @click="deleteUser()">Apagar</button>
      <modal name="atualizarUtilizadorModal" height="auto" :scrollable="true">
        <div class="w3-container w3-row">
          <div class="w3-cell-row">
            <div class="w3-container w3-cell-top w3-display-topleft">
              <h3 class="w3-text-blue" style="margin-top:10px">Atualizar Utilizador</h3>
            </div>
            <div class="w3-container w3-cell-top w3-display-topright">
              <button
                class="w3-button w3-white w3-border-white w3-shadow-white w3-hover-white"
                style="width:40px;height:30px"
                @click="$modal.hide('atualizarUtilizadorModal')"
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
            <h5 class>Nome de Utilizador</h5>
            <input
              :id="userName"
              v-model="userName"
              @keyup="checkNull"
              class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
              style="border:2px solid grey"
              type="text"
              name="UserName"
            />
            <hr style="border: 0.7px solid gray;" />
            <h5>Numero de Cartão de Cidadão:</h5>
            <input
              :id="ccNumber"
              v-model="ccNumber"
              @keyup="checkNull"
              class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
              style="border:2px solid grey"
              type="text"
              name="cc"
            />
            <hr style="border: 0.7px solid gray;" />
            <h5>Palavra Passe:</h5>
            <input
              :id="palavraPasse"
              v-model="palavraPasse"
              @keyup="checkNull"
              class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
              style="border:2px solid grey"
              type="text"
              name="palavrapasse"
            />
            <hr style="border: 0.7px solid gray;" />
            <h5>Ocupação:</h5>

            <div class="dropdown">
              <button
                class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
                style="border:2px solid grey"
                name="palavrapasse"
              >
                {{this.Ocupacao}}
                <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
              </button>
              <div class="dropdown-content">
                <a @click="Ocupacao='Hospital'" href="#">Hospital</a>
                <a @click="Ocupacao='Policia'" href="#">Polícia</a>
                <a @click="Ocupacao='Civil'" href="#">Civil</a>
                <a @click="Ocupacao='Gestor'" href="#">Gestor</a>
              </div>
            </div>
            <hr style="border: 0.7px solid gray;" />
            <h5>Distrito:</h5>
            <div class="dropdown">
              <button
                class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
                style="border:2px solid grey"
              >
                {{this.Distrito}}
                <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
              </button>
              <div class="dropdown-content" style="max-height:150px;
   overflow:auto;">
                <a @mouseleave="checkNull" @click="Distrito='Aveiro' " href="#">Aveiro</a>
                <a @mouseleave="checkNull" @click="Distrito='Braga'" href="#">Braga</a>
                <a @mouseleave="checkNull" @click="Distrito='Braganca'" href="#">Bragança</a>
                <a @mouseleave="checkNull" @click="Distrito='Beja'" href="#">Beja</a>
                <a
                  @mouseleave="checkNull"
                  @click="Distrito='Castelo Branco' "
                  href="#"
                >Castelo Branco</a>
                <a @mouseleave="checkNull" @click="Distrito='Coimbra'" href="#">Coimbra</a>
                <a @mouseleave="checkNull" @click="Distrito='Evora' " href="#">Évora</a>
                <a @mouseleave="checkNull" @click="Distrito='Faro' " href="#">Faro</a>
                <a @mouseleave="checkNull" @click="Distrito='Guarda' " href="#">Guarda</a>
                <a @mouseleave="checkNull" @click="Distrito='Leiria' " href="#">Leiria</a>
                <a @mouseleave="checkNull" @click="Distrito='Lisboa'" href="#">Lisboa</a>
                <a @mouseleave="checkNull" @click="Distrito='Portalegre'" href="#">Portalegre</a>
                <a @mouseleave="checkNull" @click="Distrito='Porto'" href="#">Porto</a>
                <a @mouseleave="checkNull" @click="Distrito='Santarem' " href="#">Santarém</a>
                <a @mouseleave="checkNull" @click="Distrito='Setubal' " href="#">Setúbal</a>
                <a
                  @mouseleave="checkNull"
                  @click="Distrito='Viana do Castelo' "
                  href="#"
                >Viana do Castelo</a>
                <a @mouseleave="checkNull" @click="Distrito='Vila Real' " href="#">Vila Real</a>
                <a @mouseleave="checkNull" @click="Distrito='Viseu'" href="#">Viseu</a>
              </div>
            </div>
          </div>
        </div>
        <p>&nbsp;</p>
        <div v-if="registFlag==false">
          <button class="w3-button w3-round w3-green w3-hover-opacity" disabled>Atualizar</button>
        </div>
        <div v-else>
          <button class="w3-button w3-round w3-green w3-hover-opacity" @click="updateUser">Atualizar</button>
        </div>
        <div class="alert alert-success" style="margin-top:20px" v-if="successFlag">
          <strong>Successo.</strong>
          Submeteu os seus dados de registo com sucesso!
        </div>
      </modal>
      <modal name="criarUtilizadorModal" height="auto" :scrollable="true">
        <div class="w3-container w3-row">
          <div class="w3-cell-row">
            <div class="w3-container w3-cell-top w3-display-topleft">
              <h3 class="w3-text-blue" style="margin-top:10px">Criar Utilizador</h3>
            </div>
            <div class="w3-container w3-cell-top w3-display-topright">
              <button
                class="w3-button w3-white w3-border-white w3-shadow-white w3-hover-white"
                style="width:40px;height:30px"
                @click="$modal.hide('criarUtilizadorModal')"
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
            <h5 class>Nome de Utilizador</h5>
            <input
              :id="userName"
              v-model="userName"
              @keypress="checkNull"
              class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
              style="border:2px solid grey"
              type="text"
            />
            <hr style="border: 0.7px solid gray;" />
            <h5>Numero de Cartão de Cidadão:</h5>
            <input
              :id="ccNumber"
              v-model="ccNumber"
              @keypress="checkNull"
              class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
              style="border:2px solid grey"
              type="text"
            />
            <hr style="border: 0.7px solid gray;" />
            <h5>Palavra Passe:</h5>
            <input
              :id="palavraPasse"
              v-model="palavraPasse"
              @keypress="checkNull"
              class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
              style="border:2px solid grey"
              type="text"
            />
            <hr style="border: 0.7px solid gray;" />
            <h5>Ocupação:</h5>

            <div class="dropdown">
              <button
                class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
                style="border:2px solid grey"
              >
                {{this.Ocupacao}}
                <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
              </button>
              <div class="dropdown-content">
                <a @click="Ocupacao='Hospital'" href="#">Hospital</a>
                <a @click="Ocupacao='Policia'" href="#">Policia</a>
                <a @click="Ocupacao='Civil'" href="#">Civil</a>
              </div>
            </div>
            <hr style="border: 0.7px solid gray;" />
            <h5>Distrito:</h5>
            <div class="dropdown">
              <button
                class="dropbtn w3-button w3-padding-small w3-light-gray w3-border-5 w3-hover-border-light-green w3-round w3-hover-opacity w3-center"
                style="border:2px solid grey"
              >
                {{this.Distrito}}
                <img :src="this.imageUrl" style="width: 16px; heigth: 15px" />
              </button>
              <div class="dropdown-content" style="max-height:150px;
   overflow:auto;">
                <a @mouseleave="checkNull" @click="Distrito='Aveiro' " href="#">Aveiro</a>
                <a @mouseleave="checkNull" @click="Distrito='Braga'" href="#">Braga</a>
                <a @mouseleave="checkNull" @click="Distrito='Braganca'" href="#">Bragança</a>
                <a @mouseleave="checkNull" @click="Distrito='Beja'" href="#">Beja</a>
                <a
                  @mouseleave="checkNull"
                  @click="Distrito='Castelo Branco' "
                  href="#"
                >Castelo Branco</a>
                <a @mouseleave="checkNull" @click="Distrito='Coimbra'" href="#">Coimbra</a>
                <a @mouseleave="checkNull" @click="Distrito='Evora' " href="#">Évora</a>
                <a @mouseleave="checkNull" @click="Distrito='Faro' " href="#">Faro</a>
                <a @mouseleave="checkNull" @click="Distrito='Guarda' " href="#">Guarda</a>
                <a @mouseleave="checkNull" @click="Distrito='Leiria' " href="#">Leiria</a>
                <a @mouseleave="checkNull" @click="Distrito='Lisboa'" href="#">Lisboa</a>
                <a @mouseleave="checkNull" @click="Distrito='Portalegre'" href="#">Portalegre</a>
                <a @mouseleave="checkNull" @click="Distrito='Porto'" href="#">Porto</a>
                <a @mouseleave="checkNull" @click="Distrito='Santarem' " href="#">Santarém</a>
                <a @mouseleave="checkNull" @click="Distrito='Setubal' " href="#">Setúbal</a>
                <a
                  @mouseleave="checkNull"
                  @click="Distrito='Viana do Castelo' "
                  href="#"
                >Viana do Castelo</a>
                <a @mouseleave="checkNull" @click="Distrito='Vila Real' " href="#">Vila Real</a>
                <a @mouseleave="checkNull" @click="Distrito='Viseu'" href="#">Viseu</a>
              </div>
            </div>
          </div>
        </div>
        <p>&nbsp;</p>
        <div v-if="registFlag==false">
          <button class="w3-button w3-round w3-green w3-hover-opacity" disabled>Registar</button>
        </div>
        <div v-else>
          <button class="w3-button w3-round w3-green w3-hover-opacity" @click="createUser">Registar</button>
        </div>
        <div class="alert alert-success" style="margin-top:20px" v-if="successFlag">
          <strong>Successo.</strong>
          Submeteu os seus dados de registo com sucesso!
        </div>
      </modal>
    </div>
  </div>
</template>
<script>
export default {
  name: "GestorComponent",
  data() {
    return {
      myInput: "Selecione o concelho",
      imageUrl: require("../../assets/img/favicon-16x16.png"),
      Ocupacao: "Selecione a sua ocupação",
      Distrito: "Selecione o seu distrito",
      palavraPasse: "",
      userName: "",
      ccNumber: 0,
      registFlag: false,
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
    users() {
      return this.$store.state.allusers;
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
    selectUser(cc, nome, ocupacao, palavrapasse, n_distrito) {
      console.log(cc);
      console.log(nome);
      console.log(ocupacao);
      console.log(palavrapasse);
      console.log(n_distrito);

      this.userName = nome;
      this.ccNumber = cc;
      this.Ocupacao = ocupacao;
      this.palavraPasse = palavrapasse;
      this.Distrito = n_distrito;
    },
    modalCreateUser: function() {
      this.$modal.show("criarUtilizadorModal");
    },
    modalUpdateUser: function() {
      this.$modal.show("atualizarUtilizadorModal");
    },
    modalCreateAcidente: function() {
      this.$modal.show("criarAcidenteModal");
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
    getUtilizadores: async function() {
      await this.$store.dispatch("get_alluser");
      console.log(this.users);
    },
    getConcelhos: async function() {
      await this.$store.dispatch("get_concelhoall");
      console.log(this.concelhos);
    },
    createUser: async function() {
      var dict = {};
      dict["cc"] = this.ccNumber;
      dict["nome"] = this.userName;
      dict["palavrapasse"] = this.palavraPasse;
      dict["ocupacao"] = this.Ocupacao;
      dict["n_distrito"] = this.Distrito;

      console.log(await this.$store.dispatch("post_user", dict));
      this.palavraPasse = "";
      this.userName = "";
      this.ccNumber = 0;
      this.registFlag = false;
      this.Ocupacao = "Selecione a sua ocupação";
      this.Distrito = "Selecione o seu distrito";
      this.successFlag = true;
      this.getUtilizadores();
    },
    checkNull() {
      console.log(this.Ocupacao);
      console.log(this.Distrito);
      console.log(this.userName);
      console.log(this.ccNumber);
      console.log(this.palavraPasse);
      if (
        this.Ocupacao != "" &&
        this.Distrito != "" &&
        this.userName != "" &&
        this.ccNumber > 1000 &&
        this.palavrapasse != ""
      ) {
        this.registFlag = true;
        console.log(this.registFlag);
      } else {
        this.registFlag = false;
        console.log(this.registFlag);
      }
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

    updateUser: async function() {
      var dict = {};
      dict["cc"] = this.ccNumber;
      dict["nome"] = this.userName;
      dict["palavrapasse"] = this.palavraPasse;
      dict["ocupacao"] = this.Ocupacao;
      dict["n_distrito"] = this.Distrito;

      console.log(await this.$store.dispatch("user_updateall", dict));
      this.palavraPasse = "";
      this.userName = "";
      this.ccNumber = 0;
      this.registFlag = false;
      this.Ocupacao = "Selecione a sua ocupação";
      this.Distrito = "Selecione o seu distrito";
      this.successFlag = true;
      this.getUtilizadores();
    },
    deleteUser: async function() {
      console.log(this.ccNumber);
      console.log(await this.$store.dispatch("del_user", this.ccNumber));
    },
    createAcidente: async function() {
      //funcao para devolver o id do ultimo acidente registrado
      var dict = {};
      var date = new Date();
      dict["id"] = this.id;
      dict["concelho"] = this.concelho;
      dict["datahora"] = date.toJSON();
      dict["mortos"] = this.mortos;
      dict["feridosg"] = this.feridosg;
      dict["via"] = this.via;
      dict["km"] = this.km;
      dict["natureza"] = this.natureza;
      console.log(date.toJSON());
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
    },
    updateAcidente: async function() {
      var dict = {};
      dict["id"] = this.id;
      dict["concelho"] = this.concelho;
      dict["mortos"] = this.mortos;
      dict["feridosg"] = this.feridosg;
      dict["via"] = this.via;
      dict["km"] = this.km;
      dict["natureza"] = this.natureza;
      console.log(await this.$store.dispatch("update_acidente", dict));
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
    },
    deleteAcidente: async function() {
      console.log(this.id);
      console.log(await this.$store.dispatch("del_acidente", this.id));
    }
  },
  mounted() {
    this.getUtilizadores();
    this.getConcelhos();
  }
};
</script>