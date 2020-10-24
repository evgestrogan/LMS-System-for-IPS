import router from "@/router";

const axios = require('axios').default;

export default {
    state: {
    },
    mutations: {
    },
    actions: {
        async create_course({commit}, data) {
            return await new Promise((resolve, reject) => {
	            axios({url: 'http://127.0.0.1:8000/api/courses/',
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
    },
    getters: {
        return_test: state => state.test,
    }
};
