<template>
  <v-card class="row ma-16">
    <v-expansion-panels>
      <v-expansion-panel v-for="subject in return_subjects_list" :key="subject.id">
          <v-expansion-panel-header color="blue-grey lighten-5">
            <div class="col-8">
              <v-row class="text--disabled text-overline text-uppercase">Название предмета</v-row>
              <v-row class="text-lg-h5 font-weight-light">{{ subject.name_subject }}</v-row>
            </div>
            <div class="col-6">
              <v-row class="text--disabled text-overline text-uppercase justify-center">Начальник цикла</v-row>
              <v-row class="justify-center"><v-avatar><v-img :src="subject.boss_subject.avatar"></v-img></v-avatar></v-row>
              <v-row class="text-lg-body-1 font-weight-light justify-center">
                <router-link :to="{ name: 'profile', params: { id_user: subject.boss_subject.id }}" class="text-decoration-none">
                  {{ subject.boss_subject.last_name }} {{ subject.boss_subject.first_name }} {{ subject.boss_subject.second_name }}
                </router-link>
              </v-row>
            </div>
          </v-expansion-panel-header>
          <v-expansion-panel-content class="pr-4">
            <v-list-item-group v-for="course in subject.courses" :key="course.id" class="row pa-4" style="border-bottom: 1px solid red;">
              <div class="col-6">
                <v-row class="text--disabled text-overline text-uppercase">Название курса</v-row>
                <v-row class="text-lg-body-1 font-weight-light">
                  <router-link :to="{ name: 'courseContent', params: { id_department: id_department, id_course: course.id }}" class="text-decoration-none">{{ course.name_course }}</router-link>
                  <v-spacer></v-spacer>
                  <router-link :to="{ name: 'editCourse', params: { id_department: id_department, id_course: course.id }}" class="text-decoration-none"><v-icon v-if="subject.boss_subject.user === client.id || course.boss_course.user === client.id">mdi-file-edit-outline</v-icon></router-link>
                </v-row>
              </div>
              <div class="col-4">
                <v-row class="text--disabled text-overline text-uppercase justify-center">Куратор курса</v-row>
                <router-link :to="{ name: 'profile', params: { id_user: course.boss_course.id }}" class="text-decoration-none">
                  <v-row class="text-lg-body-1 font-weight-light justify-center">{{ course.boss_course.last_name }} {{ course.boss_course.first_name }} {{ course.boss_course.second_name }}</v-row>
                </router-link>
              </div>
              <div class="col-2">
                <v-row class="text--disabled text-overline text-uppercase justify-center">итоговой тест курса</v-row>
                <router-link :to="{ name: 'testContent', params: { id_department: id_department, id_course:course.id, id_test: course.test.id }}" class="text-decoration-none">{{ course.test.title }}</router-link>
              </div>
            </v-list-item-group>
          </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
  </v-card>
</template>

<script>
import {mapGetters, mapMutations} from "vuex";

export default {
  name: "subjectContent",
  data() {
    return {
      id_department: this.$route.params.id_department
    };
  },
  computed: {
    ...mapGetters(['return_subjects_list', 'client']),
  },
  methods: {
    ...mapMutations(['clear_chapters_list', 'clear_subjects_list']),
    createSubject: function () {
      this.$store.dispatch(
        'get_subjects_list', {
        data: this.$route.params.id_department
      })
    }
  },
  created() {
    this.clear_subjects_list()
    this.createSubject()
  },
  watch: {
    $route(to, from) {
      this.clear_subjects_list()
      this.createSubject()
    }
  }
}
</script>

<style scoped>

</style>