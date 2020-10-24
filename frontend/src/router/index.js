import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'
import authentication from '../views/Authentication.vue'
import body from '../views/Profile.vue'
import edit from '../components/Editor'
import courseContent from '../components/CourseContent'
import subjectContent from '../components/SubjectContent'
import subchapterContent from '../components/SubchapterContent'
import profile from '../components/ProfileUser'
import courseCreator from '../components/CourseCreator'
import testContent from '../components/TestContent'
import editCourse from '../components/CourseEditor'

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
    path: '/',
    name: 'Profile',
    component: body,
    meta: {
      auth: true
    },

    children: [
      {
        path: 'course_creator',
        component: courseCreator,
        name: 'course_creator',
        meta: {
          auth: true,
        }
      },
      {
        path: 'user_:id_user',
        component: profile,
        name: 'profile',
        meta: {
          auth: true,
        },
      },
      {
        path: 'createCourse',
        component: edit,
        meta: {
          auth: true
        },
      },
      {
        path: 'department_:id_department',
        component: subjectContent,
        name: 'subjectContent',
        meta: {
          auth: true
        },
        props: true
      },
      {
        path: 'department_:id_department/edit_course_:id_course',
        component: editCourse,
        name: 'editCourse',
        meta: {
          auth: true
        },
      },
      {
        path: 'department_:id_department/course_:id_course',
        component: courseContent,
        name: 'courseContent',
        meta: {
          auth: true
        },
      },
      {
        path: 'department_:id_department/course_:id_course/subchapter_:id_subchapter',
        component: subchapterContent,
        name: 'subchapterContent',
        meta: {
          auth: true
        },
      },
      {
        path: 'department_:id_department/course_:id_course/test_:id_test',
        component: testContent,
        name: 'testContent',
        meta: {
          auth: true
        },
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
    .then(() => next({ name: 'profile' }))
    .catch(() => next())
  } else {
    store.dispatch('refreshTokens')
    .then(() => next())
    .catch(() => next({ name: 'Authentication' }))
  }
})

export default router
