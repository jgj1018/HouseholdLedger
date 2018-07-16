import Host from './Host'

const account = {
  login: '/account/login/',
  logout: '/account/logout/',
  register: '/account/registration/'
}

const bootUp = {
  boot: '/boot/',
  getBudgetType: '/budget-type/'
}

const accounting = {
  transaction: '/transaction/',
  inputTransaction: '/asset/transaction/'
}

const budget = {
  create: '/asset/budget/',
  list: '/asset/budget/'

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
