<template>
   <div class="input">
    <form id="loginForm">
        {% csrf_token %}
        <input type="hidden" name="next" value="" />
        <input type="text" name="email">
        <input type="text" name="password">
        {{ form.as_p }}
        <button type="submit">로그인</button>
    </form>

  </div>
</template>

<script>
import AccountingInput from './AccountingInput'

export default {
  name: 'Test',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {AccountingInput}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
