y = int(input('enter the year:'))

if(y%4 == 0):
    if(y%100 == 0):
        if(y%400 == 0):
            print(f'{y} is leap year')
        else:
            print(f'{y} is not leap year')
    else:
        print(f'{y} is leap year')
else:
    print(f'{y} is not leap year')










   