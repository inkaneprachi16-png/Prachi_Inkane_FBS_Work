num = int(input('enter a 3 digit number:'))


#digit spration
d1 = num % 10
num = num //10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10


reverse = d1*100+d2*10+d3
print(f'reverse of three digits is {reverse}')




