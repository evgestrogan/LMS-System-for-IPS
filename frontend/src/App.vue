<template>
  <v-app>

    <v-navigation-drawer v-if="this.authStatus"  :value=return_drawer app color="purple accent-2" width="350">
      <SideBar></SideBar>
    </v-navigation-drawer>

    <NavBar></NavBar>

    <v-main class="grey lighten-4">
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import NavBar from '../src/components/NavBar'
import SideBar from "@/components/SideBar";

export default {
  name: 'App',
  components: {
    NavBar,
    SideBar,
  },
  computed: {
    ...mapGetters(['authStatus', 'return_drawer'])
  },
  methods: {
  ...mapActions(['refreshTokens'])
  },
};
</script>
