import { mount } from 'vue-test-utils'
import Login from '@/components/Login'
import mockAxios from 'axios' // axios here is the mock from above!

describe('Login.vue', () => {
  let cmp = null

  beforeEach(() => {
    mockAxios.post.mockImplementationOnce(() =>
      Promise.resolve({
        data: {token: 'TOKEN'}
      })
    )
  })
  it('Login called', async () => {
    cmp = mount(Login)
    cmp.setData({'email': 'admin@admin.com'})
    cmp.setData({'password': 'gring21!'})
    expect(cmp.vm.email).toBe('admin@admin.com')
    expect(cmp.vm.password).toBe('gring21!')
    const result = await cmp.vm.submitLogin()

    expect(cmp.vm.loginResult).toEqual('SUCCESS')
    expect(mockAxios.post).toBeCalledWith('http://0.0.0.0:8000/account/login/', {'email': 'admin@admin.com', 'password': 'gring21!'})
  })
})
