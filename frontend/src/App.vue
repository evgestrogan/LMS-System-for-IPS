<template>
  <div id="app">
    <NavBar/>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/NavBar'

export default {
  name: 'app',
  components: {NavBar},
  // computed : {
  //   isLoggedIn : function(){ return this.$store.getters.isLoggedIn},
  // },
  // created: function () {
  //   this.$http.interceptors.response.use(undefined, function (err) {
  //     return new Promise(function (resolve, reject) {
  //       if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
  //         this.$store.dispatch("refreshTokens")
  //       }
  //       throw err;
  //     });
  //   });
  // }
}
</script>

<style>
</style>
