
num = int(input('enter a 3 digit number:'))

#seprate digits
d1 = num % 10
num = num //10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

if(d1 == d3):
    print(f'given number is palindrom number.')
else:
    print(f'given number is not palindrom number.')



