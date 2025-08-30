num = int(input('enter the tree digit number:'))

#digit sepration
d1 = num%10
num = num // 10

d2 = num%10
num = num// 10

d3 = num%10
num = num//10

#addition of digits 
sum = d1 + d2 + d3

print(f' sum of three digit is {sum}')
