const axios = require('axios').default;
import VueJwtDecode from 'vue-jwt-decode'


export default {
    state: {
        user_id: null,
        user_status: null,
        user_info: {},
        user_avatar: null,
        profile_info: {},
        profile_avatar: null,
        is_authenticated: false,
    },
    mutations: {
        state_main_user_data(state, response) {
            const refresh_token = response.resp.data.refresh
            const access_token = response.resp.data.access
            localStorage.setItem('refresh_token', refresh_token)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + access_token
            const user = VueJwtDecode.decode(access_token)
            state.user_id = user.user_id.id
            state.user_status = user.user_id.staff
            state.is_authenticated = true
        },
        clear_main_user_data(state) {
            localStorage.removeItem('refresh_token')
            delete axios.defaults.headers.common['Authorization']
            state.user_id = null
            state.user_status = null
            state.is_authenticated = false
        },
        state_user_info(state, response) {
            state.user_info = response
        },
        clear_user_info(state) {
            state.user_info = {}
        },
    },
    actions: {
        async authorization({ commit }, user) {
            return await new Promise((resolve, reject) => {
	            axios({url: 'http://127.0.0.1:8000/auth/access/',
                    data: user,
                    method: 'POST',
                })
	            .then(resp => {
	                commit('state_main_user_data', { resp })
                    resolve(resp)
	            })
	            .catch(err => {
	                commit('clear_main_user_data')
	                reject(err)
	            })
	        })
        },
        async refresh({ commit }) {
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/auth/refresh/',
                    data: { refresh: localStorage.getItem('refresh_token') },
                    method: 'POST',
                })
                .then(resp => {
                    commit('state_main_user_data', {resp})
                    resolve(resp)
                })
                .catch(err => {
                    commit('clear_main_user_data')
                    reject(err)
                })
            })
        },
        async get_user_info({ commit }, data) {
            return await new Promise((resolve, reject) => {
                axios.get( 'http://127.0.0.1:8000/api/user/' + data.id)
                .then(resp => {
                    commit('state_user_info', resp.data)
                    resolve(resp)
                })
                .catch(err => {
                    commit('clear_user_info')
                    reject(err)
                })
            })
        },
    },
    getters: {
        is_authenticated: state => state.is_authenticated,
        user_id: state => state.user_id,
        user_info: state => state.user_info,
        user_status: state => state.user_status,
        user_avatar: state => {
            if (state.user_info.manager) {
                return state.user_info.manager.avatar
            }
            if (state.user_info.student) {
                return state.user_info.student.avatar
            }
            return null
        },
        user_manager_id: state => {
            if (state.user_info.manager) {
                return state.user_info.manager.id
            }
            return null
        },
    }
}