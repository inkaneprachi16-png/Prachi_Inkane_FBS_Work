n = int(input('how many numbers you want in list:'))
Number =[]
Square = []
Cube = []

for i in range(1, n+1):
    Number.append(i)
    Square.append(i**2)
    Cube.append(i**3)

print(f'numbers: {Number}')
print(f'Square: {Square}')
print(f'Cube: {Cube}')