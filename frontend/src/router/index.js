import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'
import authentication from '../views/AuthenticationPage.vue'
import profile from '../views/ProfilePage'
import department from '../views/DepartmentPage'
import course from '../views/CoursePage'
import subchapterPage from '../views/SubchapterPage'
import testPage from '../views/TestPage'
import course_constructorPage from '../views/CourseСonstructorPage'
import chapters_constructorPage from '../views/ChaptersConstructorPage'

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
    path: '/user/:id_user',
    name: 'Profile',
    component: profile,
    meta: {
      auth: true
    },
  },
  {
    path: '/department/:id_department',
    name: 'Department',
    component: department,
    meta: {
      auth: true
    },
  },
  {
    path: '/department/:id_department/course/:id_course',
    name: 'Course',
    component: course,
    meta: {
      auth: true
    },
  },
  {
    path: '/department/:id_department/course/:id_course/subchapter/:id_subchapter',
    name: 'SubchapterPage',
    component: subchapterPage,
    meta: {
      auth: true
    },
  },
  {
    path: '/test/:id_test/',
    name: 'TestPage',
    component: testPage,
    meta: {
      auth: true
    },
  },
  {
    path: '/courseConstructor/',
    name: 'CourseСonstructorPage',
    component: course_constructorPage,
    meta: {
      auth: true
    },
    children: [
      {
        path: '/courseConstructor/:id_course',
        name: 'CourseEditorPage',
        component: course_constructorPage,
        meta: {
          auth: true
        },
      },
    ],
  },
  {
    path: '/chaptersConstructor/:id_course',
    name: 'ChaptersСonstructorPage',
    component: chapters_constructorPage,
    meta: {
      auth: true
    },
  },
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

router.beforeEach((to, from, next) => {
  if (!to.matched.some(record => record.meta.auth)) {
    store.dispatch('refresh')
    .then(() => next({ name: 'Profile', params: {id_user: store.getters.user_id}}))
    .catch(() => next())
  } else {
    store.dispatch('refresh')
    .then(() => next())
    .catch(() => next({ name: 'Authentication' }))
  }
})

export default router
