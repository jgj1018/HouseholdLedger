debit_type = (
  {'code': 1, 'name': '자산의 증가'},
  {'code': 2, 'name': '부채의 감소'},
  {'code': 3, 'name': '지출의 발생'},
)
credit_type = (
  {'code': 4, 'name': '부채의 증가'},
  {'code': 5, 'name': '자산의 감소'},
  {'code': 6, 'name': '수입의 발생'},
)

transaction_type = {
  'debit': debit_type, 'credit': credit_type
}

budget_type = (
  {'01': 'balance'}, {'02': 'cache'}, {'03': 'insurance'}, {'04': "stock"}
)
