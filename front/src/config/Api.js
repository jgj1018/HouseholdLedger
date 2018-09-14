import Host from './Host'

const account = {
  login: '/account/login/',
  logout: '/account/logout/',
  register: '/account/registration/',
  refreshToken: '/refresh-token/'
}

const bootUp = {
  boot: '/boot/',
  getBudgetType: '/budget-type/'
}

const accounting = {
  transaction: '/transaction/transaction/',
  inputTransaction: '/transaction/transaction/'
}

const budget = {
  create: '/budget/budget/',
  list: '/budget/budget/'

}
const Api = {
  account: concatHost(account),
  bootUp: concatHost(bootUp),
  accounting: concatHost(accounting),
  budget: concatHost(budget)
}

function concatHost (ips) {
  const host = Host.host + ':' + Host.port
  return Object.assign({}, ...Object.keys(ips)
    .map(k => ({[k]: host + ips[k]})))
}
export default Api
