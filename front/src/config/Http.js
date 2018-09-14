import axios from 'axios'
import Cookies from 'js-cookie'
import jwtDecode from 'jwt-decode'
import Api from './Api'
import Router from '../router/index'
const JWT_TAG = 'JWT '
axios.interceptors.request.use(function (config) {
  let url = config.url.toLowerCase()

  if ((!url.includes('account') && !url.includes(Api.account.refreshToken))) {
    let tokenCookie = Cookies.get('user-token')

    if (tokenCookie !== null && tokenCookie !== undefined) {
      config.headers.common['Authorization'] = JWT_TAG + tokenCookie
    }
  }
  return config
}, function (error) {
  // Do something with request error
  return Promise.reject(error)
})

// Add a response interceptor
axios.interceptors.response.use(function (response) {
  // let token = response.data['token']
  let req = response.request
  let url = req.responseURL.toLowerCase()
  if ((!url.includes('account') && !url.includes(Api.account.refreshToken))) {
    let token = Cookies.get('user-token')
    refreshToken(token)
  } else {
    let token = response.data['token']
    if (!checkTokenExpiration(token)) {
      Cookies.set('user-token', token)
    }
  }

  return response
}, function (error) {
  if (error.response.status === 400) {
    Cookies.remove('user-token')
    Router.push({name: 'login'})
  }
})

function checkTokenExpiration (token) {
  if (token === null || token === undefined) {
    return true
  }

  let decoded = jwtDecode(token)
  let currentTime = new Date().getTime() / 1000
  console.log(currentTime)
  console.log(decoded.exp)
  if (currentTime > decoded.exp) {
    return true
  } else {
    return false
  }
}

async function refreshToken (token) {
  let resp = await axios.post(Api.account.refreshToken, {'token': token})
  let refreshed = resp.data['token']
  if (refreshed !== undefined) {
    Cookies.set('user-token', refreshed)
  }
}

export default {
  get (...args) {
    return axios.get(...args)
  },
  post (...args) {
    return axios.post(...args)
  },
  'refreshToken': refreshToken,
  'checkTokenExpiration': checkTokenExpiration

}
