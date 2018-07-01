<template>
  <div class="hello">
    <div>
      <accounting-input @renew-book="renewBook">
      <TransactionType slot="debit-transaction-type" type="credit" v-bind:transactionTypes="transactionTypes.credit"></TransactionType>
      <TransactionType slot="credit-transaction-type" type="debit" v-bind:transactionTypes="transactionTypes.debit"></TransactionType>

      </accounting-input>

    </div>
    <table>
      <thead>
        <tr>
          <th>transactionName</th>
          <th rowspan="2">debit-side</th>
          <th rowspan="2">credit-side</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(record, idx) in accountings" :key="idx">
          <td>{{record.transactionName}}</td>
          <td>{{record.credit.transactionType}}</td>
          <td>{{record.credit.costAmount}}</td>
          <td>{{record.debit.transactionType}}</td>
          <td>{{record.debit.costAmount}}</td>

        </tr>

      </tbody>
      <div>

      </div>
    </table>
  </div>
</template>

<script>
import AccountingInput from './AccountingInput'

import TransactionType from '../slot/TransactionType'
import Http from '../config/Http'
import Api from '../config/Api'
import Host from '../config/Host'
export default {
  name: 'AccountingBooks',
  methods: {
    renewBook: function (response) {
      console.log(response)
    }
  },
  data () {
    return {
      accountings: [],
      transactionTypes: []

    }
  },
  created: async function () {
    console.dir(Host)
    const host = Host.host
    const port = Host.port
    console.log(host + ':' + port + '/boot/')
    let types = await Http.get(host + ':' + port + '/boot/')
    this.transactionTypes = types.data
    //let result = await Http.get(Api.get.getTransactions)
    let result = await Http.post(host + ':' + port + '/transaction/')
    this.accountings = result.data
  },
  components: {TransactionType, AccountingInput}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
