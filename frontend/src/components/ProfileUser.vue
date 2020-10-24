<template>
  <div>
    <v-card class="mx-auto" max-width="1000" max-height="1000">
      <v-img class="white--text align-end" max-height="400px" :src="  profile.avatar">
      </v-img>
      <v-card-title>{{profile.last_name}} {{profile.first_name}} {{profile.second_name}}
        <v-spacer></v-spacer>
        <v-btn icon v-if="this.$route.params.id_user === client.id">
          <v-icon>mdi-account-edit-outline</v-icon>
        </v-btn>
      </v-card-title>
      <v-card-subtitle class="pb-0" v-if="profile.group_id">Студент {{profile.group_id.number_group}} группы</v-card-subtitle>
      <v-card-subtitle class="pb-0" v-else>Преподаватель</v-card-subtitle>
      <v-divider class="mx-0"></v-divider>

      <v-card-text class="text--primary">
        <v-row v-if="profile.boss_department">
          <v-col>
            Начальник кафедры:
          </v-col>
          <v-col>
            <router-link :to="{ name: 'subjectContent', params: { id_department: profile.boss_department.id }}" class="text-decoration-none">{{profile.boss_department.name_department}}</router-link>
          </v-col>
        </v-row>
        <v-row v-if="profile.boss_subject">
          <v-col>
            Начальник цикла:
          </v-col>
          <v-col>
            <router-link :to="{ name: 'subjectContent', params: { id_department: profile.boss_subject.department }}" class="text-decoration-none">{{profile.boss_subject.name_subject}}</router-link>
          </v-col>
        </v-row>
        <v-row v-if="profile.boss_course">
          <v-col>
            Разработчик курса(ов):
          </v-col>
          <v-col>
            <router-link v-for="course in profile.boss_course" v-bind:key=course.id :to="{ name: 'courseContent', params: { id_course: course.id, id_department: course.subject.department }}" class="text-decoration-none">{{course.name_course}}<br></router-link>
          </v-col>
        </v-row>
        <v-divider class="mx-0"></v-divider>
      </v-card-text>

    </v-card>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import router from "@/router";

export default {
  name: "ProfileUser",
  computed: {
    ...mapGetters(['profile', 'client']),
  },
  created() {
    this.$store.dispatch('get_user_information', { id: this.$route.params.id_user })
    .catch(err => {router.push({name: 'profile', params: {id_user: this.client.id}})})
  },
  beforeRouteUpdate (to, from, next) {
    next()
    this.$store.dispatch('get_user_information', { id: this.$route.params.id_user })
    .catch(err => {router.push({name: 'profile', params: {id_user: this.client.id}})})
  }
}
</script>

<style scoped>

</style>