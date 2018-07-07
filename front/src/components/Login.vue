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
import Host from '../config/Host'

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
      const host = Host.host
      const port = Host.port
      let resp = await axios.post(host + ':' + port + '/account/login/', {email: this.email, password: this.password})
      if (resp.data !== undefined) {
        Cookies.set('user-token', resp)
        this.$router.push({name: 'accounting'})
        this.loginResult = 'SUCCESS'
      } else {
        this.loginResult = 'Fail'
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
