def sumOfNumber(n):
    if(n==0):
        return 0
    else:
        return n+sumOfNumber(n-1)
    
n= int(input('enter number:'))
sum = sumOfNumber(n)
print(f'sum of number is :{sum}')
