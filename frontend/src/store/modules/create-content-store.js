const axios = require('axios').default;

export default {
    state: {},
    mutations: {},
    actions: {
        async subchapter_creator_editor({ commit }, data) {
            console.log(data)
            let formData = new FormData()
            formData.append('file', data.body);
            formData.append('info', JSON.stringify(data));
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/api/subchapter/',
                    data: formData,
                    method: 'POST',
                    headers: { 'Content-Type': 'multipart/form-data' },
                })
                .then(resp => {resolve(resp)})
                .catch(err => {reject(err)})
            })
        },
        async chapter_creator_editor({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/api/chapter/',
                    data: data,
                    method: 'POST',
                })
                .then(resp => {resolve(resp)})
                .catch(err => {reject(err)})
            })
        },
        async course_creator_editor({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/api/courses/',
                    data: data,
                    method: 'POST',
                })
                .then(resp => {resolve(resp)})
                .catch(err => {reject(err)})
            })
        },
        async test_creator_editor({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/api/tests/',
                    data: data,
                    method: 'POST',
                })
                .then(resp => {
                    resolve(resp)
                })
                .catch(err => {reject(err)})
            })
        },
        async register_for_the_course({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/api/course/' + data.id + '/',
                    data: data,
                    method: 'PUT',
                })
                .then(resp => {resolve(resp)})
                .catch(err => {reject(err)})
            })
        },
    },
    getters: {},
}