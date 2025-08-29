num = int(input('enter three digit number:'))

#digt sepration
d1 = num // 100
d2 = (num//10)%10
d3 = num%10

if(d1 == d2*d2 and d1 == d3/2):
    print(f'yes, you have done it')
else:
    print(f'Please try next time')