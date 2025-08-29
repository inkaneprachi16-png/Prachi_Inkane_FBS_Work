a = int(input('enter the area of rooms:'))
# i = int(input('enter the no. of interial walls of a given rooms:'))
c = int(input('enter the cost of paint for interial:'))
# e = int(input('enter the no. of exterial walls of given rooms:'))
c1 = int(input('enter the cost of paint for exterial:'))


i_a = 8 * a

i_c = i_a * c

print(f'the cost of interial paint is {i_c}')

e_a = 7 * a

e_c = e_a * c1

print(f'the cost of exterial paint is {e_c} ')

print(f'the total cost of interial and extrial pain is {i_c + e_c}')

