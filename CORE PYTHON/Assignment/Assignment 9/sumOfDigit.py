def sumOfDigit(n):
    if(n==0):
        return 0
    else:
        return n%10 + sumOfDigit(n//10)

n = int(input('enter number:'))
sum = sumOfDigit(n)
print(f'sum of digits of given number is : { sum}')