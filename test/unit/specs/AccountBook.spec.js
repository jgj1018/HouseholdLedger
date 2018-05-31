import { shallow } from 'vue-test-utils'
import AccountingBooks from '@/components/AccountingBooks'
import mockAxios from 'axios' // axios here is the mock from above!
import Transaction from '../../../src/vo/Transaction'
import Accounting from '../../../src/vo/Accounting'

import Api from '../../../src/config/Api'

describe('AccountingBooks.vue', () => {
  let cmp = null
  let testData
  beforeEach(() => {
    mockAxios.get.mockImplementation(() =>
      Promise.resolve({
        data: testData
      })
    )
  })
  it('Api called', async () => {
    testData = [
      new Transaction(
        'record1',
        new Accounting(1000, 'type1-a'),

        new Accounting(1000, 'type1-b')

      ),
      {
        transactionName: 'record2',
        debit: new Accounting(2000, 'type2-b'),

        credit: new Accounting(2000, 'type2-c')

      }
    ]

    cmp = shallow(AccountingBooks)

    expect(mockAxios.get).toHaveBeenCalledTimes(1)
    // Within cmp.vm, we can access all Vue instance methods
    expect(mockAxios.get).toBeCalledWith('http://localhost:8000/boot/')

  })

  describe('AccountingBooks.vue Data Test', () => {
    it('data must be same', () => {
      expect(mockAxios.get).toBeCalledWith(Api.get.getTransactions)

      expect(cmp.vm.accountings).toEqual(testData)
    })
    it('structure must be same', () => {
      expect(cmp.element).toMatchSnapshot()
    })
  })
})
