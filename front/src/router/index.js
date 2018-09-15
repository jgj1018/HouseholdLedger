import Vue from 'vue'
import Router from 'vue-router'
import Cookies from 'js-cookie'

import AccountingBooks from '@/components/AccountingBooks'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Budget from '@/components/Budget'
import Profit from '@/components/Profit'
import Http from '../config/Http'
Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/set-budget',
      name: 'Budget',
      component: Budget
    },
    {
      path: '/profit',
      name: 'profit',
      component: Profit
    },
    {
      path: '/',
      name: 'accounting',
      component: AccountingBooks
    }

  ]
})

router.beforeEach((to, from, next) => {
  let path = to.path
  console.log(path)
  if (path !== '/login' && path !== '/register') {
    guard(to, from, next)
  } else {
    next()
  }
})

function guard (to, from, next) {
  let tokenCookie = Cookies.get('user-token')
  if (tokenCookie === null || tokenCookie === undefined) {
    next('/login')
  }
  if (!Http.checkTokenExpiration(tokenCookie)) {
    Http.refreshToken(tokenCookie)
    next()
  } else {
    Cookies.remove('user-token')
    next('/login')
  }
}

export default router
