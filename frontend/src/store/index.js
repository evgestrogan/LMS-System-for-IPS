import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth-user';
import body from './modules/get-body';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    body,
  },
});