import axios from 'axios'
import Cookies from 'js-cookie'
import jwtDecode from 'jwt-decode'
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
  if (token !== null) {
    config.headers.common['Authorization'] = 'Bearer' + token
    let userInfo = jwtDecode(token)
    config.data = (config.data) ? config.data : {}
    config.data['user'] = userInfo['user_id']
  }
  return config
}, function (error) {
  // Do something with request error
  return Promise.reject(error)
})
// Add a response interceptor
axios.interceptors.response.use(function (response) {
  let token = response.data['token']
  let req = response.request
  if (req.responseURL.toLowerCase().includes('/account/logout') &&
        req.status === 200) {
    console.log('logOut')
    Cookies.remove('user-token')
  }

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
