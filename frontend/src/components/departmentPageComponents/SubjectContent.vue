<template>
  <v-expansion-panel-header color="blue-grey lighten-5">
    <div class="col-8">
      <v-row class="text--disabled text-overline text-uppercase">Название предмета</v-row>
      <v-row class="text-lg-h5 font-weight-light">{{ subject.name }}</v-row>
    </div>
    <div class="col-6">
      <v-row class="text--disabled text-overline text-uppercase justify-center">Начальник цикла</v-row>
      <v-row class="justify-center"><v-avatar><v-img :src="'http://127.0.0.1:8000' + subject.manager.avatar"></v-img></v-avatar></v-row>
      <v-row class="text-lg-body-1 font-weight-light justify-center">
        <router-link :to="{ name: 'Profile', params: { id_user: subject.manager.user.id }}" class="text-decoration-none">
          {{ subject.manager.user.last_name }} {{ subject.manager.user.first_name }} {{ subject.manager.user.second_name }}
        </router-link>
      </v-row>
    </div>
  </v-expansion-panel-header>
</template>

<script>
export default {
  name: "subjectContent",
  props: {
    subject: Object,
  },
}
</script>

<style scoped>

</style>