<template>
  <div class="hello">
    <div>
      <accounting-input @renew-book="renewBook">
      <TransactionType slot="debit-transaction-type" type="credit"></TransactionType>
      <TransactionType slot="credit-transaction-type" type="debit"></TransactionType>

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
          <td>{{record.debit.transactionType}}</td>
          <td>{{record.debit.costAmount}}</td>
          <td>{{record.credit.transactionType}}</td>
          <td>{{record.credit.costAmount}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import AccountingInput from './AccountingInput'
import Accounting from '../vo/Accounting'
import Transaction from '../vo/Transaction'
import TransactionType from '../slot/TransactionType'
export default {
  name: 'AccountingBooks',
  methods: {
    renewBook: function (response) {
      console.log(response)
    }
  },
  data () {
    return {
      accountings: [
        new Transaction(
          'record1',
          new Accounting(1000, 'type1-b'),

          new Accounting(1000, 'type1-c')
        ),
        new Transaction(
          'record2',
          new Accounting(2000, 'type2-b'),

          new Accounting(2000, 'type2-c')

        )
      ]
    }
  },
  created () {
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
