<template>
  <div>
    <MainUser></MainUser>
  </div>
</template>

<script>
import * as Cookies from "js-cookie";
import MainUser from "../components/userPages/MainUserComponent.vue";

export default {
  name: "MainUserComponent",
  data: function() {
    return {};
  },
  components: {
    MainUser
  },
  mounted() {
    console.log(Cookies.get("stop"));
    if (Cookies.get("stop") === "false") {
      window.location.reload(true);
      Cookies.set("stop", true);
      console.log(Cookies.get("stop"));
    }
  }
};
</script>