n = int(input('enter numner:'))

square_dictionary = {}

for x in range(1, n+1):
    square_dictionary[x]= x*x

print(f' Generate dictionary : {square_dictionary}')