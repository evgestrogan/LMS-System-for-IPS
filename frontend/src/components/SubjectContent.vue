<template>
  <v-card class="row ma-16">
    <v-expansion-panels>
        <v-expansion-panel v-for="(subject, id) in return_subjects_list" :key="id">
          <v-expansion-panel-header>
            <div class="col-8">
              <v-row class="text--disabled text-overline text-uppercase">Название предмета</v-row>
              <v-row class="text-lg-h5 font-weight-light">{{ subject.name_subject }}</v-row>
            </div>
            <div class="col-4">
              <v-row class="text--disabled text-overline text-uppercase justify-center">Начальник цикла</v-row>
              <v-row class="text-lg-body-1 font-weight-light justify-center">{{ subject.name_subject }}</v-row>
            </div>
          </v-expansion-panel-header>
          <v-expansion-panel-content class="pl-4 pr-4">
            <v-list-item-group v-for="course in subject.courses" :key="course.id" class="row">
              <div class="col-8">
                <v-row class="text--disabled text-overline text-uppercase">Название курса</v-row>
                <v-row class="text-lg-body-1 font-weight-light">
                  <router-link :to="{ name: 'courseContent', params: { id_course: course.id }}" class="text-decoration-none">{{ course.name_course }}</router-link>
                </v-row>
              </div>
              <div class="col-2">
                <v-row class="text--disabled text-overline text-uppercase justify-center">Создатель курса</v-row>
                <v-row class="text-lg-body-1 font-weight-light justify-center">{{ course.user }}</v-row>
              </div>
              <div class="col-2">
                <v-row class="text--disabled text-overline text-uppercase justify-center">итоговой тест</v-row>
                <v-row class="text-lg-body-1 font-weight-light justify-center">{{ course.test }}</v-row>
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
  computed: {
    ...mapGetters(['return_subjects_list']),
  },
  methods: {
    ...mapMutations(['clear_chapters_list']),
    createSubject: function () {
      this.$store.dispatch(
        'get_subjects_list', {
        data: this.$route.params.id_department
      })
    }
  },
  created() {
    this.createSubject()
    this.clear_chapters_list()
  },
  watch: {
    $route(to, from) {
      this.createSubject()
    }
  }
}
</script>

<style scoped>

</style>