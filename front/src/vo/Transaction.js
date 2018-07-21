
export default class Transaction {
  constructor (userId, transactionName, costAmount, transactionType) {
    this.user_id = userId
    this.transaction_name = transactionName
    this.cost_amount = costAmount
    this.transaction_type = transactionType
  }
}
