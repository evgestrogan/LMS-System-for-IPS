<template>
  <div class="col ma-16">
      <v-card class="mb-6 pa-6 row" v-for="chapter in return_chapters_list" :key="chapter.id">
        <v-card-text class="col">
          <div>Курс: {{chapter.course.name_course}}</div>
          <div class="display-1 text--primary">Глава: {{chapter.name_chapter}}</div>
          <div>Результирующий тест: {{chapter.test.id}}</div>
        </v-card-text>
        <div class="row justify-end">
          <v-card-actions>
            <v-btn text color="deep-purple accent-4">Пройти итоговый тест</v-btn>
          </v-card-actions>
        </div>
      </v-card>
  </div>
</template>

<script>
import {mapGetters, mapMutations} from 'vuex';

export default {
  name: "courseContent",
  methods: {
    ...mapMutations(['clear_subjects_list']),
    createChapters: function () {
      this.$store.dispatch(
        'get_chapters_list', {
        data: this.$route.params.id_course
      })
    }
  },
  computed: {
    ...mapGetters(['return_chapters_list']),
  },
  created() {
    this.clear_subjects_list()
    this.createChapters()
  },
}
</script>

<style scoped>

</style>