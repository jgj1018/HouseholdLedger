import { mount } from 'vue-test-utils'
import Login from '@/components/Login'
import Api from '../../../src/config/Api'
import Http from '../../../src/config/Http'

describe('Login.vue', () => {
  let cmp = null
  const createCmp = propsData => mount(Login, { propsData })
  cmp = createCmp({})
  let postSpy = jest.spyOn(Http, 'post')

  it('Login called', async () => {
    const spy = jest.spyOn(cmp.vm, 'submitLogin')

    cmp.update()
    cmp.setData({'email': 'admin@admin.com'})
    cmp.setData({'password': 'gring21!'})
    expect(cmp.vm.email).toBe('admin@admin.com')
    expect(cmp.vm.password).toBe('gring21!')

    const el = cmp.find('#loginForm').trigger('submit')
    expect(cmp.vm.submitLogin).toBeCalled()
    expect(await postSpy).toHaveBeenCalledWith(Api.account.login, {'email': 'admin@admin.com', 'password': 'gring21!'})
  })
})
