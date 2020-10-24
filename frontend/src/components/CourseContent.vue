<template>
  <div class="col ma-16">
      <v-card class="mb-6 pa-6 row" v-for="(chapter, count) in return_chapters_list" :key="chapter.id">
          <v-card-text class="col">
              <div>Курс: {{chapter.course.name_course}}</div>
              <v-list-group color="gray">
                  <template v-slot:activator>
                      Глава {{count + 1}}: {{chapter.name_chapter}}
                  </template>
                  <router-link v-for="subchapter in chapter.subchapters" :key="subchapter.id" :to="{ name: 'subchapterContent', params: { id_subchapter: subchapter.id }}"  class="text-decoration-none text-lg-body-1 font-weight-light"><v-list-item link>{{subchapter.name_subchapter}}</v-list-item></router-link>
              </v-list-group>
          </v-card-text>
          <v-card-text class="col ">
              <div class="text-end">Результирующий тест: {{chapter.test.title}}</div>
              <v-card-actions class="justify-end">
                  <router-link :to="{ name: 'testContent', params: { id_test: chapter.test.id }}" class="text-decoration-none text-lg-body-1 font-weight-light">Пройти итоговый тест</router-link>
              </v-card-actions>
          </v-card-text>
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