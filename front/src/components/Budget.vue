<template>
  <div class="hello">
    <form id="loginForm" @submit.prevent="createBudget" method="post">
      <input type="text" v-model="budgetName" placeholder="budgetName">
      <select v-model="type">
          <option value=""></option>
          <option :value="item.code"
          v-for="(item, idx) in budgetType" :key="idx"
          >{{item.name}}</option>
      </select>
      <input type="number" v-model="costAmount" placeholder="amount">
      <div>
          <ul>
            <li v-bind:key="param" v-for="(messages, param) in errors">
              {{param}} {{messages}}
            </li>
          </ul>
      </div>
      <button type="submit" >Register</button>
      <ul>
        <li v-for="(item, idx) in budget" :key="idx">
          {{idx}} : {{item}}
        </li>
      </ul>
    </form>
  </div>
</template>

<script>
import Http from '../config/Http'
import Api from '../config/Api'
import Budget from '../vo/BUdget'
import Charts from './Profit'

export default {
  name: 'Budget',
  data () {
    return {
      budgetType: [],
      type: null,
      budgetName: '',
      costAmount: null,
      budget: [],
      errors: []

    }
  },
  methods: {
    createBudget: async function (e) {
      let budgetObj = new Budget(this.budgetName, this.type, this.costAmount)
      let budgetVue = this

      Http.post(Api.budget.create, budgetObj).then(async function (r) {
        if (r.status === 201) {
          let budget = await Http.get(Api.budget.list)
          console.log('BUDGET', budget)
          budgetVue.budget = budget.data
        }
      }).catch(function (error) {
        console.dir(error.response.data)
        this.errors = error.response.data
      })
    }
  },
  created: async function () {
    let data = await Http.get(Api.bootUp.getBudgetType)
    this.budgetType = data.data
    let budgetList = await Http.get(Api.budget.list)
    console.dir(budgetList)
    this.budget = budgetList.data
  },
  components: {
    Charts
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
