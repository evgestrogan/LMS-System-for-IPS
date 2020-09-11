import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'
import authentication from '../views/Authentication.vue'
import body from '../views/Profile.vue'
import edit from '../components/Editor'
import dashboard from '../components/Dashboard'
import courseContent from '../components/CourseContent'
import subjectContent from '../components/SubjectContent'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Authentication',
    component: authentication,
    meta: {
      auth: false
    },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: body,
    meta: {
      auth: true
    },

    children: [
      {
        path: 'createCourse',
        component: edit,
        meta: {
          auth: true
        },
      },

      {
        path: '/',
        component: dashboard,
        name: 'dashboard',
        meta: {
          auth: true
        },

        children: [
          {
            path: 'department_' +
                ':id_department',
            component: subjectContent,
            name: 'subjectContent',
            meta: {
              auth: true
            },
          },
          {
            path: 'course_:id_course',
            component: courseContent,
            name: 'courseContent',
            meta: {
              auth: true
            },
          },
        ]
      },
    ]
  },
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

router.beforeEach((to, from, next) => {
  if (!to.matched.some(record => record.meta.auth)) {
    store.dispatch('refreshTokens')
    .then(() => next({ name: 'Profile' }))
    .catch(() => next())
  } else {
    store.dispatch('refreshTokens')
    .then(() => next())
    .catch(() => next({ name: 'Authentication' }))
  }
})

export default router
