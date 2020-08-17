import router from "@/router";

const axios = require('axios').default;
import VueJwtDecode from 'vue-jwt-decode'

export default {
    state: {
        status: '',
  		refresh_token: localStorage.getItem('refresh_token') || '',
        user: {}
    },
    mutations: {
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token){
            state.status = 'success'
            state.refresh_token = token
        },
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = ''
            state.refresh_token = ''
        },
        login_success(state){
            state.status = 'success'
        },
        appendUser(state, username){
            state.user = username
        }
    },
    actions: {
        authorizationUser({commit}, user) {
            return new Promise((resolve, reject) => {
	            commit('auth_request')
	            axios({url: 'http://127.0.0.1:8000/auth/access/', data: user, method: 'POST' })
	            .then(resp => {
	                const refresh_token = resp.data.refresh
	                const access_token = resp.data.access
	                localStorage.setItem('refresh_token', refresh_token)
	                sessionStorage.setItem('access_token', access_token)
	                axios.defaults.headers.common['Authorization'] = refresh_token
	                commit('auth_success', refresh_token)
                    // const user = VueJwtDecode.decode(access_token).user_id
                    commit('appendUser', VueJwtDecode.decode(access_token).user_id)
	                resolve(resp)
	            })
	            .catch(err => {
	                commit('auth_error')
	                localStorage.removeItem('refresh_token')
	                reject(err)
	            })
	        })
        },
        verifyToken(ctx){
            return new Promise((resolve, reject) => {
                ctx.commit('auth_request')
                axios({url: 'http://127.0.0.1:8000/auth/verify/', data: {token: sessionStorage.getItem('access_token')}, method: 'POST'})
                .then(resp => {
                    ctx.commit('login_success')
                    commit('appendUser', VueJwtDecode.decode(sessionStorage.getItem('access_token')).user_id)
                    resolve(resp)
                })
                .catch(err => {
                    ctx.dispatch('refreshTokens')
                    .then(resp => {
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
                })
            })
        },
        refreshTokens({commit}) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({url: 'http://127.0.0.1:8000/auth/refresh/', data: {refresh: localStorage.getItem('refresh_token')}, method: 'POST'})
                .then(resp => {
                    const refresh_token = resp.data.refresh
	                const access_token = resp.data.access
	                localStorage.setItem('refresh_token', refresh_token)
	                sessionStorage.setItem('access_token', access_token)
                    axios.defaults.headers.common['Authorization'] = refresh_token
                    commit('auth_success', refresh_token)
                    commit('appendUser', VueJwtDecode.decode(access_token).user_id)
	                resolve(resp)
                })
                .catch(err => {
                    commit('auth_error')
	                localStorage.removeItem('refresh_token')
                    sessionStorage.removeItem('access_token')
	                reject(err)
                })
            })
        },
        logout({commit}){
            return new Promise((resolve, reject) => {
                commit('logout')
                localStorage.removeItem('refresh_token')
                sessionStorage.removeItem('access_token')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        },
        getUser({commit}){
            const user = VueJwtDecode.decode(sessionStorage.getItem('access_token')).user_id
            commit('appendUser', user.username)
        }
    },
    getters: {
        isLoggedIn: state => !!state.refresh_token,
        authStatus: state => state.status,
        userName: state => state.user,
    },
};
