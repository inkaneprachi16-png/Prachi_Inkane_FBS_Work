di = {'a':1, 'b': 2, 'c':3, 'd':5}

key = input('enter the key to remove:')

if key in di:
    del di[key]
    print(f' key {key} removed')
else:
    print(f'key {key} not found in dictionary')


print(f'dictionary is :{di}')