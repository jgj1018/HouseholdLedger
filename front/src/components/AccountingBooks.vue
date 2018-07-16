<template>
  <div class="hello">
    <div>
      <accounting-input @renew-book="renewBook">
      <TransactionType slot="debit-transaction-type" type="credit" v-bind:transactionTypes="transactionTypes.credit"></TransactionType>
      <TransactionType slot="credit-transaction-type" type="debit" v-bind:transactionTypes="transactionTypes.debit"></TransactionType>
      </accounting-input>
    </div>
    <br/>
    <br/>
    <table>
      <thead>
        <tr>
          <th>created_at</th>
          <th>transaction_name</th>
          <th>cost_amount</th>
          <th>total_amount</th>
          <th>category</th>
          <th>transaction_type</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(record, idx) in accountings.data" :key="idx">
          <td>{{ record.created_at }}</td>
          <td>{{ record.transaction_name }}</td>
          <td>{{ record.cost_amount }}</td>
          <td>TO DO</td>
          <td>TO DO</td>
          <td>{{ record.transaction_type }}</td>
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
    let types = await Http.get(Api.bootUp.boot)
    this.transactionTypes = types.data['data']
    let result = await Http.get(Api.accounting.transaction)
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
table {
  width: 100%;
}
</style>
