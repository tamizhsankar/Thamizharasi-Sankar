if not is_code_tested:
  test()
elif is_code_slow:
  optimize()
elif not is_code_sustainable:
  refactor()
else:
  document()
