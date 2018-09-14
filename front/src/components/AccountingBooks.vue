<template>
  <div class="">
    <div>
      <accounting-input @renew-book="renewBook">
        <TransactionType slot="debit-transaction-type" type="debit" v-bind:transactionTypes="transactionTypes.debit">
        </TransactionType>
        <TransactionType slot="credit-transaction-type" type="credit" v-bind:transactionTypes="transactionTypes.credit">
        </TransactionType>
      </accounting-input>
      <br/>
      <br/>
      <table>
        <thead>
          <tr>
            <th>created_at</th>
            <th>transaction_name</th>
            <th>cost_amount</th>
            <th>total_amount</th>
            <th>debit_type</th>
            <th>credit_type</th>
            <th>operation</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(record, idx) in accountings" :key="idx">
            <td>{{ record.created_at }}</td>
            <td>{{ record.transaction_name }}</td>
            <td>{{ record.cost_amount }}</td>
            <td>TO DO</td>
            <td>{{ record.debit_type }}</td>
            <td>{{ record.credit_type }}</td>
            <td>
              <button type="button" v-on:click="updateTrns(record.transaction_id)">Update</button>
              <button type="button" v-on:click="deleteTrns(record.transaction_id)">Delete</button>
            </td>
          </tr>
        </tbody>
        <div>
        </div>
      </table>
    </div>
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
    renewBook: async function () {
      let result = await Http.get(Api.accounting.transaction)
      this.accountings = result.data
    },
    updateTrns: function (event) {
      alert('test')
    },
    deleteTrns: function (trns_id, event) {
      Http.delete(Api.accounting.transaction + trns_id)
        .then(response => {
          this.renewBook()
        });
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
    this.transactionTypes = types.data
    this.renewBook()
  },
  components: {
    TransactionType, AccountingInput
  }
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
