<template>
  <v-card class="row ma-16">
    <v-expansion-panels>
      <v-expansion-panel v-for="subject in department.subject" :key="subject.id">
        <subjectContent :subject="subject"></subjectContent>
          <course-content :courses="subject.course" :subject_manager="subject.manager.user.id" :department_manager="department.manager.user.id"></course-content>
      </v-expansion-panel>
  </v-expansion-panels>
</v-card>
</template>

<script>
import {mapGetters, mapMutations} from "vuex";
import subjectContent from '../components/departmentPageComponents/SubjectContent';
import courseContent from '../components/departmentPageComponents/CourseContent'
import router from "@/router";

export default {
  name: "DepartmentPage",
  components: {
    subjectContent,
    courseContent
  },
  computed: {
    ...mapGetters(['department', 'user_id']),
  },
  methods: {
    ...mapMutations(['clear_department']),
    createDepartment: function () {
      this.clear_department()
      this.$store.dispatch('department', { id: this.$route.params.id_department })
      .catch(err => {router.push({name: 'Profile', params: {id_user: this.user_id}})})
    }
  },
  created() {
    this.createDepartment()
  },
  watch: {
    $route(to, from) {
      this.createDepartment()
    }
  }
}
</script>

<style scoped>

</style>