import dateFns from 'date-fns'
import InvalidDateError from '../errors/InvalidDateError'
export default {

  getDateRange: function (first, type) {
    let result = {'first': null, 'last': null}
    if (type.toUpperCase() === 'MONTH') {
      result['first'] = dateFns.format(new Date(first), 'YYYY-MM-01')
      result['last'] = dateFns.format(dateFns.lastDayOfMonth(new Date(result['first'])), 'YYYY-MM-DD')
    }
    if (type.toUpperCase() === 'YEAR') {
      result['first'] = dateFns.format(new Date(first), 'YYYY-01-01')
      result['last'] = dateFns.format(new Date(first), 'YYYY-12-31')
    }

    if (type.toUpperCase() === 'QUARTER') {
      result['first'] = dateFns.format(dateFns.startOfQuarter(new Date(first)), 'YYYY-MM-DD')
      result['last'] = dateFns.format(dateFns.lastDayOfQuarter(new Date(first)), 'YYYY-MM-DD')
    }

    if (result['first'] === 'Invalid Date' || result['last'] === 'Invalid Date') {
      throw new InvalidDateError('Invalid Date')
    }

    return result
  }
}
