li=[44,78,99,33,3,5,8,24]
odd_Num = []

for num in li:
    if num%2 != 0:
        odd_Num.append(num)

print(f'list after removing even number: {odd_Num}')
