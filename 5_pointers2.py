#   use immutable data structure -> to test pointers working in Memory Management

dict1 = {'value': 11}
dict2 = dict1

print('\n Before value is updated:')
print('dict1 = ',dict1)
print('dict2 = ', dict2)

print('\n dict1 points to: ', id(dict1))
print('dict2 points to: ',id(dict2))

dict2['value'] = 22

print('\n after value is updated')
print('dict1 value is: ', dict1)
print('dict2 value is: ', dict2)

print("\ndict1 points to ",id(dict1))
print('dict2 points to ',id(dict2))