x = int(input('enter the first side of triagle:'))
y = int(input('enter the second side of triangle:'))
z = int(input('enter the thrid side of triangle:'))


if(x==y==z):
    print('triangle is Equilateral triangle')          #all sides are same
elif(x==y or y==z or z==x):
    print('triangle is Isosceles triangle')         #two sides are same
else:
    print('triangle is scalene traingle')           #all sides are different