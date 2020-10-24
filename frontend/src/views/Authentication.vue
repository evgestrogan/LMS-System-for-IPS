<template>
  <v-row align="center" justify="center">
    <v-col cols="12" sm="8" md="4">
      <v-card class="elevation-12">
        <v-toolbar color="purple lighten-3" dark flat>
          <v-toolbar-title>Login form</v-toolbar-title>
        </v-toolbar>
        <v-alert v-if="error" type="error" icon="mdi-shield-alert-outline">
          Check your username or password
        </v-alert>
        <v-card-text>
          <v-form>
            <v-text-field label="Login" name="login" prepend-icon="mdi-account" type="text" v-model="username"></v-text-field>
            <v-text-field id="password" label="Password" name="password" prepend-icon="mdi-lock" type="password" v-model="password"></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn class="ps-16 pr-16" large color="teal lighten-3" dark @click="login">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  import router from "@/router";
  import {mapGetters} from "vuex";

  export default {
    data() {
      return {
        username: '',
        password: '',
        error: false
      };
    },
    computed: {
      ...mapGetters(['client']),
    },
    methods: {
      login: function () {
        let username = this.username
        let password = this.password
        this.$store.dispatch('authorizationUser', { 'username': username, 'password': password })
        .then(resp => {router.push({name: 'profile', params: { id_user: this.client.id }})})
        .catch(err => { this.error = true })
      },
    },
  }
</script>
