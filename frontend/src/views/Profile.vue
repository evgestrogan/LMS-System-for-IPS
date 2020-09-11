<template>
  <v-row align="center" justify="center">
    <router-view></router-view>
  </v-row>
</template>

<script>
  import { mapGetters } from 'vuex';

  export default {
    name: "Profile",
    computed: {
      ...mapGetters(['userName']),
    },
    created() {
      this.$store.dispatch('get_departmets_list')
    }
  }
</script>