<template>
  <v-app-bar flat app>
    <v-btn icon @click.stop=state_drawer>
      <v-icon>mdi-menu</v-icon>
    </v-btn>
    <router-link :to="{ name: 'Profile', params: { id_user: this.user_id }}"  class="text-decoration-none">
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-black">LMS</span>
        <span>ystem</span>
      </v-toolbar-title>
    </router-link>
    <v-spacer></v-spacer>
    <v-btn v-if="is_authenticated" text @click="logout">
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
    ...mapMutations(['state_drawer', 'clear_main_user_data']),
    logout: function () {
      this.clear_main_user_data()
      router.push({name: 'Authentication'})
    }
  },
  computed: {
    ...mapGetters(['user_id', 'is_authenticated'])
  }
}
</script>

<style scoped>

</style>