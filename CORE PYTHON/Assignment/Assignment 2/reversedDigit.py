num = int(input('enter a 3 digit number:'))


#digit spration
d1 = num % 10
num = num //10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10


print(f'reverse of the given three digits  is {d1} {d2} {d3}')



