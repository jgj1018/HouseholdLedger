import Host from './Host'

const account = {
  login: '/account/login/',
  logout: '/account/logout/',
  register: '/account/registration/',
  refreshToken: '/refresh-token/'
}

const accounting = {
  list: '/transaction/',
  'delete': '/transaction/',
  create: '/transaction/',
  transactionTypes: '/transaction/types'

}

const budget = {
  create: '/budget/',
  list: '/budget/',
  getTypes: '/budget/types'
}

const Api = {
  account: concatHost(account),
  accounting: concatHost(accounting),
  budget: concatHost(budget)
}

function concatHost (ips) {
  const host = Host.host + ':' + Host.port
  return Object.assign({}, ...Object.keys(ips)
    .map(k => ({[k]: host + ips[k]})))
}
export default Api
