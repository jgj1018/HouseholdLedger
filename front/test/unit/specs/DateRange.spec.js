import DateRange from '../../../src/utils/DateRange'
import dateFns from 'date-fns'

describe('DateRange', () => {
  it('DateRange this month Range ', async () => {
    let tmpRange = DateRange.getDateRange(dateFns.format(new Date(), 'YYYY-MM-DD'), 'month')
    expect(tmpRange).toEqual({'first': dateFns.format(new Date(), 'YYYY-MM-01'),
      'last': dateFns.format(dateFns.lastDayOfMonth((new Date())), 'YYYY-MM-DD')})

    let yearRange = DateRange.getDateRange('2018-01-01', 'year')
    expect(yearRange).toEqual({'first': '2018-01-01', 'last': '2018-12-31'})

    let quarterRange = DateRange.getDateRange('2018-01-01', 'quarter')
    expect(quarterRange).toEqual({'first': '2018-01-01', 'last': '2018-03-31'})

    let noDayyearRange = DateRange.getDateRange('2018-01', 'year')
    expect(noDayyearRange).toEqual({'first': '2018-01-01', 'last': '2018-12-31'})

    let noDayquarterRange = DateRange.getDateRange('2018-04', 'quarter')
    expect(noDayquarterRange).toEqual({'first': '2018-04-01', 'last': '2018-06-30'})

    expect(
      () => {
        DateRange.getDateRange('2018--04', 'quarter')
      }
    ).toThrow()
  })
})
