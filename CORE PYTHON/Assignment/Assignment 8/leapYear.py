def leapYear(n):
        if(n%4==0):
            print(f'The entered year {n} is leap year')
        else:
            print(f'The entered year {n} is not leap year')
        
n = int(input('enter year to check leap year or not:'))
leapYear(n)
            