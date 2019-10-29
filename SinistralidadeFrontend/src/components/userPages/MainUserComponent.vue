<template>
  <div>
    <div v-if="this.userInfo[0].ocupacao==='Gestor'">
      <GestorComponent></GestorComponent>
    </div>
    <div v-else-if="this.userInfo[0].ocupacao==='Policia'">
      <PoliciaComponent></PoliciaComponent>
    </div>
    <div v-else-if="this.userInfo[0].ocupacao==='Hospital'">
      <HospitalComponent></HospitalComponent>
    </div>
    <div v-else>
      <CivilComponent></CivilComponent>
    </div>
    <p>&nbsp;</p>
    <router-link v-bind:key="link.id" :to="`${link.page}`">
      <button class="w3-button w3-green w3-round">Dados da Conta</button>
    </router-link>
    <p>&nbsp;</p>
  </div>
</template>

<script>
import GestorComponent from "./GestorComponent.vue";
import HospitalComponent from "./HospitalComponent.vue";
import PoliciaComponent from "./PoliciaComponent.vue";
import CivilComponent from "./CivilComponent.vue";
export default {
  name: "MainUserComponent",
  data() {
    return {
      link: { id: 0, text: "AccountInfo", page: "/accInfo" },
      userInfo: []
    };
  },
  components: {
    GestorComponent,
    PoliciaComponent,
    HospitalComponent,
    CivilComponent
  },

  methods: {},
  mounted() {
    var userInfo = JSON.parse(localStorage.getItem("userInfo"));
    this.userInfo = userInfo;
    console.log(userInfo);
  }
};
</script>