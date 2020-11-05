<template>
  <v-app>

    <v-navigation-drawer v-if=is_authenticated :value=drawer app color="grey darken-4" width="350">
      <SideBar></SideBar>
    </v-navigation-drawer>

    <NavBar></NavBar>

    <v-main class="grey lighten-4">
      <v-row align="center" justify="center">
        <router-view></router-view>
      </v-row>
    </v-main>

  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import NavBar from './components/barsComponent/NavBar'
import SideBar from "@/components/barsComponent/SideBar";

export default {
  name: 'App',
  components: {
    NavBar,
    SideBar,
  },
  computed: {
    ...mapGetters(['is_authenticated', 'drawer'])
  },
};
</script>
