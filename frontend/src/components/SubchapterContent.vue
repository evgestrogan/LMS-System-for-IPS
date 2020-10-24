<template>
  <div style="height: 900px; width: 100%">
    <iframe style="width: 100%; height: 100%" :src="return_subchapter.body"></iframe>
  </div>

</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "subchapterContent",
  created() {
    this.$store.dispatch('get_subchapter', { id: this.$route.params.id_subchapter })
  },
  computed: {
    ...mapGetters(['return_subchapter']),
  },
}

</script>

<style scoped>
</style>