<template>
  <div class="hello">
    <form id="loginForm" @submit.prevent="submitRegister" method="post">
      <input type="text" v-model="username" placeholder="username">
      <input type="text" v-model="email" placeholder="email">
      <input type="text" v-model="password1" placeholder="password1">
      <input type="text" v-model="password2" placeholder="password2">
      <div>
          <ul>
            <li v-bind:key="param" v-for="(messages, param) in errors">
              {{param}} {{messages}}
            </li>
          </ul>
      </div>
      <button type="submit" >Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'
import Host from '../config/Host'

export default {
  name: 'Register',
  data () {
    return {
      email: '',
      password1: '',
      username: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    submitRegister: async function (e) {
      const host = Host.host
      const port = Host.port
      try {
        let resp = await axios.post(host + ':' + port + '/account/registration/',
          {username: this.username, email: this.email, password1: this.password1, password2: this.password2})
          .catch((error) => {
            console.dir(error.response.data)
            this.errors = error.response.data
          })

        if (resp.data !== undefined) {
          Cookies.set('user-token', resp)
          this.$router.push({name: 'accounting'})
        }
      } catch (e) {
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
