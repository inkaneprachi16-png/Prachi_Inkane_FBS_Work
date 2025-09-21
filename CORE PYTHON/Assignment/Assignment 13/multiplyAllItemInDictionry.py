di1 = {'a': 2, 'b':3, 'c':4, 'd':5}

multiplication = 1

for item in di1.values():
    multiplication *= item


print(f'multiplication of all item in dictionary is : {multiplication}')
