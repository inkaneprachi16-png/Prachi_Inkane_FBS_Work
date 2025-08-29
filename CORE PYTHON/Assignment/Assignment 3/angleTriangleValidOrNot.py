a = int(input('enter first angle of triangle:'))
b = int(input('enter second angle of triangle:'))
c = int(input('enter third angle of triangle:'))

sum = a+b+c

if(sum == 180):
    print('triangle is valid')
else:
    print('triangle is not valid')