<template>
  <div class="hello">
    <form id="loginForm" @submit.prevent="submitRegister" method="post">
      <input type="text" v-model="username" placeholder="username">
      <input type="text" v-model="email" placeholder="email">
      <input type="password" v-model="password1" placeholder="password1">
      <input type="password" v-model="password2" placeholder="password2">
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
import Http from '../config/Http'
import Api from '../config/Api'

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
      try {
        let resp = await Http.post(Api.account.register,
          {username: this.username, email: this.email, password1: this.password1, password2: this.password2})
          .catch((error) => {
            console.dir(error.response.data)
            this.errors = error.response.data
          })

        if (resp.data.token !== undefined) {
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
