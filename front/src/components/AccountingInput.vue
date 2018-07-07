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
import Accounting from '../vo/Accounting.js'
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
      let cost = this.costAmount
      let name = this.transactionName
      if (isNaN(cost)) {
        alert('Please only input Number ')
      }
      if (name.length < 1) {
        alert('Please input transActionName')
      }
      if (this.creditType.length < 1 && this.debitType.length < 0) {
        alert('Please select at least one transaction-type')
      }
      let credit = new Accounting(cost, this.creditType)
      let debit = new Accounting(cost, this.debitType)
      let transAction = new Transaction(name, debit, credit)
      try {
        let param = await Http.post(Api.put.inputTransaction, transAction)
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
