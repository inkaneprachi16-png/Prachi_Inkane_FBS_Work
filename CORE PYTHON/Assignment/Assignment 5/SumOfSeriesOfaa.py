a = int(input('enter value of a :'))
s = 0

for n in range(1, 11):
    s+=(a**n)/n

print(f'The sum of series a+a2/2+a3/3+...+a10/10 is : {s}')


print()
