<template>
  <v-list dark >
    <alert-component v-if="error" :status="error"></alert-component>
    <v-list-item class="justify-content-center">
      <v-list-item-avatar class="ma-0 pa-0" size="45">
        <v-img :src="'http://127.0.0.1:8000' + user_avatar"></v-img>
      </v-list-item-avatar>
      <router-link :to="{ name: 'Profile', params: { id_user: user_id }}"  class="text-decoration-none">
        <v-list-item-title class="pl-6 text-uppercase">{{user_info.last_name}} {{user_info.first_name}}</v-list-item-title>
      </router-link>
    </v-list-item>

    <v-divider></v-divider>
    <v-list-group prepend-icon="mdi-file-cad-box" value="false" color="white">
      <template v-slot:activator>
        <v-list-item-title class="text-uppercase">Кафедры</v-list-item-title>
      </template>
      <v-divider></v-divider>
      <router-link v-for="department in departments" v-bind:key="department.id" :to="{ name: 'Department', params: { id_department: department.id }}" class="text-decoration-none">
        <v-list-item link class="row">
          <v-list-item>
            <span class="text-uppercase">Кафедра {{ department.name}}</span>
            <v-spacer></v-spacer>
            <v-list-item-action v-if="department.manager.user.id === user_id">
              <v-btn icon>
                <v-icon>mdi-file-edit-outline</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
          <v-list-item>
            <span class="caption">Начальник кафедры: {{ department.manager.user.last_name}} {{ department.manager.user.first_name}} {{ department.manager.user.second_name}}</span>
          </v-list-item>
        </v-list-item>
        <v-divider></v-divider>
      </router-link>
    </v-list-group>
    <v-list-group prepend-icon="mdi-feature-search-outline" value="false" color="white">
      <template v-slot:activator>
        <v-list-item-title class="text-uppercase">Мои курсы</v-list-item-title>
      </template>
    </v-list-group>
    <v-list-group prepend-icon="mdi-clipboard-list-outline" value="false" color="white">
      <template v-slot:activator>
        <v-list-item-title class="text-uppercase">Мои тесты</v-list-item-title>
      </template>
    </v-list-group>
    <router-link :to="{name: 'CourseСonstructorPage'}" class="text-decoration-none" v-if="user_status">
      <v-list-item link prepend-icon="mdi-new-box">
        <v-list-item-action>
          <v-icon>mdi-new-box</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="text-uppercase">Создать курс</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </router-link>
  </v-list>
</template>

<script>
import {mapGetters} from "vuex";
import alertComponent from "@/components/AlertComponent";

export default {
  name: "SideBar",
  computed: {
    ...mapGetters(['user_id', 'user_avatar', 'user_info', 'user_status', 'departments']),
  },
  data: function () {
    return {
      error: null,
    }
  },
  components: {
    alertComponent,
  },
  created() {
    this.$store.dispatch('get_user_info', {'id': this.user_id})
    .catch(err => {
      this.error = err.request.status
    })
    this.$store.dispatch('departments')
    .catch(err => {
      this.error = err.request.status
    })
  },
}
</script>

<style scoped>

</style>