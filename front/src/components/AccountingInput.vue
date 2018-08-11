<template>
  <div class="input">
    <h3>INPUT SECTION</h3>
    <input type="text" placeholder="transactionName" v-model="transactionName">
    <input type="text" placeholder="costAmount" v-model="costAmount">

    <slot name="credit-transaction-type"></slot>
    <slot name="debit-transaction-type" ></slot>

    <button @click.prevent="onSubmit">SUBMIT</button>
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
    onSubmit: async function () {
      let costAmount = parseInt(this.costAmount)
      let transactionName = this.transactionName
      let creditType = this.creditType
      let debitType = this.debitType
      if (isNaN(costAmount)) {
        alert('Please only input Number ')
      }
      if (transactionName.length < 1) {
        alert('Please input transActionName')
      }
      let transAction = new Transaction(transactionName, creditType, debitType, costAmount)
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
