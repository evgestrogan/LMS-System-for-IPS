<template>
  <v-list dark >

    <v-list-item class="justify-content-center">
      <v-list-item-avatar class="ma-0 pa-0" size="45">
        <v-img :src="'http://127.0.0.1:8000/media/' + client.avatar"></v-img>
      </v-list-item-avatar>
      <router-link :to="{ name: 'profile', params: { id_user: client.id }}"  class="text-decoration-none">
        <v-list-item-title class="pl-6 text-uppercase">{{client.last_name}} {{client.first_name}}</v-list-item-title>
      </router-link>
    </v-list-item>

    <v-divider></v-divider>
    <v-list-group prepend-icon="mdi-file-cad-box" value="false" color="white">
      <template v-slot:activator>
        <v-list-item-title class="text-uppercase">Кафедры</v-list-item-title>
      </template>
      <router-link v-for="department in return_departments_list" v-bind:key="department.id" :to="{ name: 'subjectContent', params: { id_department: department.id }}" class="text-decoration-none">
        <v-list-item link>
          <span class="text-uppercase">Кафедра {{ department.name_department}}</span>
          <v-spacer></v-spacer>
          <v-list-item-action v-if="department.boss_department === client.id">
            <v-btn icon>
              <v-icon>mdi-file-edit-outline</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
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
    <router-link :to="{name: 'course_creator'}" class="text-decoration-none" v-if="client.staff">
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

export default {
  name: "SideBar",
  computed: {
    ...mapGetters(['return_departments_list', 'client']),
  },
}
</script>

<style scoped>

</style>