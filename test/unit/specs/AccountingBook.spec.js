import Vue from 'vue'
import AccountingBooks from '@/components/AccountingBooks'

describe('AccountingBooks.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(AccountingBooks)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.input h3').textContent)
      .toEqual('INPUT SECTION')
  })
  it('click event test', () => {
    const Constructor = Vue.extend(AccountingBooks)
    const vm = new Constructor().$mount()
  vm.$el.querySelector('#test').simulate('click')
  expect(vm.$el.querySelector('#result').textContent)
      .toEqual('GETIT')
  })

})
