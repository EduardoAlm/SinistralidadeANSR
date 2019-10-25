<template>
  <div>
    <AccInfo></AccInfo>
  </div>
</template>

<script>
import * as Cookies from "js-cookie";
import AccInfo from "../components/userPages/AccountInfo.vue";

export default {
  name: "AccountInfo",
  data: function() {
    return {};
  },
  components: {
    AccInfo
  }
};
</script>
