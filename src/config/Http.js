import axios from 'axios'
import Cookies from 'js-cookie'
axios.interceptors.request.use(function (config) {
  let tokenCookie = Cookies.get('user-token')
  let token = null
  if (tokenCookie !== null && tokenCookie !== undefined) {
    try {
      token = JSON.parse(tokenCookie).data.token
    } catch (e) {
      token = tokenCookie
    }
  }
  if (config.method === 'get') {
    config.params = (config.params !== undefined) ? config.params : {}
    if (token !== null) {
      config.params.token = token
    }
    console.log('ToKEN GET')
    console.log(config.params.token)
  } else {
    config.data = (config.data !== undefined) ? config.data : {}
    if (token !== null) {
      config.data.token = token
    }
    console.log('ToKEN POST')
    console.log(config.data.token)
  }

  return config
}, function (error) {
  // Do something with request error
  return Promise.reject(error)
})
// Add a response interceptor
axios.interceptors.response.use(function (response) {
  let token = response.data.token

  if (token !== undefined) {
    let data = {token: token}
    console.log('ToKEN SAVE')
    console.dir(data)
    Cookies.set('user-token', {data: data})
  } else {
    console.log('ERRR')
  }
  return response
}, function (error) {
  // Do something with response error
  return Promise.reject(error)
})

export default {
  get (...args) {
    return axios.get(...args)
  },
  post (...args) {
    return axios.post(...args)
  }

}
