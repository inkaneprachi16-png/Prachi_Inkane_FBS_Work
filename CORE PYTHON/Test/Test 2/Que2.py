num = int(input('enter three digit number:'))

#digit spration
d1 = num % 10
num = num //10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10


if(d3 == 2*d2 and d3 == d1/2):
    print(f'yes, you have done it')
else:
    print(f'Please try next time')
