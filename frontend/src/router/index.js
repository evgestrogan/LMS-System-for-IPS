import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'
import authentication from '../views/Authentication.vue'
import body from '../views/body.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Authentication',
    component: authentication,
  },
  {
    path: '/body',
    name: 'Body',
    component: body,
    meta: {
        requiresAuth: true
    }
  },
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

router.beforeEach( (to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
      store.dispatch('verifyToken')
      .then(() => {
        next()
        // return
      })
          .catch(err => next('/'))
    } else {
      next()
    }


})


export default router
