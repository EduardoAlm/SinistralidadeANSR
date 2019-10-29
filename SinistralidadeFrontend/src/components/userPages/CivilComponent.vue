
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
    </div>
  </div>
</template>
<script>
export default {
  name: "CivilComponent",
  data() {
    return {
      myInput: "Selecione o concelho"
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
    }
  },
  mounted() {
    this.getConcelhos();
  }
};
</script>