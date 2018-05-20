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
  })
  it('Api called', () => {
    testData = [
      new Transaction(
        'test_record1',
        new Accounting(3000, 'test_type1-a'),

        new Accounting(4000, 'type1-b')
      ),
      new Transaction(
        'test_record2',
        new Accounting(5000, 'test_type2-c'),

        new Accounting(6000, 'type2-d')

      )
    ]
    mockAxios.get.mockImplementationOnce(() =>
      Promise.resolve({
        data: testData
      })
    )
    cmp = shallow(AccountingBooks)

    expect(mockAxios.get).toHaveBeenCalledTimes(1)
    // Within cmp.vm, we can access all Vue instance methods
    expect(mockAxios.get).toBeCalledWith(Api.get.getTransactions)
  })
  describe('AccountingBooks.vue Data Test', () => {
    it('data must be same', () => {
      expect(cmp.vm.accountings).toEqual(testData)
    })
    it('structure must be same', () => {
      expect(cmp.element).toMatchSnapshot()
    })
  })
})
