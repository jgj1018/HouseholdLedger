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
              <button type="button" v-on:click="showModalForUpdate(record.transaction_id)">Update</button>
              <button type="button" v-on:click="deleteTrns(record.transaction_id)">Delete</button>
            </td>
          </tr>
        </tbody>
        <div>
        </div>
      </table>
    </div>
    <TrnsUpdateModal
      v-if="isModalVisible"
      @close="closeModal"
      @renewBook="renewBook"
      :transactionId="updateTransactionId"
    />
  </div>

</template>

<script>
import AccountingInput from './AccountingInput'
import TransactionType from '../slot/TransactionType'
import Http from '../config/Http'
import Api from '../config/Api'
import TrnsUpdateModal from './TransactionUpdateModal'

export default {
  name: 'AccountingBooks',
  components: {
    TransactionType,
    AccountingInput,
    TrnsUpdateModal
  },

  data () {
    return {
      isModalVisible: false,
      accountings: [],
      transactionTypes: [],
      updateTransactionId: null
    }
  },

  methods: {
    renewBook: async function () {
      let result = await Http.get(Api.accounting.list)
      this.accountings = result.data
    },
    showModalForUpdate: function (trnsId, event) {
      this.isModalVisible = true
      this.updateTransactionId = trnsId
    },
    closeModal: function (event) {
      this.isModalVisible = false
    },
    deleteTrns: function (trnsId, event) {
      Http.delete(Api.accounting.delete + trnsId)
        .then(response => {
          this.renewBook()
        })
    }
  },

  created: async function () {
    let types = await Http.get(Api.accounting.transactionTypes)
    this.transactionTypes = types.data
    this.renewBook()
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
