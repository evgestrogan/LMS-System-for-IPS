import router from "@/router";

const axios = require('axios').default;
import VueJwtDecode from 'vue-jwt-decode'

export default {
    state: {
        client_status: false,
        client: {},
        profile: {},
    },
    mutations: {
        auth_success(state, resp){
            const refresh_token = resp.resp.data.refresh
            const access_token = resp.resp.data.access
            localStorage.setItem('refresh_token', refresh_token)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + access_token
            const client = VueJwtDecode.decode(access_token)
            state.client = client.user_id
            state.client_status = true
        },
        state_profile_information(state, resp){
            state.profile = resp
        },
        auth_error(state){
            localStorage.removeItem('refresh_token')
            delete axios.defaults.headers.common['Authorization']
            state.client = {}
            state.profile = {}
            state.client_status = false
        },
    },
    actions: {
        get_user_information({commit}, id){
            return new Promise((resolve, reject) => {
                axios.get('http://127.0.0.1:8000/api/user_info/' + id.id)
                .then(resp => {
                    commit('state_profile_information', resp.data)
                    resolve(resp)
                })
                .catch(err => {
                    reject(err)
                })
            })
        },
        async authorizationUser({ commit }, user) {
            return await new Promise((resolve, reject) => {
	            axios({url: 'http://127.0.0.1:8000/auth/access/',
                    data: user,
                    method: 'POST',
                })
	            .then(resp => {
	                commit('auth_success', { resp })
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
        client_status: state => state.client_status,
        client: state => state.client,
        profile: state => state.profile,
    }
};
