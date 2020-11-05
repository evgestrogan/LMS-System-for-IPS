<template xmlns="http://www.w3.org/1999/html">
  <v-card class="mx-auto" max-width="1000" max-height="1000">
    <v-img v-if="profile_avatar" class="white--text align-end" max-height="400px" :src="'http://127.0.0.1:8000' + profile_avatar">
    </v-img>
    <v-card-title>{{profile.last_name}} {{profile.first_name}} {{profile.second_name}}
      <v-spacer></v-spacer>
      <v-btn icon v-if="this.$route.params.id_user === user_id">
        <v-icon>mdi-account-edit-outline</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-subtitle class="pb-0" v-if="profile.student">Студент {{profile.student.group}} группы</v-card-subtitle>
    <v-card-subtitle class="pb-0" v-else>Преподаватель</v-card-subtitle>
    <v-divider class="mx-0"></v-divider>

    <v-card-text class="text--primary" v-if="profile.manager">
      <v-row v-if="profile.manager.department_manager">
        <v-col>
          Начальник кафедры:
        </v-col>
        <v-col>
          <v-row v-for="department in profile.manager.department_manager" v-bind:key=department.id>
            <router-link :to="{ name: 'Department', params: { id_department: department.id }}" class="text-decoration-none">{{department.name}}</router-link>
          </v-row>
        </v-col>
      </v-row>
      <v-row v-if="profile.manager.subject_manager">
        <v-col>
          Начальник цикла:
        </v-col>
        <v-col>
          <v-row v-for="subject in profile.manager.subject_manager" v-bind:key=subject.id>
            <router-link :to="{ name: 'Department', params: { id_department: subject.department.id }}" class="text-decoration-none">{{subject.name}}</router-link>
          </v-row>
        </v-col>
      </v-row>
      <v-row v-if="profile.manager.course_manager">
        <v-col>
          Разработчик курса(ов):
        </v-col>
        <v-col>
          <v-row v-for="course in profile.manager.course_manager" v-bind:key=course.id>
            <router-link :to="{ name: 'Course', params: { id_course: course.id, id_department: course.subject.department.id }}" class="text-decoration-none">{{course.name}}<br></router-link>
          </v-row>
        </v-col>
      </v-row>
      <v-divider class="mx-0"></v-divider>
    </v-card-text>
    <v-card-text class="text--primary" v-if="profile.student">
      <v-row>
        <v-col>
          Доступные курсы:
        </v-col>
        <v-col>
          <v-row v-for="course in profile.student.course" v-bind:key=course.id>
            <router-link :to="{ name: 'Course', params: { id_course: course.id, id_department: course.subject.department.id }}" class="text-decoration-none">{{course.name}}</router-link>
          </v-row>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
  import {mapGetters} from "vuex";
  import router from "@/router";
  const axios = require('axios').default;

  export default {
    name: "Profile",
    data: function () {
      return {
        profile: {},
        profile_avatar: null,
      }
    },
    computed: {
      ...mapGetters(['user_id']),
    },
    methods: {
      get_profile: function () {
        axios.get( 'http://127.0.0.1:8000/api/profile/' + this.$route.params.id_user)
        .then(resp => {
          this.profile = resp.data
          if (resp.data.manager) {
                this.profile_avatar = resp.data.manager.avatar
            }
            if (resp.data.student) {
                this.profile_avatar = resp.data.student.avatar
            }
        })
        .catch(err => {router.push({name: 'Profile', params: {id_user: this.user_id}})})
      },
    },
    created() {
      this.get_profile()
    },
    beforeRouteUpdate (to, from, next) {
      next()
      this.get_profile()
    }
  }
</script>