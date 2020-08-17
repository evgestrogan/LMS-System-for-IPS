import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'
import authentication from '../views/Authentication.vue'
import body from '../views/Profile.vue'
import edit from '../components/Editor'
import departments_list from '../components/Departments_list'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Authentication',
    component: authentication,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: body,
    meta: {
      requiresAuth: true
    },
    children: [
      {
        path: 'createCourse',
        component: edit
      },
      {
        path: 'departments',
        component: departments_list
      },
    ]
  },
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

router.beforeEach( (to, from, next) => {
  if (to.path === '/profile/departments') store.dispatch('get_departmets_list')
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
