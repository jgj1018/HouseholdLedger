<template>
  <div id="app">
    <div style="float: left;">
      <ul>
        <router-link tag="li" :to="{name: 'Budget'}">Setting Budget</router-link>
        <router-link tag="li" :to="{name: 'accounting'}">Setting transaction</router-link>
      </ul>

    </div>
    <div style="float: right"  >
      <button @click.prevent="register">Sign up</button>
      <button @click.prevent="logout">Logout</button>
    </div>
    <router-view/>
  </div>
</template>

<script>
// import Http from './config/Http'
import axios from 'axios'
import Api from './config/Api'

export default {
  name: 'App',
  methods: {
    logout: async function () {
      let result = await axios.post(Api.account.logout)
      if (result.status === 200) {
        this.$router.push({name: 'login'})
      }
    },
    register: function () {
      this.$router.push({name: 'register'})
    }
  }
}
</script>

<style scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
ul {
  list-style-type: none;
}
ul > li {
  text-align: left;
  cursor: pointer;
}
</style>
