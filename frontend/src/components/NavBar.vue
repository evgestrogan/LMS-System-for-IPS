<template>
  <v-app-bar flat app>
    <v-btn icon @click.stop=state_drawer>
      <v-icon>mdi-menu</v-icon>
    </v-btn>
    <router-link :to="{ name: 'profile', params: { id_user: this.client.id }}"  class="text-decoration-none">
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-black">LMS</span>
        <span>ystem</span>
      </v-toolbar-title>
    </router-link>
    <v-spacer></v-spacer>
    <v-btn v-if="client_status" text @click="logout">
      <v-icon left color="grey">mdi-exit-to-app</v-icon>
      <span class="text-uppercase grey--text">Log-Out</span>
    </v-btn>
  </v-app-bar>
</template>

<script>
import {mapMutations, mapGetters} from "vuex";
import router from "@/router";

export default {
  name: "NavBar",
  methods: {
    ...mapMutations(['state_drawer', 'auth_error']),
    logout: function () {
      this.auth_error()
      router.push('/')
    }
  },
  computed: {
    ...mapGetters(['client', 'client_status'])
  }
}
</script>

<style scoped>

</style>