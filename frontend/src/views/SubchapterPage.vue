<template>
  <div style="height: 900px; width: 100%">
    <iframe style="width: 100%; height: 100%" :src="'http://127.0.0.1:8000' + subchapter.body"></iframe>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import router from "@/router";

export default {
name: "SubchapterPage",
  created() {
    this.$store.dispatch('subchapter', { id: this.$route.params.id_subchapter })
    .catch(err => {router.push({name: 'Profile', params: {id_user: this.user_id}})})
  },
  computed: {
    ...mapGetters(['subchapter']),
  },
}
</script>

<style scoped>

</style>