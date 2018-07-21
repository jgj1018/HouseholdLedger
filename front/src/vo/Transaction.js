
export default class Transaction {
  constructor (userId, transactionName, creditType, debitType, costAmount) {
    this.user_id = userId
    this.transaction_name = transactionName
    this.credit_type = creditType
    this.debit_type = debitType
    this.cost_amount = costAmount
  }
}
