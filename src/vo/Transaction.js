import Accouting from './Accounting'

export default class {
  constructor (transactionName, debit = {}, credit = {}) {
    this.transactionName = transactionName
    if (debit instanceof Accouting) {
      this.debit = debit
    }
    if (credit instanceof Accouting) {
      this.credit = debit
    }
  }
}
