<template>
  <div>
    <Index></Index>
  </div>
</template>

<script>
import Index from "../components/mainPage/Index.vue";
import * as Cookies from "js-cookie";
export default {
  name: "Home",
  components: {
    Index
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
