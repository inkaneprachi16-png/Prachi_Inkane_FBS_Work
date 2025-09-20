def power(m, n):
    if(n==0):
        return 1
    else:
        return m*power(m, n-1)
    
m = int(input('enter base m:'))
n = int(input('enter exponent n:'))

result = power(m, n)
print(f'{m} to the power {n} is : { result}')