<template>
  <div id="app">
    <div style="float: right"  >
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
    }
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
