import VueJwtDecode from "vue-jwt-decode";

const axios = require('axios').default;

export default {
    state: {
        departments_list: NaN,
    },
    mutations: {
        state_departmets_list(state, list){
            state.departments_list = list
        }
    },
    actions: {
        get_departmets_list({commit}) {
            const auth = 'Bearer ' + sessionStorage.getItem('access_token')
            return new Promise((resolve, reject) => {
	            axios.get('http://127.0.0.1:8000/api/courses/', { headers: { Authorization: auth }})
	            .then(resp => {
	                console.log('resp')
	                commit('state_departmets_list', resp.data)
                    resolve(resp)
	            })
	            .catch(err => {
	                console.log(err)
	                reject(err)
	            })
	        })
        },
    },
    getters: {
        return_departments_list: state => state.departments_list,
    },
};
