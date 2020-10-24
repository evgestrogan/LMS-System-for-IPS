import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth-user';
import body from './modules/get-body';
import create_body from './modules/create-body'
import processing_course_content from './modules/processing_course_content'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    body,
    create_body,
    processing_course_content,
  },
});