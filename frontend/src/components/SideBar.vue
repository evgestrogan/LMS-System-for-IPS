<template>
  <v-list dark class="text-center">
    <v-list-item-avatar class="ma-0 pa-0" size="150">
      <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>
    </v-list-item-avatar>
    <v-list-item>
      <v-list-item-title>{{this.userName.username}}</v-list-item-title>
    </v-list-item>
    <v-divider></v-divider>
    <router-link v-if="userName.staff" to="/profile/createCourse" class="text-decoration-none">
      <v-list-item link>
        <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </router-link>
    <router-link v-for="(department, id) in return_departments_list" v-bind:key="id" :to="{ name: 'subjectContent', params: { id_department: id }}" class="text-decoration-none">
      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title>Кафедра {{ department.name_department}}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </router-link>
  </v-list>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "SideBar",
  computed: {
    ...mapGetters(['return_departments_list', 'userName']),
  },
}
</script>

<style scoped>

</style>