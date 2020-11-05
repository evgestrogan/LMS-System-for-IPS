<template>
  <v-expansion-panel-content class="pr-4">
    <v-list-item-group v-for="course in courses" :key="course.id" class="row pa-4" style="border-bottom: 1px solid red;">

      <v-col cols="4" align="left">
        <v-list-item-subtitle class="text--disabled text-uppercase justify-center">Название курса</v-list-item-subtitle>
        <router-link v-if="access || user_status || manager" :to="{ name: 'Course', params: { id_department: id_department, id_course: course.id }}" class="text-decoration-none">
          <v-list-item-title class="text-lg-body-1 font-weight-light">
            {{ course.name }}
          </v-list-item-title>
        </router-link>
        <v-list-item-title v-else class="text-lg-body-1 font-weight-light">
          {{ course.name }}
        </v-list-item-title>
      </v-col>

      <v-col cols="3" align="center">
        <v-list-item-subtitle class="text--disabled text-uppercase justify-center">Куратор курса</v-list-item-subtitle>
        <router-link :to="{ name: 'Profile', params: { id_user: course.manager.user.id }}" class="text-decoration-none">
          <v-list-item-title class="text-lg-body-1 font-weight-light">
            {{ course.manager.user.last_name }} {{ course.manager.user.first_name }} {{ course.manager.user.second_name }}
          </v-list-item-title>
        </router-link>
      </v-col>

      <v-col cols="3" align="center">
        <v-list-item-subtitle class="text--disabled text-uppercase">Итоговой тест курса</v-list-item-subtitle>
        <router-link v-if="access || manager || user_status" :to="{ name: 'TestPage', params: { id_test: course.test.id }}" class="text-decoration-none">
          <v-list-item-title class="text-lg-body-1 font-weight-light">
            {{ course.test.title }}
          </v-list-item-title>
        </router-link>
        <v-list-item-title v-else class="text-lg-body-1 font-weight-light">
          {{ course.test.title }}
        </v-list-item-title>

      </v-col>

      <v-col cols="2" v-if="manager" align="center">
        <v-list-item-subtitle class="text--disabled text-uppercase">Изменение курса</v-list-item-subtitle>
        <router-link :to="{ name: 'CourseEditorPage', params: { id_course: course.id }}" class="text-decoration-none justify-center">
          <v-list-item-title class="text-lg-body-1 font-weight-light">
            <v-icon>mdi-file-edit-outline</v-icon>
          </v-list-item-title>
        </router-link>
      </v-col>

      <v-col cols="2" v-if="!access && !user_status" align="center">
        <v-list-item-subtitle class="text--disabled text-uppercase">Запись</v-list-item-subtitle>
        <v-list-item-title class="text-lg-body-1 font-weight-light v-list-item--link" @click="registration_for_the_course(course.id)">
          <v-icon>mdi-account-check-outline</v-icon>
        </v-list-item-title>
      </v-col>

    </v-list-item-group>
  </v-expansion-panel-content>
</template>

<script>
import {mapGetters} from "vuex";
import router from "@/router";

export default {
  name: "CourseContent",
  props: {
    courses: Array,
    subject_manager: Number,
    department_manager: Number,
  },
  data() {
    return {
      id_department: this.$route.params.id_department,
      access: false,
      manager: false,
    };
  },
  computed: {
    ...mapGetters(['user_id', 'user_status']),
  },
  created() {
    for (const course of this.courses) {
      for (const trainee of course.trainee) {
        if (this.user_id.toString() === trainee.user_id) {
          this.access = true
        }
        if (this.subject_manager === this.user_id || course.manager.user.id === this.user_id || this.department_manager === this.user_id) {
          this.manager = true
        }
      }
    }
  },
  methods: {
    registration_for_the_course(id) {
      this.$store.dispatch('register_for_the_course', { id: id, user_id: this.user_id })
      .then(resp => {router.push({ name: 'Course', params: { id_department: this.id_department, id_course: id }})})
      .catch(err => {router.push({name: 'Profile', params: {id_user: this.user_id}})})
    }
  }
}
</script>

<style scoped>

</style>