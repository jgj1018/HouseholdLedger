import { shallow } from 'vue-test-utils'
import AccountingBooks from '@/components/AccountingBooks'

import Api from '../../../src/config/Api'
import Http from '../../../src/config/Http'

describe('AccountingBooks.vue', () => {
  let cmp = null
  let testData
  let bookSpy = jest.spyOn(AccountingBooks, 'created')
  let getSpy = jest.spyOn(Http, 'get')
  it('Api called', async () => {
    testData = []

    cmp = shallow(AccountingBooks)
    // Within cmp.vm, we can access all Vue instance methods
    expect(await getSpy).toHaveBeenCalledWith(Api.bootUp.boot)
    expect(bookSpy).toHaveBeenCalled()
  })

  describe('AccountingBooks.vue Data Test', () => {

    it('data must be same', async () => {
      expect(await bookSpy).toHaveBeenCalled()

      expect(cmp.vm.accountings).toEqual(testData)
    })
    it('structure must be same', () => {
      expect(cmp.element).toMatchSnapshot()
    })
  })
})
