n = int(input('enter a 3 digit number:'))

#seprate digits
hundred = n // 100
ten = (n // 10) % 10
unit = n % 10


print(f'reverse of the given three digits {n} is {unit}{ten}{hundred}')



