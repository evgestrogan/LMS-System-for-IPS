const axios = require('axios').default;

export default {
    state: {
        drawer: false,
        departments_list: {},
        subjects_list: {},
        chapter_list: {},
    },
    mutations: {
        state_drawer(state){
          state.drawer = !state.drawer
        },
        state_departmets_list(state, list){
            state.departments_list = list
        },
        state_subjects_list(state, list){
            state.subjects_list = list
        },
        clear_subjects_list(state){
            state.subjects_list = {}
        },
        state_chapters_list(state, list){
            state.chapter_list = list
        },
        clear_chapters_list(state){
            state.chapter_list = {}
        },
    },
    actions: {
        get_departmets_list({commit}) {
            return new Promise((resolve, reject) => {
	            axios.get('http://127.0.0.1:8000/api/departments')
	            .then(resp => {
	                commit('state_departmets_list', resp.data)
                    resolve(resp)
	            })
	            .catch(err => {
	                reject(err)
	            })
	        })
        },
        get_subjects_list({commit}, data) {
            return new Promise((resolve, reject) => {
	            axios({
                  method: 'get',
                  url: 'http://127.0.0.1:8000/api/subjects',
                  headers: data
                })
	            .then(resp => {
	                commit('state_subjects_list', resp.data)
                    resolve(resp)
	            })
	            .catch(err => {
	                reject(err)
	            })
	        })
        },
        get_chapters_list({commit}, data) {
            return new Promise((resolve, reject) => {
	            axios({
                  method: 'get',
                  url: 'http://127.0.0.1:8000/api/chapters',
                  headers: data
                })
	            .then(resp => {
	                commit('state_chapters_list', resp.data)
                    resolve(resp)
	            })
	            .catch(err => {
	                reject(err)
	            })
	        })
        },
    },
    getters: {
        return_drawer: state => state.drawer,
        return_departments_list: state => state.departments_list,
        return_subjects_list: state => state.subjects_list,
        return_chapters_list: state => state.chapter_list,
    },
};
