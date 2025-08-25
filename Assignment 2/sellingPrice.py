cp = int(input('inter the cost prise:'))
d = int(input('enter the discount percent:'))

#calculate discount

d_a = (d /100)*cp

#caluculate celling prise

c_p = cp - d_a

print(f'the celling prise is {c_p}')