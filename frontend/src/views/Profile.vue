<template>
  <v-row align="center" justify="center">
    <router-view></router-view>
  </v-row>
</template>

<script>
  export default {
    name: "Profile",
    created() {
      this.$store.dispatch('get_departmets_list')
    }
  }
</script>