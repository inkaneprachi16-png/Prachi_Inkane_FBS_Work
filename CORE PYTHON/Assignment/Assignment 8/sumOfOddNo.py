def sumOddNo(n):
    sum=0
    for i in range(1, n+1):
        if (i % 2 != 0):
            sum=sum+i
    print(f'sum of odd number 1- {n} number is :{sum}')

n = int(input('enter number :'))
sumOddNo(n)

