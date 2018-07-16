<template>
  <div class="input">
    <h3>INPUT SECTION</h3>
    <input type="text" placeholder="transactionName" v-model="transactionName">
    <input type="text" placeholder="costAmount" v-model="costAmount">

    <slot name="credit-transaction-type"></slot>
    <slot name="debit-transaction-type" ></slot>

    <button @click.prevent="onSubmit">SUBMIT</button>
    <button id="test" @click="show">Test</button>
    <div id="result">{{test}}</div>
  </div>
</template>

<script>

import Http from '../config/Http'

import EventBus from '../EventBus.js'
import Api from '../config/Api.js'
import Transaction from '../vo/Transaction.js'

export default {
  name: 'Test',
  data () {
    return {
      test: '',
      transactionName: '',
      costAmount: 0,
      creditType: '',
      debitType: ''
    }
  },
  methods: {
    show: function () {
      this.test = 'GETIT'
      EventBus.pass(this.test)
    },
    onSubmit: async function () {
      let cost_amount = parseInt(this.costAmount)
      let transaction_name = this.transactionName
      let credit_type = this.creditType
      let debit_type = this.debitType
      if (isNaN(cost_amount)) {
        alert('Please only input Number ')
      }
      if (transaction_name.length < 1) {
        alert('Please input transActionName')
      }
      // TODO: temporary type. logic will be added.
      let transaction_type = 1
      let user_id = 1
      let transAction = new Transaction(user_id, transaction_name, cost_amount, transaction_type)
      try {
        let param = await Http.post(Api.accounting.inputTransaction, transAction)
        this.$emit('renew-book', param)
      } catch (e) {
        console.log('err', e)
      }
    }
  },
  created () {
    let vm = this
    EventBus.$on('type-selected', function (param) {
      if (param.type === 'debit') {
        vm.creditType = param.value
      } else if (param.type === 'credit') {
        vm.debitType = param.value
      }
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
