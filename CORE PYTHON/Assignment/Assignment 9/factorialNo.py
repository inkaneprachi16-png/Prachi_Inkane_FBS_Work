def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    
n = int(input('enter number:'))
factorial = fact(n)
print(f'the factorial of a {n} is : {factorial}')

