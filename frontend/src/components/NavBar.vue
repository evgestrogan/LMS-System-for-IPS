<template>
  <v-app-bar flat app>
    <v-btn icon @click.stop=state_drawer>
      <v-icon>menu</v-icon>
    </v-btn>
    <router-link to="/profile" class="text-decoration-none">
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-black">LMS</span>
        <span>ystem</span>
      </v-toolbar-title>
    </router-link>
    <v-spacer></v-spacer>
    <v-btn v-if="this.authStatus" text @click="logout">
      <v-icon left color="grey">exit_to_app</v-icon>
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
      console.log(this.authStatus)
      this.auth_error()
      router.push('/')
    }
  },
  computed: {
    ...mapGetters(['authStatus'])
  }
}
</script>

<style scoped>

</style>