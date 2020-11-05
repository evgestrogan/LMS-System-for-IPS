<template>
  <v-col cols="12" sm="8" md="4">
    <v-card class="elevation-12">
      <v-toolbar color="purple lighten-3" dark flat>
        <v-toolbar-title>Login form</v-toolbar-title>
      </v-toolbar>
      <alert-component v-if="error !== null" :status="error"></alert-component>
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
</template>

<script>
  import router from "@/router";
  import {mapGetters} from "vuex";
  import alertComponent from "@/components/AlertComponent";

  export default {
    data() {
      return {
        username: '',
        password: '',
        error: null,
      };
    },
    components: {
      alertComponent,
    },
    computed: {
      ...mapGetters(['user_id']),
    },
    methods: {
      login: function () {
        this.error = null
        this.$store.dispatch('authorization', { 'username': this.username, 'password': this.password })
        .then(resp => {
          router.push({name: 'Profile', params: {id_user: this.user_id}})
        })
        .catch(err => {
          this.error = err.request.status
        })
      },
    },
  }
</script>
