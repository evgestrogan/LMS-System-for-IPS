import router from "@/router";

const axios = require('axios').default;
import VueJwtDecode from 'vue-jwt-decode'

export default {
    state: {
        status: false,
        user: {}
    },
    mutations: {
        auth_success(state, resp){
            const refresh_token = resp.resp.data.refresh
            const access_token = resp.resp.data.access
            localStorage.setItem('refresh_token', refresh_token)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + access_token
            state.user = VueJwtDecode.decode(access_token).user_id
            state.status = true
        },
        auth_error(state){
            state.user = {}
            localStorage.removeItem('refresh_token')
            delete axios.defaults.headers.common['Authorization']
            state.status = false
        },
    },
    actions: {
        async authorizationUser({ commit }, user) {
            return await new Promise((resolve, reject) => {
	            axios({url: 'http://127.0.0.1:8000/auth/access/',
                    data: user,
                    method: 'POST',
                })
	            .then(resp => {
	                commit('auth_success', { resp })
                    router.push('/profile')
                    resolve(resp)
	            })
	            .catch(err => {
	                commit('auth_error')
	                reject(err)
	            })
	        })
        },

        async refreshTokens({ commit }) {
            return await new Promise((resolve, reject) => {
                axios({
                    url: 'http://127.0.0.1:8000/auth/refresh/',
                    data: {refresh: localStorage.getItem('refresh_token')},
                    method: 'POST',
                })
                .then(resp => {
                    commit('auth_success', {resp})
                    resolve(resp)
                })
                .catch(err => {
                    commit('auth_error')
                    reject(err)
                })
            })
        },
    },
    getters: {
        authStatus: state => state.status,
        userName: state => state.user,
    },
};
