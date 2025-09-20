def prime(n, i=2):
    if (n%i==0):
        return 1
    else:
        return prime(n, i+1)
    
n = int(input('enter number:'))
if prime(n):
    print(f'{n} is prime number:')
else:
    print(f'{n} is not prime number:')