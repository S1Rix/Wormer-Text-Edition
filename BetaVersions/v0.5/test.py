import defs
test = {
    'test-key': 'test-value'
}
print(list(test.values()))
print(defs.find_key_in(test, 'test-value'))