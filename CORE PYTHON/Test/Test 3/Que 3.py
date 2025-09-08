n= int(input('enter no. of empolyee:'))
total_emp=0

for i in range(1, n):
    salary =int(input(f'enter basic salary of employee {i}:'))
    
    if salary<2000:
        da = salary*10/100
        ta = salary*12/100
        hra = salary*15/100
    else:
        da=salary*15/100
        ta=salary*18/100
        hra = salary*20/100

    total=salary+da+ta+hra
    print(f'total salary of employee {i}:{total}')
    total_emp+=total

    print(f'total salary of employee :{total}')





