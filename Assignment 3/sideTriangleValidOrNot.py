a = int(input('enter the first side of triangle:'))
b = int(input('enter the second side of triangle:'))
c = int(input('enter the third side of triangle:'))

if(a+b>c and b+c>a and a+c>b):
    print('triangle is valid')
else:
    print('triangle is not valid')