<template>
  <div>
    <gestorComp></gestorComp>
  </div>
</template>

<script>
import * as Cookies from "js-cookie";
import gestorComp from "../components/userPages/GestorComponent.vue";

export default {
  name: "GestorComponent",
  data: function() {
    return {};
  },
  components: {
    gestorComp
  }
};
</script>
