<template>
  <div class="hello">
    <form id="loginForm" @submit.prevent="submitLogin" method="post">
      <input type="text" v-model="email">
      <input type="text" v-model="password">
      <button type="submit" >로그인</button>
    </form>
    <div>{{loginResult}}</div>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      loginResult: '',
      results: ''
    }
  },
  methods: {
    submitLogin: async function (e) {
      let resp = await axios.post('http://0.0.0.0:8000/account/login/', {email: this.email, password: this.password})
      if (resp.data !== undefined) {
        Cookies.set('user-token', resp)
        this.loginResult = 'SUCCESS'
      } else {
        this.loginResult = 'SUCCESS'
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
