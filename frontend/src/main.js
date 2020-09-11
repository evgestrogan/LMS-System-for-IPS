import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
import CKEditor from '@ckeditor/ckeditor5-vue';
import vuetify from './plugins/vuetify';

Vue.use( CKEditor );

Vue.prototype.$http = Axios;

Vue.config.productionTip = false

new Vue({
  CKEditor,
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
