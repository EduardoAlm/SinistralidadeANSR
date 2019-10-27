<template>
  <div>
    <router-link v-bind:key="link.id" :to="`${link.page}`">
      <button class="w3-button w3-green w3-round">Dados da Conta</button>
    </router-link>
  </div>
  <!--  <div v-if="this.user==='Administrador'"></div>
  <div v-else-if="this.user==='Medico'"></div>
  <div v-else-if="this.user==='Hospital'"></div>
  <div v-else-if="this.user==='Civil'"></div>-->
</template>

<script>
export default {
  name: "MainUserComponent",
  data() {
    return {
      link: { id: 0, text: "AccountInfo", page: "/accInfo" }
    };
  },
  computed: {
    user() {
      return this.$store.state.user;
    }
  },
  methods: {},
  mounted() {
    console.log(this.user);
  }
};
</script>