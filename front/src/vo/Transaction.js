
export default class Transaction {
  constructor (transactionName, creditType, debitType, costAmount) {
    this.transaction_name = transactionName
    this.credit_type = creditType
    this.debit_type = debitType
    this.cost_amount = costAmount
  }
}
