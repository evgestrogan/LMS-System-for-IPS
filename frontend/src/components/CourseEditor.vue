<template>
  <div class="col ma-16">
    <chapter-item-for-creating v-for="(chapter, id_chapter) in chapters_list_for_editions" :chapter='chapter' :id_chapter="id_chapter" :key="id_chapter"></chapter-item-for-creating>
    <v-row class="justify-center">
      <v-btn class="ma-2" outlined color="indigo" @click="create_chapter">Добавить главу</v-btn>
    </v-row>
  </div>
</template>

<script>
import {mapGetters, mapMutations} from "vuex";
import chapterItemForCreating from './ChapterItemForCreating'

export default {
  name: "CourseEditor",
  components: {
    chapterItemForCreating,
  },
  methods: {
    ...mapMutations(['clear_chapters_for_editions', 'create_chapter']),
  },
  computed: {
    ...mapGetters(['chapters_list_for_editions']),
  },
  created() {
    this.clear_chapters_for_editions()
    this.$store.dispatch(
      'get_chapters_for_editions', {
      data: this.$route.params.id_course
    })
  },
}
</script>

<style scoped>

</style>