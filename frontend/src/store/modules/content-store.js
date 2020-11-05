const axios = require('axios').default;

export default {
    state: {
        drawer: false,
        departments: [],
        department: {'subject': []},
        course: {},
        subchapter: {},
    },
    mutations: {
        state_drawer(state) {
            state.drawer = !state.drawer
        },
        state_departments(state, response) {
          state.departments = response
        },
        state_department(state, response) {
          state.department = response
        },
        clear_department(state) {
            state.department = {}
        },
        state_course(state, response) {
          state.course = response
        },
        clear_course(state, response) {
          state.course = {}
        },
        state_subchapter(state, response) {
          state.subchapter = response
        },
    },
    actions: {
        async departments({ commit }) {
            return await new Promise((resolve, reject) => {
                axios.get( 'http://127.0.0.1:8000/api/departments/')
                .then(resp => {
                    commit('state_departments', resp.data)
                    resolve(resp)
                })
                .catch(err => {
                    reject(err)
                })
            })
        },
        async department({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios.get( 'http://127.0.0.1:8000/api/department/' + data.id)
                .then(resp => {
                    commit('state_department', resp.data)
                    resolve(resp)
                })
                .catch(err => {
                    reject(err)
                })
            })
        },
        async course({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios.get( 'http://127.0.0.1:8000/api/course/' + data.id)
                .then(resp => {
                    commit('state_course', resp.data)
                    resolve(resp)
                })
                .catch(err => {
                    reject(err)
                })
            })
        },
        async subchapter({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios.get( 'http://127.0.0.1:8000/api/subchapter/' + data.id)
                .then(resp => {
                    commit('state_subchapter', resp.data)
                    resolve(resp)
                })
                .catch(err => {
                    reject(err)
                })
            })
        },
        async test({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios.get( 'http://127.0.0.1:8000/api/test/' + data.id)
                .then(resp => {
                    resolve(resp)
                })
                .catch(err => {
                    reject(err)
                })
            })
        },
    },
    getters: {
        drawer: state => state.drawer,
        departments: state => state.departments,
        department: state => state.department,
        course: state => state.course,
        subchapter: state => state.subchapter,
    }
}