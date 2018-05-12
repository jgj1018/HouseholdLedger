<template>
  <div class="input">
    <h3>INPUT SECTION</h3>
    <input type="text">
    <input type="text">

    <button>SUBMIT</button>
    <button id="test" @click="show">Test</button>
    <div id="result">{{test}}</div>
  </div>
</template>

<script>
export default {
  name: 'Test',
  data () {
    return {
      test: ''
    }
  },
  methods: {
    show: function () {
      this.test = 'GETIT'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
