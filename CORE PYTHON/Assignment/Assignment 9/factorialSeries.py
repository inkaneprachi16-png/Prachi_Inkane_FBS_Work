def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    
def sumSeries(n):
    if(n==0):
        return fact(n)
    else:
        return fact(n)+ sumSeries(n-1)

n = int(input('enter number:'))
sum = sumSeries(n)
print(f'sum of  the series 1!+2!+3!+....={n}! is { sum}')