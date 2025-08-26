
n = int(input('enter a 3 digit number:'))

#seprate digits
hundred = n // 100
ten = (n // 10) % 10
unit = n % 10

if(hundred == unit):
    print(f'{n} is palindrom number.')
else:
    print(f'{n} is not palindrom number.')


