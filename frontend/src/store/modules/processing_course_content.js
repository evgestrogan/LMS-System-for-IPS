const axios = require('axios').default;

export default {
    state: {
        chapters_for_editions: {},
    },
    mutations: {
        state_chapters_for_editions(state, list){
            state.chapters_for_editions = list
        },
        clear_chapters_for_editions(state){
            state.chapters_for_editions = {}
        },
        create_chapter(state){
            state.chapters_for_editions.push({'id': null, 'name_chapter': '', 'subchapters': []})
        },
        create_subchapter(state, id_chapter) {
            state.chapters_for_editions[id_chapter].subchapters.push({'id': null, 'name_subchapter': ''})
        },
        create_test_for_chapter(state, id_chapter){
            state.chapters_for_editions[id_chapter]['test'] = {}
        },
    },
    actions: {
        get_chapters_for_editions({commit}, data) {
            return new Promise((resolve, reject) => {
	            axios({
                  method: 'get',
                  url: 'http://127.0.0.1:8000/api/chaptersSimple',
                  headers: data
                })
	            .then(resp => {
	                commit('state_chapters_for_editions', resp.data)
                    resolve(resp)
	            })
	            .catch(err => {
	                reject(err)
	            })
	        })
        },
        async create_or_edit_chapter({commit}, data) {
            return await new Promise((resolve, reject) => {
	            axios({url: 'http://127.0.0.1:8000/api/chaptersSimple/',
                    data: data,
                    method: 'POST',
                })
	            .then(resp => {
	                resolve(resp)
	            })
	            .catch(err => {
                    reject(err)
	            })
	        })
        },
        async save_file({commit}, data) {
            console.log(data.file)
            let formData = new FormData();
            formData.append('file', data.file)
            return await new Promise((resolve, reject) => {
	            axios({url: 'http://127.0.0.1:8000/api/subchapters/',
                    data: formData,
                    method: 'POST',
                    head: {'Content-Type': 'multipart/form-data'}
                })
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
        chapters_list_for_editions: state => state.chapters_for_editions,
    }
}