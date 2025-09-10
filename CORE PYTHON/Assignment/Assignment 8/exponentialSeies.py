def exponenSeies(n):
    sum=0
    for i in range(1, n+1):
        sum=sum+(n**i)
    print(f'sum of series is 1^1+2^2+3^3+...+{n^n} is : {sum}')

n=int(input('enter number to find sum of seies:'))
exponenSeies(n)