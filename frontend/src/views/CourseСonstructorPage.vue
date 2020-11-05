<template>
  <v-col class="ma-16" style="min-width: 300px; max-width: 800px">
    <alert-component v-if="error" :status="error"></alert-component>
    <v-select v-if="course.id === ''" @change="get_subject" v-model="course.department"  :items="departments" label="Выберите кафедру" solo item-text="name" item-value="value"></v-select>
    <v-select v-if="course.id === ''" :items='department.subject' v-model="course.subject" label="Выберите предмет" solo item-text="name" item-value="value"></v-select>
    <v-text-field v-model="course.name" label="Введите название курса"></v-text-field>
    <test-creator :test="test_list"></test-creator>
    <v-row class="justify-center">
      <v-btn class="ma-2" @click="create_course()" outlined color="indigo">Создать курс</v-btn>
    </v-row>
  </v-col>
</template>

<script>

import router from "@/router";
import {mapGetters, mapMutations} from "vuex";
import testCreator from "@/components/CreatorComponents/TestCreator";
import alertComponent from "@/components/AlertComponent";

export default {
  name: "CourseСonstructorPage",
  data: function () {
    return {
      course: {
        'id': '',
        'department': '',
        'subject': '',
        'name': '',
      },
      test_list: {
        'id': null,
        'title': '',
        'question': [],
      },
      error: null,
    };
  },
  components: {
    testCreator,
    alertComponent,
  },
  computed: {
    ...mapGetters(['departments', 'department', 'user_id', 'user_manager_id']),
  },
  methods: {
    ...mapMutations(['clear_course']),
    get_subject() {
      this.course.subject = ''
      this.error = null
      for (const department of this.departments) {
        if (this.course.department === department.name) {
          this.$store.dispatch('department', { id: department.id })
          .catch(err => {
            this.error = err.request.status
          })
        }
      }
    },
    create_course() {
      let subject_id = null
      this.error = null
      for (const subject of this.department.subject) {
        if (subject.name === this.course.subject) {
          subject_id = subject.id
        }
      }
      this.$store.dispatch('test_creator_editor', this.test_list)
      .then(resp => {
        this.course.test_id = resp.data.test_id
        this.course.subject_id = subject_id
        this.course.manager_id = this.user_manager_id
        this.$store.dispatch('course_creator_editor', this.course)
        .then(response => {
          router.push({name: 'ChaptersСonstructorPage', params: {id_course: response.data.course_id}})
        })
        .catch(err => {
          this.error = err.request.status
        })
      })
      .catch(err => {
        this.error = err.request.status
      })
    }
  },
  created() {
    this.error = null
    if (this.$route.params.id_course) {
      this.$store.dispatch('course', { id: this.$route.params.id_course })
      .then(resp => {
        this.course = resp.data
        this.$store.dispatch('test', { id: resp.data.test_id})
        .then(resp => {
          this.test_list = resp.data
        })
        .catch(err => {
          this.error = err.request.status
        })
      })
      .catch(err => { router.push({name: 'Profile', params: {id_user: this.user_id}}) })
    }
  },
  watch: {
    $route(to, from) {
      this.error = null
      this.course = {
        'id': '',
        'department': '',
        'subject': '',
        'name': '',
      }
      this.test_list = {
        'id': null,
        'title': '',
        'question': [],
      }
    }
  }
}
</script>

<style scoped>

</style>