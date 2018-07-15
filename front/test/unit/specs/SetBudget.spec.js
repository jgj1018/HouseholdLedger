import { shallow } from 'vue-test-utils'
import Budget from '@/components/Budget'

describe('Set Budget Test.vue', () => {
  let cmp = null
  cmp = shallow(Budget)
  describe('Budget.vue Data Test', () => {
    it('structure must be same', () => {
      expect(cmp.element).toMatchSnapshot()
    })
  })
}
)
