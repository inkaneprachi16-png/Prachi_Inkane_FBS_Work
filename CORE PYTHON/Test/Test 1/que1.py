l = int(input('enter the length:'))
b = int(input('enter the breadth:'))
r = int(input('enter the radius:'))
pi = 3.14

a_r = l * b

a_c = pi * (r**2)

a_cc = a_c/2

print(f'area of given figure is {a_r + a_cc}')

p = 2 + l + b + pi +r       #perimeter 

print(f'perimeter of given figure is {p}')
