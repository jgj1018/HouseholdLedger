
export default class Transaction {
  constructor (userId, transactionName, costAmount, transactionType) {
    this.userId = userId
    this.transactionName = transactionName
    this.costAmount = costAmount
    this.transactionType = transactionType
  }
}
