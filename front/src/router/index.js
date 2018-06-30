import Vue from 'vue'
import Router from 'vue-router'
import AccountingBooks from '@/components/AccountingBooks'
import Login from '@/components/Login'
import Cookies from 'js-cookie'
import jwtDecode from 'jwt-decode'
Vue.use(Router)
const router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/',
      name: 'accouting',
      component: AccountingBooks
    }
  ]
})
router.beforeEach((to, from, next) => {
  let path = to.path
  console.log(path)
  if (path !== '/login') {
    guard(to, from, next)
  } else {
    next()
  }
})

function guard (to, from, next) {
  let tokenCookie = Cookies.get('user-token')
  let token = null
  if (tokenCookie !== null && tokenCookie !== undefined) {
    try {
      token = JSON.parse(tokenCookie).data.token
    } catch (e) {
      token = tokenCookie
    }
  } else {
    next('/login')
  }
  if (checkTokenExpiration(token)) {
    next()
  } else {
    next('/login')
  }
}

function checkTokenExpiration (token) {
  if (token === null || token === undefined) {
    return false
  }

  let decoded = jwtDecode(token)
  let currentTime = new Date().getTime() / 1000
  console.log(currentTime)
  console.log(decoded.exp)
  if (currentTime > decoded.exp) {
    return false
  } else {
    return true
  }
}

export default router
