<template>
  <div class="w3-container w3-panel w3-leftbar w3-border-blue">
    <nav class="w3-section w3-bar">
      <div class="w3-left">
        <router-link
          class="w3-btn w3-wide"
          v-for="routes in links"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        >
          <img v-if="routes.imageUrl" :src="routes.imageUrl" style="width: 40px; height: 40px;" />
          {{ routes.text }}
        </router-link>
      </div>
      <div class="w3-right">
        <router-link
          class="w3-btn w3-wide"
          v-for="routes in links1"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        >
          <img v-if="routes.imageUrl" :src="routes.imageUrl" style="width: 40px; height: 40px;" />
          {{ routes.text }}
        </router-link>
        <button
          :id="logout"
          class="w3-button w3-red w3-hover-opacity w3-margin-left"
          style="font-family: sans-serif, letter-spacing: 3px"
          @click="logout"
        >Terminar Sessão</button>
      </div>
    </nav>
  </div>
</template>

<script>
import * as Cookies from "js-cookie";

export default {
  name: "Nav2",
  data: function() {
    return {
      links: [
        {
          id: 0,
          page: "/",
          imageUrl: require("../../assets/img/logo.png")
        },
        {
          id: 1,
          text: "SinistralidadeANSR",
          page: "/"
        }
      ],
      links1: [
        {
          id: 2,
          text: Cookies.get("loggedName"),
          page: "/mainUser"
        }
      ]
    };
  },
  methods: {
    logout() {
      Cookies.set("loggedIn", 0);
      Cookies.remove("loggedName");
      window.location.reload(true);
    }
  }
};
</script>