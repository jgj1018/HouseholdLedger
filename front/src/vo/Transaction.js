
export default class Transaction {
  constructor (user_id, transaction_name, cost_amount, transaction_type) {
    this.user_id = user_id
    this.transaction_name = transaction_name
    this.cost_amount = cost_amount
    this.transaction_type = transaction_type
  }
}
