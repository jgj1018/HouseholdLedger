const host = ''
const putUri = {
  method: 'put',
  inputTransaction: {
    uri: 'transaction'
  }
}
const api = {
  get: {
  },
  put: makeProxy(putUri)
}

const Api = makeProxy(api)

function makeProxy (origin) {
  return new Proxy(origin, {
    get: function (target, name, receiver) {
      var rv = target[name]
      let result = ''
      if (rv.hasOwnProperty('uri')) {
        result = `${host}${rv.uri}/${target['method']}`
      } else {
        result = rv
      }

      return result
    }
  })
}
export default Api
