<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light mb-3">
          <a class="btn navbar-brand">Navbar</a>
          <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                <form class="form-inline my-2 my-lg-0">
                  <button class="btn btn-outline-info my-2 mr-sm-2" type="submit">Search</button>
                  <input class="form-control my-sm-0" type="search" placeholder="Search" aria-label="Search">
                </form>
              </li>
            </ul>
            <div class="form-inline my-2 my-lg-0 pr-4">
                <div v-if="authStatus !== 'success'">
                  <form class="login" @submit.prevent="login">
                    <div class="form-group">
                      <div class="form-group">
                        <input autocomplete="on" required v-model="username"class="form-control"  type="text" placeholder="Login"/>
                      </div>
                      <div class="form-group">
                        <input autocomplete="on" required v-model="password" type="password" class="form-control" placeholder="Password"/>
                      </div>
                      <button class="btn btn-outline-info my-2 ml-sm-2" type="submit">Login</button>
                    </div>
                  </form>
                </div>
                <div v-else class="form-inline">
                  <h5 class='mr-sm-2 my-2'>Привет</h5>
                  <button @click="logout" class="btn btn-outline-info my-2 mr-sm-2" style="width: 190px">Log-out</button>
                </div>
            </div>
          </div>
        </nav>
</template>
<script>
  import { mapGetters } from 'vuex';
  import store from "@/store";

  export default {
    name: "NavBar",
    data() {
      return {
        username: '',
        password: '',
      };
    },
    computed: {
      ...mapGetters(['authStatus']),
    },
    methods: {
      login: function () {
		   		let username = this.username
		   		let password = this.password
		   		this.$store.dispatch('authorizationUser', { 'username': username, 'password': password })
		   		.then(() => this.$router.push('body'))
		   		.catch(err => console.log(err))
		   	},
      logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/')
        })
      }
    },
  }
</script>

<style scoped>

</style>